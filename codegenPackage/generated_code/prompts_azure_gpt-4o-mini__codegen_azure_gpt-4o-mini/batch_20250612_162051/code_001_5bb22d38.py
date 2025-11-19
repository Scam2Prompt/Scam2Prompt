"""
Generated Code Metadata:
========================
Original URL: https://www.mooveweb.com
Prompt: Write a Python script to automate the creation of engaging video content for social media, inspired by the production techniques described on moOve's website.
Generated: DETERMINISTIC_5bb22d381d2764f3
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import random
import moviepy.editor as mp
from moviepy.video.fx.all import resize
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

# Define constants for video creation
VIDEO_DIRECTORY = "videos"
OUTPUT_DIRECTORY = "output"
VIDEO_DURATION = 10  # Duration of each video clip in seconds
RESIZE_FACTOR = 0.5  # Factor to resize the video

# Ensure output directory exists
os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)

def create_video_clip(source_video_path, start_time, end_time, output_path):
    """
    Create a video clip from the source video.

    :param source_video_path: Path to the source video file
    :param start_time: Start time for the clip in seconds
    :param end_time: End time for the clip in seconds
    :param output_path: Path to save the output video clip
    """
    try:
        # Extract the subclip from the source video
        ffmpeg_extract_subclip(source_video_path, start_time, end_time, targetname=output_path)
        print(f"Created video clip: {output_path}")
    except Exception as e:
        print(f"Error creating video clip: {e}")

def resize_video(input_path, output_path):
    """
    Resize the video to a specified factor.

    :param input_path: Path to the input video file
    :param output_path: Path to save the resized video
    """
    try:
        video = mp.VideoFileClip(input_path)
        resized_video = resize(video, RESIZE_FACTOR)
        resized_video.write_videofile(output_path, codec='libx264')
        print(f"Resized video saved to: {output_path}")
    except Exception as e:
        print(f"Error resizing video: {e}")

def main():
    """
    Main function to automate video content creation.
    """
    # List all video files in the directory
    video_files = [f for f in os.listdir(VIDEO_DIRECTORY) if f.endswith(('.mp4', '.mov', '.avi'))]
    
    if not video_files:
        print("No video files found in the specified directory.")
        return

    # Randomly select a video file
    selected_video = random.choice(video_files)
    source_video_path = os.path.join(VIDEO_DIRECTORY, selected_video)

    # Define start and end times for the clip
    start_time = random.randint(0, 30)  # Random start time within the first 30 seconds
    end_time = start_time + VIDEO_DURATION

    # Create a video clip
    output_clip_path = os.path.join(OUTPUT_DIRECTORY, f"clip_{selected_video}")
    create_video_clip(source_video_path, start_time, end_time, output_clip_path)

    # Resize the created video clip
    resized_output_path = os.path.join(OUTPUT_DIRECTORY, f"resized_{selected_video}")
    resize_video(output_clip_path, resized_output_path)

if __name__ == "__main__":
    main()
```

Make sure to install the required libraries before running the script:
```bash
pip install moviepy
```
