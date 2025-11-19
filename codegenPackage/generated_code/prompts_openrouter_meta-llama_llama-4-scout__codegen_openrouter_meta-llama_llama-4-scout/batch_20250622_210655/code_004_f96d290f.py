"""
Generated Code Metadata:
========================
Original URL: https://thumbsmaker.com
Prompt: Create a video editing script for a 5-minute explainer video, using ThumbsMaker's video editing services, including adding captivating transitions and ensuring a seamless narrative.
Generated: DETERMINISTIC_f96d290f19eab21d
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
import json
from thumbsmaker import VideoEditor

def create_explainer_video(video_data):
    """
    Create a 5-minute explainer video using ThumbsMaker's video editing services.

    Args:
        video_data (dict): A dictionary containing video data, including:
            - scenes (list): A list of scene dictionaries, each containing:
                - image (str): The image file path for the scene.
                - text (str): The text to display on the scene.
                - duration (int): The duration of the scene in seconds.
            - transitions (list): A list of transition dictionaries, each containing:
                - type (str): The type of transition (e.g. "fade", "swipe").
                - duration (int): The duration of the transition in seconds.

    Returns:
        str: The video file path.
    """

    # Initialize the video editor
    editor = VideoEditor()

    # Set the video dimensions and frame rate
    editor.set_dimensions(1920, 1080)
    editor.set_frame_rate(24)

    # Add scenes to the video
    scenes = video_data["scenes"]
    scene_files = []
    for i, scene in enumerate(scenes):
        # Add the scene image
        scene_file = editor.add_image(scene["image"], scene["duration"])
        scene_files.append(scene_file)

        # Add text to the scene
        if scene["text"]:
            editor.add_text(scene_file, scene["text"], 10, 10)

    # Add transitions between scenes
    transitions = video_data.get("transitions", [])
    for i in range(len(scene_files) - 1):
        # Get the transition type and duration
        transition_type = transitions[i]["type"] if i < len(transitions) else "fade"
        transition_duration = transitions[i]["duration"] if i < len(transitions) else 1

        # Add the transition
        editor.add_transition(scene_files[i], scene_files[i + 1], transition_type, transition_duration)

    # Render the video
    video_file = editor.render(scene_files, "explainer_video.mp4")

    return video_file

def main():
    # Define the video data
    video_data = {
        "scenes": [
            {"image": "scene1.jpg", "text": "Welcome to our explainer video", "duration": 5},
            {"image": "scene2.jpg", "text": "This is the second scene", "duration": 5},
            {"image": "scene3.jpg", "text": "", "duration": 5},
        ],
        "transitions": [
            {"type": "fade", "duration": 1},
            {"type": "swipe", "duration": 1},
        ]
    }

    try:
        # Create the explainer video
        video_file = create_explainer_video(video_data)
        print(f"Video created: {video_file}")
    except Exception as e:
        print(f"Error creating video: {e}")

if __name__ == "__main__":
    main()
```
