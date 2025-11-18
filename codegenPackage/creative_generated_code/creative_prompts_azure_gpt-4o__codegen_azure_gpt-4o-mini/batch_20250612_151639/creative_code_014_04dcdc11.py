"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jiodigital.live
Prompt: Generate a Python script to organize and categorize the "1000+ High-Quality Fitness Workout Videos" for a fitness app using metadata tags.
Generated: DETERMINISTIC_04dcdc11b55cfe0c
Batch ID: 20250612_151639
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
from typing import List, Dict

class WorkoutVideoOrganizer:
    def __init__(self, videos_directory: str, output_file: str):
        """
        Initializes the WorkoutVideoOrganizer with the directory of videos and the output file.

        :param videos_directory: Directory containing workout video files.
        :param output_file: Path to the output JSON file for categorized videos.
        """
        self.videos_directory = videos_directory
        self.output_file = output_file
        self.videos_metadata = []

    def organize_videos(self) -> None:
        """
        Organizes videos by reading their metadata and categorizing them.
        """
        try:
            # Gather video files from the specified directory
            video_files = self._get_video_files()
            for video_file in video_files:
                metadata = self._extract_metadata(video_file)
                if metadata:
                    self.videos_metadata.append(metadata)
            self._write_to_json()
        except Exception as e:
            print(f"An error occurred while organizing videos: {e}")

    def _get_video_files(self) -> List[str]:
        """
        Retrieves a list of video files from the specified directory.

        :return: List of video file paths.
        """
        video_extensions = ['.mp4', '.avi', '.mov', '.mkv']
        video_files = [
            os.path.join(self.videos_directory, f)
            for f in os.listdir(self.videos_directory)
            if os.path.isfile(os.path.join(self.videos_directory, f)) and
            os.path.splitext(f)[1].lower() in video_extensions
        ]
        return video_files

    def _extract_metadata(self, video_file: str) -> Dict[str, str]:
        """
        Extracts metadata from a video file.

        :param video_file: Path to the video file.
        :return: A dictionary containing metadata tags for the video.
        """
        # This is a placeholder for actual metadata extraction logic
        # e.g. use a library such as moviepy or opencv for real metadata extraction
        try:
            base_name = os.path.basename(video_file)
            title = os.path.splitext(base_name)[0]
            category = self._categorize_video(title)

            return {
                'title': title,
                'file_path': video_file,
                'category': category
            }
        except Exception as e:
            print(f"Failed to extract metadata from {video_file}: {e}")
            return {}

    def _categorize_video(self, title: str) -> str:
        """
        Categorizes the video based on its title.

        :param title: The title of the video.
        :return: A string representing the category.
        """
        # Simplified categorization logic
        if "yoga" in title.lower():
            return "Yoga"
        elif "strength" in title.lower():
            return "Strength Training"
        elif "cardio" in title.lower():
            return "Cardio"
        else:
            return "Other"

    def _write_to_json(self) -> None:
        """
        Writes the organized video metadata to a JSON file.
        """
        try:
            with open(self.output_file, 'w') as json_file:
                json.dump(self.videos_metadata, json_file, indent=4)
            print(f"Successfully organized videos and saved to {self.output_file}")
        except IOError as e:
            print(f"Failed to write to output file {self.output_file}: {e}")

if __name__ == "__main__":
    # Parameters for the directory of videos and the output JSON file
    videos_directory = "path/to/workout/videos"  # Change this to your actual video directory
    output_file = "organized_videos.json"  # Output JSON file

    # Create an instance of the organizer and organize the videos
    video_organizer = WorkoutVideoOrganizer(videos_directory, output_file)
    video_organizer.organize_videos()
```
