"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-306--pensive-lamport-5822d2.netlify.app
Prompt: Create a tutorial on using Jetson Nano and SainSmart IMX219 to create an anime-style selfie video, as described in the blog post "Jetson nano + SainSmart IMX219でアニメ風自撮り動画を作る".
Generated: DETERMINISTIC_8e4968ff2bbcef07
Batch ID: 20250622_211429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Jetson Nano + SainSmart IMX219 Anime-Style Selfie Video Tutorial Code

This script captures video from the SainSmart IMX219 camera connected to a Jetson Nano,
applies an anime-style filter using OpenCV, and displays the processed video in real-time.

Requirements:
- Jetson Nano with SainSmart IMX219 camera module
- OpenCV installed (`pip install opencv-python`)
- Python 3.x

Author: [Your Name]
Date: [Insert Date]
"""

import cv2
import numpy as np

def apply_anime_filter(frame):
    """
    Applies an anime-style filter to the input frame.
    
    Parameters:
        frame (numpy.ndarray): Input video frame.
    
    Returns:
        numpy.ndarray: Anime-style filtered frame.
    """
    try:
        # Step 1: Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Step 2: Apply median blur to reduce noise
        blurred = cv2.medianBlur(gray, 7)

        # Step 3: Detect edges using adaptive thresholding
        edges = cv2.adaptiveThreshold(
            blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 10
        )

        # Step 4: Apply bilateral filter to smooth colors while preserving edges
        color = cv2.bilateralFilter(frame, d=9, sigmaColor=75, sigmaSpace=75)

        # Step 5: Combine edges with the color image
        anime_frame = cv2.bitwise_and(color, color, mask=edges)

        return anime_frame
    except Exception as e:
        print(f"Error applying anime filter: {e}")
        return frame  # Return original frame in case of error

def main():
    """
    Main function to capture video, apply anime filter, and display the output.
    """
    # Initialize video capture (camera ID 0 for SainSmart IMX219)
    cap = cv2.VideoCapture(0)

    # Check if the camera opened successfully
    if not cap.isOpened():
        print("Error: Unable to access the camera.")
        return

    print("Press 'q' to exit the video stream.")

    try:
        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()
            if not ret:
                print("Error: Unable to read frame from camera.")
                break

            # Resize frame for better performance (optional)
            frame = cv2.resize(frame, (640, 480))

            # Apply anime-style filter
            anime_frame = apply_anime_filter(frame)

            # Display the resulting frame
            cv2.imshow("Anime-Style Selfie Video", anime_frame)

            # Exit the loop when 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    except Exception as e:
        print(f"An error occurred during video processing: {e}")
    finally:
        # Release the camera and close all OpenCV windows
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
```
