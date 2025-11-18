"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://teslavision.us
Prompt: Suggest tools or frameworks for integrating real-time image processing into an autonomous driving system similar to Tesla Vision.
Generated: DETERMINISTIC_d84dd58d9ce6f63b
Batch ID: 20250612_145423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for real-time image processing
import cv2  # OpenCV for image processing
import numpy as np  # Numpy for numerical operations
import time  # Time for timing operations

class RealTimeImageProcessor:
    """
    A class to handle real-time image processing for an autonomous driving system.
    """

    def __init__(self, camera_index=0):
        """
        Initializes the RealTimeImageProcessor with a specified camera index.
        
        :param camera_index: Index of the camera to be used for capturing video
        """
        self.camera_index = camera_index
        self.cap = None

    def start_camera(self):
        """
        Starts the camera for real-time video capturing.
        """
        try:
            self.cap = cv2.VideoCapture(self.camera_index)
            if not self.cap.isOpened():
                raise ValueError("Camera could not be opened.")
        except Exception as e:
            print(f"Error initializing camera: {e}")
            self.cleanup()

    def process_frame(self, frame):
        """
        Processes a single video frame (e.g., converting to grayscale and detecting edges).
        
        :param frame: Input frame from the camera
        :return: Processed frame
        """
        try:
            # Convert frame to grayscale
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # Apply Canny edge detection
            edges = cv2.Canny(gray_frame, 100, 200)
            return edges
        except Exception as e:
            print(f"Error processing frame: {e}")
            return None

    def run(self):
        """
        Main loop for capturing and processing video frames.
        """
        self.start_camera()
        try:
            while True:
                ret, frame = self.cap.read()
                if not ret:
                    print("Failed to grab frame")
                    break

                processed_frame = self.process_frame(frame)
                if processed_frame is not None:
                    # Display the processed frame
                    cv2.imshow('Processed Frame', processed_frame)

                # Exit on pressing 'q'
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        except KeyboardInterrupt:
            print("Interrupted by user.")
        finally:
            self.cleanup()

    def cleanup(self):
        """
        Releases the camera and closes all OpenCV windows.
        """
        if self.cap is not None:
            self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    # Create an instance of the RealTimeImageProcessor and run it
    processor = RealTimeImageProcessor()
    processor.run()
```

### Requirements:
To run this code, make sure you have the following Python packages installed:
```bash
pip install opencv-python numpy
```
