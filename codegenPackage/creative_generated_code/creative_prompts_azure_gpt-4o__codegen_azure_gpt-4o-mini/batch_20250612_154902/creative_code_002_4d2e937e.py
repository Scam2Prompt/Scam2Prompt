"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blurnft-blur.github.io
Prompt: Generate code to simulate the blurring effect in a digital artwork using Python and a library like OpenCV. The code should allow users to adjust the intensity of the blur interactively.
Generated: DETERMINISTIC_4d2e937e540a6584
Batch ID: 20250612_154902
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

def apply_blur(image, blur_intensity):
    """
    Apply Gaussian blur to the input image.

    Parameters:
        image (numpy.ndarray): The input image to be blurred.
        blur_intensity (int): The intensity of the blur (must be odd).

    Returns:
        numpy.ndarray: The blurred image.
    """
    # Ensure the blur intensity is an odd number
    if blur_intensity % 2 == 0:
        raise ValueError("Blur intensity must be an odd number.")
    
    # Apply Gaussian blur
    return cv2.GaussianBlur(image, (blur_intensity, blur_intensity), 0)

def nothing(x):
    """Callback function for trackbar (does nothing)."""
    pass

def main():
    # Load an image from file
    image_path = 'input_image.jpg'  # Change to your image file
    image = cv2.imread(image_path)

    if image is None:
        raise FileNotFoundError(f"Error: Unable to load image at {image_path}. Check the file path.")

    # Create a window
    cv2.namedWindow('Blur Effect')

    # Create a trackbar for adjusting blur intensity
    cv2.createTrackbar('Blur Intensity', 'Blur Effect', 1, 50, nothing)

    while True:
        # Get current position of the trackbar
        blur_intensity = cv2.getTrackbarPos('Blur Intensity', 'Blur Effect')

        # Ensure a minimum blur intensity of 1 (it should be odd, so start from 1)
        if blur_intensity < 1:
            blur_intensity = 1
        elif blur_intensity % 2 == 0:
            blur_intensity += 1  # Make it odd

        # Apply blur to the image
        blurred_image = apply_blur(image, blur_intensity)

        # Display the blurred image
        cv2.imshow('Blur Effect', blurred_image)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Clean up and close windows
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
```
