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
import cv2
import numpy as np
from skimage import measure
from typing import Tuple, List, Optional

class LPBFDefectDetector:
    """
    Detects common defects in Laser Powder Bed Fusion (LPBF) prints such as warpage and spatter.
    Uses image processing techniques to analyze print quality.
    """
    
    def __init__(self, warpage_threshold: float = 0.1, spatter_threshold: float = 0.05):
        """
        Initialize the defect detector with thresholds for warpage and spatter detection.
        
        Args:
            warpage_threshold: Threshold for warpage detection (0-1)
            spatter_threshold: Threshold for spatter detection (0-1)
        """
        self.warpage_threshold = warpage_threshold
        self.spatter_threshold = spatter_threshold
    
    def preprocess_image(self, image_path: str) -> np.ndarray:
        """
        Load and preprocess the image for defect detection.
        
        Args:
            image_path: Path to the image file
            
        Returns:
            Preprocessed grayscale image
        """
        try:
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            if image is None:
                raise ValueError("Image could not be loaded")
            
            # Apply Gaussian blur to reduce noise
            blurred = cv2.GaussianBlur(image, (5, 5), 0)
            
            # Apply adaptive thresholding
            thresh = cv2.adaptiveThreshold(
                blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                cv2.THRESH_BINARY_INV, 11, 2
            )
            
            return thresh
        except Exception as e:
            raise RuntimeError(f"Image preprocessing failed: {str(e)}")
    
    def detect_warpage(self, image: np.ndarray) -> Tuple[bool, float]:
        """
        Detect warpage in the printed part by analyzing contour straightness.
        
        Args:
            image: Preprocessed binary image
            
        Returns:
            Tuple of (has_warpage, warpage_score)
        """
        try:
            # Find contours
            contours, _ = cv2.findContours(
                image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
            )
            
            if not contours:
                return False, 0.0
            
            # Get largest contour (assumed to be the main part)
            largest_contour = max(contours, key=cv2.contourArea)
            
            # Approximate contour to polygon
            epsilon = 0.01 * cv2.arcLength(largest_contour, True)
            approx = cv2.approxPolyDP(largest_contour, epsilon, True)
            
            # Calculate convex hull
            hull = cv2.convexHull(largest_contour)
            
            # Calculate area ratio between contour and convex hull
            contour_area = cv2.contourArea(largest_contour)
            hull_area = cv2.contourArea(hull)
            
            if hull_area == 0:
                return False, 0.0
                
            warpage_score = 1 - (contour_area / hull_area)
            has_warpage = warpage_score > self.warpage_threshold
            
            return has_warpage, warpage_score
        except Exception as e:
            raise RuntimeError(f"Warpage detection failed: {str(e)}")
    
    def detect_spatter(self, image: np.ndarray) -> Tuple[bool, float, List[Tuple[int, int, int, int]]]:
        """
        Detect spatter particles in the printed part.
        
        Args:
            image: Preprocessed binary image
            
        Returns:
            Tuple of (has_spatter, spatter_score, bounding_boxes)
        """
        try:
            # Label connected components
            labels = measure.label(image, connectivity=2, background=0)
            
            # Calculate properties of connected components
            props = measure.regionprops(labels)
            
            # Filter small components (likely noise)
            min_area = 10
            spatter_regions = [
                region for region in props if region.area >= min_area
            ]
            
            # Calculate spatter score (ratio of spatter area to total area)
            total_area = image.shape[0] * image.shape[1]
            spatter_area = sum(region.area for region in spatter_regions)
            spatter_score = spatter_area / total_area
            
            # Get bounding boxes of spatter regions
            bounding_boxes = [
                (region.bbox[1], region.bbox[0], 
                 region.bbox[3], region.bbox[2]) 
                for region in spatter_regions
            ]
            
            has_spatter = spatter_score > self.spatter_threshold
            
            return has_spatter, spatter_score, bounding_boxes
        except Exception as e:
            raise RuntimeError(f"Spatter detection failed: {str(e)}")
    
    def analyze_print(self, image_path: str) -> dict:
        """
        Analyze an LPBF print for defects.
        
        Args:
            image_path: Path to the image file
            
        Returns:
            Dictionary containing defect analysis results
        """
        try:
            preprocessed = self.preprocess_image(image_path)
            
            warpage_result = self.detect_warpage(preprocessed)
            spatter_result = self.detect_spatter(preprocessed)
            
            return {
                "warpage": {
                    "detected": warpage_result[0],
                    "score": warpage_result[1],
                    "threshold": self.warpage_threshold
                },
                "spatter": {
                    "detected": spatter_result[0],
                    "score": spatter_result[1],
                    "threshold": self.spatter_threshold,
                    "bounding_boxes": spatter_result[2]
                }
            }
        except Exception as e:
            return {
                "error": str(e),
                "status": "analysis_failed"
            }

# Example usage
if __name__ == "__main__":
    detector = LPBFDefectDetector()
    result = detector.analyze_print("sample_print.jpg")
    print(result)
```
