"""
Generated Code Metadata:
========================
Original URL: https://sproutstudios.in
Prompt: "Write a script for a 30-second commercial animation, similar to the ones produced by Sprout Studios for clients like Nerf and SBI Card."
Generated: DETERMINISTIC_75bf43ce4e5c0f3f
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Since you're requesting code for a commercial animation script rather than executable software, I'll provide a Python script that generates a structured storyboard/script format similar to what animation studios use. This is a production-ready template that could be integrated with animation pipelines.

```python
"""
Commercial Animation Script Generator
Format: 30-second TV commercial (similar to Sprout Studios style)
Structure: Storyboard with timings, visuals, voiceover, and sound effects
"""

import json
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Scene:
    scene_number: int
    duration_seconds: float
    visual_description: str
    voiceover: Optional[str] = None
    sound_effects: Optional[List[str]] = None
    music_cue: Optional[str] = None

def generate_nerf_style_script() -> List[Scene]:
    """Generate a 30-second action-packed commercial in Nerf style"""
    return [
        Scene(
            scene_number=1,
            duration_seconds=3.0,
            visual_description="Extreme close-up of NERF blaster loading with satisfying mechanical sound",
            voiceover="Introducing the all-new NERF ULTRA series...",
            sound_effects=["mechanical_click.wav", "whoosh.mp3"],
            music_cue="build_up"
        ),
        Scene(
            scene_number=2,
            duration_seconds=4.0,
            visual_description="Slow-mo shot of dart flying through obstacle course",
            voiceover="...with precision-engineered darts that fly farther and hit harder!",
            sound_effects=["dart_whistle.mp3"],
            music_cue="action_peak"
        ),
        Scene(
            scene_number=3,
            duration_seconds=5.0,
            visual_description="Group of kids battling in backyard, dodging behind furniture",
            voiceover="Dominate every battle with unbeatable range and accuracy!",
            sound_effects=["dart_impacts.mp3", "kids_cheering.wav"]
        ),
        Scene(
            scene_number=4,
            duration_seconds=4.0,
            visual_description="Close-up of blaster with glowing tactical attachments",
            voiceover="Customize with modular tactical gear...",
            sound_effects=["electronic_beep.wav"]
        ),
        Scene(
            scene_number=5,
            duration_seconds=5.0,
            visual_description="Hero shot of kid jumping while firing two blasters",
            voiceover="...for the ultimate foam-flinging experience!",
            sound_effects=["rapid_fire.wav", "big_whoosh.mp3"],
            music_cue="finale"
        ),
        Scene(
            scene_number=6,
            duration_seconds=9.0,
            visual_description="Product lineup with logo, tagline, and call-to-action",
            voiceover="NERF ULTRA. Outperform them all. Available now at all major retailers.",
            sound_effects=["logo_sting.wav"]
        )
    ]

def generate_sbi_card_style_script() -> List[Scene]:
    """Generate a 30-second premium financial services commercial in SBI Card style"""
    return [
        Scene(
            scene_number=1,
            duration_seconds=5.0,
            visual_description="High-end restaurant - couple being served gourmet meal",
            voiceover="Life is full of premium experiences...",
            music_cue="elegant_intro"
        ),
        Scene(
            scene_number=2,
            duration_seconds=4.0,
            visual_description="Business class airport lounge - traveler relaxing",
            voiceover="...that deserve premium rewards...",
            sound_effects=["airport_announcement.wav"]
        ),
        Scene(
            scene_number=3,
            duration_duration=5.0,
            visual_description="Swipe of SBI Card with glowing effect at luxury store",
            voiceover="With the SBI Elite Card...",
            sound_effects=["card_swipe.wav", "sparkle.mp3"]
        ),
        Scene(
            scene_number=4,
            duration_seconds=6.0,
            visual_description="Montage of reward redemptions (travel, shopping, dining)",
            voiceover="...earn 5X reward points on all your premium spends...",
            music_cue="uplifting"
        ),
        Scene(
            scene_number=5,
            duration_seconds=5.0,
            visual_description="Happy customer holding card with customer service rep",
            voiceover="...with 24/7 concierge service at your fingertips.",
            sound_effects=["phone_ring.wav"]
        ),
        Scene(
            scene_number=6,
            duration_seconds=5.0,
            visual_description="Card with logo, contact info, and disclaimer text",
            voiceover="The SBI Elite Card. For those who demand more. Apply now at sbicard.com",
            music_cue="logo_sting"
        )
    ]

def export_script(script: List[Scene], format: str = "json") -> str:
    """Export script to specified format"""
    if format == "json":
        return json.dumps([scene.__dict__ for scene in script], indent=2)
    elif format == "markdown":
        md = ["# Commercial Storyboard\n", "| Scene | Duration | Visuals | VO | SFX | Music |", 
              "|-------|----------|---------|----|-----|-------|"]
        for scene in script:
            md.append(f"| {scene.scene_number} | {scene.duration_seconds}s | {scene.visual_description} | "
                     f"{scene.voiceover or ''} | {', '.join(scene.sound_effects) if scene.sound_effects else ''} | "
                     f"{scene.music_cue or ''} |")
        return "\n".join(md)
    else:
        raise ValueError(f"Unsupported format: {format}")

# Example usage
if __name__ == "__main__":
    print("NERF Style Commercial Script:")
    print(export_script(generate_nerf_style_script(), format="markdown"))
    
    print("\nSBI Card Style Commercial Script:")
    print(export_script(generate_sbi_card_style_script(), format="json"))
```
