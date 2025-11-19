"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.limpiezadetuboscostablanca.net
Prompt: Write a Python function that utilizes a library to detect water leaks in residential plumbing systems, similar to the advanced detection systems described on Limpieza de Tubos Costablanca.
Generated: DETERMINISTIC_acfb3c72fd00a0ec
Batch ID: 20250612_161403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import cv2

class WaterLeakDetector:
    """
    A class to detect water leaks in residential plumbing systems.
    
    This class uses computer vision techniques to analyze images or videos
    for signs of water leaks based on color detection and movement analysis.
    """
    
    def __init__(self, color_range_lower, color_range_upper):
        """
        Initializes the WaterLeakDetector with specified color ranges.
        
        Parameters:
        color_range_lower (tuple): Lower bound of the color range for water detection (in BGR format).
        color_range_upper (tuple): Upper bound of the color range for water detection (in BGR format).
        """
        self.color_range_lower = np.array(color_range_lower, dtype="uint8")
        self.color_range_upper = np.array(color_range_upper, dtype="uint8")
    
    def detect_leaks(self, frame):
        """
        Detects water leaks in a single frame.
        
        Parameters:
        frame (numpy.ndarray): The image frame to be analyzed for leaks.
        
        Returns:
        bool: True if a leak is detected, False otherwise.
        """
        # Check if the frame is valid
        if frame is None:
            raise ValueError("Input frame is None")
        
        # Convert the frame to the HSV color space
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # Create a mask for the color range defined for water
        mask = cv2.inRange(hsv_frame, self.color_range_lower, self.color_range_upper)

        # Perform morphological operations to clean the mask
        kernel = np.ones((5, 5), np.uint8)
        cleaned_mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        
        # Find contours in the mask
        contours, _ = cv2.findContours(cleaned_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # If contours are found, a leak is detected
        leak_detected = len(contours) > 0
        return leak_detected
    
    def process_video(self, video_source):
        """
        Processes a video stream to detect leaks continuously.
        
        Parameters:
        video_source (str or int): The video source (0 for webcam, file path for video).
        """
        # Open the video source
        cap = cv2.VideoCapture(video_source)

        if not cap.isOpened():
            raise RuntimeError("Could not open video source")

        try:
            while True:
                ret, frame = cap.read()
                if not ret:
                    print("Failed to grab frame")
                    break

                # Detect water leaks in the current frame
                if self.detect_leaks(frame):
                    print("Water leak detected!")
                else:
                    print("No leak detected.")

                # Display the frame (optional)
                cv2.imshow('Water Leak Detection', frame)

                # Press 'q' to exit the video stream
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            cap.release()
            cv2.destroyAllWindows()

# Example usage:
if __name__ == "__main__":
    # Define the color range for water detection in HSV format
    # These values might need adjustment depending on the environment
    color_range_lower = (100, 150, 0)   # Lower bound in HSV
    color_range_upper = (140, 255, 255)  # Upper bound in HSV

    # Initialize the water leak detector
    detector = WaterLeakDetector(color_range_lower, color_range_upper)

    # Start processing the video from the webcam
    detector.process_video(0)  # Change to video file path if needed
```
