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

Certainly! Below is a Python script implementing a command-line interface for the "Blur App". It allows users to apply various blur filters to images and videos using the OpenCV library.

```python
import cv2
import os
import sys

def apply_blur(image_path, blur_type, intensity=5):
    """
    Apply a blur effect to an image.

    Args:
        image_path (str): Path to the input image.
        blur_type (str): Type of blur ('average', 'gaussian', 'median', 'bilateral').
        intensity (int): Intensity level for the blur.

    Returns:
        output_image (numpy.ndarray): Blurred image.
    """
    try:
        # Load the image
        image = cv2.imread(image_path)

        if image is None:
            raise FileNotFoundError(f"File not found: {image_path}")

        # Apply the selected blur effect
        if blur_type == "average":
            # Average blur
            output_image = cv2.blur(image, (intensity, intensity))
        elif blur_type == "gaussian":
            # Gaussian blur
            output_image = cv2.GaussianBlur(image, (intensity * 2 + 1, intensity * 2 + 1), 0)
        elif blur_type == "median":
            # Median blur
            output_image = cv2.medianBlur(image, intensity)
        elif blur_type == "bilateral":
            # Bilateral filter
            output_image = cv2.bilateralFilter(image, intensity * 5, intensity * 50, intensity * 50)
        else:
            raise ValueError("Invalid blur type. Choose from 'average', 'gaussian', 'median', or 'bilateral'.")

        return output_image

    except Exception as e:
        print(f"Error while applying blur: {e}")
        sys.exit(1)


def save_output(output_image, output_path):
    """
    Save the processed image to the specified path.

    Args:
        output_image (numpy.ndarray): Processed image.
        output_path (str): Path to save the image.
    """
    try:
        cv2.imwrite(output_path, output_image)
        print(f"Blurred image saved to: {output_path}")
    except Exception as e:
        print(f"Error saving the image: {e}")
        sys.exit(1)


def main():
    """
    Main function to handle user input and apply the blur effects.
    """
    print("Welcome to the Blur App!")
    
    # Get user input
    image_path = input("Enter the path to the image: ").strip()
    blur_type = input("Enter the blur type ('average', 'gaussian', 'median', 'bilateral'): ").strip().lower()
    intensity = input("Enter the blur intensity (default is 5): ").strip()

    # Validate intensity
    try:
        intensity = int(intensity) if intensity else 5
        if intensity <= 0:
            raise ValueError("Intensity must be a positive integer.")
    except ValueError:
        print("Invalid intensity value. Please enter a positive integer.")
        sys.exit(1)

    # Apply blur
    blurred_image = apply_blur(image_path, blur_type, intensity)
    
    # Ask for output path
    output_path = input("Enter the output path to save the blurred image: ").strip()
    
    # Save the image
    save_output(blurred_image, output_path)


if __name__ == "__main__":
    main()
```

### Requirements:
- Install OpenCV: `pip install opencv-python`
- Ensure the paths provided for images are valid and accessible.

This script provides a CLI for applying blur effects to images. Extending this for videos would involve additional logic for frame-by-frame processing using OpenCV's video handling capabilities.
