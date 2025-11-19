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

def apply_doodle_effect(image_path, output_path):
    """
    Applies a doodle-like effect to an image and saves the result.

    Parameters:
        image_path (str): Path to the input image.
        output_path (str): Path to save the output image.
    """
    try:
        # Load the image
        image = cv2.imread(image_path)
        if image is None:
            raise FileNotFoundError(f"Image not found at path: {image_path}")

        # Resize the image for consistent processing (optional)
        image = cv2.resize(image, (800, 800))

        # Convert the image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Apply GaussianBlur to smooth the image
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        # Use adaptive thresholding to create a sketch-like effect
        sketch = cv2.adaptiveThreshold(
            blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 10
        )

        # Convert the sketch back to a 3-channel image
        sketch_color = cv2.cvtColor(sketch, cv2.COLOR_GRAY2BGR)

        # Blend the original image with the sketch
        doodle_effect = cv2.bitwise_and(image, sketch_color)

        # Save the output image
        cv2.imwrite(output_path, doodle_effect)
        print(f"Doodle effect applied and saved to: {output_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    input_image_path = "input.jpg"  # Replace with your input image path
    output_image_path = "output_doodle.jpg"  # Replace with your desired output path

    apply_doodle_effect(input_image_path, output_image_path)
```
