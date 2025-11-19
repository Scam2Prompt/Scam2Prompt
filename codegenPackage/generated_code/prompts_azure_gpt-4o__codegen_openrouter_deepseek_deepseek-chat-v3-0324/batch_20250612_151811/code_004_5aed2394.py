"""
Generated Code Metadata:
========================
Original URL: https://metamasks.art
Prompt: Suggest open-source alternatives to AndreaMosaic for creating artistic mosaics and provide example code for using one of them.
Generated: DETERMINISTIC_5aed2394a66ba731
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script demonstrates using OpenMosaic, an open-source alternative to AndreaMosaic,
to create an artistic mosaic from a collection of images.
"""

import os
import cv2
import numpy as np
from glob import glob
from sklearn.cluster import KMeans

class OpenMosaic:
    def __init__(self, target_image_path, tile_images_dir, output_path, tile_size=(50, 50)):
        """
        Initialize the mosaic creator.
        
        Args:
            target_image_path (str): Path to the target image to recreate as mosaic
            tile_images_dir (str): Directory containing tile images
            output_path (str): Path to save the output mosaic
            tile_size (tuple): Size of each tile in pixels (width, height)
        """
        self.target_image = cv2.imread(target_image_path)
        if self.target_image is None:
            raise ValueError(f"Could not load target image from {target_image_path}")
            
        self.tile_images_dir = tile_images_dir
        self.output_path = output_path
        self.tile_size = tile_size
        self.tile_images = []
        self.tile_colors = []
        
    def load_tile_images(self):
        """Load and preprocess all tile images from the directory."""
        image_paths = glob(os.path.join(self.tile_images_dir, '*.*'))
        if not image_paths:
            raise ValueError(f"No images found in {self.tile_images_dir}")
            
        for path in image_paths:
            img = cv2.imread(path)
            if img is not None:
                img = cv2.resize(img, self.tile_size)
                self.tile_images.append(img)
                avg_color = np.mean(img, axis=(0, 1))
                self.tile_colors.append(avg_color)
                
        if not self.tile_images:
            raise ValueError("No valid tile images were loaded")
            
    def create_mosaic(self):
        """Create the mosaic image."""
        self.load_tile_images()
        
        # Resize target image to fit exact number of tiles
        h, w = self.target_image.shape[:2]
        tiles_x = w // self.tile_size[0]
        tiles_y = h // self.tile_size[1]
        target_resized = cv2.resize(self.target_image, 
                                  (tiles_x * self.tile_size[0], 
                                   tiles_y * self.tile_size[1]))
        
        # Cluster tile colors for better matching
        kmeans = KMeans(n_clusters=min(256, len(self.tile_colors)), random_state=42)
        kmeans.fit(self.tile_colors)
        tile_labels = kmeans.predict(self.tile_colors)
        
        # Create mosaic
        mosaic = np.zeros_like(target_resized)
        
        for y in range(0, target_resized.shape[0], self.tile_size[1]):
            for x in range(0, target_resized.shape[1], self.tile_size[0]):
                # Get target region average color
                region = target_resized[y:y+self.tile_size[1], x:x+self.tile_size[0]]
                avg_color = np.mean(region, axis=(0, 1))
                
                # Find best matching tile
                label = kmeans.predict([avg_color])[0]
                matching_indices = np.where(tile_labels == label)[0]
                best_match_idx = np.argmin([
                    np.linalg.norm(avg_color - self.tile_colors[i]) 
                    for i in matching_indices
                ])
                best_tile = self.tile_images[matching_indices[best_match_idx]]
                
                # Place tile in mosaic
                mosaic[y:y+self.tile_size[1], x:x+self.tile_size[0]] = best_tile
                
        # Save the result
        cv2.imwrite(self.output_path, mosaic)
        return mosaic

if __name__ == "__main__":
    try:
        mosaic_creator = OpenMosaic(
            target_image_path="input.jpg",
            tile_images_dir="tiles/",
            output_path="output_mosaic.jpg",
            tile_size=(30, 30)
        )
        result = mosaic_creator.create_mosaic()
        print("Mosaic created successfully!")
    except Exception as e:
        print(f"Error creating mosaic: {str(e)}")
```
