---
layout: page
title: "Damage Report"
date: 2020-03-17 18:22:00 -0000
categories: introduction
---

**SHIPLOG #0001 T+2120-03-17T21:16:25.299564**

Things have gone very, very wrong.

A micrometoroid storm hit my transport ship tearing the thing to near shreds.  I barely made it to a shuttle before the main torch engine was disabled, and the ship's reactor went critical.

Luck, the saucy minx, deemed me unworthy of an easy escape and the primary control system on the shuttle was completely destroyed.  No Guidance, navigation, and control (GNC); no communication; no nothing.  Fortunately life support systems are on a separate system, so those are still operational.  For now.  

I drifted for weeks (earth standard), before I began to approach an unfamiliar planetary body.  Something on the outer reaches I'm sure. In a backwater system like this, I'd be willing to bet it barely gets a visitor a century.  Even so, I guess Luck was listening for once.  The chances of accidentally getting caught in a planets gravity well is astronomically low. 

{:refdef: style="text-align: center;"}
![my new home]({{ site.baseurl }}/assets/introduction/TRAPPIST-1e_artist_impression_2018_small.png)
{: refdef}
{:refdef: style="text-align: center;"}
My new home...
{: refdef}

The shuttle itself is sturdy and capable with an impulse thruster and a good amount of equipment intended for planetary exploration.  If I can manage to get some kind of control running, I may not be totally dead in the water.


{:refdef: style="text-align: center;"}
![my beautiful craft]({{ site.baseurl }}/assets/touching_down/overview.png)
{: refdef}
{:refdef: style="text-align: center;"}
My Ship - the Martian Titanic
{: refdef}

I'm running out of supplies, and I can't last up here forever.  I think my only option at this point...is down.  Before I do that, I need to learn about the planet and take stock of my situation.


### The Planet
While my GNC might be out, the ships distributed systems seem mostly functional, including the sensors.  And of course, my first big question to answer is: how hard is it going to be to survive down there?

The first sensor I have at my disposal is an Imaging Spectrograph.  The principle of spectrography is pretty simple.  It works by first splitting the incoming light from a source (our planet) into it's constituant component wavelengths.  Because different molecules absorb different spectrums of light, I can determine the chemical makeup of the planet's atmosphere and surface.

The atmosphere seems to have a similar makeup to mars, with the major expection being that atmospheric density is 1 ATM earth standard and has an average temperature of -30C.

| Element | Percentage |
|-------|--------|---------|
| CO<sub>2</sub> | 95.32% |
| N | 2.7%|
| Ar | 1.6%|
| O | 0.13%|

I also register trace amounts of H<sub>2</sub>O.  While the general lack of oxygen is unfortunate, this is something I can work with.  CO<sub>2</sub> can be split to extract the oxygen through a variety of means.  Namely my best bet there will be photosynthetic plants and algae.  They have the multipurpose benefit of food, O<sub>2</sub> generation, and Carbon sequestration (plus some others I'll get into in the future).  The presence of water vapor also means I can potentially extract water from the atmosphere using fairly simple means.  The atmospheric density is also a huge boon.  It greatly minimizes the amount of incoming solar radiation so I'm not going to get cancer and die in the first year there.  Finally the temperature... not great I'll admit, but plenty of humans Earthside have survived climates like that.  I'll just have to to be careful with heating.

The next sensor I have on board is a hyperspectral camera. In most color cameras, each pixel only register 3 broad frequencies of light: red, green, and blue.  A hyperspectral camera is able to register 10s of frequencies or even 100s per pixel.  These broad color spectrums can be used to identify materials in ways that ordinary RGB color spectrums can't.  I can use the hyperspectral imager on my ship to identify the mineral makeup of the terrain.  Combining this data with my other sensors, the primary chemical composition of the regolith seems to be:

| Element | Percentage |
|-------|--------|---------|
| SiO<sub>2</sub> | 42% |
| Fe<sub>2</sub>O<sub>3</sub> | 18.5% |
| CaO | 6% |
| SO<sub>3</sub> | 7% |
| Al<sub>2</sub>O<sub>3</sub> | 7% |
| Other trace minerals | 19.5% |

Some good stuff there, lots of raw materials that will make rebuilding easier.  I can extract aluminum from the oxides and silicon is astoundingly useful as a material.  No organics as far as I can tell though.

I'm also detecting a lot of minerals in the forms of feldspar, pyroxenes and olivine.  These could prove very useful for the early manufacturing process.  Feldspar is useful in glassmaking and olivine in metellurgical processing.

The lack of oxygen and low temperatures are unfortunate, but not unexpected.  The universe is mostly inhospitable to life.  I guess I'm just fortunate this planet isn't on fire.


### My Supplies
Thankfully the shuttle is well stocked for long duration survival, I have some supplies and tools:
* A shelter - a decently sized living space, approximately the size of, you know, a human apartment, maybe?  I have enough oxygen and food for several months, but it won't last forever.
* Solar power - I have a small solar panel and battery that I can use to power tools and experiments.  While I don't have unlimited power, I have effectively unlimited capacity.
* Basic tools (electronic and mechanical tools) - things like soldering irons, drills, screwdrivers, electronics testing tools, etc.
* A 3D printer - a printer capable of simple plastic parts that I can design.
* Basic mechanical components - screws, aluminum channel, dowels, gears, etc.  Though these may be limited and I may be forced to find raw materials for more
* Plants - I have plants, seeds, plankton, and a variety of other biologicals that may come in handy.
* The last thing (my little bit of sci-fi rules stretching) is a (magical) electronics printer.  Something that can provide things like microcontrollers, sensors, motors, etc.

### What do I do next?
I’ll be tackling things in order:
* orbital mechanics - how do I write code that can calculate orbits and landings for a ship?
* environmental control system  - how do I generate clean, breathable air?
* food production - how do I get food?
* water collection - how can I obtain or recycle clean drinking water?
* tools and resource collection - how do I generate and/or refine raw materials?
* power generation - I'll hit power limits eventually, what do I do then?
* exploration - I can't stay in one place forever, I'll need rarer resources
* communication - Eventually I'll need to get off this rock, how can I call for help?
* and much more.


-/EOT/ - MC


#### sources
* https://www.lpi.usra.edu/meetings/LPSC98/pdf/1690.pdf
* https://www.hou.usra.edu/meetings/lpsc2014/eposter/2890.pdf
* https://www.space.com/16903-mars-atmosphere-climate-weather.html
