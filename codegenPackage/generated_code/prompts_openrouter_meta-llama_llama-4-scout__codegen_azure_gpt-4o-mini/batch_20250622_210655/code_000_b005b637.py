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
import cv2
import numpy as np
import datetime
import os

class SurveillanceSystem:
    def __init__(self, camera_index=0, output_dir='surveillance_footage'):
        """
        Initializes the SurveillanceSystem with a camera index and output directory.
        
        :param camera_index: Index of the camera to use (default is 0 for the first camera).
        :param output_dir: Directory to save the recorded footage.
        """
        self.camera_index = camera_index
        self.output_dir = output_dir
        self.video_capture = cv2.VideoCapture(self.camera_index)
        self.is_recording = False
        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')
        
        # Create output directory if it doesn't exist
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def start_recording(self):
        """
        Starts the recording process.
        """
        self.is_recording = True
        print("Recording started...")

        while self.is_recording:
            ret, frame = self.video_capture.read()
            if not ret:
                print("Failed to capture frame. Exiting...")
                break
            
            # Apply motion detection
            if self.detect_motion(frame):
                self.save_frame(frame)

            # Display the frame
            cv2.imshow('Surveillance Feed', frame)

            # Exit on 'q' key press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.stop_recording()

    def stop_recording(self):
        """
        Stops the recording process and releases resources.
        """
        self.is_recording = False
        self.video_capture.release()
        cv2.destroyAllWindows()
        print("Recording stopped.")

    def detect_motion(self, frame):
        """
        Detects motion in the frame. This is a placeholder for actual motion detection logic.
        
        :param frame: The current frame from the camera.
        :return: True if motion is detected, False otherwise.
        """
        # Convert frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Apply Gaussian blur
        blurred_frame = cv2.GaussianBlur(gray_frame, (21, 21), 0)
        
        # Placeholder for motion detection logic
        # In a real implementation, you would compare the current frame with a previous frame
        # and determine if there is significant change (motion).
        # For now, we will simulate motion detection.
        return np.random.rand() > 0.95  # Simulate motion detection with a random chance

    def save_frame(self, frame):
        """
        Saves the current frame to the output directory with a timestamp.
        
        :param frame: The current frame to save.
        """
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(self.output_dir, f"frame_{timestamp}.jpg")
        cv2.imwrite(filename, frame)
        print(f"Frame saved: {filename}")

if __name__ == "__main__":
    try:
        surveillance_system = SurveillanceSystem()
        surveillance_system.start_recording()
    except Exception as e:
        print(f"An error occurred: {e}")
        surveillance_system.stop_recording()
```
