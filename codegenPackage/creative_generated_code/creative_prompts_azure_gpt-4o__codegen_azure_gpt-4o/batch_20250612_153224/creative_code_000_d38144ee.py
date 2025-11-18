"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://insidesafety.com.mx
Prompt: Write Python code to integrate a CCTV system with a control panel for monitoring, referencing the type of systems described on the Inside Safety website.
Generated: DETERMINISTIC_d38144eeafb1f5a7
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
import time

# Configure logging for the application
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)

class CCTVSystem:
    """
    A class representing the CCTV system.
    """
    def __init__(self, cameras):
        """
        Initialize the CCTV system with a list of cameras.

        :param cameras: List of camera IDs or names
        """
        self.cameras = cameras
        self.camera_status = {camera: False for camera in cameras}  # All cameras are initially inactive
        logging.info("CCTV system initialized with cameras: %s", cameras)

    def activate_camera(self, camera_id):
        """
        Activate a specific camera.

        :param camera_id: ID or name of the camera to activate
        :raises ValueError: If the camera ID is invalid
        """
        if camera_id not in self.cameras:
            raise ValueError(f"Invalid camera ID: {camera_id}")
        self.camera_status[camera_id] = True
        logging.info("Camera '%s' activated.", camera_id)

    def deactivate_camera(self, camera_id):
        """
        Deactivate a specific camera.

        :param camera_id: ID or name of the camera to deactivate
        :raises ValueError: If the camera ID is invalid
        """
        if camera_id not in self.cameras:
            raise ValueError(f"Invalid camera ID: {camera_id}")
        self.camera_status[camera_id] = False
        logging.info("Camera '%s' deactivated.", camera_id)

    def get_camera_status(self):
        """
        Get the current status of all cameras.

        :return: Dictionary representing the activation status of each camera
        """
        return self.camera_status


class ControlPanel:
    """
    A class representing the control panel for monitoring the CCTV system.
    """
    def __init__(self, cctv_system):
        """
        Initialize the control panel with a CCTV system instance.

        :param cctv_system: An instance of CCTVSystem
        """
        self.cctv_system = cctv_system
        logging.info("Control Panel connected to CCTV system.")

    def display_status(self):
        """
        Display the activation status of all cameras.
        """
        status = self.cctv_system.get_camera_status()
        logging.info("Displaying camera status:")
        for camera_id, is_active in status.items():
            state = "Active" if is_active else "Inactive"
            print(f"Camera '{camera_id}': {state}")

    def toggle_camera(self, camera_id):
        """
        Toggle the activation state of a specific camera.

        :param camera_id: ID or name of the camera to toggle
        """
        try:
            current_status = self.cctv_system.get_camera_status()[camera_id]
            if current_status:
                self.cctv_system.deactivate_camera(camera_id)
            else:
                self.cctv_system.activate_camera(camera_id)
        except ValueError as e:
            logging.error("Error toggling camera: %s", e)
            print(f"Failed to toggle camera: {e}")


if __name__ == "__main__":
    # Example usage of the CCTV system and control panel

    # Define the cameras available in the CCTV system
    camera_ids = ["Camera1", "Camera2", "Camera3"]

    # Initialize the CCTV system
    cctv_system = CCTVSystem(camera_ids)

    # Initialize the control panel and connect it to the CCTV system
    control_panel = ControlPanel(cctv_system)

    # Simulate user interaction with the control panel
    try:
        control_panel.display_status()
        control_panel.toggle_camera("Camera1")
        control_panel.toggle_camera("Camera2")
        control_panel.display_status()
        control_panel.toggle_camera("Camera4")  # Invalid camera ID for demonstration
    except Exception as e:
        logging.error("An unexpected error occurred: %s", e)

    # Simulate periodic status updates
    for _ in range(3):
        control_panel.display_status()
        time.sleep(5)  # Wait 5 seconds before the next update
```
