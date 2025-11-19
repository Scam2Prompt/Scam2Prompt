"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kabaitan.ro
Prompt: Write a Python script that generates subtitles for video content, focusing on accessibility for deaf and hard-of-hearing audiences, as demonstrated by Kabaitan's projects.
Generated: DETERMINISTIC_6c4423422e855215
Batch ID: 20250612_161353
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
import re
from typing import List, Dict
from datetime import timedelta

class SubtitleGenerator:
    def __init__(self, video_duration: float):
        """
        Initializes the SubtitleGenerator with the total video duration.

        :param video_duration: Duration of the video in seconds.
        """
        self.video_duration = video_duration
        self.subtitles: List[Dict[str, str]] = []

    def add_subtitle(self, start_time: timedelta, end_time: timedelta, text: str):
        """
        Adds a subtitle entry to the list.

        :param start_time: Start time of the subtitle.
        :param end_time: End time of the subtitle.
        :param text: The text to display as a subtitle.
        """
        subtitle = {
            'start': str(start_time),
            'end': str(end_time),
            'text': text
        }
        self.subtitles.append(subtitle)

    def format_timedelta(self, td: timedelta) -> str:
        """
        Formats a timedelta object to 'HH:MM:SS,mmm' format.

        :param td: The timedelta to format.
        :return: Formatted string.
        """
        total_seconds = int(td.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        milliseconds = int(td.microseconds / 1000)
        return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"

    def export_to_srt(self, file_path: str):
        """
        Exports the collected subtitles to an SRT file.

        :param file_path: Path to save the SRT file.
        """
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                for index, subtitle in enumerate(self.subtitles, start=1):
                    f.write(f"{index}\n")
                    f.write(f"{self.format_timedelta(timedelta(seconds=self.get_seconds(subtitle['start'])))} --> "
                             f"{self.format_timedelta(timedelta(seconds=self.get_seconds(subtitle['end'])))}\n")
                    f.write(f"{subtitle['text']}\n\n")
            print(f"Subtitles exported successfully to {file_path}")
        except IOError as e:
            print(f"Error writing to file: {e}")

    @staticmethod
    def get_seconds(time_str: str) -> float:
        """
        Converts a formatted time string to total seconds.

        :param time_str: Time string in 'HH:MM:SS,mmm' format.
        :return: Total seconds as a float.
        """
        try:
            time_parts = re.match(r'(\d{2}):(\d{2}):(\d{2}),(\d{3})', time_str).groups()
            hours, minutes, seconds, milliseconds = map(int, time_parts)
            return hours * 3600 + minutes * 60 + seconds + milliseconds / 1000
        except (AttributeError, ValueError) as e:
            print(f"Invalid time format: {time_str}. Error: {e}")
            raise

def main():
    # Video duration in seconds (example: 120 seconds)
    video_duration = 120.0
    generator = SubtitleGenerator(video_duration)

    # Sample subtitles - in a real application these would be dynamically generated
    subtitles_data = [
        (0, 10, "Welcome to our video."),
        (10, 20, "In this video, we will discuss important topics."),
        (20, 30, "Let's begin with the first topic."),
        # Additional subtitles can be added here
    ]

    for start_sec, end_sec, text in subtitles_data:
        generator.add_subtitle(timedelta(seconds=start_sec), timedelta(seconds=end_sec), text)

    # Export subtitles to SRT file
    output_file = "subtitles.srt"
    generator.export_to_srt(output_file)

if __name__ == "__main__":
    main()
```
