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
import cv2
import numpy as np
import logging

# Setting up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CCTVSystem:
    def __init__(self, camera_index=0):
        """
        Initializes the CCTV system with a specified camera index.
        
        :param camera_index: Index of the camera to be used (default is 0 for the first camera).
        """
        self.camera_index = camera_index
        self.capture = None
        self.is_running = False

    def start_camera(self):
        """
        Starts the camera feed and begins monitoring.
        """
        try:
            self.capture = cv2.VideoCapture(self.camera_index)
            if not self.capture.isOpened():
                raise ValueError("Camera could not be opened.")
            self.is_running = True
            logging.info("Camera started successfully.")

            while self.is_running:
                ret, frame = self.capture.read()
                if not ret:
                    raise RuntimeError("Failed to read frame from camera.")
                
                self.process_frame(frame)

        except Exception as e:
            logging.error(f"An error occurred while starting the camera: {e}")
            self.stop_camera()

    def process_frame(self, frame):
        """
        Processes and displays the captured frame.
        
        :param frame: The current frame captured from the camera.
        """
        # Add any processing logic here (e.g., motion detection, object recognition)
        cv2.imshow('CCTV Feed', frame)

        # Exit on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            self.stop_camera()

    def stop_camera(self):
        """
        Stops the camera feed and releases resources.
        """
        if self.capture is not None:
            self.capture.release()
            cv2.destroyAllWindows()
            self.is_running = False
            logging.info("Camera stopped successfully.")

def main():
    """
    Main function to run the CCTV system.
    """
    cctv_system = CCTVSystem(camera_index=0)  # Replace with actual camera index as needed
    cctv_system.start_camera()

if __name__ == "__main__":
    main()
```

Make sure to install OpenCV before running the code using the following command:
```bash
pip install opencv-python
```
