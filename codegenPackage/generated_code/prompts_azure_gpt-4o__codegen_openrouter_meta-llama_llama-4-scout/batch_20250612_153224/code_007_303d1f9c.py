"""
Generated Code Metadata:
========================
Original URL: https://www.mooveweb.com
Prompt: Write code to generate dynamic video ads using a library suitable for a marketing agency specializing in audiovisual production, like MoOve Marketing.
Generated: DETERMINISTIC_303d1f9cee1adeae
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Dynamic Video Ad Generator**
=====================================

**Requirements:**

* Python 3.8+
* moviepy library (`pip install moviepy`)
* ffmpeg installed on the system

**Code:**
```python
import os
from moviepy.editor import *

def generate_dynamic_video_ad(
    background_image: str, 
    foreground_video: str, 
    text_overlay: str, 
    output_file: str
):
    """
    Generate a dynamic video ad by combining a background image, 
    a foreground video, and a text overlay.

    Args:
        background_image (str): Path to the background image.
        foreground_video (str): Path to the foreground video.
        text_overlay (str): Text to overlay on the video.
        output_file (str): Path to save the generated video ad.

    Raises:
        ValueError: If any of the input files do not exist.
    """

    # Check if input files exist
    if not os.path.exists(background_image):
        raise ValueError(f"Background image not found: {background_image}")
    if not os.path.exists(foreground_video):
        raise ValueError(f"Foreground video not found: {foreground_video}")

    # Load background image and foreground video
    background = ImageClip(background_image).set_duration(10)  # assume 10-second ad
    foreground = VideoFileClip(foreground_video).set_duration(10)

    # Create text overlay
    text = TextClip(text_overlay, fontsize=70, color='white')
    text = text.set_position('center').set_duration(10)

    # Composite video ad
    video_ad = CompositeVideoClip([background, foreground, text])

    # Write video ad to file
    try:
        video_ad.write_videofile(output_file, 
                                 fps=30, 
                                 codec='libx264', 
                                 audio_codec='aac')
    except Exception as e:
        raise RuntimeError(f"Failed to generate video ad: {e}")

    # Close clips to free up resources
    background.close()
    foreground.close()
    text.close()
    video_ad.close()

if __name__ == "__main__":
    background_image = "background.jpg"
    foreground_video = "foreground.mp4"
    text_overlay = "MoOve Marketing: Move Your Brand Forward"
    output_file = "dynamic_ad.mp4"

    generate_dynamic_video_ad(background_image, foreground_video, text_overlay, output_file)
```
**Example Use Case:**

* Save this code in a file named `dynamic_video_ad_generator.py`.
* Replace the input file paths with your own assets.
* Run the script using `python dynamic_video_ad_generator.py`.
* The generated video ad will be saved as `dynamic_ad.mp4` in the same directory.
