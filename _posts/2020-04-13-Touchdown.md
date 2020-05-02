---
layout: page
title: "Touchdown"
date: 2020-04-13 18:56:23 -0000
categories: None
---
<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>


**SHIPLOG #0006 T+2120-04-13T18:56:23.423515**

Finally, the moment of truth.  Touchdown.  Either I live or I die a horrible death.  The only thing keeping me from slamming into the surface of the planet is a little piece of silicon that's been tricked into thinking.  The tricky part here, is desining the math to land the ship.

Someday I'm going to have to get off of Semotus, but for now, I think this is my best bet.  I'd be lying if I said I wasn't afraid.  Not a lot to look forward to down there either.  It's probably going to be months or years before I can do enough to get home.  But I don't have a lot of options at this point.

I don't have a lot fuel so my autopilot needs to be effective.  Luckily I think I have just the thing.


### Landing
I only need to do one thing, make sure my velocity is 0 when my ship is at the location I want to land.  The big question is when to start the ships thrusters and how much thrust to give.  Now I could just turn my thrust to max until my speed is 0, but that's going to waste a lot of fuel.  And it's not going to put me where I want to go.  I have to formulate a landing solution that lands my in my desired location while at the same time ensuring I use the minimal amount of thrust required.

There are two major parts to a landing problem like this one: trajectory generation and control.  Trajectory generation calculates an optimal path for my ship to follow, it basically says something like: 'when I'm at position A, I should have velocity V'.  When creating a trajectory I can optimize it such that it ensures the ship itself is actually capable of following that trajectory.  Control actually changes the ship's thrust and angle during descent to try and follow that trajectory.  By using the known dynamics of my spacecraft I can create highly optimal controllers.


### Trajectory Generation
Now to generate my trajectory, the simplest way would be to always target a safe speed, like 5 m/s.  However I would end up wasting a lot of fuel fighting gravity and likely run out of fuel by the time I make it down.  Fortunately there are ways of solving an optimal trajectory with just a few pieces of information.  

The trajectory optimization problem takes in the dynamics of the system (i.e. my ship), some constraints, and desired start/end values.  It then attempts to optimize the trajectory while obeying the constraints and ensuring the start/end states are correct (or at least close).  The method I'll be using to solve the trajectory problem is called pseudospectral collocation.  

I've worked out the dynamics of the spacecraft already, so the next step is to establish the constraints.


### Control
There are many ways to create optimal controllers for a system like this, especially ones that accurately guarantee good tracking of a trajectory.  Our trajectory generation ensures we stay within a number of contraints however, so a linear controller 



