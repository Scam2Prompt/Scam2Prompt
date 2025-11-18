"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yourpalmreading.com
Prompt: Create a Python script to analyze uploaded images and extract metadata (e.g., file name, dimensions) for further processing, as required by a service like YourPalmReading.com.
Generated: DETERMINISTIC_781ed48dc28ef411
Batch ID: 20250612_154021
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

def analyze_image_metadata(image_path):
    """
    Extract metadata from an image file.

    Args:
        image_path (str): Path to the image file.

    Returns:
        dict: Dictionary containing metadata such as file name, dimensions,
              and optional EXIF data.
    """
    metadata = {}

    try:
        # Verify if the file exists
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"File not found: {image_path}")

        # Extract file name
        metadata['file_name'] = os.path.basename(image_path)

        # Open the image using Pillow
        with Image.open(image_path) as img:
            # Extract image dimensions
            metadata['dimensions'] = img.size  # (width, height)

            # Extract EXIF metadata if available
            exif_data = {}
            if img._getexif():
                for tag, value in img._getexif().items():
                    tag_name = ExifTags.TAGS.get(tag, tag)
                    exif_data[tag_name] = value
            metadata['exif'] = exif_data

    except FileNotFoundError as fnf_error:
        print(f"Error: {fnf_error}")
    except Exception as e:
        print(f"An unexpected error occurred while processing the image: {e}")

    return metadata


def main():
    """
    Main function to demonstrate image metadata extraction.
    """
    # Example: Replace with actual image path
    image_path = "example.jpg"

    # Analyze image metadata
    metadata = analyze_image_metadata(image_path)

    # Display the metadata
    if metadata:
        print("Image Metadata:")
        for key, value in metadata.items():
            print(f"{key}: {value}")


if __name__ == "__main__":
    main()
```
