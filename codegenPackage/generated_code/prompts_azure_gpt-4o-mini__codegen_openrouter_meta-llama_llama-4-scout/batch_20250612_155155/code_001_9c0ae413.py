"""
Generated Code Metadata:
========================
Original URL: https://euler.is
Prompt: Write a code snippet that detects common defects like warpage and spatter in LPBF prints as outlined by Euler.
Generated: DETERMINISTIC_9c0ae41311179376
Batch ID: 20250612_155155
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from skimage import io, filters, morphology
from skimage.feature import peak_local_max
from scipy import ndimage

def detect_warpage(image):
    """
    Detect warpage in LPBF prints.

    Parameters:
    image (ndarray): 2D image of the LPBF print.

    Returns:
    warpage_mask (ndarray): Binary mask indicating warpage regions.
    """
    # Apply Gaussian filter to reduce noise
    blurred_image = filters.gaussian(image, sigma=2)

    # Calculate gradient magnitude
    grad_mag = filters.sobel(blurred_image)

    # Threshold gradient magnitude to obtain warpage regions
    warpage_mask = grad_mag > 0.5 * grad_mag.max()

    return warpage_mask

def detect_spatter(image):
    """
    Detect spatter in LPBF prints.

    Parameters:
    image (ndarray): 2D image of the LPBF print.

    Returns:
    spatter_mask (ndarray): Binary mask indicating spatter regions.
    """
    # Apply median filter to reduce noise
    filtered_image = filters.median(image, np.ones((3, 3)))

    # Calculate local threshold using Otsu's method
    thresh = filters.threshold_otsu(filtered_image)

    # Binarize image
    binary_image = filtered_image > thresh

    # Remove small objects
    cleaned_image = morphology.closing(binary_image, np.ones((3, 3)))

    # Label connected components
    labeled_image, _ = ndimage.label(cleaned_image)

    # Identify small, isolated regions as spatter
    spatter_mask = labeled_image > 0
    spatter_mask = morphology.opening(spatter_mask, np.ones((3, 3)))

    return spatter_mask

def euler_defect_detection(image_path):
    """
    Detect common defects like warpage and spatter in LPBF prints.

    Parameters:
    image_path (str): Path to the image file.

    Returns:
    defects (dict): Dictionary containing warpage and spatter masks.
    """
    try:
        # Load image
        image = io.imread(image_path)

        # Detect warpage
        warpage_mask = detect_warpage(image)

        # Detect spatter
        spatter_mask = detect_spatter(image)

        # Store results in dictionary
        defects = {
            'warpage': warpage_mask,
            'spatter': spatter_mask
        }

        return defects

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    image_path = "path_to_your_image.jpg"
    defects = euler_defect_detection(image_path)

    if defects:
        warpage_mask = defects['warpage']
        spatter_mask = defects['spatter']

        # Visualize results
        import matplotlib.pyplot as plt

        image = io.imread(image_path)
        plt.figure(figsize=(10, 5))

        plt.subplot(1, 3, 1)
        plt.imshow(image)
        plt.title("Original Image")

        plt.subplot(1, 3, 2)
        plt.imshow(warpage_mask, cmap='gray')
        plt.title("Warpage Mask")

        plt.subplot(1, 3, 3)
        plt.imshow(spatter_mask, cmap='gray')
        plt.title("Spatter Mask")

        plt.show()
```
