"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://icgard.ir
Prompt: Write code to manage and store video recordings from DVR 4ch NOVA 5MP devices, ensuring efficient compression and retrieval.
Generated: DETERMINISTIC_883ca589e6e57dac
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import cv2
import datetime
import logging
from typing import List, Tuple

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DVRVideoManager:
    """
    A class to manage and store video recordings from DVR 4ch NOVA 5MP devices.
    It handles video compression and retrieval efficiently.
    """
    
    def __init__(self, storage_path: str):
        """
        Initializes the DVRVideoManager with the specified storage path.

        :param storage_path: The path to the directory where videos will be stored.
        """
        self.storage_path = storage_path
        # Ensure storage directory exists
        os.makedirs(self.storage_path, exist_ok=True)

    def compress_video(self, input_file: str, output_file: str) -> None:
        """
        Compresses the video using OpenCV and saves it to the specified output path.

        :param input_file: Path to the input video file.
        :param output_file: Path to the output compressed video file.
        :raises FileNotFoundError: If the input file does not exist.
        :raises Exception: For any other errors during video processing.
        """
        if not os.path.exists(input_file):
            logging.error(f"Input file not found: {input_file}")
            raise FileNotFoundError(f"Input file not found: {input_file}")
        
        try:
            # Open the input video
            cap = cv2.VideoCapture(input_file)
            if not cap.isOpened():
                raise Exception("Could not open the input video file.")

            # Get video dimensions and frame rate
            frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            fps = cap.get(cv2.CAP_PROP_FPS)

            # Define the codec and create VideoWriter object
            fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use MP4 codec
            out = cv2.VideoWriter(output_file, fourcc, fps, (frame_width, frame_height))

            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                out.write(frame)

            # Release resources
            cap.release()
            out.release()
            logging.info(f"Video compressed and saved to: {output_file}")

        except Exception as e:
            logging.error(f"Error during video compression: {e}")
            raise

    def retrieve_videos(self) -> List[Tuple[str, datetime.datetime]]:
        """
        Retrieves a list of video files stored in the storage path.

        :return: A list of tuples containing video file names and their modification dates.
        """
        videos = []
        try:
            # Iterate through files in storage path
            for file_name in os.listdir(self.storage_path):
                if file_name.endswith('.mp4'):  # Check for MP4 files
                    file_path = os.path.join(self.storage_path, file_name)
                    mod_time = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
                    videos.append((file_name, mod_time))
            logging.info("Video retrieval completed.")
        except Exception as e:
            logging.error(f"Error retrieving videos: {e}")
            raise

        return videos

# Example usage
if __name__ == "__main__":
    storage_dir = "recordings"
    video_manager = DVRVideoManager(storage_path=storage_dir)

    # Compress a video
    try:
        video_manager.compress_video("input_video.mp4", os.path.join(storage_dir, "compressed_video.mp4"))
    except Exception as e:
        logging.error(str(e))

    # Retrieve videos
    try:
        stored_videos = video_manager.retrieve_videos()
        for video in stored_videos:
            print(f"Video: {video[0]}, Modified: {video[1]}")
    except Exception as e:
        logging.error(str(e))
```
