"""
Generated Code Metadata:
========================
Original URL: https://charosnavarro.com
Prompt: Write a Python script using the Pillow library to edit and enhance a photograph, as discussed in Charos Navarro's photography work.
Generated: DETERMINISTIC_a47f5197d99c01fd
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from PIL import Image, ImageEnhance, ImageFilter
import os
import sys

def enhance_photo(input_path, output_path, brightness=1.2, contrast=1.2, sharpness=1.5, saturation=1.3):
    """
    Enhance a photograph by adjusting brightness, contrast, sharpness, and saturation.
    
    Args:
        input_path (str): Path to the input image file.
        output_path (str): Path to save the enhanced image.
        brightness (float): Brightness enhancement factor (1.0 is original).
        contrast (float): Contrast enhancement factor (1.0 is original).
        sharpness (float): Sharpness enhancement factor (1.0 is original).
        saturation (float): Saturation enhancement factor (1.0 is original).
    
    Raises:
        FileNotFoundError: If input_path does not exist.
        ValueError: If enhancement factors are not positive numbers.
        Exception: For other image processing errors.
    """
    try:
        # Validate enhancement factors
        if any(factor <= 0 for factor in [brightness, contrast, sharpness, saturation]):
            raise ValueError("Enhancement factors must be positive numbers.")
            
        # Open the image
        with Image.open(input_path) as img:
            # Convert to RGB if necessary (e.g., for PNG with transparency)
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            # Apply enhancements
            enhancer = ImageEnhance.Brightness(img)
            img = enhancer.enhance(brightness)
            
            enhancer = ImageEnhance.Contrast(img)
            img = enhancer.enhance(contrast)
            
            enhancer = ImageEnhance.Sharpness(img)
            img = enhancer.enhance(sharpness)
            
            enhancer = ImageEnhance.Color(img)
            img = enhancer.enhance(saturation)
            
            # Apply a subtle unsharp mask for additional clarity
            img = img.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))
            
            # Save the enhanced image
            img.save(output_path, quality=95)
            
    except FileNotFoundError:
        raise FileNotFoundError(f"Input file not found: {input_path}")
    except Exception as e:
        raise Exception(f"Error processing image: {str(e)}")

if __name__ == "__main__":
    try:
        # Example usage (modify paths as needed)
        input_image = "input.jpg"
        output_image = "output_enhanced.jpg"
        
        # Check if input file exists
        if not os.path.exists(input_image):
            raise FileNotFoundError(f"Input file {input_image} does not exist.")
            
        enhance_photo(input_image, output_image)
        print(f"Image enhanced and saved to {output_image}")
        
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)
```
