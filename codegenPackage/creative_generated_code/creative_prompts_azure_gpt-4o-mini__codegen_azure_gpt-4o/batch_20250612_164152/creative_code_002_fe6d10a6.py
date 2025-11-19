"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fantom.de
Prompt: Write a script that automates the photo and video editing process, inspired by the multimedia services provided by Fantom.
Generated: DETERMINISTIC_fe6d10a69238f821
Batch ID: 20250612_164152
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import sys
import subprocess
from moviepy.editor import VideoFileClip, concatenate_videoclips, CompositeVideoClip, TextClip
from PIL import Image, ImageEnhance

def edit_photo(photo_path, output_path, brightness=1.2, contrast=1.3, sharpness=1.5):
    """
    Function to edit a photo: adjusts brightness, contrast, and sharpness.
    :param photo_path: Path to the input photo.
    :param output_path: Path to save the edited photo.
    :param brightness: Brightness adjustment factor (default: 1.2).
    :param contrast: Contrast adjustment factor (default: 1.3).
    :param sharpness: Sharpness adjustment factor (default: 1.5).
    """
    try:
        # Open the image
        image = Image.open(photo_path)
        
        # Enhance brightness
        enhancer = ImageEnhance.Brightness(image)
        image = enhancer.enhance(brightness)
        
        # Enhance contrast
        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(contrast)
        
        # Enhance sharpness
        enhancer = ImageEnhance.Sharpness(image)
        image = enhancer.enhance(sharpness)
        
        # Save the edited image
        image.save(output_path)
        print(f"Edited photo saved to {output_path}")
    except Exception as e:
        print(f"Error editing photo: {e}")
        sys.exit(1)


def edit_video(video_path, output_path, text_overlay=None, text_position=("center", "center")):
    """
    Function to edit a video: adds a text overlay and saves the edited video.
    :param video_path: Path to the input video.
    :param output_path: Path to save the edited video.
    :param text_overlay: Text to overlay on the video (default: None).
    :param text_position: Position of the text overlay (default: center).
    """
    try:
        # Load the video
        clip = VideoFileClip(video_path)
        
        if text_overlay:
            # Create a text clip
            text = TextClip(text_overlay, fontsize=50, color='white')
            
            # Set position and duration for text overlay
            text = text.set_pos(text_position).set_duration(clip.duration)
            
            # Overlay text on video
            video = CompositeVideoClip([clip, text])
        else:
            video = clip
        
        # Save the edited video
        video.write_videofile(output_path, codec="libx264")
        print(f"Edited video saved to {output_path}")
    except Exception as e:
        print(f"Error editing video: {e}")
        sys.exit(1)


def main():
    """
    Main function to run the script.
    Prompts the user for input file paths and allows them to choose editing options.
    """
    try:
        print("Welcome to the multimedia editing script!")
        
        # Ask user for input
        file_type = input("Enter file type (photo/video): ").strip().lower()
        input_path = input("Enter the path to the input file: ").strip()
        output_path = input("Enter the path to save the edited file: ").strip()
        
        # Check if the input file exists
        if not os.path.exists(input_path):
            print("The input file does not exist.")
            sys.exit(1)
        
        if file_type == "photo":
            # Edit photo
            edit_photo(input_path, output_path)
        elif file_type == "video":
            # Ask for optional text overlay
            text_overlay = input("Enter text to overlay on the video (or leave blank): ").strip()
            edit_video(input_path, output_path, text_overlay if text_overlay else None)
        else:
            print("Invalid file type. Please enter 'photo' or 'video'.")
            sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
