"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.mooveweb.com
Prompt: Write a Python script to automate the creation of engaging video content for social media, inspired by the production techniques described on moOve's website.
Generated: DETERMINISTIC_5bb22d381d2764f3
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, concatenate_videoclips
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_social_media_video(input_videos, output_file, text_overlay, duration_per_clip=5, resolution=(1080, 1080)):
    """
    Automates the creation of engaging video content for social media.

    Parameters:
    - input_videos: List of file paths to input video clips.
    - output_file: Path to save the final video.
    - text_overlay: Text to overlay on the video.
    - duration_per_clip: Duration (in seconds) to use per input clip (defaults to 5 seconds).
    - resolution: Resolution of the output video (defaults to 1080x1080).

    Returns:
    - None. Saves the final video to the specified output file.
    """
    try:
        # Ensure input videos exist
        for video_path in input_videos:
            if not os.path.exists(video_path):
                raise FileNotFoundError(f"Input video not found: {video_path}")

        # Load and process video clips
        clips = []
        for video_path in input_videos:
            logging.info(f"Processing video: {video_path}")
            clip = VideoFileClip(video_path).subclip(0, min(duration_per_clip, VideoFileClip(video_path).duration))
            clip = clip.resize(newsize=resolution)
            clips.append(clip)

        # Combine clips into a single video
        final_clip = concatenate_videoclips(clips)

        # Add text overlay
        text_clip = TextClip(text_overlay, fontsize=50, color='white', size=resolution, method='caption').set_duration(final_clip.duration)
        text_clip = text_clip.set_position('center').set_opacity(0.8)
        final_video = CompositeVideoClip([final_clip, text_clip])

        # Export final video
        logging.info(f"Exporting final video to {output_file}")
        final_video.write_videofile(output_file, codec='libx264', fps=24)

        logging.info("Video creation completed successfully.")
    except Exception as e:
        logging.error(f"An error occurred: {e}", exc_info=True)

if __name__ == "__main__":
    # Example usage
    input_videos = ["video1.mp4", "video2.mp4", "video3.mp4"]  # Replace with your actual video paths
    output_file = "final_social_media_video.mp4"
    text_overlay = "Follow us for more amazing content!"
    create_social_media_video(input_videos, output_file, text_overlay)
```
