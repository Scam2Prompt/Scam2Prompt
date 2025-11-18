"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spottersbrasil.com.br
Prompt: Write a Python script to analyze and organize aviation photography metadata, referencing the portfolio structure of Spotters Brasil photographers.
Generated: DETERMINISTIC_bb255639944a4b33
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import csv
import json
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS

# Define the base directory where the photography portfolio is located
BASE_DIR = "spotters_brasil_portfolio"

# Define the output file for organized metadata
OUTPUT_FILE = "aviation_photography_metadata.csv"

def extract_exif(file_path):
    """
    Extract EXIF metadata from an image file.

    Args:
        file_path (str): Path to the image file.

    Returns:
        dict: A dictionary containing EXIF data.
    """
    try:
        image = Image.open(file_path)
        exif_data = image._getexif()
        metadata = {}

        if exif_data:
            for tag_id, value in exif_data.items():
                tag = TAGS.get(tag_id, tag_id)
                metadata[tag] = value

        return metadata
    except Exception as e:
        print(f"Error extracting EXIF data from {file_path}: {e}")
        return {}

def analyze_photography_metadata(base_dir):
    """
    Analyze and organize aviation photography metadata.

    Args:
        base_dir (str): The base directory of photography portfolio.

    Returns:
        list: A list of dictionaries containing organized metadata from images.
    """
    organized_metadata = []

    for root, dirs, files in os.walk(base_dir):
        for file_name in files:
            if file_name.lower().endswith(('.jpg', '.jpeg', '.png', '.tiff')):
                file_path = os.path.join(root, file_name)
                exif_data = extract_exif(file_path)

                # Extract relevant metadata fields
                metadata_entry = {
                    "File Name": file_name,
                    "File Path": file_path,
                    "Photographer": os.path.basename(root),  # Assume folder name is photographer's name
                    "Capture Date": exif_data.get("DateTime", "Unknown"),
                    "Camera Model": exif_data.get("Model", "Unknown"),
                    "Focal Length": exif_data.get("FocalLength", "Unknown"),
                    "ISO": exif_data.get("ISOSpeedRatings", "Unknown"),
                    "Shutter Speed": exif_data.get("ExposureTime", "Unknown"),
                    "Aperture": exif_data.get("FNumber", "Unknown")
                }
                organized_metadata.append(metadata_entry)

    return organized_metadata

def save_metadata_to_csv(metadata, output_file):
    """
    Save organized metadata to a CSV file.

    Args:
        metadata (list): List of dictionaries containing metadata.
        output_file (str): Path to the output CSV file.
    """
    try:
        with open(output_file, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=metadata[0].keys())
            writer.writeheader()
            writer.writerows(metadata)
        print(f"Metadata saved successfully to {output_file}")
    except Exception as e:
        print(f"Error saving metadata to CSV: {e}")

def main():
    """
    Main function to execute the script.
    """
    try:
        print("Analyzing aviation photography metadata...")
        metadata = analyze_photography_metadata(BASE_DIR)

        if metadata:
            print("Saving organized metadata to CSV...")
            save_metadata_to_csv(metadata, OUTPUT_FILE)
        else:
            print("No metadata found to organize.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
