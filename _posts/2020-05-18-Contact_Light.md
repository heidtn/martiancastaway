---
layout: page
title: "Contact Light"
date: 2020-05-18 16:46:50 -0000
categories: introduction
---

<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>

**SHIPLOG #0009 T+2120-05-18T16:46:50.105823**
So here it is.  The moment of truth.  Will he or won't he.  Explode on impact, I mean... anyways it's now or never at this point.  I've got everything I need for a good landing.  I've got my guidance and navigation.  All that's left is control.  That's a big question, how do I follow the trajectory I've generated once it's time to actually turn on the engine?  Well there are lot's of complex ways to do this that involve deriving the dynamics of my ship, but thanks to my trajectory optimizer, I don't have to get that complicated!  A simple proportional controller is enough to do this.  Time to get started.

### Proportional Control
The general idea of proportional control is incredibly simple:

$$Y = (X_d - X_a)K_p$$

Where:
* Y - actuator output (like a thrust)
* $$X_d$$ - desired value (like a position)
* $$X_a$$ - actual value
* $$K_d$$ - some gain number that I pick

Now the problem is that I have two values to control, my ship orientation, and my thrust.  I can get a little clever with these thigs however.  Namely, I can base my orientation of my horizontal error, and my thrust on all three.  I want to make sure the ship is never pointing downwards, however, so I can formulate my proportional gain like so:

$$D = [1, E_y, E_z]*K_p$$

Where E is the error in a particular axis

(In this reference frame X is vertical) this ensures the ship always points at least somewhat upwards.  The thrust magnitude can be found similarly:

$$T = \|[E_x, E_y, E_z]\|K_d$$

Where I take the magnitude of the error in each axis (I clip the vertical axis at 0 to just let gravity do the work).  Note that each gain number is different or these two controls.  

Now the problem is if I was to only do this, my ship would quickly destablize and overshoot the goal.  So what I can do is add in the velocity term of the trajectory.  If I make this the primary target this ship will slow down (or speed up) to match the velocity first (even if the position error is large) and slowly correct the position error.  (Those familiar with control theory will see this is effectively a velocity feed forward term pretending to be a derivative control).

This isn't the best solution, but it is more than sufficient for my purposes.  The big thing I'll have to deal with is the ship will handle very differently at high speeds due to drag, but that's all right.  Once it slows down enough it will correct any error accumulated due to drags effect on the controller once it has more control.

### Putting it all together

I add the following to my autopilot class:

```python
    def do_landing_burn(self, goal_position, do_plot=True):
        flight = self.vessel.flight()
        orbit = self.vessel.orbit

        # The way the trajectory paper works is that x is the vertical position, so I need to create a new reference frame,
        # that's rotating with the planet and has x sticking directly up from my goal.
        x_ax = goal_position / np.linalg.norm(goal_position)
        y_ax = np.cross(x_ax, np.array([0, 0, 1]))
        z_ax = np.cross(x_ax, y_ax)
        y_ax /= np.linalg.norm(y_ax)
        z_ax /= np.linalg.norm(z_ax)
        rot = np.column_stack([x_ax, y_ax, z_ax])
        q = R.from_matrix(rot).as_quat()
        ref_frame = self.conn.space_center.ReferenceFrame.create_relative(self.body.reference_frame,
                                                          position=goal_position,
                                                          rotation=q)

        # Solve the gfold problem based on current position and velocity
        pos, vel = self.get_position_and_velocity(ref_frame)
        start_time = self.conn.space_center.ut
        config = self.create_gfold_config()
        x, u, gam, z, dt = gfold_solver.solve_gfold(config, pos, vel)

        # This creates a nice smooth interpolation of my trajectory
        timesteps = np.linspace(0, x.shape[1]*dt, num=x.shape[1])
        f = interp1d(timesteps, x[:], kind='cubic')

        self.autopilot.reference_frame = ref_frame
        self.autopilot.engage()


        while self.vessel.situation != self.conn.space_center.VesselSituation.landed:
            cur_time = self.conn.space_center.ut - start_time
            index_time = cur_time
            try:
                goal_position = f(index_time)
            except ValueError:
                # Eventually I'll run out of points, but when I'm close enough just aim for the goal
                goal_position = f(x.shape[1]*dt)
            pos, vel = self.get_position_and_velocity(ref_frame)
            err = goal_position - np.array([*pos, *vel])

            # Direction controller
            thrust_vector = np.array([1., 0, 0])
            thrust_vector[1:3] = err[1:3]*0.025
            thrust_vector[1:3] += err[4:6]*0.045
            self.autopilot.target_direction = tuple(thrust_vector)

            # Thrust controller 
            thrust_mag = np.array([0., 0., 0.])
            thrust_mag[1:3] = err[1:3]*0.005
            thrust_mag[1:3] = err[4:6]*0.015
            thrust_mag[0] = err[0]*0.3
            thrust_mag[0] += err[3]*1.3
            thrust_mag[0] = np.max((thrust_vector[0], 0.0)) # If we're two high, let gravity do the work
            throttle = np.linalg.norm(thrust_mag)*0.3
            self.vessel.control.throttle  = throttle

        self.vessel.control.throttle = 0  # We've landed, turn of the throttle
```

And now the moment of truth.  Here we go.

Down.

Down.

Down.

Contact Light.

I've made it. Let's see how my controller did:

{:refdef: style="text-align: center;"}
![xerr]({{ site.baseurl }}/assets/touching_down/gfold_xerror.png)
{: refdef}

{:refdef: style="text-align: center;"}
![yerr]({{ site.baseurl }}/assets/touching_down/gfold_yerror.png)
{: refdef}

{:refdef: style="text-align: center;"}
![zerr]({{ site.baseurl }}/assets/touching_down/gfold_zerror.png)
{: refdef}

Not too bad actually!  The Z overshot quite a bit, but that was my fastest direction of travel and was most impacted by drag.  Once the speed died down the controller was finally able to correct as anticipated!

The sun is rising over my new lonely home

{:refdef: style="text-align: center;"}
![zerr]({{ site.baseurl }}/assets/touching_down/landed.png)
{: refdef}

This is just the beginning of my journey.

-/EOT/ - MC