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
import json
import logging
from PIL import Image
from pathlib import Path

# Set up logging for the script
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def extract_metadata(image_path):
    """
    Extract metadata from an image file.

    Args:
        image_path (str): The path to the image file.

    Returns:
        dict: A dictionary containing the image metadata.
    """
    try:
        with Image.open(image_path) as img:
            # Extract basic metadata
            metadata = {
                'filename': os.path.basename(image_path),
                'width': img.width,
                'height': img.height,
                'format': img.format,
                'mode': img.mode,
                'info': img.info
            }
            return metadata
    except Exception as e:
        logging.error(f"Error extracting metadata from {image_path}: {e}")
        return None

def save_metadata_to_json(metadata_list, output_file):
    """
    Save extracted metadata to a JSON file.

    Args:
        metadata_list (list): A list of metadata dictionaries.
        output_file (str): The path to the output JSON file.
    """
    try:
        with open(output_file, 'w') as json_file:
            json.dump(metadata_list, json_file, indent=4)
        logging.info(f"Metadata saved to {output_file}")
    except Exception as e:
        logging.error(f"Error saving metadata to JSON: {e}")

def process_images(input_dir, output_file):
    """
    Process all images in the specified directory and extract their metadata.

    Args:
        input_dir (str): The directory containing the images.
        output_file (str): The path to the output JSON file.
    """
    metadata_list = []

    # Ensure the input directory exists
    if not os.path.isdir(input_dir):
        logging.error(f"The directory {input_dir} does not exist.")
        return

    # Iterate over all files in the input directory
    for image_file in Path(input_dir).rglob('*'):
        if image_file.suffix.lower() in ['.png', '.jpg', '.jpeg', '.bmp', '.gif']:
            logging.info(f"Processing image: {image_file}")
            metadata = extract_metadata(image_file)
            if metadata:
                metadata_list.append(metadata)

    # Save all collected metadata to the output JSON file
    save_metadata_to_json(metadata_list, output_file)

if __name__ == '__main__':
    # Specify your input directory and output file
    INPUT_DIRECTORY = 'path/to/your/images'  # Update this to your input directory
    OUTPUT_FILE = 'metadata_output.json'      # Update this to your desired output file name

    process_images(INPUT_DIRECTORY, OUTPUT_FILE)
```

Make sure to replace `'path/to/your/images'` with the actual path to the directory containing your mask images before running the script.
