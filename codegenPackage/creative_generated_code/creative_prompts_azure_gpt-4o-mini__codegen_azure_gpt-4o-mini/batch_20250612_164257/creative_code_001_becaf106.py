"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://masterclicsolutions.com
Prompt: Write a Python script that automates the creation of interactive videos for e-learning courses, as described by MasterClic Solutions.
Generated: DETERMINISTIC_becaf10608ba8c43
Batch ID: 20250612_164257
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import logging
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class InteractiveVideoCreator:
    def __init__(self, video_path, output_path):
        """
        Initializes the InteractiveVideoCreator with the specified video path and output path.
        
        :param video_path: Path to the input video file.
        :param output_path: Path to save the output interactive video.
        """
        self.video_path = video_path
        self.output_path = output_path
        
        # Check if the video file exists
        if not os.path.isfile(video_path):
            logging.error(f"Video file not found: {video_path}")
            raise FileNotFoundError(f"Video file not found: {video_path}")
        
        logging.info(f"Initialized with video: {video_path} and output: {output_path}")

    def create_interactive_video(self, text_overlays, output_format='mp4'):
        """
        Creates an interactive video by overlaying text on a video clip.
        
        :param text_overlays: List of dictionaries containing text and when to display it.
        :param output_format: The format for the output video file (default is mp4).
        """
        logging.info("Starting to create interactive video.")
        
        # Load the video clip
        try:
            video_clip = VideoFileClip(self.video_path)
        except Exception as e:
            logging.error(f"Error loading video file: {e}")
            raise
        
        # Create a list to hold video clips with text overlays
        clips = [video_clip]

        # Process each text overlay
        for overlay in text_overlays:
            try:
                start_time = overlay.get('start_time', 0)
                duration = overlay.get('duration', 2)  # Default duration is 2 seconds
                text = overlay.get('text', '')

                # Create text clip
                text_clip = TextClip(text, fontsize=70, color='white')
                text_clip = text_clip.set_position('center').set_duration(duration).set_start(start_time)

                # Add text clip to the composite clip
                clips.append(text_clip)

                logging.info(f"Added text overlay: '{text}' from {start_time} for {duration} seconds.")
            except Exception as e:
                logging.error(f"Error processing overlay: {overlay} - {e}")
        
        # Combine all clips into one composite
        final_video = CompositeVideoClip(clips)
        
        # Write the final video to a file
        try:
            final_video.write_videofile(self.output_path, codec='libx264', audio_codec='aac')
            logging.info(f"Interactive video created successfully: {self.output_path}")
        except Exception as e:
            logging.error(f"Error saving video file: {e}")
            raise

if __name__ == "__main__":
    # Example usage
    video_path = "path/to/your/input_video.mp4"  # Change this to your input video path
    output_path = "path/to/your/output_video.mp4"  # Change this to your desired output path
    
    # Example text overlays
    text_overlays = [
        {"text": "Welcome to the Course!", "start_time": 0, "duration": 3},
        {"text": "Let's get started.", "start_time": 3, "duration": 4},
        {"text": "Remember to take notes!", "start_time": 10, "duration": 3},
    ]

    try:
        video_creator = InteractiveVideoCreator(video_path, output_path)
        video_creator.create_interactive_video(text_overlays)
    except Exception as e:
        logging.error(f"Failed to create interactive video: {e}")
```
