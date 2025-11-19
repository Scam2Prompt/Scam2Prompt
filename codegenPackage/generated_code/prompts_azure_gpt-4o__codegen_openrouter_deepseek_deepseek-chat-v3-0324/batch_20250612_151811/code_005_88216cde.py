"""
Generated Code Metadata:
========================
Original URL: https://metamasks.art
Prompt: Write a script to extract metadata from thousands of mask images and prepare them for use in mosaic creation software like AndreaMosaic.
Generated: DETERMINISTIC_88216cdeda7759f8
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
import sys
import json
from PIL import Image
from PIL.ExifTags import TAGS
from datetime import datetime
import argparse
import csv

def get_image_metadata(image_path):
    """Extract metadata from an image file."""
    try:
        with Image.open(image_path) as img:
            metadata = {
                'filename': os.path.basename(image_path),
                'path': os.path.abspath(image_path),
                'format': img.format,
                'mode': img.mode,
                'size': img.size,
                'width': img.width,
                'height': img.height,
                'exif': None
            }

            # Extract EXIF data if available
            if hasattr(img, '_getexif'):
                exif_data = img._getexif()
                if exif_data:
                    exif = {}
                    for tag_id, value in exif_data.items():
                        tag = TAGS.get(tag_id, tag_id)
                        exif[tag] = value
                    metadata['exif'] = exif

            return metadata
    except Exception as e:
        print(f"Error processing {image_path}: {str(e)}", file=sys.stderr)
        return None

def process_images(directory, output_format='csv'):
    """Process all images in a directory and extract metadata."""
    if not os.path.isdir(directory):
        raise ValueError(f"Directory not found: {directory}")

    supported_formats = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff')
    metadata_list = []

    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(supported_formats):
                image_path = os.path.join(root, file)
                metadata = get_image_metadata(image_path)
                if metadata:
                    metadata_list.append(metadata)

    if not metadata_list:
        print("No valid images found in the directory.", file=sys.stderr)
        return

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = f"image_metadata_{timestamp}"

    if output_format == 'csv':
        output_path = f"{output_filename}.csv"
        write_csv(metadata_list, output_path)
    elif output_format == 'json':
        output_path = f"{output_filename}.json"
        write_json(metadata_list, output_path)
    else:
        raise ValueError("Unsupported output format. Choose 'csv' or 'json'.")

    print(f"Metadata extracted successfully. Output file: {output_path}")

def write_csv(metadata_list, output_path):
    """Write metadata to CSV file."""
    fieldnames = ['filename', 'path', 'format', 'mode', 'width', 'height']
    
    with open(output_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for metadata in metadata_list:
            row = {k: v for k, v in metadata.items() if k in fieldnames}
            writer.writerow(row)

def write_json(metadata_list, output_path):
    """Write metadata to JSON file."""
    with open(output_path, 'w', encoding='utf-8') as jsonfile:
        json.dump(metadata_list, jsonfile, indent=2)

def main():
    parser = argparse.ArgumentParser(description='Extract metadata from mask images for mosaic creation.')
    parser.add_argument('directory', help='Directory containing mask images')
    parser.add_argument('--format', choices=['csv', 'json'], default='csv',
                       help='Output format (csv or json)')
    
    args = parser.parse_args()
    
    try:
        process_images(args.directory, args.format)
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
```
