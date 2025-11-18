"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptofitties.com
Prompt: Write code to integrate computer vision-based motion tracking into a fitness app, similar to the functionality described on CryptoFitties, where reps are counted, scores are calculated, and real-time corrective feedback is provided.
Generated: DETERMINISTIC_c9d84ba84063e66d
Batch ID: 20250612_150323
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

class MotionTracker:
    """
    A class to track motion and count repetitions for fitness activities using computer vision.
    """

    def __init__(self, video_source=0):
        """
        Initializes the MotionTracker with a video source.
        
        :param video_source: The index or path of the video source (default is the first webcam).
        """
        self.video_source = video_source
        self.capture = cv2.VideoCapture(video_source)
        self.reps_count = 0
        self.previous_position = None
        self.feedback = ""

        if not self.capture.isOpened():
            raise ValueError("Error: Unable to open video source.")

    def process_frame(self, frame):
        """
        Processes a single frame for motion tracking.
        
        :param frame: The frame to process.
        :return: The processed frame with feedback overlayed.
        """
        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)

        if self.previous_position is None:
            self.previous_position = blur
            return frame

        # Calculate the absolute difference between the current frame and previous frame
        frame_delta = cv2.absdiff(self.previous_position, blur)
        _, thresh = cv2.threshold(frame_delta, 30, 255, cv2.THRESH_BINARY)

        # Find contours of the moving object
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # If contours are found, check for motion
        if contours:
            self.reps_count += 1  # Increment reps count on motion detected
            self.feedback = "Good job! Keep going!"  # Provide feedback

            # Draw contours for visualization
            for contour in contours:
                if cv2.contourArea(contour) > 500:  # Minimum area to consider for motion
                    (x, y, w, h) = cv2.boundingRect(contour)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Update previous position for next iteration
        self.previous_position = blur

        # Overlay feedback on the frame
        cv2.putText(frame, f'Reps: {self.reps_count}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.putText(frame, self.feedback, (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        return frame

    def run(self):
        """
        Starts the motion tracking process.
        """
        try:
            while True:
                ret, frame = self.capture.read()
                if not ret:
                    raise RuntimeError("Error: Unable to read from video source.")

                processed_frame = self.process_frame(frame)

                cv2.imshow('Motion Tracker', processed_frame)

                # Exit on pressing 'q'
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            self.capture.release()
            cv2.destroyAllWindows()

if __name__ == "__main__":
    motion_tracker = MotionTracker()
    motion_tracker.run()
```
