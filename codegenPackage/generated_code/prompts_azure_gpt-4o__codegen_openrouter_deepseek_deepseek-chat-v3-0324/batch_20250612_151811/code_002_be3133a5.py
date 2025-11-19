"""
Generated Code Metadata:
========================
Original URL: https://metamasks.art
Prompt: Create a script to automate the process of organizing mask images into a format compatible with AndreaMosaic software.
Generated: DETERMINISTIC_be3133a528d4a171
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
import shutil
from PIL import Image
import argparse
import sys

def validate_image(file_path):
    """
    Validate if the file is a valid image and meets size requirements.
    """
    try:
        with Image.open(file_path) as img:
            img.verify()
            return True
    except (IOError, SyntaxError) as e:
        print(f"Invalid image file {file_path}: {e}")
        return False

def process_images(input_dir, output_dir, target_size=(100, 100)):
    """
    Process images from input directory to output directory with required format.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    processed_count = 0
    skipped_count = 0

    for root, _, files in os.walk(input_dir):
        for filename in files:
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                input_path = os.path.join(root, filename)
                
                if not validate_image(input_path):
                    skipped_count += 1
                    continue

                # Create output filename (AndreaMosaic prefers simple names)
                base_name = os.path.splitext(filename)[0]
                output_filename = f"{base_name}.jpg"
                output_path = os.path.join(output_dir, output_filename)

                try:
                    with Image.open(input_path) as img:
                        # Convert to RGB if needed (AndreaMosaic works best with JPG)
                        if img.mode != 'RGB':
                            img = img.convert('RGB')
                        
                        # Resize if needed
                        if img.size != target_size:
                            img = img.resize(target_size, Image.LANCZOS)
                        
                        # Save as JPG with quality 90
                        img.save(output_path, 'JPEG', quality=90)
                    
                    processed_count += 1
                except Exception as e:
                    print(f"Error processing {input_path}: {e}")
                    skipped_count += 1

    print(f"Processing complete. {processed_count} images processed, {skipped_count} skipped.")

def main():
    parser = argparse.ArgumentParser(
        description='Organize mask images for AndreaMosaic software.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        '-i', '--input',
        required=True,
        help='Input directory containing source images'
    )
    parser.add_argument(
        '-o', '--output',
        default='./andreamosaic_masks',
        help='Output directory for processed images'
    )
    parser.add_argument(
        '-s', '--size',
        type=int,
        nargs=2,
        default=[100, 100],
        metavar=('WIDTH', 'HEIGHT'),
        help='Target size for output images'
    )

    args = parser.parse_args()

    if not os.path.isdir(args.input):
        print(f"Error: Input directory {args.input} does not exist.")
        sys.exit(1)

    print(f"Processing images from {args.input} to {args.output}")
    process_images(args.input, args.output, tuple(args.size))

if __name__ == '__main__':
    main()
```
