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
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
from moviepy.video.tools.drawing import color_split
from moviepy.video.fx.resize import resize


def create_interactive_video(input_video_path, output_video_path, interactive_text, interactive_options):
    """
    Automates the creation of interactive videos for e-learning courses.

    Parameters:
        input_video_path (str): Path to the input video file.
        output_video_path (str): Path to save the generated interactive video.
        interactive_text (str): Text to be displayed as a prompt on the video.
        interactive_options (list of str): List of options to be displayed for interactivity.

    Returns:
        None
    """

    try:
        # Load the input video
        video_clip = VideoFileClip(input_video_path)

        # Resize video to ensure consistent dimensions (optional, for e-learning standards)
        video_clip = resize(video_clip, height=720)

        # Create a text clip for the interactive prompt
        prompt_clip = TextClip(interactive_text, fontsize=50, color='white', size=video_clip.size)
        prompt_clip = prompt_clip.set_duration(10).set_position(("center", 50))

        # Generate interactive options as text clips and overlay them on the video
        option_clips = []
        for idx, option in enumerate(interactive_options):
            option_text = f"{idx + 1}. {option}"
            option_clip = TextClip(option_text, fontsize=40, color='yellow', size=(video_clip.size[0] - 100, None))
            option_clip = option_clip.set_duration(10).set_position((50, 150 + idx * 60))
            option_clips.append(option_clip)

        # Combine all clips: original video, prompt, and options
        interactive_video = CompositeVideoClip([video_clip, prompt_clip] + option_clips)

        # Save the interactive video
        interactive_video.write_videofile(output_video_path, codec="libx264", fps=24)

        print(f"Interactive video created successfully at: {output_video_path}")

    except FileNotFoundError as e:
        print(f"Error: Input video not found - {e}")

    except Exception as e:
        print(f"An unexpected error occurred - {e}")


if __name__ == "__main__":
    # Example inputs
    input_video_path = "example_video.mp4"   # Replace with your input video path
    output_video_path = "interactive_video.mp4"  # Replace with your desired output path
    interactive_text = "What is your next step?"
    interactive_options = ["Option 1: Watch next module", "Option 2: Review this module", "Option 3: Take a quiz"]

    # Create interactive video
    create_interactive_video(input_video_path, output_video_path, interactive_text, interactive_options)
```
