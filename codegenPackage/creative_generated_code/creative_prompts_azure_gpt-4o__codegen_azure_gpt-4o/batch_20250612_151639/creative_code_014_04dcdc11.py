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
import shutil

# Constants
METADATA_FILE = "video_metadata.json"  # Path to the metadata file
VIDEO_FOLDER = "workout_videos"  # Path to the folder containing videos
OUTPUT_FOLDER = "categorized_videos"  # Path to the output folder

# Ensure the output folder exists
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def load_metadata(metadata_file):
    """
    Load the metadata file (JSON format).
    
    Args:
        metadata_file (str): Path to the metadata file.
    Returns:
        dict: A dictionary of video metadata.
    """
    try:
        with open(metadata_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: Metadata file '{metadata_file}' not found.")
        return {}
    except json.JSONDecodeError:
        print("Error: Failed to parse the metadata file. Ensure it's valid JSON.")
        return {}

def organize_videos(metadata, video_folder, output_folder):
    """
    Organize videos into categorized folders based on metadata tags.
    
    Args:
        metadata (dict): Metadata containing video information and tags.
        video_folder (str): Path to the folder containing videos.
        output_folder (str): Path to the folder where categorized videos will be stored.
    """
    for video_name, tags in metadata.items():
        video_path = os.path.join(video_folder, video_name)
        
        # Check if the video file exists
        if not os.path.exists(video_path):
            print(f"Warning: Video file '{video_name}' not found. Skipping...")
            continue
        
        # Create folders based on tags and move the video
        for tag in tags:
            tag_folder = os.path.join(output_folder, tag)
            os.makedirs(tag_folder, exist_ok=True)  # Create folder if it doesn't exist
            
            try:
                # Copy video to the corresponding tag folder
                shutil.copy(video_path, tag_folder)
            except Exception as e:
                print(f"Error: Failed to copy '{video_name}' to '{tag_folder}'. Reason: {str(e)}")

def main():
    """
    Main function to organize workout videos based on metadata tags.
    """
    print("Loading metadata...")
    metadata = load_metadata(METADATA_FILE)
    
    if not metadata:
        print("No metadata found. Exiting...")
        return
    
    print("Organizing videos...")
    organize_videos(metadata, VIDEO_FOLDER, OUTPUT_FOLDER)
    print("Videos successfully organized into categorized folders.")

if __name__ == "__main__":
    main()
```

**Notes for Implementation:**
- Ensure the `video_metadata.json` file is structured as a dictionary where the keys are video filenames, and the values are lists of tags. Example:
  ```json
  {
      "workout1.mp4": ["cardio", "beginner"],
      "workout2.mp4": ["strength", "advanced"],
      "workout3.mp4": ["yoga", "intermediate"]
  }
  ```
- Place all video files in the `workout_videos` folder before running the script.
- The categorized videos will be copied into subfolders under `categorized_videos` based on tags.
