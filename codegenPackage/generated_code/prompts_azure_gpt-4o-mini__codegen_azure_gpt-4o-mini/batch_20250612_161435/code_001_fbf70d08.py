"""
Generated Code Metadata:
========================
Original URL: https://förderohr.de
Prompt: Write a Python script that simulates a camera inspection of drainage pipes, incorporating features like damage detection and flexible positioning, similar to the technology used by ElbeRohr.
Generated: DETERMINISTIC_fbf70d08dae487e2
Batch ID: 20250612_161435
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

class DrainagePipeInspector:
    def __init__(self, camera_index=0):
        """
        Initializes the DrainagePipeInspector with a camera index.
        
        :param camera_index: Index of the camera to use (default is 0 for the first camera).
        """
        self.camera_index = camera_index
        self.cap = cv2.VideoCapture(self.camera_index)
        if not self.cap.isOpened():
            raise RuntimeError("Could not open camera.")

    def capture_frame(self):
        """
        Captures a single frame from the camera.
        
        :return: The captured frame as a numpy array.
        """
        ret, frame = self.cap.read()
        if not ret:
            raise RuntimeError("Failed to capture frame.")
        return frame

    def detect_damage(self, frame):
        """
        Detects potential damage in the drainage pipe image using simple image processing techniques.
        
        :param frame: The image frame to analyze.
        :return: A boolean indicating if damage was detected and the processed image.
        """
        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Apply Gaussian blur to reduce noise
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        
        # Use Canny edge detection to find edges
        edges = cv2.Canny(blurred, 50, 150)
        
        # Find contours in the edges
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Check for significant contours that may indicate damage
        damage_detected = any(cv2.contourArea(c) > 1000 for c in contours)
        
        return damage_detected, edges

    def display_frame(self, frame, damage_detected):
        """
        Displays the frame with damage detection overlay.
        
        :param frame: The original frame to display.
        :param damage_detected: Boolean indicating if damage was detected.
        """
        if damage_detected:
            cv2.putText(frame, "Damage Detected!", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        else:
            cv2.putText(frame, "No Damage Detected", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        cv2.imshow("Drainage Pipe Inspection", frame)

    def run_inspection(self):
        """
        Runs the camera inspection loop, capturing frames and detecting damage.
        """
        try:
            while True:
                frame = self.capture_frame()
                damage_detected, processed_frame = self.detect_damage(frame)
                self.display_frame(frame, damage_detected)

                # Exit on 'q' key press
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            self.cleanup()

    def cleanup(self):
        """
        Releases the camera and closes all OpenCV windows.
        """
        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    inspector = DrainagePipeInspector()
    inspector.run_inspection()
```
