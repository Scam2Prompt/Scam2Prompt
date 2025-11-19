"""
Generated Code Metadata:
========================
Original URL: https://mydrones.gr
Prompt: Create a Python script to process drone footage and generate a portfolio grid layout, similar to the gallery formats described on "Drone Media."
Generated: DETERMINISTIC_c284f3425ad3849a
Batch ID: 20250612_152924
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
from PIL import Image, ImageDraw, ImageFont
import argparse
from typing import List, Tuple, Optional

class DroneGalleryGenerator:
    """
    A class to process drone footage and generate a portfolio grid layout.
    """
    
    def __init__(self, input_path: str, output_path: str, grid_size: Tuple[int, int] = (3, 3)):
        """
        Initialize the DroneGalleryGenerator.
        
        Args:
            input_path: Path to directory containing drone footage/images
            output_path: Path to save the generated gallery
            grid_size: Tuple representing rows and columns in the grid (default: 3x3)
        """
        self.input_path = input_path
        self.output_path = output_path
        self.grid_size = grid_size
        self.valid_extensions = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff')
        
        # Create output directory if it doesn't exist
        os.makedirs(self.output_path, exist_ok=True)
    
    def load_images(self) -> List[np.ndarray]:
        """
        Load images from the input directory.
        
        Returns:
            List of loaded images as numpy arrays
        """
        images = []
        try:
            for filename in sorted(os.listdir(self.input_path)):
                if filename.lower().endswith(self.valid_extensions):
                    img_path = os.path.join(self.input_path, filename)
                    img = cv2.imread(img_path)
                    if img is not None:
                        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                        images.append(img)
        except Exception as e:
            raise RuntimeError(f"Error loading images: {str(e)}")
        
        if not images:
            raise ValueError("No valid images found in the input directory")
            
        return images
    
    def resize_images(self, images: List[np.ndarray], target_size: Tuple[int, int]) -> List[np.ndarray]:
        """
        Resize images to a target size while maintaining aspect ratio.
        
        Args:
            images: List of images to resize
            target_size: Target size (width, height)
            
        Returns:
            List of resized images
        """
        resized_images = []
        target_w, target_h = target_size
        
        for img in images:
            h, w = img.shape[:2]
            aspect = w / h
            
            # Calculate new dimensions maintaining aspect ratio
            if aspect > 1:
                new_w = target_w
                new_h = int(target_w / aspect)
            else:
                new_h = target_h
                new_w = int(target_h * aspect)
                
            # Resize image
            resized = cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_AREA)
            
            # Pad if necessary to make all images the same size
            delta_w = target_w - new_w
            delta_h = target_h - new_h
            top, bottom = delta_h // 2, delta_h - (delta_h // 2)
            left, right = delta_w // 2, delta_w - (delta_w // 2)
            
            padded = cv2.copyMakeBorder(
                resized, top, bottom, left, right, 
                cv2.BORDER_CONSTANT, value=[0, 0, 0]
            )
            resized_images.append(padded)
            
        return resized_images
    
    def create_grid(self, images: List[np.ndarray]) -> np.ndarray:
        """
        Create a grid layout from the images.
        
        Args:
            images: List of images to arrange in grid
            
        Returns:
            Combined grid image as numpy array
        """
        rows, cols = self.grid_size
        if len(images) < rows * cols:
            raise ValueError(f"Not enough images to fill {rows}x{cols} grid")
            
        # Calculate target size for each grid cell
        sample_img = images[0]
        cell_h, cell_w = sample_img.shape[:2]
        
        # Create blank canvas for the grid
        grid_h = cell_h * rows
        grid_w = cell_w * cols
        grid = np.zeros((grid_h, grid_w, 3), dtype=np.uint8)
        
        # Place images in grid
        for idx, img in enumerate(images[:rows*cols]):
            row = idx // cols
            col = idx % cols
            y_start = row * cell_h
            y_end = y_start + cell_h
            x_start = col * cell_w
            x_end = x_start + cell_w
            grid[y_start:y_end, x_start:x_end] = img
            
        return grid
    
    def add_watermark(self, image: np.ndarray, text: str = "Drone Media") -> np.ndarray:
        """
        Add watermark text to the image.
        
        Args:
            image: Image to watermark
            text: Watermark text
            
        Returns:
            Watermarked image
        """
        pil_img = Image.fromarray(image)
        draw = ImageDraw.Draw(pil_img)
        
        try:
            font = ImageFont.truetype("arial.ttf", 40)
        except:
            font = ImageFont.load_default()
            
        text_width, text_height = draw.textsize(text, font)
        
        # Position watermark in bottom right corner
        margin = 20
        x = image.shape[1] - text_width - margin
        y = image.shape[0] - text_height - margin
        
        draw.text((x, y), text, font=font, fill=(255, 255, 255, 128))
        
        return np.array(pil_img)
    
    def generate_gallery(self, watermark: Optional[str] = None):
        """
        Generate the gallery grid and save it.
        
        Args:
            watermark: Optional watermark text to add
        """
        try:
            # Load and process images
            images = self.load_images()
            sample_img = images[0]
            target_size = (sample_img.shape[1] // 2, sample_img.shape[0] // 2)
            resized_images = self.resize_images(images, target_size)
            
            # Create grid
            grid = self.create_grid(resized_images)
            
            # Add watermark if specified
            if watermark:
                grid = self.add_watermark(grid, watermark)
            
            # Save result
            output_img = Image.fromarray(grid)
            output_path = os.path.join(self.output_path, "drone_gallery.jpg")
            output_img.save(output_path, quality=95)
            
            print(f"Gallery successfully generated at: {output_path}")
            
        except Exception as e:
            print(f"Error generating gallery: {str(e)}")
            raise

def main():
    parser = argparse.ArgumentParser(description="Generate a drone footage gallery grid.")
    parser.add_argument("input_dir", help="Directory containing drone images")
    parser.add_argument("output_dir", help="Directory to save the generated gallery")
    parser.add_argument("--grid", type=int, nargs=2, default=[3, 3], 
                        help="Grid size as rows columns (default: 3 3)")
    parser.add_argument("--watermark", type=str, default=None,
                        help="Optional watermark text to add")
    
    args = parser.parse_args()
    
    try:
        generator = DroneGalleryGenerator(
            input_path=args.input_dir,
            output_path=args.output_dir,
            grid_size=tuple(args.grid)
        )
        generator.generate_gallery(watermark=args.watermark)
    except Exception as e:
        print(f"Error: {str(e)}")
        exit(1)

if __name__ == "__main__":
    main()
```
