---
layout: page
title: "taking control"
date: 2020-03-18 15:53:27 -0000
categories: None
---

**SHIPLOG #0002 T+2120-03-18T15:53:27.299564**

I've been caught in high orbit around my new home for a couple days.  I've been poring over ship schematics figuring out how I can get control back. 

The primary control system is out, but all of the ships sensors and engines communicate over a distributed network. I have a personal computer I can use to tap into this network and potentially start moving things in the right direction.

Once I start getting data I can plot my ships orbit to figure out where I am.  Then it's a simple matter of creating a program for a landing system to put me safetly on the surface.

### Tapping into the ship
*Author's Note: for this part of the project, I'm using Kerbal Space Program to simulate the spacecraft.  In order to connect to it, I'm using the kRPC python library (https://krpc.github.io/krpc/).  If you want to follow along, install following the instructions in the link. I'm also using the Ferram Aerospace Research plugin which is required to access certain useful data.* 

I've found a diagram of the ships communication network and subsystems
{:refdef: style="text-align: center;"}
![my new home]({{ site.baseurl }}/assets/touching_down/ship_subsystem.jpg)
{: refdef}
All of the ships system communicate over a TCP/IP connection and I can access everything via a standard ethernet jack from the access panel.