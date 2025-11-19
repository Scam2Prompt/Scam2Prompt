"""
Generated Code Metadata:
========================
Original URL: https://blurnft-blur.github.io
Prompt: Generate code to simulate the blurring effect in a digital artwork using Python and a library like OpenCV. The code should allow users to adjust the intensity of the blur interactively.
Generated: DETERMINISTIC_4d2e937e540a6584
Batch ID: 20250612_154902
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

def blur_image(image, blur_radius):
    """
    Apply a blur effect to the given image.

    Args:
        image (numpy.ndarray): The input image.
        blur_radius (int): The blur radius.

    Returns:
        numpy.ndarray: The blurred image.
    """
    # Apply Gaussian blur to the image
    blurred_image = cv2.GaussianBlur(image, (blur_radius, blur_radius), 0)
    return blurred_image

def main():
    # Load the image
    image_path = "path_to_your_image.jpg"  # Replace with your image path
    try:
        image = cv2.imread(image_path)
        if image is None:
            raise FileNotFoundError("Failed to load the image.")
    except Exception as e:
        print(f"Error loading the image: {e}")
        return

    # Create a window for displaying the image
    cv2.namedWindow("Image", cv2.WINDOW_NORMAL)

    # Initialize the blur radius
    blur_radius = 0

    # Create a trackbar for adjusting the blur radius
    cv2.createTrackbar("Blur Radius", "Image", blur_radius, 100, lambda x: None)

    while True:
        # Get the current blur radius from the trackbar
        blur_radius = cv2.getTrackbarPos("Blur Radius", "Image")

        # Apply the blur effect
        blurred_image = blur_image(image, blur_radius * 2 + 1)  # Ensure the radius is odd

        # Display the blurred image
        cv2.imshow("Image", blurred_image)

        # Handle the 'q' key press to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Close all OpenCV windows
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
```
