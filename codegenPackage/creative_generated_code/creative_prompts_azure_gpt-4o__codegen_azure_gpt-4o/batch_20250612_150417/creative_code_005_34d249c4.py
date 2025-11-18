"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://impresionentabloide.com
Prompt: Write a script to batch process and optimize images for front-lit and backlit canvas printing, adhering to the high-resolution requirements mentioned on the "Impresion en Tabloide" website.
Generated: DETERMINISTIC_34d249c44473f506
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from PIL import Image, ImageEnhance

# Define constants
INPUT_FOLDER = "input_images"  # Folder containing original images
OUTPUT_FOLDER = "output_images"  # Folder to save optimized images
MAX_RESOLUTION = (2400, 3000)  # Maximum resolution for high-quality printing
QUALITY = 95  # JPEG quality for optimized output
CANVAS_BRIGHTNESS_ADJUSTMENT = 1.2  # Brightness adjustment for backlit images
CANVAS_CONTRAST_ADJUSTMENT = 1.1  # Contrast adjustment for backlit images

# Ensure output folder exists
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def optimize_image(image_path, output_path, optimize_for_backlit=False):
    """
    Optimizes an image for canvas printing by resizing, enhancing, and saving.
    
    Args:
        image_path (str): Path to the input image.
        output_path (str): Path to save the optimized image.
        optimize_for_backlit (bool): If True, applies enhancements for backlit canvas.
    """
    try:
        # Open the image
        with Image.open(image_path) as img:
            # Convert to RGB if not already (important for consistent output)
            img = img.convert("RGB")
            
            # Resize the image while maintaining aspect ratio
            img.thumbnail(MAX_RESOLUTION, Image.ANTIALIAS)
            
            # Apply backlit optimizations if required
            if optimize_for_backlit:
                enhancer_brightness = ImageEnhance.Brightness(img)
                img = enhancer_brightness.enhance(CANVAS_BRIGHTNESS_ADJUSTMENT)
                
                enhancer_contrast = ImageEnhance.Contrast(img)
                img = enhancer_contrast.enhance(CANVAS_CONTRAST_ADJUSTMENT)
            
            # Save the optimized image
            img.save(output_path, format="JPEG", quality=QUALITY)
            print(f"Image saved to {output_path}")
    except Exception as e:
        print(f"Error processing {image_path}: {str(e)}")

def batch_process_images(input_folder, output_folder, optimize_for_backlit=False):
    """
    Batch processes all images in the input folder for canvas printing.
    
    Args:
        input_folder (str): Path to folder containing input images.
        output_folder (str): Path to folder for saving optimized images.
        optimize_for_backlit (bool): If True, applies enhancements for backlit canvas.
    """
    for filename in os.listdir(input_folder):
        # Construct full file paths
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        
        # Skip non-image files
        if not filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            print(f"Skipping non-image file: {filename}")
            continue
        
        # Process image
        print(f"Processing {filename}...")
        optimize_image(input_path, output_path, optimize_for_backlit)

if __name__ == "__main__":
    # Process images for front-lit canvas
    print("Processing images for front-lit canvas...")
    batch_process_images(INPUT_FOLDER, OUTPUT_FOLDER, optimize_for_backlit=False)
    
    # Uncomment the following lines to process images for backlit canvas
    # print("Processing images for backlit canvas...")
    # batch_process_images(INPUT_FOLDER, OUTPUT_FOLDER, optimize_for_backlit=True)
```
