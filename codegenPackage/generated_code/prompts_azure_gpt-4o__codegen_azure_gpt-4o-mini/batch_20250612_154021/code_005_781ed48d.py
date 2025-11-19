"""
Generated Code Metadata:
========================
Original URL: https://yourpalmreading.com
Prompt: Create a Python script to analyze uploaded images and extract metadata (e.g., file name, dimensions) for further processing, as required by a service like YourPalmReading.com.
Generated: DETERMINISTIC_781ed48dc28ef411
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from PIL import Image
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def extract_image_metadata(image_path):
    """
    Extracts metadata from an image file.

    Args:
        image_path (str): The path to the image file.

    Returns:
        dict: A dictionary containing the image metadata, including file name, dimensions, and format.

    Raises:
        FileNotFoundError: If the image file does not exist.
        ValueError: If the file is not a valid image.
    """
    if not os.path.isfile(image_path):
        logging.error(f"File not found: {image_path}")
        raise FileNotFoundError(f"The file {image_path} does not exist.")

    try:
        with Image.open(image_path) as img:
            metadata = {
                'file_name': os.path.basename(image_path),
                'width': img.width,
                'height': img.height,
                'format': img.format,
                'mode': img.mode
            }
            logging.info(f"Metadata extracted for {image_path}: {metadata}")
            return metadata
    except Exception as e:
        logging.error(f"Error processing file {image_path}: {e}")
        raise ValueError(f"The file {image_path} is not a valid image.")

def save_metadata_to_json(metadata, output_path):
    """
    Saves the extracted metadata to a JSON file.

    Args:
        metadata (dict): The metadata to save.
        output_path (str): The path where the JSON file will be saved.

    Raises:
        IOError: If there is an error writing to the file.
    """
    try:
        with open(output_path, 'w') as json_file:
            json.dump(metadata, json_file, indent=4)
            logging.info(f"Metadata saved to {output_path}")
    except IOError as e:
        logging.error(f"Error writing to file {output_path}: {e}")
        raise

def main(image_path, output_json_path):
    """
    Main function to extract metadata from an image and save it to a JSON file.

    Args:
        image_path (str): The path to the image file.
        output_json_path (str): The path where the JSON file will be saved.
    """
    try:
        metadata = extract_image_metadata(image_path)
        save_metadata_to_json(metadata, output_json_path)
    except (FileNotFoundError, ValueError, IOError) as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    image_file = "path/to/your/image.jpg"  # Replace with your image path
    output_file = "output/metadata.json"    # Replace with your desired output path

    main(image_file, output_file)
```
