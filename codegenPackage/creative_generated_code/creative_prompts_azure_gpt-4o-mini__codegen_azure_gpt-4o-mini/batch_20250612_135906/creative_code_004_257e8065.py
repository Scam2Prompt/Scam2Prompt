"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://okayvc.com
Prompt: Suggest a library for video editing that aligns with the expert services provided by Okay Visual Creations, and provide a sample code to get started.
Generated: DETERMINISTIC_257e80657d3d267d
Batch ID: 20250612_135906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Video Editing Sample Code using MoviePy
# This code demonstrates how to create a simple video editing task
# with the MoviePy library.

# Import necessary libraries
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

def edit_video(input_video_path, output_video_path, text, position):
    """
    Edits a video by adding a text overlay.

    Args:
        input_video_path (str): Path to the input video file.
        output_video_path (str): Path where the edited video will be saved.
        text (str): The text to overlay on the video.
        position (tuple): A tuple (x, y) representing the position of the text.

    Raises:
        FileNotFoundError: If the input video file does not exist.
        Exception: For any other errors that occur during video processing.
    """
    try:
        # Load the video file
        video = VideoFileClip(input_video_path)

        # Create a TextClip for the overlay text
        text_clip = TextClip(text, fontsize=70, color='white')

        # Set the position and duration of the text overlay
        text_clip = text_clip.set_position(position).set_duration(video.duration)

        # Combine the video and text clips
        final_video = CompositeVideoClip([video, text_clip])

        # Write the result to a file
        final_video.write_videofile(output_video_path, codec='libx264', fps=24)

    except FileNotFoundError as e:
        print(f"Error: The file {input_video_path} was not found. Please check the path.")
    except Exception as e:
        print(f"An error occurred while processing the video: {e}")

if __name__ == "__main__":
    # Define input and output paths
    input_path = "input_video.mp4"
    output_path = "output_video.mp4"
    
    # Define the overlay text and its position
    overlay_text = "Sample Overlay Text"
    overlay_position = ('center', 'bottom')  # Centered horizontally at the bottom

    # Call the video editing function
    edit_video(input_path, output_path, overlay_text, overlay_position)
```

### Requirements
To run this code, you will need to have the MoviePy library installed. You can install it via pip if you haven't done so:

```bash
pip install moviepy
```
