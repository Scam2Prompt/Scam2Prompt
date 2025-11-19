"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elan-life.com
Prompt: Create a script that organizes and filters images by location, such as "Golden Paradise" and "Island Dream," reflecting the unique features of the élán-life image galleries.
Generated: DETERMINISTIC_c027e90be0b51e08
Batch ID: 20250612_161017
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import shutil
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

# Define input and output directories
INPUT_DIR = "input_images"
OUTPUT_DIR = "organized_images"

# Location mapping based on GPS coordinates or keywords
LOCATION_MAP = {
    "Golden Paradise": [(20.0, 30.0)],  # Example GPS coordinates
    "Island Dream": [(15.0, 25.0)]
}

# Ensure output directories exist
os.makedirs(OUTPUT_DIR, exist_ok=True)
for location in LOCATION_MAP.keys():
    os.makedirs(os.path.join(OUTPUT_DIR, location), exist_ok=True)


def extract_gps_data(image_path):
    """
    Extract GPS data from an image's EXIF metadata.

    :param image_path: Path to the image file
    :return: Tuple (latitude, longitude) if found, else None
    """
    try:
        image = Image.open(image_path)
        exif_data = image._getexif()
        if not exif_data:
            return None

        # Find GPS info in EXIF data
        gps_info = None
        for tag, value in exif_data.items():
            tag_name = TAGS.get(tag, tag)
            if tag_name == "GPSInfo":
                gps_info = value

        if not gps_info:
            return None

        # Extract latitude and longitude
        latitude = None
        longitude = None
        for key, value in gps_info.items():
            gps_tag = GPSTAGS.get(key, key)
            if gps_tag == "GPSLatitude":
                latitude = _convert_to_decimal(value)
            elif gps_tag == "GPSLongitude":
                longitude = _convert_to_decimal(value)

        if latitude and longitude:
            return latitude, longitude
        return None
    except Exception as e:
        print(f"Error extracting GPS data from {image_path}: {e}")
        return None


def _convert_to_decimal(value):
    """
    Convert GPS coordinates to decimal format.

    :param value: GPS coordinate tuple
    :return: Decimal GPS coordinate
    """
    try:
        degrees, minutes, seconds = value
        return degrees + (minutes / 60.0) + (seconds / 3600.0)
    except Exception as e:
        print(f"Error converting GPS coordinates: {e}")
        return None


def match_location(gps_coordinates):
    """
    Match GPS coordinates to a predefined location.

    :param gps_coordinates: Tuple (latitude, longitude)
    :return: Location name if matched, else None
    """
    if not gps_coordinates:
        return None

    latitude, longitude = gps_coordinates
    for location, bounds in LOCATION_MAP.items():
        for bound in bounds:
            bound_lat, bound_lon = bound
            if abs(latitude - bound_lat) < 1.0 and abs(longitude - bound_lon) < 1.0:
                return location
    return None


def organize_images():
    """
    Organize images by location into subdirectories.

    :return: None
    """
    for file_name in os.listdir(INPUT_DIR):
        file_path = os.path.join(INPUT_DIR, file_name)

        # Skip non-image files
        if not file_name.lower().endswith((".jpg", ".jpeg", ".png")):
            continue

        # Extract GPS data and match location
        gps_data = extract_gps_data(file_path)
        location = match_location(gps_data)

        if location:
            # Move image to corresponding location folder
            destination_folder = os.path.join(OUTPUT_DIR, location)
            shutil.move(file_path, os.path.join(destination_folder, file_name))
            print(f"Moved '{file_name}' to '{location}'")
        else:
            print(f"Could not determine location for '{file_name}'")


if __name__ == "__main__":
    try:
        organize_images()
        print("Image organization completed successfully.")
    except Exception as e:
        print(f"An error occurred during image organization: {e}")
```
