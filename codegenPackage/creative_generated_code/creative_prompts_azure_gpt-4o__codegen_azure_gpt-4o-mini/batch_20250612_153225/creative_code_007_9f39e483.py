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

```python
class Camera:
    """Base class for all camera types."""
    def __init__(self, model, camera_type):
        """
        Initializes a new camera.

        Args:
            model (str): The model of the camera.
            camera_type (str): The type of the camera (Dome, Bullet, Box).
        """
        self.model = model
        self.camera_type = camera_type
        self.night_vision = False
        self.motion_detection = False

    def enable_night_vision(self):
        """Enables night vision for the camera."""
        self.night_vision = True
        print(f"Night vision enabled for {self.model} ({self.camera_type})")

    def disable_night_vision(self):
        """Disables night vision for the camera."""
        self.night_vision = False
        print(f"Night vision disabled for {self.model} ({self.camera_type})")

    def enable_motion_detection(self):
        """Enables motion detection for the camera."""
        self.motion_detection = True
        print(f"Motion detection enabled for {self.model} ({self.camera_type})")

    def disable_motion_detection(self):
        """Disables motion detection for the camera."""
        self.motion_detection = False
        print(f"Motion detection disabled for {self.model} ({self.camera_type})")


class DomeCamera(Camera):
    """Class representing a dome camera."""
    def __init__(self, model):
        super().__init__(model, camera_type='Dome')


class BulletCamera(Camera):
    """Class representing a bullet camera."""
    def __init__(self, model):
        super().__init__(model, camera_type='Bullet')


class BoxCamera(Camera):
    """Class representing a box camera."""
    def __init__(self, model):
        super().__init__(model, camera_type='Box')


class CCTVSystem:
    """Class representing a CCTV system."""
    def __init__(self):
        """
        Initializes the CCTV system with an empty camera list.
        """
        self.cameras = []

    def add_camera(self, camera):
        """
        Adds a camera to the CCTV system.

        Args:
            camera (Camera): The camera to add.
        """
        if not isinstance(camera, Camera):
            raise ValueError("Only instances of Camera can be added.")
        self.cameras.append(camera)
        print(f"{camera.camera_type} camera {camera.model} added to the system.")

    def configure_cameras(self):
        """Configures all cameras in the system."""
        for camera in self.cameras:
            camera.enable_night_vision()
            camera.enable_motion_detection()

    def display_system_info(self):
        """Displays the information of all cameras in the system."""
        if not self.cameras:
            print("No cameras in the system.")
            return
        
        for camera in self.cameras:
            print(f"{camera.camera_type} | Model: {camera.model} | Night Vision: {camera.night_vision} | Motion Detection: {camera.motion_detection}")


if __name__ == "__main__":
    try:
        # Create CCTV system
        cctv_system = CCTVSystem()

        # Create cameras
        dome_camera = DomeCamera("Dome-001")
        bullet_camera = BulletCamera("Bullet-001")
        box_camera = BoxCamera("Box-001")

        # Add cameras to the CCTV system
        cctv_system.add_camera(dome_camera)
        cctv_system.add_camera(bullet_camera)
        cctv_system.add_camera(box_camera)

        # Configure cameras
        cctv_system.configure_cameras()

        # Display system information
        cctv_system.display_system_info()

    except Exception as e:
        print(f"An error occurred: {e}")
```
