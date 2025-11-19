"""
Generated Code Metadata:
========================
Original URL: https://officineimmagine.it
Prompt: Write code to analyze and enhance the lighting in boudoir photography images, ensuring an intimate and relaxed atmosphere as described on Officine dell’Immagine's website.
Generated: DETERMINISTIC_e03ca5170a04663d
Batch ID: 20250612_154740
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
import matplotlib.pyplot as plt

def enhance_boudoir_lighting(image_path, output_path):
    """
    Enhance the lighting of boudoir photography images to create an intimate and relaxed atmosphere.

    Parameters:
    - image_path: str, path to the input image.
    - output_path: str, path to save the enhanced image.
    """
    try:
        # Load the image
        image = cv2.imread(image_path)
        if image is None:
            raise FileNotFoundError(f"Image not found at the path: {image_path}")

        # Convert the image to the LAB color space
        lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

        # Split the LAB image into L, A, and B channels
        l_channel, a_channel, b_channel = cv2.split(lab_image)

        # Apply CLAHE (Contrast Limited Adaptive Histogram Equalization) to the L channel
        clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
        cl = clahe.apply(l_channel)

        # Merge the enhanced L channel back with A and B channels
        enhanced_lab_image = cv2.merge((cl, a_channel, b_channel))

        # Convert the LAB image back to BGR color space
        enhanced_image = cv2.cvtColor(enhanced_lab_image, cv2.COLOR_LAB2BGR)

        # Apply a slight Gaussian blur to soften the image
        enhanced_image = cv2.GaussianBlur(enhanced_image, (5, 5), 0)

        # Save the enhanced image
        cv2.imwrite(output_path, enhanced_image)

        print(f"Enhanced image saved at: {output_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    input_image_path = 'path/to/your/boudoir_image.jpg'  # Replace with your image path
    output_image_path = 'path/to/save/enhanced_image.jpg'  # Replace with desired output path
    enhance_boudoir_lighting(input_image_path, output_image_path)

    # Display the original and enhanced images for comparison
    original_image = cv2.imread(input_image_path)
    enhanced_image = cv2.imread(output_image_path)

    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title('Original Image')
    plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.title('Enhanced Image')
    plt.imshow(cv2.cvtColor(enhanced_image, cv2.COLOR_BGR2RGB))
    plt.axis('off')

    plt.show()
```
