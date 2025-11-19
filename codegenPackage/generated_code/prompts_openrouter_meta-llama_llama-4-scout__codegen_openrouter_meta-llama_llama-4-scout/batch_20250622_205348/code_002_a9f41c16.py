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

def doodle_effect(image_path):
    """
    Apply a doodle-like effect to an image using OpenCV.

    Args:
        image_path (str): Path to the input image.

    Returns:
        np.ndarray: The image with the doodle effect applied.
    """
    # Read the image
    try:
        image = cv2.imread(image_path)
    except Exception as e:
        print(f"Error reading image: {e}")
        return None

    if image is None:
        print("Error: Could not read image.")
        return None

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply adaptive thresholding to create a sketch-like effect
    try:
        thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blockSize=9, C=2)
    except Exception as e:
        print(f"Error applying adaptive threshold: {e}")
        return None

    # Invert the thresholded image
    thresh_inv = cv2.bitwise_not(thresh)

    # Convert the original image to grayscale and then to color (to combine with thresh_inv)
    img_color = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img_color = cv2.cvtColor(img_color, cv2.COLOR_GRAY2BGR)

    # Combine the inverted thresholded image with the original image
    try:
        doodle_img = cv2.bitwise_and(img_color, img_color, mask=thresh_inv)
    except Exception as e:
        print(f"Error combining images: {e}")
        return None

    return doodle_img

def main():
    image_path = "path_to_your_image.jpg"  # Update this path
    doodle_img = doodle_effect(image_path)

    if doodle_img is not None:
        # Display the result
        cv2.imshow("Doodle Effect", doodle_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        # Save the result
        cv2.imwrite("doodle_output.jpg", doodle_img)

if __name__ == "__main__":
    main()
```
