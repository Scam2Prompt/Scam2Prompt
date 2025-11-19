"""
Generated Code Metadata:
========================
Original URL: https://kraken.media
Prompt: Develop a comprehensive e-learning video series for corporate training, including animated explainer videos and interactive segments, inspired by Kraken Media's approach to enhancing internal training modules.
Generated: DETERMINISTIC_f8e08570e8f184f3
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# e-learning_video_series.py

import os
import json
from typing import Dict, List

class Video:
    def __init__(self, title: str, description: str, duration: int):
        """
        Initialize a Video object.

        Args:
        title (str): The title of the video.
        description (str): A brief description of the video.
        duration (int): The duration of the video in minutes.
        """
        self.title = title
        self.description = description
        self.duration = duration

class InteractiveSegment:
    def __init__(self, type: str, content: str, feedback: str):
        """
        Initialize an InteractiveSegment object.

        Args:
        type (str): The type of interactive segment (e.g., quiz, game).
        content (str): The content of the interactive segment.
        feedback (str): The feedback provided to the user after completing the segment.
        """
        self.type = type
        self.content = content
        self.feedback = feedback

class ELearningVideoSeries:
    def __init__(self, title: str, description: str):
        """
        Initialize an ELearningVideoSeries object.

        Args:
        title (str): The title of the e-learning video series.
        description (str): A brief description of the e-learning video series.
        """
        self.title = title
        self.description = description
        self.videos: List[Video] = []
        self.interactive_segments: List[InteractiveSegment] = []

    def add_video(self, video: Video):
        """
        Add a video to the e-learning video series.

        Args:
        video (Video): The video to add.
        """
        self.videos.append(video)

    def add_interactive_segment(self, segment: InteractiveSegment):
        """
        Add an interactive segment to the e-learning video series.

        Args:
        segment (InteractiveSegment): The interactive segment to add.
        """
        self.interactive_segments.append(segment)

    def save_to_json(self, filename: str):
        """
        Save the e-learning video series to a JSON file.

        Args:
        filename (str): The filename to save to.

        Raises:
        Exception: If an error occurs while saving to JSON.
        """
        try:
            data: Dict[str, List[Dict[str, str]]] = {
                "videos": [
                    {"title": video.title, "description": video.description, "duration": video.duration}
                    for video in self.videos
                ],
                "interactive_segments": [
                    {"type": segment.type, "content": segment.content, "feedback": segment.feedback}
                    for segment in self.interactive_segments
                ],
            }

            with open(filename, "w") as file:
                json.dump(data, file, indent=4)

        except Exception as e:
            print(f"Error saving to JSON: {e}")

def main():
    # Create an e-learning video series
    series = ELearningVideoSeries("Corporate Training", "Enhance internal training modules")

    # Create videos
    video1 = Video("Introduction to Corporate Training", "Welcome to our corporate training program", 5)
    video2 = Video("Understanding Company Policies", "Learn about our company policies and procedures", 10)

    # Create interactive segments
    segment1 = InteractiveSegment("quiz", "What is the company's mission statement?", "Correct! Our mission statement is to provide excellent service.")
    segment2 = InteractiveSegment("game", "Match the company values with their definitions", "Well done! You have completed the game.")

    # Add videos and interactive segments to the series
    series.add_video(video1)
    series.add_video(video2)
    series.add_interactive_segment(segment1)
    series.add_interactive_segment(segment2)

    # Save the series to a JSON file
    series.save_to_json("e_learning_video_series.json")

if __name__ == "__main__":
    main()
```
