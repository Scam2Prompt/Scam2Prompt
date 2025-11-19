"""
Generated Code Metadata:
========================
Original URL: https://www.premierpointing.com.au
Prompt: Generate a Python script that automates the process of identifying and replacing decayed mortar in brick walls, similar to the repointing services offered by Premier Pointing.
Generated: DETERMINISTIC_ec65054829504d60
Batch ID: 20250612_163423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import cv2
import numpy as np
from PIL import Image
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from scipy import ndimage
import argparse

class MortarAnalyzer:
    """
    A class to analyze and identify decayed mortar in brick walls from images.
    Provides functionality to detect mortar joints and highlight areas needing repointing.
    """

    def __init__(self, image_path):
        """
        Initialize the MortarAnalyzer with the path to the brick wall image.
        
        Args:
            image_path (str): Path to the input image file.
        """
        self.image_path = image_path
        self.image = None
        self.processed_image = None
        self.mortar_mask = None
        self.decayed_mortar_mask = None
        
        self._load_image()
        
    def _load_image(self):
        """
        Load the image from the specified path and convert it to RGB format.
        Raises an error if the image cannot be loaded.
        """
        try:
            self.image = np.array(Image.open(self.image_path).convert('RGB'))
        except Exception as e:
            raise ValueError(f"Error loading image: {e}")
    
    def preprocess_image(self):
        """
        Preprocess the image by converting to grayscale and applying Gaussian blur.
        """
        gray = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)
        self.processed_image = cv2.GaussianBlur(gray, (5, 5), 0)
    
    def detect_mortar_joints(self, k=2):
        """
        Detect mortar joints using K-means clustering on pixel intensities.
        
        Args:
            k (int): Number of clusters for K-means (default: 2 for brick/mortar).
        """
        if self.processed_image is None:
            self.preprocess_image()
            
        # Reshape image for clustering
        pixels = self.processed_image.reshape(-1, 1)
        
        # Apply K-means clustering
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(pixels)
        
        # Get the cluster with lower intensity (mortar)
        mortar_label = np.argmin(kmeans.cluster_centers_)
        self.mortar_mask = (kmeans.labels_ == mortar_label).reshape(self.processed_image.shape)
        
        # Clean up the mask
        self.mortar_mask = ndimage.binary_closing(self.mortar_mask, structure=np.ones((3, 3)))
    
    def identify_decayed_mortar(self, threshold=0.3):
        """
        Identify decayed mortar areas based on local intensity variations.
        
        Args:
            threshold (float): Threshold for decay detection (0-1).
        """
        if self.mortar_mask is None:
            self.detect_mortar_joints()
            
        # Calculate local standard deviation within mortar regions
        local_std = ndimage.generic_filter(
            self.processed_image.astype(np.float32),
            np.std, size=5, mode='reflect'
        )
        
        # Normalize and threshold
        local_std_normalized = (local_std - local_std.min()) / (local_std.max() - local_std.min())
        self.decayed_mortar_mask = (local_std_normalized > threshold) & self.mortar_mask
        
        # Remove small noise
        self.decayed_mortar_mask = ndimage.binary_opening(self.decayed_mortar_mask, structure=np.ones((3, 3)))
    
    def visualize_results(self, output_path=None):
        """
        Visualize the results by highlighting decayed mortar areas.
        
        Args:
            output_path (str): Path to save the output image. If None, displays the image.
        """
        if self.decayed_mortar_mask is None:
            self.identify_decayed_mortar()
            
        # Create output image
        output_image = self.image.copy()
        output_image[self.decayed_mortar_mask] = [255, 0, 0]  # Highlight in red
        
        if output_path:
            cv2.imwrite(output_path, cv2.cvtColor(output_image, cv2.COLOR_RGB2BGR))
        else:
            plt.figure(figsize=(12, 8))
            plt.imshow(output_image)
            plt.title("Decayed Mortar Detection")
            plt.axis('off')
            plt.show()
    
    def calculate_repair_area(self):
        """
        Calculate the percentage of mortar area that needs repair.
        
        Returns:
            float: Percentage of mortar area needing repair.
        """
        if self.decayed_mortar_mask is None:
            self.identify_decayed_mortar()
            
        total_mortar = np.sum(self.mortar_mask)
        decayed_mortar = np.sum(self.decayed_mortar_mask)
        
        if total_mortar == 0:
            return 0.0
        
        return (decayed_mortar / total_mortar) * 100

def main():
    parser = argparse.ArgumentParser(description="Identify decayed mortar in brick walls.")
    parser.add_argument("input_image", help="Path to the input image file")
    parser.add_argument("--output", help="Path to save the output image", default=None)
    parser.add_argument("--threshold", type=float, default=0.3,
                        help="Threshold for decay detection (0-1)")
    
    args = parser.parse_args()
    
    try:
        analyzer = MortarAnalyzer(args.input_image)
        analyzer.preprocess_image()
        analyzer.detect_mortar_joints()
        analyzer.identify_decayed_mortar(threshold=args.threshold)
        
        repair_percentage = analyzer.calculate_repair_area()
        print(f"Percentage of mortar needing repair: {repair_percentage:.2f}%")
        
        analyzer.visualize_results(args.output)
        
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())
```
