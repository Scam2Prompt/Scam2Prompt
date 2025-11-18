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
import datetime
import cv2  # OpenCV for video processing

class DVRVideoManager:
    """
    A class to manage and store video recordings from DVR 4ch NOVA 5MP devices.
    Ensures efficient compression and retrieval of stored recordings.
    """
    def __init__(self, storage_path: str):
        """
        Initializes the DVRVideoManager.
        :param storage_path: The root directory where video files will be stored.
        """
        self.storage_path = storage_path
        os.makedirs(self.storage_path, exist_ok=True)  # Create storage directory if it doesn't exist
    
    def compress_video(self, input_file: str, output_file: str, codec: str = "XVID", resolution=(1280, 720), fps=30):
        """
        Compresses the video to reduce storage usage while maintaining reasonable quality.
        :param input_file: Path to the input video file.
        :param output_file: Path to the output compressed video file.
        :param codec: Compression codec to use (default: XVID).
        :param resolution: Target resolution for the compressed video (default: 1280x720).
        :param fps: Target frames per second for the compressed video.
        """
        try:
            # Open the input video file
            cap = cv2.VideoCapture(input_file)
            if not cap.isOpened():
                raise ValueError(f"Failed to open video file: {input_file}")
            
            # Get video properties
            fourcc = cv2.VideoWriter_fourcc(*codec)
            width, height = resolution
            out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))
            
            while True:
                ret, frame = cap.read()
                if not ret:
                    break
                # Resize the frame to target resolution
                resized_frame = cv2.resize(frame, (width, height))
                # Write the compressed frame to the output file
                out.write(resized_frame)

            cap.release()
            out.release()
        except Exception as e:
            print(f"Error during video compression: {e}")
    
    def store_recording(self, input_file: str, camera_id: str):
        """
        Stores a recording in the designated folder structure based on date and camera ID.
        :param input_file: Path to the input video file.
        :param camera_id: Identifier for the camera (e.g., "Camera1").
        """
        try:
            # Get current date for folder structure
            current_date = datetime.datetime.now().strftime("%Y-%m-%d")
            camera_folder = os.path.join(self.storage_path, camera_id, current_date)
            os.makedirs(camera_folder, exist_ok=True)  # Create folder structure if it doesn't exist
            
            # Define the output file path
            recording_name = f"{datetime.datetime.now().strftime('%H-%M-%S')}_recording.mp4"
            output_file = os.path.join(camera_folder, recording_name)
            
            # Compress and store the video
            self.compress_video(input_file, output_file)
            print(f"Recording saved at: {output_file}")
        except Exception as e:
            print(f"Error storing recording: {e}")
    
    def retrieve_recording(self, camera_id: str, date: str) -> list:
        """
        Retrieves a list of recordings for the given camera ID and date.
        :param camera_id: Identifier for the camera.
        :param date: Date in YYYY-MM-DD format to filter recordings.
        :return: List of file paths for the recordings.
        """
        try:
            # Define the folder path based on camera ID and date
            camera_folder = os.path.join(self.storage_path, camera_id, date)
            if not os.path.exists(camera_folder):
                raise FileNotFoundError(f"No recordings found for Camera '{camera_id}' on {date}")
            
            # Retrieve all video files in the folder
            recordings = [os.path.join(camera_folder, f) for f in os.listdir(camera_folder) if f.endswith(".mp4")]
            return recordings
        except Exception as e:
            print(f"Error retrieving recordings: {e}")
            return []

# Example usage:
if __name__ == "__main__":
    manager = DVRVideoManager(storage_path="./recordings")
    
    # Compress and store a sample video
    manager.store_recording(input_file="sample_video.mp4", camera_id="Camera1")
    
    # Retrieve recordings for a specific camera and date
    recordings = manager.retrieve_recording(camera_id="Camera1", date="2023-10-05")
    print("Retrieved recordings:", recordings)
```
