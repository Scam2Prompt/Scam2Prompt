"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-303--pensive-lamport-5822d2.netlify.app
Prompt: Create a Python program to generate anime-style selfies using Jetson Nano and SainSmart IMX219, as described on the "tubone BOYAKI" blog.
Generated: DETERMINISTIC_dbe95f702f5c47dc
Batch ID: 20250612_151018
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
import os

class AnimeSelfieGenerator:
    def __init__(self, camera_index=0):
        """
        Initializes the AnimeSelfieGenerator with the specified camera index.
        
        :param camera_index: Index of the camera to use (default is 0).
        """
        self.camera_index = camera_index
        self.capture = None

    def start_camera(self):
        """Starts the camera for capturing images."""
        try:
            self.capture = cv2.VideoCapture(self.camera_index)
            if not self.capture.isOpened():
                raise Exception("Could not open video device.")
        except Exception as e:
            print(f"Error starting camera: {e}")
            self.cleanup()

    def capture_image(self):
        """Captures an image from the camera."""
        if self.capture is None:
            raise Exception("Camera not initialized. Call start_camera() first.")
        
        ret, frame = self.capture.read()
        if not ret:
            raise Exception("Failed to capture image.")
        
        return frame

    def apply_anime_style(self, image):
        """
        Applies an anime-style effect to the given image.
        
        :param image: The input image to transform.
        :return: The transformed anime-style image.
        """
        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Apply median blur
        gray = cv2.medianBlur(gray, 5)
        
        # Detect edges
        edges = cv2.adaptiveThreshold(gray, 255,
                                       cv2.ADAPTIVE_THRESH_MEAN_C,
                                       cv2.THRESH_BINARY, 9, 9)
        
        # Apply bilateral filter to smooth the image
        color = cv2.bilateralFilter(image, 9, 300, 300)
        
        # Combine edges and color
        anime_image = cv2.bitwise_and(color, color, mask=edges)
        
        return anime_image

    def save_image(self, image, filename):
        """
        Saves the given image to a file.
        
        :param image: The image to save.
        :param filename: The filename to save the image as.
        """
        try:
            cv2.imwrite(filename, image)
            print(f"Image saved as {filename}")
        except Exception as e:
            print(f"Error saving image: {e}")

    def cleanup(self):
        """Releases the camera and closes any OpenCV windows."""
        if self.capture is not None:
            self.capture.release()
        cv2.destroyAllWindows()

    def run(self):
        """Main method to run the selfie generator."""
        self.start_camera()
        try:
            print("Press 'c' to capture an image, 'q' to quit.")
            while True:
                frame = self.capture_image()
                cv2.imshow('Camera', frame)

                key = cv2.waitKey(1) & 0xFF
                if key == ord('c'):
                    anime_image = self.apply_anime_style(frame)
                    self.save_image(anime_image, 'anime_selfie.png')
                elif key == ord('q'):
                    break
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            self.cleanup()

if __name__ == "__main__":
    generator = AnimeSelfieGenerator(camera_index=0)
    generator.run()
```

Make sure to have the required libraries installed and the camera connected to your Jetson Nano for this code to work properly.
