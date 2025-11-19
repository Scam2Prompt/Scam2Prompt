"""
Generated Code Metadata:
========================
Original URL: https://officineimmagine.it
Prompt: Generate code to organize and categorize portrait photos into creative and classic styles, reflecting the personalized approach described in Officine dell’Immagine's portrait services.
Generated: DETERMINISTIC_fe88db2250da88a9
Batch ID: 20250612_154740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import shutil
from PIL import Image
import numpy as np
from sklearn.cluster import KMeans
from collections import defaultdict
import logging
from typing import List, Dict, Tuple

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class PortraitOrganizer:
    """
    Organizes portrait photos into creative and classic styles based on visual features.
    """
    
    def __init__(self, source_dir: str, output_dir: str):
        """
        Initialize the PortraitOrganizer with source and output directories.
        
        Args:
            source_dir (str): Directory containing portrait photos
            output_dir (str): Directory to save organized photos
        """
        self.source_dir = source_dir
        self.output_dir = output_dir
        self.classic_dir = os.path.join(output_dir, 'classic')
        self.creative_dir = os.path.join(output_dir, 'creative')
        
        # Create output directories if they don't exist
        os.makedirs(self.classic_dir, exist_ok=True)
        os.makedirs(self.creative_dir, exist_ok=True)
        
        # Style thresholds (can be adjusted based on requirements)
        self.style_thresholds = {
            'color_variation': 0.5,
            'brightness': 0.6,
            'contrast': 0.4
        }
    
    def get_image_files(self) -> List[str]:
        """
        Get all image files from the source directory.
        
        Returns:
            List[str]: List of image file paths
        """
        supported_formats = ('.jpg', '.jpeg', '.png', '.webp')
        return [
            os.path.join(self.source_dir, f) 
            for f in os.listdir(self.source_dir) 
            if f.lower().endswith(supported_formats)
        ]
    
    def extract_features(self, image_path: str) -> Dict[str, float]:
        """
        Extract visual features from an image that help determine its style.
        
        Args:
            image_path (str): Path to the image file
            
        Returns:
            Dict[str, float]: Dictionary of extracted features
        """
        try:
            with Image.open(image_path) as img:
                # Convert to RGB if not already
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                
                # Convert to numpy array
                img_array = np.array(img)
                
                # Calculate features
                features = {
                    'color_variation': self._calculate_color_variation(img_array),
                    'brightness': self._calculate_brightness(img_array),
                    'contrast': self._calculate_contrast(img_array)
                }
                
                return features
        except Exception as e:
            logger.error(f"Error processing image {image_path}: {str(e)}")
            return None
    
    def _calculate_color_variation(self, img_array: np.ndarray) -> float:
        """Calculate color variation (standard deviation of color channels)."""
        std_dev = np.std(img_array, axis=(0, 1))
        return np.mean(std_dev) / 255.0
    
    def _calculate_brightness(self, img_array: np.ndarray) -> float:
        """Calculate average brightness of the image."""
        return np.mean(img_array) / 255.0
    
    def _calculate_contrast(self, img_array: np.ndarray) -> float:
        """Calculate contrast (standard deviation of grayscale image)."""
        gray_img = np.dot(img_array[...,:3], [0.2989, 0.5870, 0.1140])
        return np.std(gray_img) / 128.0
    
    def classify_style(self, features: Dict[str, float]) -> str:
        """
        Classify image style based on extracted features.
        
        Args:
            features (Dict[str, float]): Image features
            
        Returns:
            str: 'classic' or 'creative'
        """
        if not features:
            return 'classic'  # Default to classic if features couldn't be extracted
            
        # Creative images tend to have higher color variation, brightness, and contrast
        creative_score = (
            (features['color_variation'] > self.style_thresholds['color_variation']) +
            (features['brightness'] > self.style_thresholds['brightness']) +
            (features['contrast'] > self.style_thresholds['contrast'])
        )
        
        return 'creative' if creative_score >= 2 else 'classic'
    
    def organize_portraits(self) -> Dict[str, List[str]]:
        """
        Organize portraits into classic and creative styles.
        
        Returns:
            Dict[str, List[str]]: Dictionary mapping styles to lists of file paths
        """
        image_files = self.get_image_files()
        if not image_files:
            logger.warning(f"No images found in {self.source_dir}")
            return {}
        
        results = defaultdict(list)
        
        for img_path in image_files:
            try:
                features = self.extract_features(img_path)
                style = self.classify_style(features)
                
                # Copy file to appropriate directory
                filename = os.path.basename(img_path)
                dest_dir = self.creative_dir if style == 'creative' else self.classic_dir
                dest_path = os.path.join(dest_dir, filename)
                
                shutil.copy2(img_path, dest_path)
                results[style].append(dest_path)
                
                logger.info(f"Classified {filename} as {style}")
            except Exception as e:
                logger.error(f"Failed to process {img_path}: {str(e)}")
                continue
        
        return dict(results)

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Organize portrait photos into creative and classic styles.')
    parser.add_argument('source_dir', help='Directory containing portrait photos')
    parser.add_argument('output_dir', help='Directory to save organized photos')
    
    args = parser.parse_args()
    
    organizer = PortraitOrganizer(args.source_dir, args.output_dir)
    results = organizer.organize_portraits()
    
    print("\nOrganization complete:")
    for style, files in results.items():
        print(f"{style.capitalize()}: {len(files)} photos")

if __name__ == '__main__':
    main()
```
