"""
Generated Code Metadata:
========================
Original URL: https://donturesystems.co.ke
Prompt: Design a basic CCTV surveillance system for a small business in Kenya using AI-powered cameras with night vision and motion detection.
Generated: DETERMINISTIC_b005b6376f1c465f
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# cctv_surveillance_system.py

import cv2
import numpy as np
from datetime import datetime
import logging
import os

# Set up logging configuration
logging.basicConfig(filename='cctv_surveillance.log', level=logging.INFO)

class Camera:
    def __init__(self, camera_id, ip_address):
        """
        Initialize a camera object.

        Args:
            camera_id (int): Unique identifier for the camera.
            ip_address (str): IP address of the camera.
        """
        self.camera_id = camera_id
        self.ip_address = ip_address
        self.cap = cv2.VideoCapture(ip_address)

    def is_open(self):
        """
        Check if the camera is open.

        Returns:
            bool: True if the camera is open, False otherwise.
        """
        return self.cap.isOpened()

    def read_frame(self):
        """
        Read a frame from the camera.

        Returns:
            numpy.ndarray: The frame read from the camera.
        """
        ret, frame = self.cap.read()
        if not ret:
            logging.error(f"Failed to read frame from camera {self.camera_id}")
            return None
        return frame

    def release(self):
        """
        Release the camera resource.
        """
        self.cap.release()

class MotionDetector:
    def __init__(self, sensitivity=0.5):
        """
        Initialize a motion detector object.

        Args:
            sensitivity (float, optional): Sensitivity of the motion detector. Defaults to 0.5.
        """
        self.sensitivity = sensitivity

    def detect_motion(self, frame1, frame2):
        """
        Detect motion between two frames.

        Args:
            frame1 (numpy.ndarray): The first frame.
            frame2 (numpy.ndarray): The second frame.

        Returns:
            bool: True if motion is detected, False otherwise.
        """
        frame_diff = cv2.absdiff(frame1, frame2)
        gray = cv2.cvtColor(frame_diff, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (21, 21), 0)
        thresh = cv2.threshold(blur, 25, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.dilate(thresh, None, iterations=2)
        contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            if cv2.contourArea(contour) > 700:
                return True
        return False

class NightVision:
    def __init__(self):
        """
        Initialize a night vision object.
        """
        pass

    def enhance_night_vision(self, frame):
        """
        Enhance night vision for a given frame.

        Args:
            frame (numpy.ndarray): The frame to enhance.

        Returns:
            numpy.ndarray: The enhanced frame.
        """
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)
        v = cv2.convertScaleAbs(v, alpha=1.5, beta=0)
        v[v > 255] = 255
        v[v < 0] = 0
        enhanced_frame = cv2.merge([h, s, v])
        enhanced_frame = cv2.cvtColor(enhanced_frame, cv2.COLOR_HSV2BGR)
        return enhanced_frame

def main():
    # Define camera IP addresses
    camera_ips = ["192.168.1.100", "192.168.1.101"]

    # Create camera objects
    cameras = []
    for i, ip in enumerate(camera_ips):
        camera = Camera(i, ip)
        if not camera.is_open():
            logging.error(f"Failed to open camera {i} at IP {ip}")
            continue
        cameras.append(camera)

    # Create motion detector and night vision objects
    motion_detector = MotionDetector()
    night_vision = NightVision()

    while True:
        for camera in cameras:
            frame = camera.read_frame()
            if frame is None:
                continue

            # Enhance night vision
            enhanced_frame = night_vision.enhance_night_vision(frame)

            # Detect motion
            if hasattr(camera, 'previous_frame'):
                motion_detected = motion_detector.detect_motion(camera.previous_frame, frame)
                if motion_detected:
                    logging.info(f"Motion detected by camera {camera.camera_id}")
                    # Save frame to file
                    filename = f"motion_detected_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
                    cv2.imwrite(os.path.join("motion_frames", filename), frame)
            camera.previous_frame = frame

            # Display enhanced frame
            cv2.imshow(f"Camera {camera.camera_id}", enhanced_frame)

        # Exit on key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release camera resources
    for camera in cameras:
        camera.release()

    # Close all OpenCV windows
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
```
