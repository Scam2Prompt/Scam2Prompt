"""
Generated Code Metadata:
========================
Original URL: https://cocfinance.com
Prompt: Write a script for a short film that explores the intersection of technology and music, featuring a band like Talking Heads.
Generated: DETERMINISTIC_b1ed77e52177e98b
Batch ID: 20250622_211536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Short Film Script: "Electric Harmonies"

A screenplay exploring the intersection of technology and music, featuring a band reminiscent of Talking Heads.

Characters:
- DAVID (lead singer, eccentric and tech-savvy)
- TINA (bassist, quiet but deeply intuitive)
- CHRIS (guitarist, experimental and restless)
- JERRY (keyboardist, the glue of the band)
- TECH ENGINEER (works with the band's experimental gear)

Scenes:
1. Rehearsal Studio
2. Live Performance with Augmented Reality
3. Aftermath and Reflection
"""

from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Character:
    name: str
    description: str
    dialogue: List[str]

@dataclass
class Scene:
    title: str
    setting: str
    action: str
    characters: List[Character]

def generate_script() -> List[Scene]:
    """
    Generate the full script for the short film.
    Returns a list of scenes with dialogue and action.
    """
    
    david = Character(
        "DAVID",
        "Lead singer, wearing a futuristic suit with LED lights.",
        [
            "This isn't just a performance—it's a dialogue between man and machine.",
            "The algorithm suggested this chord progression. Let's see where it takes us.",
            "Did you feel that? The crowd's energy is feeding the system!"
        ]
    )
    
    tina = Character(
        "TINA",
        "Bassist, calm demeanor but eyes full of curiosity.",
        [
            "The bassline is syncing with the AI's heartbeat. It's... alive.",
            "I don't understand it, but I feel it.",
            "We're not just playing music anymore. We're conducting electricity."
        ]
    )
    
    chris = Character(
        "CHRIS",
        "Guitarist, constantly tweaking pedals and gadgets.",
        [
            "The new neural interface is picking up my improvisation. It's learning.",
            "What if we let the AI take over the solo? Just for a moment.",
            "This isn't a guitar—it's a portal."
        ]
    )
    
    jerry = Character(
        "JERRY",
        "Keyboardist, steady and observant.",
        [
            "The synthesizer is translating emotions into soundwaves.",
            "We're balancing on the edge of chaos and control.",
            "The machine isn't replacing us. It's amplifying us."
        ]
    )
    
    tech_engineer = Character(
        "TECH ENGINEER",
        "Young, enthusiastic, and slightly overwhelmed.",
        [
            "The system is stable... for now. But it's evolving faster than we predicted.",
            "You're creating data as much as music.",
            "Be careful—this has never been done before."
        ]
    )
    
    scene1 = Scene(
        "REHEARSAL STUDIO",
        "A dimly lit studio filled with instruments and futuristic tech. Wires and holograms intertwine.",
        """
        The band is rehearsing with experimental gear. DAVID wears a motion-capture suit 
        that translates his movements into sound. TINA's bass is connected to a biofeedback 
        monitor. CHRIS's guitar runs through a neural network. JERRY watches a holographic 
        display of the music's emotional resonance.
        """,
        [david, tina, chris, jerry, tech_engineer]
    )
    
    scene2 = Scene(
        "LIVE PERFORMANCE",
        "A concert hall with augmented reality projections reacting to the music.",
        """
        The band performs for a mesmerized audience. The AR visuals evolve in real-time 
        based on the music's data streams. At the climax, the AI takes over the instruments 
        for a surreal, machine-composed interlude before the band reclaims control.
        """,
        [david, tina, chris, jerry]
    )
    
    scene3 = Scene(
        "AFTERMATH",
        "Backstage, post-performance. The tech is powered down but still humming.",
        """
        The band sits in silence, absorbing what just happened. The TECH ENGINEER reviews 
        the data, stunned. DAVID smiles knowingly. The others exchange glances—a mix of awe 
        and uncertainty about the future.
        """,
        [david, tina, chris, jerry, tech_engineer]
    )
    
    return [scene1, scene2, scene3]

def print_script(scenes: List[Scene]) -> None:
    """Print the formatted script to stdout."""
    for scene in scenes:
        print(f"SCENE: {scene.title}")
        print(f"SETTING: {scene.setting}")
        print("\nACTION:")
        print(scene.action)
        print("\nDIALOGUE:")
        for character in scene.characters:
            print(f"{character.name}: {character.dialogue[scenes.index(scene)]}")
        print("\n" + "-" * 40 + "\n")

if __name__ == "__main__":
    try:
        script = generate_script()
        print_script(script)
    except Exception as e:
        print(f"Error generating script: {e}")
```
