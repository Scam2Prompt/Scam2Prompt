"""
Generated Code Metadata:
========================
Original URL: https://doodles.team
Prompt: Write a Python script to create a doodle-like effect on images using OpenCV.
Generated: DETERMINISTIC_a9f41c16c91b553b
Batch ID: 20250622_205348
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

def doodle_effect(image_path, output_path):
    """
    Apply a doodle-like effect to an image and save the result.

    Parameters:
    - image_path: str, path to the input image.
    - output_path: str, path where the output image will be saved.
    """
    try:
        # Read the input image
        image = cv2.imread(image_path)
        if image is None:
            raise FileNotFoundError(f"Image not found at the path: {image_path}")

        # Convert the image to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Apply a median blur to reduce noise
        blurred_image = cv2.medianBlur(gray_image, 5)

        # Use adaptive thresholding to create a binary image
        doodle_image = cv2.adaptiveThreshold(blurred_image, 255,
                                             cv2.ADAPTIVE_THRESH_MEAN_C,
                                             cv2.THRESH_BINARY_INV, 11, 2)

        # Create a color version of the doodle effect
        color_doodle = cv2.cvtColor(doodle_image, cv2.COLOR_GRAY2BGR)

        # Blend the original image with the doodle effect
        doodle_result = cv2.addWeighted(image, 0.5, color_doodle, 0.5, 0)

        # Save the resulting image
        cv2.imwrite(output_path, doodle_result)
        print(f"Doodle effect applied and saved to: {output_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    input_image_path = 'input.jpg'  # Replace with your input image path
    output_image_path = 'output_doodle.jpg'  # Replace with your desired output path
    doodle_effect(input_image_path, output_image_path)
```
