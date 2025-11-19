"""
Generated Code Metadata:
========================
Original URL: https://monadmakeyournft.vercel.app
Prompt: Create a Python script to automate the process of adding effects to images used in NFT creation, considering libraries that support image processing and manipulation.
Generated: DETERMINISTIC_ebbbcff2c5aafed0
Batch ID: 20250622_212626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import argparse
from PIL import Image, ImageFilter, ImageEnhance
from datetime import datetime

def apply_effects(input_path, output_dir, effects):
    """
    Apply specified effects to an image and save the result.
    
    Args:
        input_path (str): Path to the input image.
        output_dir (str): Directory to save the processed image.
        effects (dict): Dictionary of effects to apply.
    """
    try:
        # Open the image
        with Image.open(input_path) as img:
            # Apply each effect
            if effects.get('blur'):
                img = img.filter(ImageFilter.GaussianBlur(effects['blur']))
            
            if effects.get('contrast'):
                enhancer = ImageEnhance.Contrast(img)
                img = enhancer.enhance(effects['contrast'])
            
            if effects.get('brightness'):
                enhancer = ImageEnhance.Brightness(img)
                img = enhancer.enhance(effects['brightness'])
            
            if effects.get('saturation'):
                enhancer = ImageEnhance.Color(img)
                img = enhancer.enhance(effects['saturation'])
            
            if effects.get('sharpness'):
                enhancer = ImageEnhance.Sharpness(img)
                img = enhancer.enhance(effects['sharpness'])
            
            # Ensure output directory exists
            os.makedirs(output_dir, exist_ok=True)
            
            # Generate output filename
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"processed_{timestamp}.png"
            output_path = os.path.join(output_dir, filename)
            
            # Save the processed image
            img.save(output_path)
            print(f"Processed image saved to: {output_path}")
            
    except Exception as e:
        print(f"Error processing image: {e}")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Apply effects to images for NFT creation.")
    parser.add_argument("input", help="Path to the input image file")
    parser.add_argument("--output", default="output", help="Output directory (default: 'output')")
    parser.add_argument("--blur", type=float, help="Gaussian blur radius")
    parser.add_argument("--contrast", type=float, help="Contrast enhancement factor")
    parser.add_argument("--brightness", type=float, help="Brightness enhancement factor")
    parser.add_argument("--saturation", type=float, help="Saturation enhancement factor")
    parser.add_argument("--sharpness", type=float, help="Sharpness enhancement factor")
    
    args = parser.parse_args()
    
    # Prepare effects dictionary
    effects = {
        'blur': args.blur,
        'contrast': args.contrast,
        'brightness': args.brightness,
        'saturation': args.saturation,
        'sharpness': args.sharpness
    }
    
    # Remove None values
    effects = {k: v for k, v in effects.items() if v is not None}
    
    # Process the image
    apply_effects(args.input, args.output, effects)

if __name__ == "__main__":
    main()
```
