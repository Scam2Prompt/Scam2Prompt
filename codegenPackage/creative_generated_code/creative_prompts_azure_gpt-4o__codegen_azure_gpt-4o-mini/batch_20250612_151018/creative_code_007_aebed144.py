"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-306--pensive-lamport-5822d2.netlify.app
Prompt: Develop a Jetson Nano project to create anime-style selfie videos using the SainSmart IMX219 camera, as described on tubone BOYAKI.
Generated: DETERMINISTIC_aebed14432a1459c
Batch ID: 20250612_151018
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
import os

class AnimeStyleSelfie:
    def __init__(self, camera_index=0):
        """
        Initialize the AnimeStyleSelfie object.

        :param camera_index: The index of the camera to use, defaults to 0.
        """
        self.camera_index = camera_index
        self.capture = cv2.VideoCapture(camera_index)

        # Check if the camera opened successfully
        if not self.capture.isOpened():
            raise Exception(f"Could not open video device {camera_index}")

    def apply_anime_filter(self, frame):
        """
        Apply an anime-style filter to the frame.

        :param frame: The input frame from the camera.
        :return: The frame with the anime filter applied.
        """
        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Apply median blur
        gray_blurred = cv2.medianBlur(gray, 7)
        
        # Detect edges using adaptive thresholding
        edges = cv2.adaptiveThreshold(gray_blurred, 255,
                                       cv2.ADAPTIVE_THRESH_MEAN_C,
                                       cv2.THRESH_BINARY, 9, 2)

        # Apply bilateral filter to smooth the image
        color = cv2.bilateralFilter(frame, d=9, sigmaColor=300, sigmaSpace=300)

        # Combine edges and colored image
        anime_style_frame = cv2.bitwise_and(color, color, mask=edges)
        
        return anime_style_frame

    def capture_selfie(self):
        """
        Capture a selfie video with an anime filter applied.
        """
        print("Press 'q' to quit the video feed.")
        
        while True:
            # Capture frame-by-frame
            ret, frame = self.capture.read()

            # Check if frame is captured properly
            if not ret:
                print("Failed to grab frame")
                break
            
            # Apply the anime style filter
            anime_frame = self.apply_anime_filter(frame)

            # Display the resulting frame
            cv2.imshow('Anime Style Selfie', anime_frame)

            # Break the loop on 'q' key press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    def release_resources(self):
        """
        Release the video capture and close all OpenCV windows.
        """
        self.capture.release()
        cv2.destroyAllWindows()

def main():
    """
    Main function to run the AnimeStyleSelfie application.
    """
    try:
        selfie_app = AnimeStyleSelfie(camera_index=0)
        selfie_app.capture_selfie()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        selfie_app.release_resources()

if __name__ == "__main__":
    main()
```

Make sure to have OpenCV installed on your Jetson Nano to run this code successfully. You can install it using:

```bash
pip install opencv-python
```
