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
from moviepy.editor import VideoFileClip, concatenate_videoclips, TextClip, CompositeVideoClip
from moviepy.video.fx.resize import resize

# Constants
INPUT_VIDEO_FOLDER = "input_videos"  # Folder containing raw video clips
OUTPUT_VIDEO_FOLDER = "output_videos"  # Folder to save the final video
OUTPUT_VIDEO_NAME = "engaging_social_media_video.mp4"
VIDEO_DURATION_LIMIT = 60  # Maximum duration of the final video in seconds
FONT = "Arial-Bold"  # Font for text overlays
TEXT_COLOR = "white"  # Color of text overlays
TEXT_SIZE = 50  # Size of text overlays
TEXT_POSITION = "center"  # Position of text overlays
BACKGROUND_COLOR = "black"  # Background color for text overlays

# Ensure output folder exists
os.makedirs(OUTPUT_VIDEO_FOLDER, exist_ok=True)

def load_video_clips(folder_path):
    """
    Load all video clips from the specified folder.
    :param folder_path: Path to the folder containing video files.
    :return: List of VideoFileClip objects.
    """
    video_clips = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith((".mp4", ".mov", ".avi")):  # Supported video formats
            try:
                clip = VideoFileClip(os.path.join(folder_path, file_name))
                video_clips.append(clip)
            except Exception as e:
                print(f"Error loading video {file_name}: {e}")
    return video_clips

def add_text_overlay(clip, text):
    """
    Add a text overlay to a video clip.
    :param clip: VideoFileClip object.
    :param text: Text to overlay on the video.
    :return: CompositeVideoClip with text overlay.
    """
    text_clip = TextClip(text, fontsize=TEXT_SIZE, color=TEXT_COLOR, font=FONT, bg_color=BACKGROUND_COLOR)
    text_clip = text_clip.set_duration(clip.duration).set_position(TEXT_POSITION)
    return CompositeVideoClip([clip, text_clip])

def create_engaging_video(clips, duration_limit):
    """
    Create an engaging video by combining clips and adding text overlays.
    :param clips: List of VideoFileClip objects.
    :param duration_limit: Maximum duration of the final video in seconds.
    :return: Final VideoFileClip object.
    """
    random.shuffle(clips)  # Shuffle clips for variety
    selected_clips = []
    total_duration = 0

    for clip in clips:
        if total_duration + clip.duration <= duration_limit:
            selected_clips.append(clip)
            total_duration += clip.duration
        else:
            break

    # Add text overlays to each clip
    clips_with_text = [
        add_text_overlay(clip, f"Clip {i + 1}") for i, clip in enumerate(selected_clips)
    ]

    # Concatenate clips into a single video
    final_video = concatenate_videoclips(clips_with_text)
    return final_video

def main():
    """
    Main function to automate the creation of engaging video content.
    """
    print("Loading video clips...")
    clips = load_video_clips(INPUT_VIDEO_FOLDER)

    if not clips:
        print("No video clips found in the input folder.")
        return

    print("Creating engaging video...")
    final_video = create_engaging_video(clips, VIDEO_DURATION_LIMIT)

    # Resize video for social media (e.g., square format)
    final_video = resize(final_video, height=720, width=720)

    output_path = os.path.join(OUTPUT_VIDEO_FOLDER, OUTPUT_VIDEO_NAME)
    try:
        final_video.write_videofile(output_path, codec="libx264", audio_codec="aac")
        print(f"Engaging video created successfully: {output_path}")
    except Exception as e:
        print(f"Error saving video: {e}")

if __name__ == "__main__":
    main()
```
