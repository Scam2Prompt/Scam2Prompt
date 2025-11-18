"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.mooveweb.com
Prompt: Write code to generate dynamic video ads using a library suitable for a marketing agency specializing in audiovisual production, like MoOve Marketing.
Generated: DETERMINISTIC_303d1f9cee1adeae
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import random
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

# Define constants for video generation
VIDEO_TEMPLATE_PATH = 'templates/video_template.mp4'
OUTPUT_DIR = 'output'
ADVERTISEMENT_DURATION = 10  # Duration of the advertisement in seconds

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_dynamic_ad(text, output_filename):
    """
    Generates a dynamic video advertisement using a text overlay on a template video.

    Args:
        text (str): The text to be overlayed on the video.
        output_filename (str): The name of the output video file.

    Raises:
        FileNotFoundError: If the video template does not exist.
        ValueError: If the text is empty or exceeds character limit.
    """
    # Validate input text
    if not text or len(text) > 50:
        raise ValueError("Text must be non-empty and less than 50 characters.")

    # Load video template
    if not os.path.exists(VIDEO_TEMPLATE_PATH):
        raise FileNotFoundError(f"Template video not found at {VIDEO_TEMPLATE_PATH}")

    # Load the video template
    video = VideoFileClip(VIDEO_TEMPLATE_PATH).subclip(0, ADVERTISEMENT_DURATION)

    # Create a text clip
    text_clip = TextClip(text, fontsize=70, color='white', size=video.size)
    text_clip = text_clip.set_position('center').set_duration(ADVERTISEMENT_DURATION)

    # Combine video and text clips
    final_video = CompositeVideoClip([video, text_clip])

    # Output file path
    output_path = os.path.join(OUTPUT_DIR, output_filename)
    
    # Write the result to a file
    final_video.write_videofile(output_path, codec='libx264', audio_codec='aac')

if __name__ == "__main__":
    try:
        # Example usage
        dynamic_text = "Your Dynamic Ad Here!"
        output_file = f"ad_{random.randint(1000, 9999)}.mp4"
        generate_dynamic_ad(dynamic_text, output_file)
        print(f"Advertisement generated successfully: {output_file}")
    except Exception as e:
        print(f"Error generating advertisement: {str(e)}")
```
