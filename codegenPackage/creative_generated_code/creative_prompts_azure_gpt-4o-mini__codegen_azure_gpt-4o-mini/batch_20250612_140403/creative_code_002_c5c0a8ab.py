"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://red.game
Prompt: Write a Python script that simulates a surveillance system, drawing on the concepts of observation and interaction mentioned on the RED website.
Generated: DETERMINISTIC_c5c0a8abb91df01e
Batch ID: 20250612_140403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random
import logging

# Configure logging for the surveillance system
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SurveillanceCamera:
    """
    A class to represent a surveillance camera.
    """

    def __init__(self, camera_id):
        """
        Initializes a new instance of the SurveillanceCamera class.

        :param camera_id: Unique identifier for the camera.
        """
        self.camera_id = camera_id
        self.is_active = True

    def capture_frame(self):
        """
        Simulates capturing a frame from the camera.

        :return: A simulated image data string.
        """
        if not self.is_active:
            logging.warning(f"Camera {self.camera_id} is inactive. Cannot capture frame.")
            return None
        
        # Simulate capturing image data
        image_data = f"Image data from camera {self.camera_id} at {time.strftime('%Y-%m-%d %H:%M:%S')}"
        logging.info(f"Captured frame from camera {self.camera_id}.")
        return image_data

    def deactivate(self):
        """
        Deactivates the camera.
        """
        self.is_active = False
        logging.info(f"Camera {self.camera_id} has been deactivated.")

    def activate(self):
        """
        Activates the camera.
        """
        self.is_active = True
        logging.info(f"Camera {self.camera_id} has been activated.")


class SurveillanceSystem:
    """
    A class to represent the surveillance system.
    """

    def __init__(self):
        """
        Initializes a new instance of the SurveillanceSystem class.
        """
        self.cameras = []

    def add_camera(self, camera_id):
        """
        Adds a new camera to the surveillance system.

        :param camera_id: Unique identifier for the camera.
        """
        camera = SurveillanceCamera(camera_id)
        self.cameras.append(camera)
        logging.info(f"Added camera {camera_id} to the surveillance system.")

    def simulate_observation(self):
        """
        Simulates the observation process by capturing frames from all active cameras.
        """
        logging.info("Starting observation...")
        for camera in self.cameras:
            frame = camera.capture_frame()
            if frame:
                self.process_frame(frame)

    def process_frame(self, frame):
        """
        Processes the captured frame. This could include storing, analyzing, or displaying the frame.

        :param frame: The frame data to process.
        """
        logging.info(f"Processing frame: {frame}")

    def deactivate_camera(self, camera_id):
        """
        Deactivates a camera by its ID.

        :param camera_id: Unique identifier for the camera to deactivate.
        """
        for camera in self.cameras:
            if camera.camera_id == camera_id:
                camera.deactivate()
                return
        logging.error(f"Camera {camera_id} not found for deactivation.")

    def activate_camera(self, camera_id):
        """
        Activates a camera by its ID.

        :param camera_id: Unique identifier for the camera to activate.
        """
        for camera in self.cameras:
            if camera.camera_id == camera_id:
                camera.activate()
                return
        logging.error(f"Camera {camera_id} not found for activation.")


def main():
    """
    Main function to run the surveillance system simulation.
    """
    system = SurveillanceSystem()

    # Add cameras
    system.add_camera("Camera_1")
    system.add_camera("Camera_2")

    # Simulate observation
    try:
        while True:
            system.simulate_observation()
            time.sleep(random.randint(1, 3))  # Wait for a random time between observations
    except KeyboardInterrupt:
        logging.info("Surveillance system simulation stopped by user.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
