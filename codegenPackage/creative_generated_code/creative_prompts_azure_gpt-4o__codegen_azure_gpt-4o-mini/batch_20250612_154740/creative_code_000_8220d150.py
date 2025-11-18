"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://officineimmagine.it
Prompt: Write Python code using the OpenCV library to create a cinematic-style filter for wedding photos, inspired by the creative approach described on Officine dell’Immagine's website.
Generated: DETERMINISTIC_8220d150c01a77c4
Batch ID: 20250612_154740
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

def apply_cinematic_filter(image_path, output_path):
    """
    Applies a cinematic-style filter to a wedding photo using OpenCV.

    :param image_path: str, path to the input image
    :param output_path: str, path to save the filtered image
    """
    try:
        # Read the input image
        image = cv2.imread(image_path)
        
        # Check if the image was loaded successfully
        if image is None:
            raise FileNotFoundError(f"Image not found: {image_path}")

        # Resize the image for consistency (optional)
        image = cv2.resize(image, (1920, 1080))

        # Apply a Gaussian Blur to smooth the image
        blurred = cv2.GaussianBlur(image, (21, 21), 0)

        # Create a vignette effect by generating a mask
        rows, cols = image.shape[:2]
        X_resultant_kernel = cv2.getGaussianKernel(cols, 200)
        Y_resultant_kernel = cv2.getGaussianKernel(rows, 200)
        kernel = Y_resultant_kernel * X_resultant_kernel.T
        mask = kernel / kernel.max()  # Normalize mask to range [0, 1]

        # Apply the vignette effect by multiplying the mask with the blurred image
        vignette = blurred * mask[:, :, np.newaxis]

        # Enhance colors using the CLAHE (Contrast Limited Adaptive Histogram Equalization)
        lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
        l, a, b = cv2.split(lab)
        clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
        cl = clahe.apply(l)
        enhanced_lab = cv2.merge((cl, a, b))
        enhanced_image = cv2.cvtColor(enhanced_lab, cv2.COLOR_LAB2BGR)

        # Blend the original image with the vignette and the enhanced image
        blended = cv2.addWeighted(enhanced_image, 0.7, vignette.astype(np.uint8), 0.3, 0)

        # Save the final image
        cv2.imwrite(output_path, blended)
        print(f"Filtered image saved as: {output_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    apply_cinematic_filter('path/to/input/photo.jpg', 'path/to/output/photo_filtered.jpg')
```
