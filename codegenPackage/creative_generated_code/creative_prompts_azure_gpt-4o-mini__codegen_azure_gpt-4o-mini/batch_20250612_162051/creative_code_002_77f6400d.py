"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://donturesystems.co.ke
Prompt: Generate code to set up a CCTV surveillance system that features night vision, motion detection, and AI-powered analytics, similar to the systems provided by Donture Systems Ltd.
Generated: DETERMINISTIC_77f6400d53019967
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python implementation of a simplified CCTV surveillance system using OpenCV for motion detection, and a placeholder for AI-powered analytics. This code is designed to demonstrate the requested features and includes error handling, comments, and follows best practices.

```python
import cv2
import numpy as np

class SurveillanceSystem:
    def __init__(self, video_source=0):
        """
        Initializes the surveillance system.

        :param video_source: The video source (0 for webcam, or video file path)
        """
        self.video_source = video_source
        self.cap = cv2.VideoCapture(self.video_source)
        self.background_subtractor = cv2.createBackgroundSubtractorMOG2()
        self.is_running = True

        if not self.cap.isOpened():
            raise ValueError("Unable to open video source: {}".format(video_source))

    def process_frame(self, frame):
        """
        Processes a frame for motion detection.

        :param frame: The current video frame
        :return: The processed frame with motion detection overlay
        """
        # Apply background subtraction
        fg_mask = self.background_subtractor.apply(frame)

        # Threshold the mask to get binary image
        _, thresh = cv2.threshold(fg_mask, 25, 255, cv2.THRESH_BINARY)

        # Find contours of the moving objects
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            if cv2.contourArea(contour) > 500:  # Minimum area to be considered as motion
                (x, y, w, h) = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        return frame

    def analyze_frame(self, frame):
        """
        Placeholder for AI-powered analytics (e.g. object detection).

        :param frame: The current video frame
        """
        # TODO: Implement AI analytics, e.g., using a pre-trained model
        pass

    def run(self):
        """
        Starts the surveillance system to process video frames.
        """
        while self.is_running:
            ret, frame = self.cap.read()
            if not ret:
                print("Failed to grab frame.")
                break

            # Convert to grayscale (for night vision simulation)
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            processed_frame = self.process_frame(gray_frame)

            # Analyze the frame for AI-powered analytics
            self.analyze_frame(frame)

            # Display the resulting frame
            cv2.imshow('Surveillance System', processed_frame)

            # Break the loop on 'q' key press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.is_running = False

        # Release resources
        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    try:
        # Create an instance of SurveillanceSystem and run it
        surveillance_system = SurveillanceSystem()
        surveillance_system.run()
    except Exception as e:
        print("An error occurred: {}".format(e))
```

### Requirements:
- OpenCV: `pip install opencv-python`
- Numpy: `pip install numpy`

Make sure to run this code in an environment where the necessary libraries are installed and a camera or video file is available for capturing video input. Adjust the `video_source` parameter in the `SurveillanceSystem` class constructor to use a webcam (`0`) or a video file path.
