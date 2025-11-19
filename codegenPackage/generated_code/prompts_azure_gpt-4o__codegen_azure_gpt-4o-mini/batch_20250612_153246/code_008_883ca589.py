"""
Generated Code Metadata:
========================
Original URL: https://icgard.ir
Prompt: Write code to manage and store video recordings from DVR 4ch NOVA 5MP devices, ensuring efficient compression and retrieval.
Generated: DETERMINISTIC_883ca589e6e57dac
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import cv2
import numpy as np
from datetime import datetime
from typing import List, Optional

class DVRVideoManager:
    def __init__(self, storage_directory: str):
        """
        Initializes the DVRVideoManager with a specified storage directory.

        :param storage_directory: Directory where video recordings will be stored.
        """
        self.storage_directory = storage_directory
        self.ensure_storage_directory()

    def ensure_storage_directory(self):
        """Ensures that the storage directory exists."""
        if not os.path.exists(self.storage_directory):
            os.makedirs(self.storage_directory)

    def save_video(self, video_data: np.ndarray, channel_id: int, timestamp: Optional[datetime] = None):
        """
        Saves a video recording to the storage directory.

        :param video_data: The video data as a NumPy array.
        :param channel_id: The channel ID for the DVR.
        :param timestamp: Optional timestamp for naming the file. If None, current time is used.
        """
        if timestamp is None:
            timestamp = datetime.now()
        
        filename = f"channel_{channel_id}_{timestamp.strftime('%Y%m%d_%H%M%S')}.mp4"
        filepath = os.path.join(self.storage_directory, filename)

        # Define video codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        height, width = video_data.shape[1:3]
        out = cv2.VideoWriter(filepath, fourcc, 30.0, (width, height))

        try:
            for frame in video_data:
                out.write(frame)
        except Exception as e:
            print(f"Error while saving video: {e}")
        finally:
            out.release()

    def retrieve_video(self, filename: str) -> Optional[np.ndarray]:
        """
        Retrieves a video recording from the storage directory.

        :param filename: The name of the video file to retrieve.
        :return: The video data as a NumPy array or None if the file does not exist.
        """
        filepath = os.path.join(self.storage_directory, filename)

        if not os.path.exists(filepath):
            print(f"File {filename} does not exist.")
            return None

        video_data = []
        cap = cv2.VideoCapture(filepath)

        if not cap.isOpened():
            print(f"Error opening video file: {filepath}")
            return None

        try:
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                video_data.append(frame)
        except Exception as e:
            print(f"Error while retrieving video: {e}")
        finally:
            cap.release()

        return np.array(video_data)

    def list_videos(self) -> List[str]:
        """
        Lists all video files in the storage directory.

        :return: A list of video filenames.
        """
        return [f for f in os.listdir(self.storage_directory) if f.endswith('.mp4')]

# Example usage:
if __name__ == "__main__":
    # Initialize the video manager with a specified storage directory
    video_manager = DVRVideoManager(storage_directory='dvr_recordings')

    # Simulate saving a video (replace with actual video data)
    dummy_video_data = np.random.randint(0, 255, (100, 480, 640, 3), dtype=np.uint8)  # Dummy video data
    video_manager.save_video(dummy_video_data, channel_id=1)

    # List saved videos
    print("Saved videos:", video_manager.list_videos())

    # Retrieve a video
    retrieved_video = video_manager.retrieve_video("channel_1_20231001_120000.mp4")
    if retrieved_video is not None:
        print("Video retrieved successfully.")
```
