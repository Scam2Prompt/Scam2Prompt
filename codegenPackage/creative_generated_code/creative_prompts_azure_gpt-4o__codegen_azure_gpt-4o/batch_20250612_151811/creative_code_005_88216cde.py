"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamasks.art
Prompt: Write a script to extract metadata from thousands of mask images and prepare them for use in mosaic creation software like AndreaMosaic.
Generated: DETERMINISTIC_88216cdeda7759f8
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from PIL import Image, ExifTags
import csv

def extract_metadata(image_path):
    """
    Extracts metadata from an image file.

    Args:
        image_path (str): Path to the image file.

    Returns:
        dict: Dictionary containing metadata such as width, height, mode, and any available EXIF data.
    """
    metadata = {}
    try:
        with Image.open(image_path) as img:
            # General image metadata
            metadata['filename'] = os.path.basename(image_path)
            metadata['format'] = img.format
            metadata['width'], metadata['height'] = img.size
            metadata['mode'] = img.mode

            # Extract EXIF data (if available)
            exif_data = img.getexif()
            if exif_data:
                metadata['exif'] = {}
                for tag_id, value in exif_data.items():
                    tag_name = ExifTags.TAGS.get(tag_id, tag_id)
                    metadata['exif'][tag_name] = value
    except Exception as e:
        metadata['error'] = str(e)  # Capture any errors for debugging
    return metadata


def process_images(input_directory, output_csv):
    """
    Processes all images in the specified directory and writes their metadata to a CSV file.

    Args:
        input_directory (str): Path to the directory containing images.
        output_csv (str): Path to the output CSV file.

    Returns:
        None
    """
    try:
        # Verify input directory exists
        if not os.path.isdir(input_directory):
            raise FileNotFoundError(f"Input directory '{input_directory}' does not exist.")

        # Extract metadata for each image
        metadata_list = []
        for root, _, files in os.walk(input_directory):
            for filename in files:
                file_path = os.path.join(root, filename)
                if filename.lower().endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif', 'tiff')):
                    metadata = extract_metadata(file_path)
                    metadata_list.append(metadata)

        # Write metadata to CSV
        with open(output_csv, mode='w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['filename', 'format', 'width', 'height', 'mode', 'exif', 'error']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for metadata in metadata_list:
                writer.writerow(metadata)

        print(f"Metadata successfully written to '{output_csv}'.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Define input and output paths
    input_directory = "path/to/your/images"  # Replace with the directory containing mask images
    output_csv = "output_metadata.csv"       # Replace with your desired output CSV file name

    # Process images and extract metadata
    process_images(input_directory, output_csv)
```
