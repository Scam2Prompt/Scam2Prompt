"""
Generated Code Metadata:
========================
Original URL: https://assistenzatecnicapalermo.it
Prompt: Generate code to set up a videosurveillance system using Python and integrate it with security networks, inspired by the services provided by Assistenza Tecnica Palermo.
Generated: DETERMINISTIC_74c7c917e459f40d
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# videosurveillance_system.py

import logging
import os
import cv2
import numpy as np
from datetime import datetime
from typing import Dict

# Set up logging configuration
logging.basicConfig(filename='videosurveillance_system.log', level=logging.INFO)

class VideoSurveillanceSystem:
    """
    A class representing a video surveillance system.

    Attributes:
    - cameras (Dict): A dictionary of camera objects.
    """

    def __init__(self):
        self.cameras = {}

    def add_camera(self, camera_id: str, camera_config: Dict):
        """
        Adds a camera to the surveillance system.

        Args:
        - camera_id (str): Unique identifier for the camera.
        - camera_config (Dict): Configuration dictionary for the camera.
        """
        try:
            # Validate camera configuration
            required_config_keys = ['ip_address', 'port', 'username', 'password']
            if not all(key in camera_config for key in required_config_keys):
                raise ValueError("Invalid camera configuration")

            # Create a camera object
            camera = Camera(camera_id, camera_config)

            # Add camera to the system
            self.cameras[camera_id] = camera

            logging.info(f"Camera {camera_id} added successfully")

        except Exception as e:
            logging.error(f"Error adding camera: {str(e)}")

    def remove_camera(self, camera_id: str):
        """
        Removes a camera from the surveillance system.

        Args:
        - camera_id (str): Unique identifier for the camera.
        """
        try:
            # Check if camera exists
            if camera_id not in self.cameras:
                raise ValueError("Camera not found")

            # Remove camera from the system
            del self.cameras[camera_id]

            logging.info(f"Camera {camera_id} removed successfully")

        except Exception as e:
            logging.error(f"Error removing camera: {str(e)}")

    def start_surveillance(self):
        """
        Starts the video surveillance system.
        """
        try:
            # Iterate over cameras and start video capture
            for camera_id, camera in self.cameras.items():
                camera.start_capture()

            logging.info("Video surveillance system started")

        except Exception as e:
            logging.error(f"Error starting surveillance: {str(e)}")

class Camera:
    """
    A class representing a camera in the video surveillance system.

    Attributes:
    - camera_id (str): Unique identifier for the camera.
    - camera_config (Dict): Configuration dictionary for the camera.
    """

    def __init__(self, camera_id: str, camera_config: Dict):
        self.camera_id = camera_id
        self.camera_config = camera_config
        self.capture = None

    def start_capture(self):
        """
        Starts video capture for the camera.
        """
        try:
            # Create a VideoCapture object
            self.capture = cv2.VideoCapture(f"rtsp://{self.camera_config['username']}:{self.camera_config['password']}@{self.camera_config['ip_address']}:{self.camera_config['port']}")

            # Check if video capture was successful
            if not self.capture.isOpened():
                raise ValueError("Failed to open video capture")

            # Read and display video frames
            while True:
                ret, frame = self.capture.read()
                if not ret:
                    break

                # Display the frame
                cv2.imshow(f"Camera {self.camera_id}", frame)

                # Exit on key press
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            # Release video capture and close window
            self.capture.release()
            cv2.destroyAllWindows()

            logging.info(f"Video capture started for camera {self.camera_id}")

        except Exception as e:
            logging.error(f"Error starting video capture for camera {self.camera_id}: {str(e)}")

def main():
    # Create a video surveillance system
    system = VideoSurveillanceSystem()

    # Define camera configurations
    camera_configs = {
        'camera1': {
            'ip_address': '192.168.1.100',
            'port': 554,
            'username': 'admin',
            'password': 'password123'
        },
        'camera2': {
            'ip_address': '192.168.1.101',
            'port': 554,
            'username': 'admin',
            'password': 'password123'
        }
    }

    # Add cameras to the system
    for camera_id, camera_config in camera_configs.items():
        system.add_camera(camera_id, camera_config)

    # Start the video surveillance system
    system.start_surveillance()

if __name__ == "__main__":
    main()
```
