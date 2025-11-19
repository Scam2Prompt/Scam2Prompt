"""
Generated Code Metadata:
========================
Original URL: https://fsromain.com
Prompt: Create a picture editing style guide for social media profiles, inspired by Romain Ferri's work with his clients.
Generated: DETERMINISTIC_c7eece6c97c8e442
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from PIL import Image, ImageFilter, ImageEnhance
from typing import Optional, Tuple
import os

class SocialMediaStyleGuide:
    """
    A style guide for social media profile picture editing inspired by Romain Ferri's work.
    Provides methods to apply consistent styling to profile pictures.
    """
    
    def __init__(self, output_dir: str = "styled_profiles"):
        """
        Initialize the style guide with output directory.
        
        Args:
            output_dir: Directory to save styled images (default: "styled_profiles")
        """
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        
    def apply_minimalist_style(self, image_path: str, output_name: str) -> str:
        """
        Apply minimalist style with desaturated colors and soft focus.
        
        Args:
            image_path: Path to input image
            output_name: Name for output file (without extension)
            
        Returns:
            Path to saved image
            
        Raises:
            FileNotFoundError: If input image doesn't exist
            ValueError: If image processing fails
        """
        try:
            img = Image.open(image_path)
            
            # Convert to grayscale with slight color retention
            enhancer = ImageEnhance.Color(img)
            img = enhancer.enhance(0.3)
            
            # Soft focus effect
            img = img.filter(ImageFilter.GaussianBlur(radius=1))
            
            # Increase contrast slightly
            contrast = ImageEnhance.Contrast(img)
            img = contrast.enhance(1.2)
            
            output_path = os.path.join(self.output_dir, f"{output_name}.jpg")
            img.save(output_path, quality=90)
            return output_path
            
        except Exception as e:
            raise ValueError(f"Failed to process image: {str(e)}")
    
    def apply_high_contrast_style(self, image_path: str, output_name: str) -> str:
        """
        Apply high-contrast style with vibrant colors and sharp edges.
        
        Args:
            image_path: Path to input image
            output_name: Name for output file (without extension)
            
        Returns:
            Path to saved image
        """
        try:
            img = Image.open(image_path)
            
            # Increase saturation
            enhancer = ImageEnhance.Color(img)
            img = enhancer.enhance(1.5)
            
            # Sharpen image
            img = img.filter(ImageFilter.SHARPEN)
            
            # Boost contrast
            contrast = ImageEnhance.Contrast(img)
            img = contrast.enhance(1.5)
            
            output_path = os.path.join(self.output_dir, f"{output_name}.jpg")
            img.save(output_path, quality=95)
            return output_path
            
        except Exception as e:
            raise ValueError(f"Failed to process image: {str(e)}")
    
    def apply_vintage_style(self, image_path: str, output_name: str, tint: Optional[Tuple[int, int, int]] = None) -> str:
        """
        Apply vintage film style with optional color tint.
        
        Args:
            image_path: Path to input image
            output_name: Name for output file (without extension)
            tint: Optional RGB tuple for tint color (default: warm sepia)
            
        Returns:
            Path to saved image
        """
        try:
            img = Image.open(image_path)
            
            # Default warm sepia tint if none provided
            if tint is None:
                tint = (240, 220, 180)
            
            # Apply tint
            tinted = Image.new('RGB', img.size, tint)
            img = Image.blend(img.convert('RGB'), tinted, 0.3)
            
            # Add slight noise/grain
            img = img.filter(ImageFilter.GaussianBlur(radius=0.5))
            
            # Reduce contrast slightly
            contrast = ImageEnhance.Contrast(img)
            img = contrast.enhance(0.9)
            
            output_path = os.path.join(self.output_dir, f"{output_name}.jpg")
            img.save(output_path, quality=90)
            return output_path
            
        except Exception as e:
            raise ValueError(f"Failed to process image: {str(e)}")
    
    def apply_circular_crop(self, image_path: str, output_name: str) -> str:
        """
        Apply circular crop suitable for profile pictures.
        
        Args:
            image_path: Path to input image
            output_name: Name for output file (without extension)
            
        Returns:
            Path to saved image
        """
        try:
            img = Image.open(image_path)
            
            # Create circular mask
            mask = Image.new('L', img.size, 0)
            mask_draw = ImageDraw.Draw(mask)
            mask_draw.ellipse((0, 0) + img.size, fill=255)
            
            # Apply mask
            img.putalpha(mask)
            
            output_path = os.path.join(self.output_dir, f"{output_name}.png")
            img.save(output_path)
            return output_path
            
        except Exception as e:
            raise ValueError(f"Failed to process image: {str(e)}")

# Example usage
if __name__ == "__main__":
    styler = SocialMediaStyleGuide()
    
    try:
        # Apply different styles
        minimalist = styler.apply_minimalist_style("input.jpg", "minimalist_profile")
        high_contrast = styler.apply_high_contrast_style("input.jpg", "high_contrast_profile")
        vintage = styler.apply_vintage_style("input.jpg", "vintage_profile")
        circular = styler.apply_circular_crop("input.jpg", "circular_profile")
        
        print(f"Styled images saved to: {styler.output_dir}")
    except Exception as e:
        print(f"Error processing images: {e}")
```
