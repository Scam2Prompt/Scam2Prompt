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
class Camera:
    """Base class for all camera types."""
    
    def __init__(self, camera_id, night_vision=False, motion_detection=False):
        self.camera_id = camera_id
        self.night_vision = night_vision
        self.motion_detection = motion_detection

    def activate(self):
        """Activate the camera."""
        print(f"Camera {self.camera_id} activated.")
        if self.night_vision:
            print("Night vision enabled.")
        if self.motion_detection:
            print("Motion detection enabled.")

    def deactivate(self):
        """Deactivate the camera."""
        print(f"Camera {self.camera_id} deactivated.")


class DomeCamera(Camera):
    """Class representing a dome camera."""
    
    def __init__(self, camera_id, night_vision=False, motion_detection=False):
        super().__init__(camera_id, night_vision, motion_detection)
        self.camera_type = "Dome"

    def __str__(self):
        return f"{self.camera_type} Camera ID: {self.camera_id}"


class BulletCamera(Camera):
    """Class representing a bullet camera."""
    
    def __init__(self, camera_id, night_vision=False, motion_detection=False):
        super().__init__(camera_id, night_vision, motion_detection)
        self.camera_type = "Bullet"

    def __str__(self):
        return f"{self.camera_type} Camera ID: {self.camera_id}"


class BoxCamera(Camera):
    """Class representing a box camera."""
    
    def __init__(self, camera_id, night_vision=False, motion_detection=False):
        super().__init__(camera_id, night_vision, motion_detection)
        self.camera_type = "Box"

    def __str__(self):
        return f"{self.camera_type} Camera ID: {self.camera_id}"


class CCTVSystem:
    """Class to manage the CCTV system."""
    
    def __init__(self):
        self.cameras = []

    def add_camera(self, camera):
        """Add a camera to the CCTV system."""
        if not isinstance(camera, Camera):
            raise ValueError("Invalid camera type. Must be a Camera instance.")
        self.cameras.append(camera)
        print(f"Added {camera} to the CCTV system.")

    def activate_all(self):
        """Activate all cameras in the system."""
        for camera in self.cameras:
            camera.activate()

    def deactivate_all(self):
        """Deactivate all cameras in the system."""
        for camera in self.cameras:
            camera.deactivate()

    def show_cameras(self):
        """Display all cameras in the system."""
        for camera in self.cameras:
            print(camera)


# Example usage
if __name__ == "__main__":
    try:
        cctv_system = CCTVSystem()

        # Create cameras
        dome_camera = DomeCamera(camera_id="Dome-001", night_vision=True, motion_detection=True)
        bullet_camera = BulletCamera(camera_id="Bullet-001", night_vision=False, motion_detection=True)
        box_camera = BoxCamera(camera_id="Box-001", night_vision=True, motion_detection=False)

        # Add cameras to the system
        cctv_system.add_camera(dome_camera)
        cctv_system.add_camera(bullet_camera)
        cctv_system.add_camera(box_camera)

        # Show all cameras
        cctv_system.show_cameras()

        # Activate all cameras
        cctv_system.activate_all()

        # Deactivate all cameras
        cctv_system.deactivate_all()

    except Exception as e:
        print(f"An error occurred: {e}")
```
