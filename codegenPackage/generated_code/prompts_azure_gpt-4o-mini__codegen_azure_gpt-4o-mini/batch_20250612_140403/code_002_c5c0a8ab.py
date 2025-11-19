"""
Generated Code Metadata:
========================
Original URL: https://red.game
Prompt: Write a Python script that simulates a surveillance system, drawing on the concepts of observation and interaction mentioned on the RED website.
Generated: DETERMINISTIC_c5c0a8abb91df01e
Batch ID: 20250612_140403
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

class SurveillanceSystem:
    def __init__(self, video_source=0):
        """
        Initializes the SurveillanceSystem with a video source.
        
        :param video_source: The source of the video feed (default is 0 for webcam).
        """
        self.video_source = video_source
        self.capture = None
        self.is_running = False

    def start(self):
        """Starts the video capture and begins the surveillance loop."""
        try:
            self.capture = cv2.VideoCapture(self.video_source)
            if not self.capture.isOpened():
                raise ValueError("Unable to open video source.")
            self.is_running = True
            self.run()
        except Exception as e:
            print(f"Error starting surveillance system: {e}")

    def run(self):
        """Main loop for capturing and processing video frames."""
        while self.is_running:
            ret, frame = self.capture.read()
            if not ret:
                print("Failed to capture frame.")
                break
            
            # Process the frame (e.g., convert to grayscale)
            processed_frame = self.process_frame(frame)

            # Display the processed frame
            cv2.imshow('Surveillance Feed', processed_frame)

            # Check for user input to exit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.stop()

    def process_frame(self, frame):
        """
        Processes the video frame (e.g., converts to grayscale).
        
        :param frame: The current video frame.
        :return: The processed frame.
        """
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    def stop(self):
        """Stops the video capture and releases resources."""
        self.is_running = False
        if self.capture:
            self.capture.release()
        cv2.destroyAllWindows()
        print("Surveillance system stopped.")

if __name__ == "__main__":
    # Create an instance of the SurveillanceSystem
    surveillance_system = SurveillanceSystem(video_source=0)
    
    # Start the surveillance system
    surveillance_system.start()
```
