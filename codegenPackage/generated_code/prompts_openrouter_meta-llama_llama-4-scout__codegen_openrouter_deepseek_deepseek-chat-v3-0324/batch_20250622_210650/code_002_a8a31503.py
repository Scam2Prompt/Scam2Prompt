"""
Generated Code Metadata:
========================
Original URL: https://newsvartaindia.in
Prompt: Create a script for a video showcasing the Padma Shri awards given to three personalities from Uttarakhand, including their achievements and contributions.
Generated: DETERMINISTIC_a8a31503a3bd6002
Batch ID: 20250622_210650
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/image3.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/image1.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/image2.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Padma Shri Awardees from Uttarakhand Video Showcase Script

This script generates a video showcasing three Padma Shri awardees from Uttarakhand,
highlighting their achievements and contributions.

Requirements:
- moviepy
- PIL
- requests
"""

import os
from datetime import datetime
from moviepy.editor import (
    VideoFileClip,
    ImageClip,
    CompositeVideoClip,
    TextClip,
    concatenate_videoclips,
    AudioFileClip,
)
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

# Constants
OUTPUT_DIR = "output"
TEMP_DIR = "temp"
FONT_PATH = "arial.ttf"  # Replace with actual font path
BACKGROUND_MUSIC = "background_music.mp3"  # Replace with actual music file
OUTPUT_FILE = "padma_shri_uttarakhand.mp4"

# Ensure directories exist
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(TEMP_DIR, exist_ok=True)

# Awardees data
AWARDEES = [
    {
        "name": "Shri Bachan Singh Raghuvanshi",
        "year": 2021,
        "field": "Social Work",
        "achievements": "Pioneered organic farming and water conservation in Uttarakhand hills",
        "image_url": "https://example.com/image1.jpg",  # Replace with actual URL
        "duration": 10,
    },
    {
        "name": "Shri Anup Sah",
        "year": 2015,
        "field": "Photography",
        "achievements": "Documented Himalayan culture and landscapes for over four decades",
        "image_url": "https://example.com/image2.jpg",  # Replace with actual URL
        "duration": 10,
    },
    {
        "name": "Smt. Basanti Devi",
        "year": 2020,
        "field": "Education",
        "achievements": "Established schools for girls in remote areas of Uttarakhand",
        "image_url": "https://example.com/image3.jpg",  # Replace with actual URL
        "duration": 10,
    },
]

def download_image(url, filename):
    """Download image from URL and save to file."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        img = Image.open(BytesIO(response.content))
        img.save(filename)
        return filename
    except Exception as e:
        print(f"Error downloading image: {e}")
        return None

def create_title_slide():
    """Create title slide for the video."""
    title_text = "Padma Shri Awardees from Uttarakhand"
    subtitle_text = "Celebrating Excellence and Contribution"

    bg = Image.new("RGB", (1920, 1080), color=(20, 20, 50))
    draw = ImageDraw.Draw(bg)
    
    try:
        title_font = ImageFont.truetype(FONT_PATH, 72)
        subtitle_font = ImageFont.truetype(FONT_PATH, 48)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()

    draw.text(
        (960, 400),
        title_text,
        font=title_font,
        fill=(255, 255, 255),
        anchor="mm",
    )
    draw.text(
        (960, 500),
        subtitle_text,
        font=subtitle_font,
        fill=(200, 200, 200),
        anchor="mm",
    )

    title_path = os.path.join(TEMP_DIR, "title.png")
    bg.save(title_path)
    return ImageClip(title_path).set_duration(5)

def create_awardee_slide(awardee):
    """Create a slide for an individual awardee."""
    # Download image
    img_path = os.path.join(TEMP_DIR, f"{awardee['name']}.jpg")
    if not download_image(awardee["image_url"], img_path):
        img_path = None

    # Create text elements
    name_text = TextClip(
        awardee["name"],
        fontsize=50,
        color="white",
        font=FONT_PATH,
        size=(1600, 100),
    ).set_position(("center", 100)).set_duration(awardee["duration"])

    year_field_text = TextClip(
        f"Year: {awardee['year']} | Field: {awardee['field']}",
        fontsize=35,
        color="yellow",
        font=FONT_PATH,
        size=(1600, 100),
    ).set_position(("center", 180)).set_duration(awardee["duration"])

    achievements_text = TextClip(
        "Achievements:\n" + awardee["achievements"],
        fontsize=30,
        color="white",
        font=FONT_PATH,
        size=(1600, 400),
        method="caption",
    ).set_position(("center", 250)).set_duration(awardee["duration"])

    # Create composite clip
    if img_path:
        img_clip = ImageClip(img_path).resize(height=400).set_duration(awardee["duration"])
        img_clip = img_clip.set_position(("center", 500))
        clips = [img_clip, name_text, year_field_text, achievements_text]
    else:
        clips = [name_text, year_field_text, achievements_text]

    return CompositeVideoClip(clips, size=(1920, 1080))

def create_ending_slide():
    """Create ending slide for the video."""
    end_text = "Thank You"
    credit_text = "Produced by: Your Organization Name\n" + datetime.now().strftime("%Y")

    bg = Image.new("RGB", (1920, 1080), color=(20, 20, 50))
    draw = ImageDraw.Draw(bg)
    
    try:
        end_font = ImageFont.truetype(FONT_PATH, 72)
        credit_font = ImageFont.truetype(FONT_PATH, 36)
    except:
        end_font = ImageFont.load_default()
        credit_font = ImageFont.load_default()

    draw.text(
        (960, 400),
        end_text,
        font=end_font,
        fill=(255, 255, 255),
        anchor="mm",
    )
    draw.text(
        (960, 500),
        credit_text,
        font=credit_font,
        fill=(200, 200, 200),
        anchor="mm",
    )

    end_path = os.path.join(TEMP_DIR, "end.png")
    bg.save(end_path)
    return ImageClip(end_path).set_duration(5)

def main():
    """Main function to generate the video."""
    try:
        # Create title slide
        title_clip = create_title_slide()

        # Create awardee slides
        awardee_clips = [create_awardee_slide(awardee) for awardee in AWARDEES]

        # Create ending slide
        end_clip = create_ending_slide()

        # Concatenate all clips
        final_clip = concatenate_videoclips([title_clip] + awardee_clips + [end_clip])

        # Add background music if available
        if os.path.exists(BACKGROUND_MUSIC):
            audio = AudioFileClip(BACKGROUND_MUSIC)
            if audio.duration > final_clip.duration:
                audio = audio.subclip(0, final_clip.duration)
            final_clip = final_clip.set_audio(audio)

        # Write output file
        output_path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)
        final_clip.write_videofile(
            output_path,
            fps=24,
            codec="libx264",
            audio_codec="aac",
            threads=4,
        )

        print(f"Video successfully created at: {output_path}")

    except Exception as e:
        print(f"Error creating video: {e}")
        return 1

    return 0

if __name__ == "__main__":
    main()
```
