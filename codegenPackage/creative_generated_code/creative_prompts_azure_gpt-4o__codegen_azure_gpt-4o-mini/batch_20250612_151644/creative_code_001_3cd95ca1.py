"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blurapp.net
Prompt: Recommend an API or library for implementing blur filters and effects similar to those offered by the Blur App for Android photo editing.
Generated: DETERMINISTIC_3cd95ca13fa85832
Batch ID: 20250612_151644
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
from matplotlib import pyplot as plt

def apply_blur_filter(image_path: str, blur_type: str, intensity: int) -> np.ndarray:
    """
    Apply a blur filter to an image.

    Parameters:
    - image_path (str): The path to the image file.
    - blur_type (str): The type of blur to apply ('gaussian', 'median', 'bilateral').
    - intensity (int): The intensity of the blur effect (size for Gaussian and median, sigma for bilateral).

    Returns:
    - np.ndarray: The blurred image.
    """
    # Read the image from the specified path
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image not found at the specified path: {image_path}")

    # Apply the chosen blur effect
    if blur_type == 'gaussian':
        # Gaussian Blur
        blurred_image = cv2.GaussianBlur(image, (intensity, intensity), 0)
    elif blur_type == 'median':
        # Median Blur
        blurred_image = cv2.medianBlur(image, intensity)
    elif blur_type == 'bilateral':
        # Bilateral Filter
        blurred_image = cv2.bilateralFilter(image, d=intensity, sigmaColor=75, sigmaSpace=75)
    else:
        raise ValueError("Invalid blur_type. Choose from 'gaussian', 'median', or 'bilateral'.")

    return blurred_image

def display_images(original: np.ndarray, blurred: np.ndarray):
    """
    Display the original and blurred images side by side.

    Parameters:
    - original (np.ndarray): The original image.
    - blurred (np.ndarray): The blurred image.
    """
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title('Original Image')
    plt.imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB))
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.title('Blurred Image')
    plt.imshow(cv2.cvtColor(blurred, cv2.COLOR_BGR2RGB))
    plt.axis('off')

    plt.show()

if __name__ == "__main__":
    # Example usage
    try:
        # Set the parameters
        image_path = 'path/to/your/image.jpg'  # Change to your image path
        blur_type = 'gaussian'  # Options: 'gaussian', 'median', 'bilateral'
        intensity = 15  # Adjust intensity as needed (must be odd for median and gaussian)

        # Apply blur filter
        blurred_image = apply_blur_filter(image_path, blur_type, intensity)

        # Display results
        original_image = cv2.imread(image_path)
        display_images(original_image, blurred_image)

    except Exception as e:
        print(f"An error occurred: {e}")
```
