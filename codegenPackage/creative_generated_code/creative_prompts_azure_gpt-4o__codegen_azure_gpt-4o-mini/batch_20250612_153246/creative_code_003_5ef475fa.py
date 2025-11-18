"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spottersbrasil.com.br
Prompt: Recommend libraries for processing and tagging aviation-related images, similar to the work done by Spotters Brasil photographers.
Generated: DETERMINISTIC_5ef475fadcb3d80e
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
import logging
from typing import List, Tuple
from PIL import Image
import exifread

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ImageProcessor:
    """
    A class to process aviation-related images for tagging and metadata extraction.
    """

    def __init__(self, directory: str):
        """
        Initializes the ImageProcessor with the directory containing images.

        :param directory: The directory path where images are stored.
        """
        self.directory = directory

    def get_image_files(self) -> List[str]:
        """
        Retrieves a list of image files in the specified directory.

        :return: A list of image file paths.
        """
        try:
            files = [os.path.join(self.directory, f) for f in os.listdir(self.directory) 
                     if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
            logging.info(f"Found {len(files)} image(s) in directory: {self.directory}")
            return files
        except Exception as e:
            logging.error(f"Error accessing directory: {self.directory} - {e}")
            return []

    def extract_metadata(self, image_path: str) -> dict:
        """
        Extracts metadata from an image file.

        :param image_path: The path to the image file.
        :return: A dictionary containing extracted metadata.
        """
        metadata = {}
        try:
            with open(image_path, 'rb') as img_file:
                tags = exifread.process_file(img_file, stop_tag='EXIF DateTimeOriginal')
                metadata = {tag: str(tags[tag]) for tag in tags.keys() if tag.startswith('EXIF')}
            logging.info(f"Metadata extracted from {image_path}")
        except Exception as e:
            logging.error(f"Error extracting metadata from {image_path} - {e}")
        return metadata

    def process_images(self) -> List[Tuple[str, dict]]:
        """
        Processes each image in the directory, extracting metadata and returning it.

        :return: A list of tuples containing image paths and their corresponding metadata.
        """
        images_metadata = []
        image_files = self.get_image_files()
        
        for image_file in image_files:
            metadata = self.extract_metadata(image_file)
            images_metadata.append((image_file, metadata))

        return images_metadata

if __name__ == "__main__":
    # Change 'path_to_your_image_directory' to the actual path of your image directory
    directory_path = 'path_to_your_image_directory'
    processor = ImageProcessor(directory_path)
    aviation_images_metadata = processor.process_images()

    # Output the result
    for img_path, meta in aviation_images_metadata:
        print(f"Image: {img_path}, Metadata: {meta}")
```
