"""
Generated Code Metadata:
========================
Original URL: https://www.pics3dstudio.com
Prompt: "Generate a Python script to stitch 360-degree photos for virtual reality experiences similar to PICS3DStudio's work."
Generated: DETERMINISTIC_02d3e2061e848fc5
Batch ID: 20250622_211932
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
import glob
from typing import List, Tuple, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class ImageStitcher:
    """
    A class to stitch 360-degree photos for VR experiences.
    """
    
    def __init__(self, output_path: str = "output_360.jpg"):
        """
        Initialize the ImageStitcher with output path.
        
        Args:
            output_path (str): Path to save the stitched image. Defaults to "output_360.jpg".
        """
        self.output_path = output_path
        self.stitcher = cv2.Stitcher_create(cv2.Stitcher_PANORAMA)
        
    def load_images(self, image_folder: str) -> Optional[List[np.ndarray]]:
        """
        Load images from a folder.
        
        Args:
            image_folder (str): Path to folder containing images.
            
        Returns:
            Optional[List[np.ndarray]]: List of loaded images or None if error occurs.
        """
        try:
            if not os.path.isdir(image_folder):
                raise FileNotFoundError(f"Folder {image_folder} does not exist.")
                
            image_paths = glob.glob(os.path.join(image_folder, "*.jpg")) + \
                          glob.glob(os.path.join(image_folder, "*.png"))
            
            if not image_paths:
                raise ValueError(f"No images found in {image_folder}")
                
            images = []
            for image_path in image_paths:
                img = cv2.imread(image_path)
                if img is not None:
                    images.append(img)
                else:
                    logger.warning(f"Could not read image: {image_path}")
            
            if not images:
                raise ValueError("No valid images loaded.")
                
            return images
            
        except Exception as e:
            logger.error(f"Error loading images: {e}")
            return None
    
    def stitch_images(self, images: List[np.ndarray]) -> Tuple[int, Optional[np.ndarray]]:
        """
        Stitch a list of images into a panorama.
        
        Args:
            images (List[np.ndarray]): List of images to stitch.
            
        Returns:
            Tuple[int, Optional[np.ndarray]]: Status code and stitched image.
                Status codes:
                    0: Success
                    1: Error
        """
        try:
            if len(images) < 2:
                raise ValueError("At least 2 images are required for stitching.")
                
            status, panorama = self.stitcher.stitch(images)
            
            if status != cv2.Stitcher_OK:
                raise RuntimeError(f"Stitching failed with status {status}")
                
            return status, panorama
            
        except Exception as e:
            logger.error(f"Error during stitching: {e}")
            return 1, None
    
    def save_image(self, image: np.ndarray) -> bool:
        """
        Save the stitched image to the output path.
        
        Args:
            image (np.ndarray): Image to save.
            
        Returns:
            bool: True if successful, False otherwise.
        """
        try:
            if image is None:
                raise ValueError("No image provided to save.")
                
            cv2.imwrite(self.output_path, image)
            logger.info(f"Image successfully saved to {self.output_path}")
            return True
            
        except Exception as e:
            logger.error(f"Error saving image: {e}")
            return False
    
    def process(self, image_folder: str) -> bool:
        """
        Complete processing pipeline: load, stitch, and save images.
        
        Args:
            image_folder (str): Path to folder containing images.
            
        Returns:
            bool: True if successful, False otherwise.
        """
        images = self.load_images(image_folder)
        if not images:
            return False
            
        status, panorama = self.stitch_images(images)
        if status != 0 or panorama is None:
            return False
            
        return self.save_image(panorama)


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="360-degree Photo Stitcher for VR Experiences")
    parser.add_argument("image_folder", help="Path to folder containing images to stitch")
    parser.add_argument("--output", help="Output file path", default="output_360.jpg")
    
    args = parser.parse_args()
    
    stitcher = ImageStitcher(args.output)
    success = stitcher.process(args.image_folder)
    
    if not success:
        logger.error("Failed to create panorama.")
        exit(1)
```
