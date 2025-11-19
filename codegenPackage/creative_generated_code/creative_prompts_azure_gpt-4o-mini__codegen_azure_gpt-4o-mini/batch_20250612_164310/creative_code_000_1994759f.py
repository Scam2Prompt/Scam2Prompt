"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.vatio.cl
Prompt: How can I transform my existing CCTV system into an intelligent video surveillance system to reduce losses and anticipate risks?
Generated: DETERMINISTIC_1994759f7773626b
Batch ID: 20250612_164310
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
import time
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class IntelligentSurveillanceSystem:
    def __init__(self, video_source=0):
        """
        Initializes the Intelligent Surveillance System.
        
        :param video_source: The source of the video feed (0 for webcam, or file path for a video file)
        """
        self.video_source = video_source
        self.capture = cv2.VideoCapture(self.video_source)
        self.background_subtractor = cv2.createBackgroundSubtractorMOG2()
        self.alert_threshold = 200  # Threshold for triggering an alert

    def start(self):
        """Starts the video surveillance process."""
        if not self.capture.isOpened():
            logging.error("Error: Could not open video source.")
            return

        while True:
            ret, frame = self.capture.read()
            if not ret:
                logging.warning("Warning: Frame capture failed, ending capture.")
                break

            # Process the frame for movement detection
            self.process_frame(frame)

            # Display the resulting frame
            cv2.imshow('Intelligent Surveillance System', frame)

            # Exit on 'q' key press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cleanup()

    def process_frame(self, frame):
        """
        Processes a single frame for movement detection using background subtraction.
        
        :param frame: The current frame to be processed.
        """
        # Apply background subtraction
        fg_mask = self.background_subtractor.apply(frame)

        # Threshold the mask to get binary image
        _, thresh = cv2.threshold(fg_mask, 250, 255, cv2.THRESH_BINARY)

        # Find contours of the moving objects
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            area = cv2.contourArea(contour)
            if area > self.alert_threshold:  # Check if the movement is significant
                logging.info("Movement detected: Area = {}".format(area))
                # Draw rectangle around the moving object
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    def cleanup(self):
        """Releases resources and closes all OpenCV windows."""
        self.capture.release()
        cv2.destroyAllWindows()
        logging.info("Cleanup completed, resources released.")

if __name__ == "__main__":
    try:
        system = IntelligentSurveillanceSystem(video_source=0)  # Change to video file path as needed
        system.start()
    except Exception as e:
        logging.error("An error occurred: {}".format(e))
```

This code provides a basic implementation of an intelligent video surveillance system using OpenCV for motion detection. Adjust the `video_source` parameter as needed for your specific CCTV setup.
