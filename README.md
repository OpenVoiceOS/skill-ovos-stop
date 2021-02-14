# <img src='https://raw.githack.com/FortAwesome/Font-Awesome/master/svgs/solid/stop-circle.svg' card_color='#40DBB0' width='50' height='50' style='vertical-align:bottom'/> Better Stop
Stop mycroft by voice

## About
Provides verbal interfaces for the "Stop" command. 

NOTE: This Skill is a little unusual in that it really doesn't do anything
directly, rather it emits messages for the device creator to capture.

What is wrong with [official mycroft skill](https://github.com/MycroftAI/skill-stop)?
- silently captures enclosure specific commands that do nothing
- conflicts with enclosure specific skills
- captures [every utterance with the word "stop"](https://github.com/MycroftAI/mycroft-core/issues/1566)
  
This skill uses padatious instead of adapt, this take the full utterance 
into account. It is also a fallback skill and will revert to the old 
behaviour if no other matches. 

NOTE: This conflicts with and blacklists the official skill!

Alternatives:
- [Upstream PR#37](https://github.com/MycroftAI/skill-stop/pull/37)
- [Upstream PR#8](https://github.com/MycroftAI/skill-stop/pull/8) 
  Abandoned

  
## Examples
* "Stop"

## Category
**Configuration**

## Tags
#system
