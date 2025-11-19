"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blurapp.net
Prompt: Develop a user guide for using the Blur App, focusing on how to apply various blur filters and effects to existing images and videos.
Generated: DETERMINISTIC_297b9a317724c2c1
Batch ID: 20250612_135754
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Blur App User Guide

This script provides a user-friendly interface for applying various blur filters 
and effects to existing images and videos. 

Requirements:
- Python 3.x
- OpenCV (cv2)
- NumPy
- MoviePy (for video processing)

Install the required packages using pip:
pip install opencv-python numpy moviepy
"""

import cv2
import numpy as np
from moviepy.editor import VideoFileClip

def apply_blur(image, blur_type='gaussian', intensity=5):
    """
    Apply the specified blur filter to an image.

    Parameters:
        image (numpy.ndarray): The input image.
        blur_type (str): The type of blur to apply (options: 'gaussian', 'median', 'bilateral').
        intensity (int): The intensity of the blur effect (must be odd for some blur types).

    Returns:
        numpy.ndarray: The blurred image.
    """
    if blur_type == 'gaussian':
        return cv2.GaussianBlur(image, (intensity, intensity), 0)
    elif blur_type == 'median':
        return cv2.medianBlur(image, intensity)
    elif blur_type == 'bilateral':
        return cv2.bilateralFilter(image, intensity, 75, 75)
    else:
        raise ValueError("Invalid blur type. Choose from 'gaussian', 'median', or 'bilateral'.")

def process_image(image_path, output_path, blur_type='gaussian', intensity=5):
    """
    Process an image by applying a blur effect and saving the result.

    Parameters:
        image_path (str): Path to the input image.
        output_path (str): Path where the blurred image will be saved.
        blur_type (str): Type of blur to apply.
        intensity (int): Intensity of the blur effect.
    """
    try:
        # Read the image
        image = cv2.imread(image_path)
        if image is None:
            raise FileNotFoundError(f"The image at {image_path} could not be found.")

        # Apply blur
        blurred_image = apply_blur(image, blur_type, intensity)

        # Save the result
        cv2.imwrite(output_path, blurred_image)
        print(f"Blurred image saved at {output_path}.")
    except Exception as e:
        print(f"An error occurred: {e}")

def process_video(video_path, output_path, blur_type='gaussian', intensity=5):
    """
    Process a video by applying a blur effect to each frame and saving the result.

    Parameters:
        video_path (str): Path to the input video.
        output_path (str): Path where the blurred video will be saved.
        blur_type (str): Type of blur to apply.
        intensity (int): Intensity of the blur effect.
    """
    try:
        # Load video
        clip = VideoFileClip(video_path)

        # Apply blur to each frame
        def blur_frame(frame):
            return apply_blur(frame, blur_type, intensity)

        blurred_clip = clip.fl_image(blur_frame)

        # Write the result
        blurred_clip.write_videofile(output_path, codec='libx264')
        print(f"Blurred video saved at {output_path}.")
    except Exception as e:
        print(f"An error occurred while processing the video: {e}")

# Example usage
if __name__ == "__main__":
    # Process an image
    process_image("input_image.jpg", "output_blurred_image.jpg", blur_type='gaussian', intensity=15)

    # Process a video
    process_video("input_video.mp4", "output_blurred_video.mp4", blur_type='median', intensity=5)
```
