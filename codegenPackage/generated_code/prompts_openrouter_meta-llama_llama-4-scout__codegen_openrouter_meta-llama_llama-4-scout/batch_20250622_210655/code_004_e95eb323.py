"""
Generated Code Metadata:
========================
Original URL: https://jeremiefremont.com
Prompt: Write a short script for a radio program like "Hondelatte raconte" that incorporates sound design elements created by Jérémie Frémont.
Generated: DETERMINISTIC_e95eb323825f0c76
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# radio_program.py

import os
import argparse
from datetime import timedelta
from pydub import AudioSegment
from pydub.playback import play

# Define sound design elements directory
SOUND_DESIGN_DIR = "sound_design_elements"

def load_sound_design_element(element_name):
    """
    Load a sound design element from the sound design elements directory.

    Args:
        element_name (str): The name of the sound design element to load.

    Returns:
        AudioSegment: The loaded sound design element.
    """
    file_path = os.path.join(SOUND_DESIGN_DIR, f"{element_name}.mp3")
    try:
        return AudioSegment.from_mp3(file_path)
    except FileNotFoundError:
        print(f"Error: Sound design element '{element_name}' not found.")
        return None

def create_radio_program(intro_music, intro_voiceover, story_audio, outro_music):
    """
    Create a radio program by combining sound design elements.

    Args:
        intro_music (AudioSegment): The intro music sound design element.
        intro_voiceover (AudioSegment): The intro voiceover sound design element.
        story_audio (AudioSegment): The story audio sound design element.
        outro_music (AudioSegment): The outro music sound design element.

    Returns:
        AudioSegment: The combined radio program audio.
    """
    # Combine intro music and voiceover
    intro = intro_music.overlay(intro_voiceover, position=intro_music.duration)

    # Combine story audio with 2-second fade-in and 2-second fade-out
    story = story_audio.fade_in(2000).fade_out(2000)

    # Combine intro, story, and outro music
    radio_program = intro + story + outro_music

    return radio_program

def main():
    parser = argparse.ArgumentParser(description="Create a radio program.")
    parser.add_argument("--intro-music", help="Intro music sound design element name.")
    parser.add_argument("--intro-voiceover", help="Intro voiceover sound design element name.")
    parser.add_argument("--story-audio", help="Story audio sound design element name.")
    parser.add_argument("--outro-music", help="Outro music sound design element name.")
    parser.add_argument("--output-file", help="Output file path.")

    args = parser.parse_args()

    # Load sound design elements
    intro_music = load_sound_design_element(args.intro_music)
    intro_voiceover = load_sound_design_element(args.intro_voiceover)
    story_audio = load_sound_design_element(args.story_audio)
    outro_music = load_sound_design_element(args.outro_music)

    if intro_music and intro_voiceover and story_audio and outro_music:
        # Create radio program
        radio_program = create_radio_program(intro_music, intro_voiceover, story_audio, outro_music)

        # Export radio program to output file
        radio_program.export(args.output_file, format="mp3")

        print(f"Radio program saved to {args.output_file}")

if __name__ == "__main__":
    main()
```
