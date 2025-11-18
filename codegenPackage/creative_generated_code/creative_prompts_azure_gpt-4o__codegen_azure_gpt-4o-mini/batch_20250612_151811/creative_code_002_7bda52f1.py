"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poolpalplatform.com
Prompt: Create a script to automate water titration testing using Taylor™ test kits and computer vision technology, inspired by PoolPal™ RoboArm's functionality.
Generated: DETERMINISTIC_7bda52f18ff499dd
Batch ID: 20250612_151811
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

class TitrationTester:
    def __init__(self, camera_index=0):
        """
        Initializes the TitrationTester with a camera for image capture.
        
        Parameters:
            camera_index (int): The index of the camera to use (default is 0).
        """
        self.camera_index = camera_index
        self.cap = cv2.VideoCapture(self.camera_index)

        if not self.cap.isOpened():
            raise RuntimeError("Could not open camera.")
        
        self.lower_bound_color = np.array([30, 100, 100])  # Example lower HSV bound for a specific color
        self.upper_bound_color = np.array([90, 255, 255])  # Example upper HSV bound for a specific color

    def capture_frame(self):
        """Captures a single frame from the camera."""
        ret, frame = self.cap.read()
        if not ret:
            raise RuntimeError("Failed to capture image from camera.")
        return frame

    def process_frame(self, frame):
        """
        Processes the captured frame to detect the color of the titration solution.
        
        Parameters:
            frame (np.ndarray): The captured image frame.
        
        Returns:
            dict: Contains the detected color and processing status.
        """
        # Convert image to HSV color space
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # Create a mask for the color detection
        mask = cv2.inRange(hsv_frame, self.lower_bound_color, self.upper_bound_color)
        
        # Calculate the percentage of the color present in the frame
        color_percentage = (np.sum(mask) / 255) / (mask.size) * 100
        
        return {
            "detected": True if color_percentage > 5 else False,  # A threshold to determine color presence
            "percentage": color_percentage
        }

    def run_titration_test(self):
        """Runs the titration test by capturing and processing frames."""
        try:
            while True:
                frame = self.capture_frame()
                result = self.process_frame(frame)

                # Display the result
                if result["detected"]:
                    print(f"Color detected with {result['percentage']:.2f}% presence.")
                else:
                    print("No significant color detected.")
                
                # Display the captured frame
                cv2.imshow('Titration Frame', frame)
                
                # Break the loop on 'q' key press
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            self.cleanup()

    def cleanup(self):
        """Releases the camera and closes any OpenCV windows."""
        if self.cap.isOpened():
            self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    tester = TitrationTester()
    tester.run_titration_test()
```
