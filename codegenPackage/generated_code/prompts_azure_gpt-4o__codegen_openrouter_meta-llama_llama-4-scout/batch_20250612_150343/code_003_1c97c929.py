"""
Generated Code Metadata:
========================
Original URL: https://starknet.in
Prompt: Create a surveillance system for traffic monitoring using the features outlined in Starknet IT Solutions' surveillance and spy services.
Generated: DETERMINISTIC_1c97c9299545a6cd
Batch ID: 20250612_150343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# surveillance_system.py

import cv2
import numpy as np
from datetime import datetime
import logging

# Set up logging configuration
logging.basicConfig(filename='surveillance.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TrafficCamera:
    def __init__(self, camera_id, camera_url):
        """
        Initialize a TrafficCamera object.

        Args:
        - camera_id (int): Unique identifier for the camera.
        - camera_url (str): URL or path to the camera feed.
        """
        self.camera_id = camera_id
        self.camera_url = camera_url
        self.capture = cv2.VideoCapture(camera_url)

    def __del__(self):
        """
        Release the camera capture on object destruction.
        """
        self.capture.release()

    def is_camera_open(self):
        """
        Check if the camera is open.

        Returns:
        - bool: True if the camera is open, False otherwise.
        """
        return self.capture.isOpened()

    def read_frame(self):
        """
        Read a frame from the camera.

        Returns:
        - frame (numpy.ndarray): The read frame, or None if the camera is not open.
        """
        if not self.is_camera_open():
            logging.error(f"Camera {self.camera_id} is not open.")
            return None
        ret, frame = self.capture.read()
        if not ret:
            logging.warning(f"Failed to read frame from camera {self.camera_id}.")
            return None
        return frame

class MotionDetector:
    def __init__(self, sensitivity=0.05):
        """
        Initialize a MotionDetector object.

        Args:
        - sensitivity (float): Sensitivity of the motion detection (default: 0.05).
        """
        self.sensitivity = sensitivity
        self.prev_frame = None

    def detect_motion(self, frame):
        """
        Detect motion in a frame.

        Args:
        - frame (numpy.ndarray): The frame to detect motion in.

        Returns:
        - bool: True if motion is detected, False otherwise.
        """
        if self.prev_frame is None:
            self.prev_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            return False

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame_diff = cv2.absdiff(self.prev_frame, gray)
        self.prev_frame = gray

        thresh = cv2.threshold(frame_diff, 25, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.dilate(thresh, None, iterations=2)

        contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        motion_detected = False
        for contour in contours:
            if cv2.contourArea(contour) > 1000:
                motion_detected = True
                break

        if motion_detected:
            logging.info("Motion detected.")

        return motion_detected

class SurveillanceSystem:
    def __init__(self):
        """
        Initialize a SurveillanceSystem object.
        """
        self.cameras = {}

    def add_camera(self, camera_id, camera_url):
        """
        Add a camera to the surveillance system.

        Args:
        - camera_id (int): Unique identifier for the camera.
        - camera_url (str): URL or path to the camera feed.
        """
        self.cameras[camera_id] = TrafficCamera(camera_id, camera_url)

    def start_monitoring(self):
        """
        Start monitoring all cameras in the surveillance system.
        """
        for camera_id, camera in self.cameras.items():
            if not camera.is_camera_open():
                logging.error(f"Failed to open camera {camera_id}.")
                continue

            motion_detector = MotionDetector()

            while True:
                frame = camera.read_frame()
                if frame is None:
                    break

                motion_detected = motion_detector.detect_motion(frame)
                if motion_detected:
                    # Perform actions when motion is detected (e.g., save frame, send alert)
                    cv2.imwrite(f"motion_detected_{camera_id}_{datetime.now().strftime('%Y%m%d%H%M%S')}.jpg", frame)

                # Display the frame
                cv2.imshow(f"Camera {camera_id}", frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            cv2.destroyAllWindows()

if __name__ == "__main__":
    surveillance_system = SurveillanceSystem()
    surveillance_system.add_camera(1, "rtsp://example.com/camera1")
    surveillance_system.add_camera(2, "rtsp://example.com/camera2")
    surveillance_system.start_monitoring()
```
