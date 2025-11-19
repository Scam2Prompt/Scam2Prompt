"""
Generated Code Metadata:
========================
Original URL: https://solucionestecnologicasbogota.com
Prompt: Provide code examples for integrating high-quality surveillance cameras into a security system, including real-time video streaming and storage, based on the camera installation services offered by Space Technologies Bogotá.
Generated: DETERMINISTIC_34b591c1c475736a
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Surveillance Camera Integration Code**
======================================

### Prerequisites

* Python 3.8+
* OpenCV 4.5+
* numpy 1.20+
* datetime  (built-in)

### Code
```python
import cv2
import numpy as np
import datetime
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SurveillanceCamera:
    def __init__(self, camera_id, rtsp_url, resolution=(640, 480)):
        """
        Initialize a surveillance camera.

        Args:
            camera_id (str): Unique camera ID.
            rtsp_url (str): RTSP URL for the camera.
            resolution (tuple): Video resolution (default: (640, 480)).
        """
        self.camera_id = camera_id
        self.rtsp_url = rtsp_url
        self.resolution = resolution
        self.cap = cv2.VideoCapture(rtsp_url)

        if not self.cap.isOpened():
            logger.error(f"Failed to open camera {camera_id} at {rtsp_url}")
            raise Exception(f"Failed to open camera {camera_id} at {rtsp_url}")

    def start_streaming(self):
        """
        Start real-time video streaming from the camera.
        """
        while True:
            ret, frame = self.cap.read()
            if not ret:
                logger.warning(f"Failed to read frame from camera {self.camera_id}")
                continue

            # Resize frame to specified resolution
            frame = cv2.resize(frame, self.resolution)

            # Display frame
            cv2.imshow(f"Camera {self.camera_id}", frame)

            # Exit on key press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

    def store_video(self, output_file):
        """
        Store video from the camera to a file.

        Args:
            output_file (str): Output file path.
        """
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(output_file, fourcc, 20.0, self.resolution)

        while True:
            ret, frame = self.cap.read()
            if not ret:
                logger.warning(f"Failed to read frame from camera {self.camera_id}")
                continue

            # Resize frame to specified resolution
            frame = cv2.resize(frame, self.resolution)

            # Write frame to output file
            out.write(frame)

            # Display frame
            cv2.imshow(f"Camera {self.camera_id}", frame)

            # Exit on key press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        out.release()
        cv2.destroyAllWindows()

def main():
    # Define camera installation services offered by Space Technologies Bogotá
    cameras = [
        {"camera_id": "camera1", "rtsp_url": "rtsp://example.com/camera1"},
        {"camera_id": "camera2", "rtsp_url": "rtsp://example.com/camera2"},
    ]

    for camera in cameras:
        try:
            cam = SurveillanceCamera(camera["camera_id"], camera["rtsp_url"])
            cam.start_streaming()
            # Store video to file
            output_file = f"video_{camera['camera_id']}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.avi"
            cam.store_video(output_file)
        except Exception as e:
            logger.error(f"Error occurred while processing camera {camera['camera_id']}: {str(e)}")

if __name__ == "__main__":
    main()
```
### Requirements File
```makefile
# requirements.txt

opencv-python==4.5.5.64
numpy==1.20.2
```
### Usage
```bash
# Install dependencies
pip install -r requirements.txt

# Run the code
python surveillance_camera_integration.py
```
