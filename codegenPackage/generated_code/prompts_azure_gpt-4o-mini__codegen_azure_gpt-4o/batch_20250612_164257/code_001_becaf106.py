"""
Generated Code Metadata:
========================
Original URL: https://masterclicsolutions.com
Prompt: Write a Python script that automates the creation of interactive videos for e-learning courses, as described by MasterClic Solutions.
Generated: DETERMINISTIC_becaf10608ba8c43
Batch ID: 20250612_164257
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
from moviepy.video.tools.drawing import color_gradient
from moviepy.video.fx.resize import resize

def create_interactive_video(input_video_path, output_video_path, interactions):
    """
    Automates the creation of interactive videos for e-learning courses.

    Parameters:
        input_video_path (str): Path to the input video file.
        output_video_path (str): Path to save the output interactive video.
        interactions (list): List of interaction dictionaries. Each dictionary should contain:
            - 'time': Time in seconds where the interaction appears.
            - 'text': Text to display for the interaction.
            - 'duration': Duration in seconds for the interaction to appear.
            - 'position': Tuple (x, y) for the position of the interaction text.
    """
    try:
        # Load the input video
        video = VideoFileClip(input_video_path)

        # List to hold all clips (original video + interactions)
        clips = [video]

        # Add interactions to the video
        for interaction in interactions:
            time = interaction.get('time', 0)
            text = interaction.get('text', 'Interaction')
            duration = interaction.get('duration', 5)
            position = interaction.get('position', ('center', 'center'))

            # Create a text clip for the interaction
            text_clip = TextClip(
                text,
                fontsize=24,
                color='white',
                bg_color='black',
                size=(video.size[0] * 0.8, video.size[1] * 0.2),
                method='caption'
            ).set_position(position).set_duration(duration).set_start(time)

            # Add the text clip to the list of clips
            clips.append(text_clip)

        # Combine all clips into a single video
        final_video = CompositeVideoClip(clips)

        # Write the final video to the output path
        final_video.write_videofile(output_video_path, codec="libx264", audio_codec="aac")

        print(f"Interactive video created successfully: {output_video_path}")

    except FileNotFoundError:
        print(f"Error: File not found at path {input_video_path}. Please check the input path.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Example usage
    input_video = "input_video.mp4"  # Path to the input video file
    output_video = "output_interactive_video.mp4"  # Path to save the output video

    # Define interactions
    interactions = [
        {
            "time": 10,  # Time in seconds
            "text": "What is the capital of France?",
            "duration": 10,  # Duration in seconds
            "position": ('center', 'top')  # Position of the text
        },
        {
            "time": 30,
            "text": "Click here to learn more!",
            "duration": 8,
            "position": ('center', 'bottom')
        }
    ]

    # Create the interactive video
    create_interactive_video(input_video, output_video, interactions)
```
