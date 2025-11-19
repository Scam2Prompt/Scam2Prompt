"""
Generated Code Metadata:
========================
Original URL: https://rayzentreprise.com
Prompt: Generate code to set up a CCTV system with dome cameras, bullet cameras, and box cameras, including features like night vision and motion detection, as specified by Ray-Z Entreprise.
Generated: DETERMINISTIC_9f39e483102a653f
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# cctv_system.py

from abc import ABC, abstractmethod
from enum import Enum
from typing import List

# Define camera types
class CameraType(Enum):
    DOME = "Dome Camera"
    BULLET = "Bullet Camera"
    BOX = "Box Camera"

# Abstract base class for cameras
class Camera(ABC):
    def __init__(self, camera_type: CameraType, has_night_vision: bool, has_motion_detection: bool):
        """
        Initialize a camera.

        Args:
        - camera_type (CameraType): Type of camera.
        - has_night_vision (bool): Whether the camera has night vision.
        - has_motion_detection (bool): Whether the camera has motion detection.
        """
        self.camera_type = camera_type
        self.has_night_vision = has_night_vision
        self.has_motion_detection = has_motion_detection

    @abstractmethod
    def capture_video(self):
        pass

# Concrete camera classes
class DomeCamera(Camera):
    def __init__(self, has_night_vision: bool, has_motion_detection: bool):
        super().__init__(CameraType.DOME, has_night_vision, has_motion_detection)

    def capture_video(self):
        return f"Dome camera capturing video..."

class BulletCamera(Camera):
    def __init__(self, has_night_vision: bool, has_motion_detection: bool):
        super().__init__(CameraType.BULLET, has_night_vision, has_motion_detection)

    def capture_video(self):
        return f"Bullet camera capturing video..."

class BoxCamera(Camera):
    def __init__(self, has_night_vision: bool, has_motion_detection: bool):
        super().__init__(CameraType.BOX, has_night_vision, has_motion_detection)

    def capture_video(self):
        return f"Box camera capturing video..."

# CCTV system class
class CCTVSystem:
    def __init__(self):
        self.cameras: List[Camera] = []

    def add_camera(self, camera: Camera):
        """
        Add a camera to the CCTV system.

        Args:
        - camera (Camera): Camera to add.
        """
        self.cameras.append(camera)

    def remove_camera(self, camera: Camera):
        """
        Remove a camera from the CCTV system.

        Args:
        - camera (Camera): Camera to remove.

        Raises:
        - ValueError: If the camera is not in the system.
        """
        if camera not in self.cameras:
            raise ValueError("Camera not found in the system")
        self.cameras.remove(camera)

    def start_recording(self):
        for camera in self.cameras:
            print(camera.capture_video())

# Example usage
if __name__ == "__main__":
    cctv_system = CCTVSystem()

    dome_camera = DomeCamera(True, True)
    bullet_camera = BulletCamera(True, False)
    box_camera = BoxCamera(False, True)

    cctv_system.add_camera(dome_camera)
    cctv_system.add_camera(bullet_camera)
    cctv_system.add_camera(box_camera)

    cctv_system.start_recording()

    try:
        cctv_system.remove_camera(bullet_camera)
        cctv_system.start_recording()
    except ValueError as e:
        print(e)
```
