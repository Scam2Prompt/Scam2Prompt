"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://teslavision.us
Prompt: Develop a safety feature in Python that continuously monitors surroundings and flags potential hazards, mimicking Tesla Vision's high-safety functionality.
Generated: DETERMINISTIC_371c989ec88e50b7
Batch ID: 20250612_145423
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

class HazardDetector:
    """
    A class to monitor surroundings using a video feed and flag potential hazards.
    """

    def __init__(self, video_source=0):
        """
        Initializes the HazardDetector with a video source.
        
        Args:
            video_source (int or str): Camera index or video file path.
        """
        self.video_source = video_source
        self.hazard_flags = []

    def start_monitoring(self):
        """
        Starts the monitoring process for detecting hazards.
        """
        # Start video capture
        cap = cv2.VideoCapture(self.video_source)
        
        if not cap.isOpened():
            raise Exception("Could not open video source: {}".format(self.video_source))

        try:
            while True:
                ret, frame = cap.read()
                if not ret:
                    raise Exception("Failed to read frame from video source.")

                # Process frame to detect hazards
                self.detect_hazards(frame)

                # Display the frame with potential hazards
                self.display_results(frame)

                # Exit the loop on 'q' key press
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        except Exception as e:
            print("Error during monitoring: {}".format(e))
        finally:
            cap.release()
            cv2.destroyAllWindows()

    def detect_hazards(self, frame):
        """
        Detect potential hazards in the frame.
        
        Args:
            frame (numpy.ndarray): The video frame to process.
        """
        # Example hazard detection logic (simplified for demonstration)
        # This should be replaced with actual detection algorithms.
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray_frame, 50, 150, apertureSize=3)

        # Example hazard condition: if edges are detected, flag as a hazard
        if np.sum(edges) > 0:
            self.hazard_flags.append("Potential hazard detected!")

    def display_results(self, frame):
        """
        Displays the processed frame with hazard flags.
        
        Args:
            frame (numpy.ndarray): The video frame to display.
        """
        # Display hazard flags on the frame
        for i, flag in enumerate(self.hazard_flags):
            cv2.putText(frame, flag, (10, 30 + i * 30), cv2.FONT_HERSHEY_SIMPLEX, 
                        0.7, (0, 255, 0), 2, cv2.LINE_AA)

        # Show the frame in a window
        cv2.imshow('Hazard Detection', frame)

if __name__ == "__main__":
    # Create an instance of HazardDetector and start monitoring
    try:
        detector = HazardDetector(video_source=0)  # Change to video file path if needed
        detector.start_monitoring()
    except Exception as e:
        print("Failed to initialize HazardDetector: {}".format(e))
```
