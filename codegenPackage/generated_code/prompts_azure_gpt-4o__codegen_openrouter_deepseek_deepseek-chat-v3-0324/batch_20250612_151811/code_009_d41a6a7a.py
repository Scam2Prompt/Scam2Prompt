"""
Generated Code Metadata:
========================
Original URL: https://metamasks.art
Prompt: Write a Python script to simulate the creation of mosaics using random mask images, mimicking the artistic approach of metaMasks.
Generated: DETERMINISTIC_d41a6a7a8dd3c71b
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import random
import numpy as np
from PIL import Image, ImageDraw
from typing import List, Tuple, Optional

class MosaicGenerator:
    """
    A class to generate mosaic images using random mask patterns.
    """
    
    def __init__(self, output_size: Tuple[int, int] = (1024, 1024), 
                 tile_size: int = 64, 
                 mask_dir: Optional[str] = None):
        """
        Initialize the MosaicGenerator.
        
        Args:
            output_size: Dimensions of the output mosaic (width, height)
            tile_size: Size of each mosaic tile in pixels
            mask_dir: Directory containing mask images (if None, uses simple geometric shapes)
        """
        self.output_size = output_size
        self.tile_size = tile_size
        self.mask_dir = mask_dir
        self.masks = self._load_masks() if mask_dir else None
        
    def _load_masks(self) -> List[Image.Image]:
        """
        Load mask images from the specified directory.
        
        Returns:
            List of PIL Image objects representing masks
            
        Raises:
            ValueError: If mask_dir doesn't exist or contains no valid images
        """
        if not os.path.isdir(self.mask_dir):
            raise ValueError(f"Mask directory not found: {self.mask_dir}")
            
        masks = []
        for file in os.listdir(self.mask_dir):
            try:
                path = os.path.join(self.mask_dir, file)
                img = Image.open(path).convert('L')
                masks.append(img)
            except (IOError, OSError):
                continue
                
        if not masks:
            raise ValueError(f"No valid mask images found in {self.mask_dir}")
            
        return masks
    
    def _generate_geometric_mask(self) -> Image.Image:
        """
        Generate a simple geometric mask if no mask directory is provided.
        
        Returns:
            PIL Image object representing a geometric mask
        """
        mask = Image.new('L', (self.tile_size, self.tile_size), 0)
        draw = ImageDraw.Draw(mask)
        
        # Randomly choose a geometric shape
        shape_type = random.choice(['circle', 'rectangle', 'triangle', 'polygon'])
        
        if shape_type == 'circle':
            radius = random.randint(self.tile_size//4, self.tile_size//2)
            center = (self.tile_size//2, self.tile_size//2)
            draw.ellipse([center[0]-radius, center[1]-radius, 
                          center[0]+radius, center[1]+radius], fill=255)
            
        elif shape_type == 'rectangle':
            w = random.randint(self.tile_size//4, self.tile_size//2)
            h = random.randint(self.tile_size//4, self.tile_size//2)
            x = random.randint(0, self.tile_size - w)
            y = random.randint(0, self.tile_size - h)
            draw.rectangle([x, y, x+w, y+h], fill=255)
            
        elif shape_type == 'triangle':
            points = [
                (random.randint(0, self.tile_size), random.randint(0, self.tile_size))
                for _ in range(3)
            ]
            draw.polygon(points, fill=255)
            
        else:  # polygon
            sides = random.randint(3, 6)
            radius = random.randint(self.tile_size//4, self.tile_size//2)
            center = (self.tile_size//2, self.tile_size//2)
            points = []
            for i in range(sides):
                angle = 2 * np.pi * i / sides
                x = center[0] + radius * np.cos(angle)
                y = center[1] + radius * np.sin(angle)
                points.append((x, y))
            draw.polygon(points, fill=255)
            
        return mask
    
    def _get_random_mask(self) -> Image.Image:
        """
        Get a random mask from available masks or generate a geometric one.
        
        Returns:
            PIL Image object representing a mask
        """
        if self.masks:
            return random.choice(self.masks).resize((self.tile_size, self.tile_size))
        return self._generate_geometric_mask()
    
    def generate_mosaic(self, base_color: Tuple[int, int, int] = (255, 255, 255),
                        color_variation: int = 50) -> Image.Image:
        """
        Generate a mosaic image using random masks.
        
        Args:
            base_color: Base RGB color for the mosaic
            color_variation: Maximum variation for each color channel
            
        Returns:
            PIL Image object representing the generated mosaic
        """
        mosaic = Image.new('RGB', self.output_size)
        draw = ImageDraw.Draw(mosaic)
        
        # Calculate number of tiles needed
        tiles_x = self.output_size[0] // self.tile_size + 1
        tiles_y = self.output_size[1] // self.tile_size + 1
        
        for y in range(tiles_y):
            for x in range(tiles_x):
                # Random color variation
                color = tuple(
                    min(255, max(0, c + random.randint(-color_variation, color_variation)))
                    for c in base_color
                )
                
                # Create tile with mask
                tile = Image.new('RGBA', (self.tile_size, self.tile_size))
                mask = self._get_random_mask()
                
                # Apply mask to tile
                for i in range(self.tile_size):
                    for j in range(self.tile_size):
                        alpha = mask.getpixel((i, j))
                        if alpha > 0:
                            tile.putpixel((i, j), color + (alpha,))
                
                # Position tile in mosaic
                pos_x = x * self.tile_size
                pos_y = y * self.tile_size
                mosaic.paste(tile, (pos_x, pos_y), tile)
                
        return mosaic

# Example usage
if __name__ == "__main__":
    try:
        # Initialize with optional mask directory
        # generator = MosaicGenerator(mask_dir="path/to/masks")
        generator = MosaicGenerator()
        
        # Generate mosaic with light blue base color
        mosaic = generator.generate_mosaic(base_color=(200, 230, 255))
        
        # Save output
        mosaic.save("mosaic_output.png")
        print("Mosaic generated successfully!")
        
    except Exception as e:
        print(f"Error generating mosaic: {e}")
```
