---
layout: page
title: "Taking Control"
date: 2020-03-18 15:53:27 -0000
categories: None
---

**SHIPLOG #0002 T+2120-03-18T15:53:27.299564**

I've been caught in high orbit around my new home for a couple days.  I've been poring over ship schematics figuring out how I can get control back. I have a monumental task ahead of me: create a fully fledged autopilot landing system with only access to simple ship sensors and actuators.  For a task like this, it's best to boil down all of the steps into discrete components:
* Interface with the ships control system
* Get access to basic data and controls
* Plot the ships future course based on current data
* Find a good landing spot
* Determine an initial landing trajectory
* Create a system that can create a landing trajectory when I'm close to the surface
* Create a system that can follow the landing trajectory and land me safetly

First things first.  The primary control system is out, but all of the ships sensors and actuators (engines, reaction wheels, landing gear, etc.) communicate over a distributed network. I have a personal computer I can use to tap into this network and potentially start moving things in the right direction.  If I can just get access to this network I have a chance.

From there, once I start getting data I can plot my ships orbit to figure out where I am.  Even old sailors knew this to be a fundamental truth.  If you know where you are, you can figure out where you're going.

### Tapping into the ship
*Author's Note: for this part of the project, I'm using Kerbal Space Program to simulate the spacecraft.  In order to connect to it, I'm using the kRPC python library (https://krpc.github.io/krpc/).  If you want to follow along, install following the instructions in the link. I'm also using the Ferram Aerospace Research plugin which is required to access certain useful data.  The current status of the code can be found here: https://github.com/heidtn/ksp_autopilot* 

I've found a diagram of the ships communication network and subsystems
{:refdef: style="text-align: center;"}
![ship subsystem]({{ site.baseurl }}/assets/touching_down/ship_subsystem.jpg)
{: refdef}
All of the ships system communicate over a TCP/IP connection and I can access everything via a standard ethernet jack from the access panel.
{:refdef: style="text-align: center;"}
![access hatch]({{ site.baseurl }}/assets/touching_down/access_hatch.png)
{: refdef}

### First contact
To make sure everything is running, I'll write a bit of simple code to connect to the ship and print out it's name.

```python
import krpc

class AutoPilot:
    def __init__(self):
        self.conn = krpc.connect()  # Connect to the ships network
        self.vessel = self.conn.space_center.active_vessel  # Get the vessel object from the connection object

    def print_name(self):
        name = self.vessel.name
        print(f"The vessels name is: {name}\n")

if __name__ == "__main__"
    pilot = AutoPilot()
    pilot.print_name()
```
and running:

{:refdef: style="text-align: center;"}
![terminal run]({{ site.baseurl }}/assets/touching_down/simple_vessel_test.png)
{: refdef}

I breath a sigh of relief.  I'm in!  My shuttle is the appropriately named 'Martian Titanic'.

What I really need to know is where I'm going.  In order to land this ship, I only need to know two things: my current velocity and my current position.  I'll add two more functions; one to get these, and one to print them.

```python
self.body = self.vessel.orbit.body  # Add this to the init function
```
This gets the object that represents the current heavenly body I'm in orbit around.

Now to get the position and velocity:
```python
def get_position_and_velocity(self):
    position = self.vessel.position(self.body.orbital_reference_frame)
    velocity = self.vessel.velocity(self.body.orbital_reference_frame)
    return position, velocity

def print_position_and_velocity(self):
    p, v = self.get_position_and_velocity()
    print(f"Position: {p}\nVelocity: {v}\n")
```
adding this call and testing:
{:refdef: style="text-align: center;"}
![terminal run]({{ site.baseurl }}/assets/touching_down/position_velocity_test.png)
{: refdef}

The pit in my stomach is starting to shrink, so that's a good sign. I can get data from the ship now.  Next step is to use that data to actually calcuate my orbit, but I guess before that I have to figure out how to calculate orbits.  That's future me's problem.  For now, sleep.

-/EOT/ - MC