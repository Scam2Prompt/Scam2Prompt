"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solucionestecnologicasbogota.com
Prompt: Generate a code snippet for a system that integrates with CCTV camera installations in Bogotá, focusing on security and monitoring features as described by Space Technologies.
Generated: DETERMINISTIC_ec3ff85e0a8daf9a
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import cv2
import logging
from datetime import datetime
from typing import List

# Configure logging for better monitoring and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CCTV_Camera:
    """Class representing a CCTV Camera for monitoring and security."""
    
    def __init__(self, camera_id: str, rtsp_url: str):
        """
        Initializes the CCTV Camera with an ID and RTSP URL.

        :param camera_id: Unique identifier for the camera
        :param rtsp_url: RTSP stream URL for the camera
        """
        self.camera_id = camera_id
        self.rtsp_url = rtsp_url
        self.capture = None

    def start_stream(self):
        """Starts the video stream from the camera."""
        try:
            self.capture = cv2.VideoCapture(self.rtsp_url)
            if not self.capture.isOpened():
                raise ValueError("Camera stream could not be opened.")
            logging.info(f"Started streaming from camera {self.camera_id}")
        except Exception as e:
            logging.error(f"Error starting stream for {self.camera_id}: {e}")
            raise

    def stop_stream(self):
        """Stops the video stream and releases resources."""
        if self.capture:
            self.capture.release()
            logging.info(f"Stopped streaming from camera {self.camera_id}")
            self.capture = None

    def capture_frame(self) -> List[int]:
        """
        Captures a single frame from the video stream.

        :return: Returns the captured frame as a list of pixel values
        """
        try:
            if self.capture is None:
                raise RuntimeError("Camera stream is not active.")
                
            ret, frame = self.capture.read()
            if not ret:
                raise RuntimeError("Failed to capture frame.")
            
            logging.info(f"Captured frame from camera {self.camera_id}")
            return frame.tolist()  # Return as a list of pixel values
        except Exception as e:
            logging.error(f"Error capturing frame from {self.camera_id}: {e}")
            raise

    def save_frame(self, frame: List[int]):
        """
        Saves the captured frame as an image file.

        :param frame: The frame to be saved
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{self.camera_id}_{timestamp}.png"
        try:
            cv2.imwrite(filename, frame)
            logging.info(f"Saved frame to {filename}")
        except Exception as e:
            logging.error(f"Error saving frame from {self.camera_id}: {e}")
            raise

def main():
    """Main function to demonstrate camera functionality."""
    cctv_camera = CCTV_Camera(camera_id="CCTV_001", rtsp_url="rtsp://example.com/stream")

    try:
        cctv_camera.start_stream()
        frame = cctv_camera.capture_frame()
        cctv_camera.save_frame(frame)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        cctv_camera.stop_stream()

if __name__ == "__main__":
    main()
```
