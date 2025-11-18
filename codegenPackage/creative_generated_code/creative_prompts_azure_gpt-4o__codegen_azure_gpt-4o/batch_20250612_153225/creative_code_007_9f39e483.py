"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rayzentreprise.com
Prompt: Generate code to set up a CCTV system with dome cameras, bullet cameras, and box cameras, including features like night vision and motion detection, as specified by Ray-Z Entreprise.
Generated: DETERMINISTIC_9f39e483102a653f
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's the clean, well-documented, production-ready code for setting up a CCTV system with dome cameras, bullet cameras, and box cameras, including night vision and motion detection. This example uses Python:

```python
import time
import logging
from abc import ABC, abstractmethod

# Set up logging for the CCTV system
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Abstract base class for Camera
class Camera(ABC):
    """
    Abstract base class for all camera types.
    """
    def __init__(self, camera_id, location):
        self.camera_id = camera_id
        self.location = location
        self.is_night_vision_enabled = False
        self.is_motion_detection_enabled = False

    @abstractmethod
    def display_info(self):
        """
        Displays the camera information.
        """
        pass

    def enable_night_vision(self):
        """
        Enables night vision for the camera.
        """
        self.is_night_vision_enabled = True
        logging.info(f'Night vision enabled for Camera ID {self.camera_id}.')

    def disable_night_vision(self):
        """
        Disables night vision for the camera.
        """
        self.is_night_vision_enabled = False
        logging.info(f'Night vision disabled for Camera ID {self.camera_id}.')

    def enable_motion_detection(self):
        """
        Enables motion detection for the camera.
        """
        self.is_motion_detection_enabled = True
        logging.info(f'Motion detection enabled for Camera ID {self.camera_id}.')

    def disable_motion_detection(self):
        """
        Disables motion detection for the camera.
        """
        self.is_motion_detection_enabled = False
        logging.info(f'Motion detection disabled for Camera ID {self.camera_id}.')

# Dome Camera Class
class DomeCamera(Camera):
    def display_info(self):
        logging.info(f'Dome Camera - ID: {self.camera_id}, Location: {self.location}, '
                     f'Night Vision: {self.is_night_vision_enabled}, Motion Detection: {self.is_motion_detection_enabled}')

# Bullet Camera Class
class BulletCamera(Camera):
    def display_info(self):
        logging.info(f'Bullet Camera - ID: {self.camera_id}, Location: {self.location}, '
                     f'Night Vision: {self.is_night_vision_enabled}, Motion Detection: {self.is_motion_detection_enabled}')

# Box Camera Class
class BoxCamera(Camera):
    def display_info(self):
        logging.info(f'Box Camera - ID: {self.camera_id}, Location: {self.location}, '
                     f'Night Vision: {self.is_night_vision_enabled}, Motion Detection: {self.is_motion_detection_enabled}')

# CCTV System Class
class CCTVSystem:
    """
    Manages the entire CCTV system.
    """
    def __init__(self):
        self.cameras = {}

    def add_camera(self, camera_type, camera_id, location):
        """
        Adds a camera to the system.
        """
        try:
            if camera_id in self.cameras:
                raise ValueError(f'Camera ID {camera_id} already exists.')

            if camera_type == 'Dome':
                self.cameras[camera_id] = DomeCamera(camera_id, location)
            elif camera_type == 'Bullet':
                self.cameras[camera_id] = BulletCamera(camera_id, location)
            elif camera_type == 'Box':
                self.cameras[camera_id] = BoxCamera(camera_id, location)
            else:
                raise ValueError(f'Unsupported camera type: {camera_type}')

            logging.info(f'Camera ID {camera_id} added successfully. Type: {camera_type}, Location: {location}')
        except Exception as e:
            logging.error(f'Error adding camera: {e}')

    def remove_camera(self, camera_id):
        """
        Removes a camera from the system.
        """
        try:
            if camera_id not in self.cameras:
                raise ValueError(f'Camera ID {camera_id} does not exist.')

            del self.cameras[camera_id]
            logging.info(f'Camera ID {camera_id} removed successfully.')
        except Exception as e:
            logging.error(f'Error removing camera: {e}')

    def list_cameras(self):
        """
        Lists all cameras in the system.
        """
        if not self.cameras:
            logging.info('No cameras in the system.')
            return

        logging.info('Listing all cameras:')
        for camera_id, camera in self.cameras.items():
            camera.display_info()

    def enable_features(self, camera_id, enable_night_vision=False, enable_motion_detection=False):
        """
        Enables specified features (e.g., night vision, motion detection) for a given camera.
        """
        try:
            if camera_id not in self.cameras:
                raise ValueError(f'Camera ID {camera_id} does not exist.')

            camera = self.cameras[camera_id]
            if enable_night_vision:
                camera.enable_night_vision()
            if enable_motion_detection:
                camera.enable_motion_detection()
        except Exception as e:
            logging.error(f'Error enabling features for Camera ID {camera_id}: {e}')

# Main execution (example setup)
if __name__ == "__main__":
    # Initialize CCTV system
    cctv_system = CCTVSystem()

    # Add cameras
    cctv_system.add_camera(camera_type='Dome', camera_id='D001', location='Entrance')
    cctv_system.add_camera(camera_type='Bullet', camera_id='B001', location='Parking Lot')
    cctv_system.add_camera(camera_type='Box', camera_id='BX001', location='Warehouse')

    # Enable features on specific cameras
    cctv_system.enable_features(camera_id='D001', enable_night_vision=True, enable_motion_detection=True)
    cctv_system.enable_features(camera_id='B001', enable_motion_detection=True)

    # List all cameras in the system
    cctv_system.list_cameras()

    # Remove a camera
    cctv_system.remove_camera(camera_id='BX001')

    # Final listing of cameras
    cctv_system.list_cameras()
```

This code sets up a robust system for managing three types of cameras with features like night vision and motion detection, following best practices for clarity, error handling, and scalability.
