"""
Generated Code Metadata:
========================
Original URL: https://financestargate.com
Prompt: Create a code snippet for preprocessing techniques to improve face recognition accuracy, inspired by Finance StarGate's content.
Generated: DETERMINISTIC_60587b31e13e3491
Batch ID: 20250612_154455
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
from skimage import exposure
from skimage.filters import unsharp_mask

def preprocess_face(image_path, target_size=(150, 150)):
    """
    Preprocess a face image for recognition by applying:
    1. Histogram equalization
    2. Unsharp masking
    3. Gaussian blur
    4. Normalization
    5. Resizing
    
    Args:
        image_path (str): Path to the input image
        target_size (tuple): Target size for resizing (width, height)
        
    Returns:
        numpy.ndarray: Preprocessed grayscale image
    """
    try:
        # Load image in grayscale
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if image is None:
            raise ValueError("Image not found or unable to load")
            
        # 1. Histogram equalization for contrast enhancement
        image_eq = exposure.equalize_hist(image)
        
        # 2. Unsharp masking to enhance edges
        image_unsharp = unsharp_mask(image_eq, radius=1, amount=2)
        image_unsharp = (image_unsharp * 255).astype(np.uint8)
        
        # 3. Gaussian blur for noise reduction
        image_blur = cv2.GaussianBlur(image_unsharp, (3, 3), 0)
        
        # 4. Normalize pixel values to [0, 1]
        image_norm = cv2.normalize(image_blur, None, 0, 1.0, cv2.NORM_MINMAX, dtype=cv2.CV_32F)
        
        # 5. Resize to target dimensions
        image_resized = cv2.resize(image_norm, target_size)
        
        return image_resized
        
    except Exception as e:
        print(f"Error during preprocessing: {str(e)}")
        return None

# Example usage
if __name__ == "__main__":
    processed_face = preprocess_face("sample_face.jpg")
    if processed_face is not None:
        cv2.imshow("Preprocessed Face", processed_face)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
```
