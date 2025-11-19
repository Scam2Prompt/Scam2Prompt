"""
Generated Code Metadata:
========================
Original URL: https://thephantomnetwork.net
Prompt: Write a Python script to create a simple video thumbnail generator, inspired by the video editing content on The Phantom Network.
Generated: DETERMINISTIC_6eae1152291489d9
Batch ID: 20250622_210935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# video_thumbnail_generator.py

import cv2
import numpy as np
from datetime import datetime
import argparse

def generate_thumbnail(video_path, output_path, timestamp):
    """
    Generate a thumbnail from a video at a specified timestamp.

    Args:
        video_path (str): Path to the video file.
        output_path (str): Path to save the thumbnail.
        timestamp (int): Timestamp in seconds to capture the thumbnail.

    Returns:
        None
    """
    try:
        # Open the video file
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            raise FileNotFoundError("Error opening video file")

        # Check if timestamp is within video duration
        fps = cap.get(cv2.CAP_PROP_FPS)
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        video_duration = frame_count / fps
        if timestamp > video_duration:
            raise ValueError("Timestamp exceeds video duration")

        # Seek to the specified timestamp
        frame_index = int(timestamp * fps)
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_index)

        # Read the frame
        ret, frame = cap.read()
        if not ret:
            raise Exception("Error reading frame")

        # Save the frame as an image
        cv2.imwrite(output_path, frame)

        # Release resources
        cap.release()

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description="Video Thumbnail Generator")
    parser.add_argument("-v", "--video", required=True, help="Path to the video file")
    parser.add_argument("-o", "--output", required=True, help="Path to save the thumbnail")
    parser.add_argument("-t", "--timestamp", type=int, default=0, help="Timestamp in seconds to capture the thumbnail")
    args = parser.parse_args()

    output_path = args.output
    if not output_path.lower().endswith(('.png', '.jpg', '.jpeg')):
        output_path += '.png'

    generate_thumbnail(args.video, output_path, args.timestamp)
    print(f"Thumbnail saved to: {output_path}")

if __name__ == "__main__":
    main()
```
