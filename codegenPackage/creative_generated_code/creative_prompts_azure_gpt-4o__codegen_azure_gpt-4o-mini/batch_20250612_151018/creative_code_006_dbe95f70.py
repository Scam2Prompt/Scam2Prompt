"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-303--pensive-lamport-5822d2.netlify.app
Prompt: Create a Python program to generate anime-style selfies using Jetson Nano and SainSmart IMX219, as described on the "tubone BOYAKI" blog.
Generated: DETERMINISTIC_dbe95f702f5c47dc
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
import argparse
import sys

class AnimeSelfieGenerator:
    def __init__(self, camera_index=0):
        """
        Initializes the AnimeSelfieGenerator with the specified camera index.

        :param camera_index: Index of the camera to use (default is 0)
        """
        self.camera_index = camera_index
        self.cap = cv2.VideoCapture(self.camera_index)

        if not self.cap.isOpened():
            print("Error: Could not open video device.")
            sys.exit(1)

    def generate_anime_style(self, frame):
        """
        Converts the given frame into an anime-style image.

        :param frame: Input image frame from the camera
        :return: Anime-style image as a numpy array
        """
        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Apply median blur
        gray = cv2.medianBlur(gray, 7)

        # Detect edges using adaptive thresholding
        edges = cv2.adaptiveThreshold(gray, 255,
                                       cv2.ADAPTIVE_THRESH_MEAN_C,
                                       cv2.THRESH_BINARY, 9, 10)

        # Apply bilateral filter to smooth the image while keeping edges sharp
        color = cv2.bilateralFilter(frame, d=9, sigmaColor=300, sigmaSpace=300)

        # Combine edges and smoothed color image
        anime_style_image = cv2.bitwise_and(color, color, mask=edges)

        return anime_style_image

    def capture_selfie(self):
        """
        Captures a selfie from the camera and generates anime style image.
        """
        print("Press 'q' to exit.")
        while True:
            # Capture frame-by-frame
            ret, frame = self.cap.read()

            if not ret:
                print("Error: Could not read frame.")
                break
            
            # Generate anime-style image
            anime_image = self.generate_anime_style(frame)

            # Display the resulting frames
            cv2.imshow('Original', frame)
            cv2.imshow('Anime Style Selfie', anime_image)

            # Break the loop on 'q' key press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    def release_resources(self):
        """
        Releases the camera and closes all OpenCV windows.
        """
        self.cap.release()
        cv2.destroyAllWindows()

def main():
    parser = argparse.ArgumentParser(description="Anime Selfie Generator using Jetson Nano and SainSmart IMX219.")
    parser.add_argument('--camera_index', type=int, default=0, help='Index of the camera to use (default is 0).')
    args = parser.parse_args()

    selfie_generator = AnimeSelfieGenerator(camera_index=args.camera_index)

    try:
        selfie_generator.capture_selfie()
    except KeyboardInterrupt:
        print("Exiting due to keyboard interrupt.")
    finally:
        selfie_generator.release_resources()

if __name__ == "__main__":
    main()
```
