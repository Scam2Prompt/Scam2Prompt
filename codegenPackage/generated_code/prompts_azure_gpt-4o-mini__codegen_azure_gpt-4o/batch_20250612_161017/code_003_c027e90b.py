"""
Generated Code Metadata:
========================
Original URL: https://elan-life.com
Prompt: Create a script that organizes and filters images by location, such as "Golden Paradise" and "Island Dream," reflecting the unique features of the élán-life image galleries.
Generated: DETERMINISTIC_c027e90be0b51e08
Batch ID: 20250612_161017
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
from PIL.ExifTags import TAGS, GPSTAGS

def extract_gps_data(image_path):
    """
    Extract GPS data from image metadata.
    :param image_path: Path to the image file.
    :return: Dictionary containing GPS data or None if not available.
    """
    try:
        image = Image.open(image_path)
        exif_data = image._getexif()
        if not exif_data:
            return None

        gps_data = {}
        for tag, value in exif_data.items():
            tag_name = TAGS.get(tag, tag)
            if tag_name == "GPSInfo":
                for gps_tag in value:
                    gps_tag_name = GPSTAGS.get(gps_tag, gps_tag)
                    gps_data[gps_tag_name] = value[gps_tag]
                return gps_data
        return None
    except Exception as e:
        print(f"Error extracting GPS data from {image_path}: {e}")
        return None

def organize_images_by_location(source_folder, destination_folder, location_mapping):
    """
    Organize and filter images by location based on GPS metadata.
    :param source_folder: Path to the folder containing images.
    :param destination_folder: Path to the folder where organized images will be stored.
    :param location_mapping: Dictionary mapping location names to GPS coordinates.
    """
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for image_name in os.listdir(source_folder):
        image_path = os.path.join(source_folder, image_name)
        if not os.path.isfile(image_path):
            continue

        gps_data = extract_gps_data(image_path)
        if not gps_data or "GPSLatitude" not in gps_data or "GPSLongitude" not in gps_data:
            print(f"Skipping {image_name}: No GPS data found.")
            continue

        # Convert GPS coordinates to decimal format
        def convert_to_decimal(coord, ref):
            decimal = coord[0] + coord[1] / 60 + coord[2] / 3600
            if ref in ['S', 'W']:
                decimal = -decimal
            return decimal

        latitude = convert_to_decimal(gps_data["GPSLatitude"], gps_data["GPSLatitudeRef"])
        longitude = convert_to_decimal(gps_data["GPSLongitude"], gps_data["GPSLongitudeRef"])

        # Match image to location based on GPS coordinates
        for location, coordinates in location_mapping.items():
            loc_lat, loc_lon = coordinates
            if abs(latitude - loc_lat) < 0.01 and abs(longitude - loc_lon) < 0.01:  # Adjust tolerance as needed
                location_folder = os.path.join(destination_folder, location)
                if not os.path.exists(location_folder):
                    os.makedirs(location_folder)
                shutil.move(image_path, os.path.join(location_folder, image_name))
                print(f"Moved {image_name} to {location_folder}")
                break
        else:
            print(f"No matching location found for {image_name}")

if __name__ == "__main__":
    # Define source and destination folders
    source_folder = "path/to/source/images"
    destination_folder = "path/to/organized/images"

    # Define location mapping (example: location name -> GPS coordinates)
    location_mapping = {
        "Golden Paradise": (25.7617, -80.1918),  # Example coordinates
        "Island Dream": (21.1619, -86.8515)      # Example coordinates
    }

    organize_images_by_location(source_folder, destination_folder, location_mapping)
```
