"""
Generated Code Metadata:
========================
Original URL: https://euler.is
Prompt: Generate a function that utilizes Euler's defect detection annotations to improve the quality of LPBF prints.
Generated: DETERMINISTIC_96045fa969de93b7
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
from scipy import ndimage
from skimage import morphology
from typing import Tuple, List, Optional

def detect_defects_using_euler_annotations(
    layer_image: np.ndarray,
    min_defect_size: int = 5,
    connectivity: int = 2,
    intensity_threshold: float = 0.2,
    euler_threshold: float = 0.5
) -> Tuple[np.ndarray, List[Tuple[int, int]]]:
    """
    Detect defects in LPBF prints using Euler's defect detection annotations.
    
    Args:
        layer_image: 2D numpy array representing the layer image (grayscale)
        min_defect_size: Minimum size of defects to be considered (in pixels)
        connectivity: Connectivity for morphological operations (1=4-connect, 2=8-connect)
        intensity_threshold: Threshold for binarizing the image (0-1)
        euler_threshold: Threshold for Euler characteristic to identify defects
        
    Returns:
        Tuple containing:
            - Binary mask of detected defects
            - List of defect centroid coordinates
    """
    
    # Input validation
    if not isinstance(layer_image, np.ndarray) or len(layer_image.shape) != 2:
        raise ValueError("Input must be a 2D numpy array")
    if not 0 <= intensity_threshold <= 1:
        raise ValueError("Intensity threshold must be between 0 and 1")
    
    try:
        # Normalize image to [0, 1] range if needed
        if layer_image.max() > 1.0:
            layer_image = layer_image.astype(np.float32) / 255.0
        
        # Binarize the image
        binary_image = layer_image > intensity_threshold
        
        # Calculate Euler characteristic
        euler_map = morphology.euler_number(binary_image, connectivity=connectivity)
        
        # Identify regions with significant Euler characteristic changes
        defect_mask = np.abs(euler_map) > euler_threshold
        
        # Clean up the defect mask
        defect_mask = morphology.remove_small_objects(defect_mask, min_size=min_defect_size)
        defect_mask = morphology.remove_small_holes(defect_mask, area_threshold=min_defect_size)
        
        # Label connected components
        labeled_defects, num_defects = ndimage.label(defect_mask)
        
        # Calculate centroids of defects
        centroids = []
        if num_defects > 0:
            centroids = ndimage.center_of_mass(defect_mask, labeled_defects, range(1, num_defects+1))
            centroids = [(int(y), int(x)) for y, x in centroids]
        
        return defect_mask, centroids
    
    except Exception as e:
        raise RuntimeError(f"Error during defect detection: {str(e)}")

def process_lpbf_layers(
    layer_images: List[np.ndarray],
    **kwargs
) -> List[Tuple[np.ndarray, List[Tuple[int, int]]]]:
    """
    Process multiple LPBF layers for defect detection.
    
    Args:
        layer_images: List of 2D numpy arrays representing layer images
        **kwargs: Additional arguments to pass to detect_defects_using_euler_annotations
        
    Returns:
        List of tuples containing defect masks and centroids for each layer
    """
    results = []
    for idx, img in enumerate(layer_images):
        try:
            result = detect_defects_using_euler_annotations(img, **kwargs)
            results.append(result)
        except Exception as e:
            print(f"Error processing layer {idx}: {str(e)}")
            results.append((np.zeros_like(img, dtype=bool), []))
    return results
```
