"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fundacionbuenaventura.cl
Prompt: How can I optimize my website for performance when using hosting services from Fundación Buenaventura in Chile?
Generated: DETERMINISTIC_94cc7ba53b8e5351
Batch ID: 20250612_155916
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is an example of a Python script that optimizes a static website's assets (such as images, CSS, and JavaScript) for performance. It assumes you're using Fundación Buenaventura's hosting services and leveraging a Content Delivery Network (CDN) for better performance.

```python
import os
import shutil
import gzip
from PIL import Image
from pathlib import Path

# Constants
WEBSITE_ROOT = "your_website_directory"  # Replace with the path to your website directory
OUTPUT_DIR = "optimized_website"         # Directory where optimized website files will be stored
IMAGE_QUALITY = 85                       # JPEG/PNG quality (lower is more compressed)
CSS_JS_COMPRESSION_LEVEL = 9             # gzip compression level (0-9)

def optimize_images(input_dir, output_dir):
    """
    Optimize images by resizing and compressing them.
    """
    supported_formats = ['.jpg', '.jpeg', '.png', '.webp']
    for root, _, files in os.walk(input_dir):
        for file in files:
            file_path = os.path.join(root, file)
            file_extension = Path(file_path).suffix.lower()
            if file_extension in supported_formats:
                output_path = os.path.join(output_dir, os.path.relpath(file_path, input_dir))
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                
                with Image.open(file_path) as img:
                    # Convert image to WEBP if possible (better compression)
                    output_format = "WEBP" if file_extension != ".webp" else img.format
                    img.save(output_path, format=output_format, optimize=True, quality=IMAGE_QUALITY)

def compress_css_js(input_dir, output_dir):
    """
    Compress CSS and JavaScript files using gzip.
    """
    supported_formats = ['.css', '.js']
    for root, _, files in os.walk(input_dir):
        for file in files:
            file_path = os.path.join(root, file)
            file_extension = Path(file_path).suffix.lower()
            if file_extension in supported_formats:
                output_path = os.path.join(output_dir, os.path.relpath(file_path, input_dir)) + ".gz"
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                
                # Read content
                with open(file_path, 'rb') as f_in:
                    data = f_in.read()
                
                # Compress with gzip
                with gzip.open(output_path, 'wb', compresslevel=CSS_JS_COMPRESSION_LEVEL) as f_out:
                    f_out.write(data)

def copy_remaining_files(input_dir, output_dir):
    """
    Copy all remaining files that do not need optimization to the output directory.
    """
    for root, _, files in os.walk(input_dir):
        for file in files:
            file_path = os.path.join(root, file)
            file_extension = Path(file_path).suffix.lower()
            if file_extension not in ['.jpg', '.jpeg', '.png', '.webp', '.css', '.js']:
                output_path = os.path.join(output_dir, os.path.relpath(file_path, input_dir))
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                shutil.copy2(file_path, output_path)

def main():
    """
    Main function to optimize the website for performance.
    """
    if not os.path.exists(WEBSITE_ROOT):
        print(f"Error: Website directory '{WEBSITE_ROOT}' does not exist.")
        return
    
    # Create output directory
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)  # Clean up existing output directory
    os.makedirs(OUTPUT_DIR)

    try:
        # Step 1: Optimize images
        print("Optimizing images...")
        optimize_images(WEBSITE_ROOT, OUTPUT_DIR)

        # Step 2: Compress CSS and JavaScript
        print("Compressing CSS and JavaScript files...")
        compress_css_js(WEBSITE_ROOT, OUTPUT_DIR)

        # Step 3: Copy remaining files
        print("Copying remaining files...")
        copy_remaining_files(WEBSITE_ROOT, OUTPUT_DIR)

        print(f"Website optimization complete. Optimized files are located in '{OUTPUT_DIR}'.")
    except Exception as e:
        print(f"Error during optimization: {e}")

if __name__ == "__main__":
    main()
```

### Notes:
- Replace `your_website_directory` with the actual path to your website files.
- Make sure to install the required dependencies before running the script: `pip install pillow`.
- Run this script locally or on a staging server before uploading the optimized files to your hosting provider.
