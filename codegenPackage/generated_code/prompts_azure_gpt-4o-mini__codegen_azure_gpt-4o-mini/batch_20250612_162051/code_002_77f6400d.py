"""
Generated Code Metadata:
========================
Original URL: https://donturesystems.co.ke
Prompt: Generate code to set up a CCTV surveillance system that features night vision, motion detection, and AI-powered analytics, similar to the systems provided by Donture Systems Ltd.
Generated: DETERMINISTIC_77f6400d53019967
Batch ID: 20250612_162051
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
import time
import threading

class SurveillanceSystem:
    def __init__(self, camera_index=0):
        """
        Initializes the surveillance system with the specified camera index.
        
        :param camera_index: Index of the camera to use (default is 0 for the first camera).
        """
        self.camera_index = camera_index
        self.capture = cv2.VideoCapture(self.camera_index)
        self.is_running = True
        self.motion_detected = False

        # Load pre-trained AI model for motion detection (placeholder)
        self.motion_detector = cv2.createBackgroundSubtractorMOG2()

    def start(self):
        """
        Starts the surveillance system, capturing video and processing frames.
        """
        if not self.capture.isOpened():
            raise Exception("Could not open video device")

        print("Surveillance system started.")
        while self.is_running:
            ret, frame = self.capture.read()
            if not ret:
                print("Failed to capture frame.")
                break

            # Process the frame for motion detection
            self.process_frame(frame)

            # Display the frame (for debugging purposes)
            cv2.imshow('Surveillance Feed', frame)

            # Exit on 'q' key press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.stop()

        self.cleanup()

    def process_frame(self, frame):
        """
        Processes a single frame for motion detection and night vision enhancement.
        
        :param frame: The captured video frame.
        """
        # Convert frame to grayscale for motion detection
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blurred_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)

        # Apply motion detection
        mask = self.motion_detector.apply(blurred_frame)
        _, thresh = cv2.threshold(mask, 25, 255, cv2.THRESH_BINARY)

        # Find contours of the detected motion
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            if cv2.contourArea(contour) > 500:  # Minimum area to consider as motion
                self.motion_detected = True
                cv2.drawContours(frame, [contour], -1, (0, 255, 0), 2)

        # Night vision effect (simple inversion for demonstration)
        if self.motion_detected:
            frame = cv2.bitwise_not(frame)

    def stop(self):
        """
        Stops the surveillance system.
        """
        print("Stopping surveillance system.")
        self.is_running = False

    def cleanup(self):
        """
        Releases the video capture and closes all OpenCV windows.
        """
        self.capture.release()
        cv2.destroyAllWindows()
        print("Surveillance system stopped and cleaned up.")

if __name__ == "__main__":
    try:
        # Create and start the surveillance system
        surveillance_system = SurveillanceSystem()
        surveillance_system.start()
    except Exception as e:
        print(f"An error occurred: {e}")
```

This code sets up a basic CCTV surveillance system with motion detection and a simple night vision effect. It uses OpenCV for video capture and processing. The AI model for advanced analytics is represented as a placeholder, as implementing a full AI model would require additional resources and data.
