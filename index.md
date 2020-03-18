---
layout: default
---
## The Martian Castaway

### Introduction

Many years ago, Andy Weir released the Martian.  This caught a lot of people's attention, including my own.  I was already deeply fascinated with space, but this got me asking questions like the ones asked in the move.  Namely, if you were stranded on Mars with no hope of rescue, how would you survive?  What technologies would be required?  What would you need to build and develop, and what is the minimum starting resources required for survival?

This project sets out to begin answering some of these questions (to the best of my ability).  In the chapters below, I will be taking the role of a castaway martian, marooned on a strange planet with nothing but minimal gear and his own wits to keep him alive.

### Chapters

1. [Damage Report](intro.md) - in depth overview of the situation
2. [Touching Down](landing.md) - the math behind landing a spacecraft
3. [Breath of Fresh Air](makingair.md) - managing the most essential resource using phytoplankton

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>