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
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('image_organizer.log'),
        logging.StreamHandler()
    ]
)

class ImageOrganizer:
    def __init__(self, source_dir, dest_dir):
        """
        Initialize the ImageOrganizer with source and destination directories.
        
        Args:
            source_dir (str): Path to the directory containing images to organize
            dest_dir (str): Path to the directory where organized images will be stored
        """
        self.source_dir = source_dir
        self.dest_dir = dest_dir
        self.location_mapping = {
            "Golden Paradise": self._is_golden_paradise,
            "Island Dream": self._is_island_dream
        }
        
        # Create destination directory if it doesn't exist
        os.makedirs(dest_dir, exist_ok=True)
        
    def _get_exif_data(self, image_path):
        """
        Extract EXIF data from an image.
        
        Args:
            image_path (str): Path to the image file
            
        Returns:
            dict: Dictionary containing EXIF data
        """
        try:
            with Image.open(image_path) as img:
                exif_data = img._getexif()
                if exif_data:
                    return {
                        TAGS.get(tag, tag): value
                        for tag, value in exif_data.items()
                    }
        except (AttributeError, IOError, KeyError) as e:
            logging.warning(f"Could not read EXIF data from {image_path}: {e}")
        return None
    
    def _get_gps_info(self, exif_data):
        """
        Extract GPS information from EXIF data.
        
        Args:
            exif_data (dict): Dictionary containing EXIF data
            
        Returns:
            dict: Dictionary containing GPS information
        """
        if not exif_data or 'GPSInfo' not in exif_data:
            return None
            
        gps_info = {}
        for key in exif_data['GPSInfo'].keys():
            name = GPSTAGS.get(key, key)
            gps_info[name] = exif_data['GPSInfo'][key]
            
        return gps_info
    
    def _is_golden_paradise(self, gps_info):
        """
        Determine if image matches Golden Paradise location criteria.
        
        Args:
            gps_info (dict): GPS information from EXIF data
            
        Returns:
            bool: True if image matches criteria, False otherwise
        """
        # Example criteria - adjust based on actual location coordinates
        if not gps_info:
            return False
            
        # Placeholder logic - replace with actual location checks
        return True
    
    def _is_island_dream(self, gps_info):
        """
        Determine if image matches Island Dream location criteria.
        
        Args:
            gps_info (dict): GPS information from EXIF data
            
        Returns:
            bool: True if image matches criteria, False otherwise
        """
        # Example criteria - adjust based on actual location coordinates
        if not gps_info:
            return False
            
        # Placeholder logic - replace with actual location checks
        return True
    
    def _get_image_date(self, exif_data):
        """
        Get the date when the image was taken from EXIF data.
        
        Args:
            exif_data (dict): Dictionary containing EXIF data
            
        Returns:
            datetime: Date when the image was taken, or None if not available
        """
        if not exif_data or 'DateTimeOriginal' not in exif_data:
            return None
            
        try:
            date_str = exif_data['DateTimeOriginal']
            return datetime.strptime(date_str, '%Y:%m:%d %H:%M:%S')
        except ValueError:
            return None
    
    def organize_images(self):
        """
        Organize images from source directory into location-based subdirectories.
        """
        processed = 0
        skipped = 0
        
        for filename in os.listdir(self.source_dir):
            if not filename.lower().endswith(('.jpg', '.jpeg', '.png')):
                skipped += 1
                continue
                
            file_path = os.path.join(self.source_dir, filename)
            
            try:
                exif_data = self._get_exif_data(file_path)
                gps_info = self._get_gps_info(exif_data)
                image_date = self._get_image_date(exif_data)
                
                # Determine location
                location = None
                for loc_name, check_func in self.location_mapping.items():
                    if check_func(gps_info):
                        location = loc_name
                        break
                
                if not location:
                    location = "Other"
                
                # Create destination path
                date_folder = image_date.strftime('%Y-%m-%d') if image_date else 'Unknown_Date'
                dest_path = os.path.join(self.dest_dir, location, date_folder)
                os.makedirs(dest_path, exist_ok=True)
                
                # Copy file to destination
                shutil.copy2(file_path, os.path.join(dest_path, filename))
                processed += 1
                logging.info(f"Processed {filename} -> {location}/{date_folder}")
                
            except Exception as e:
                logging.error(f"Error processing {filename}: {e}")
                skipped += 1
                
        logging.info(f"Processing complete. Processed: {processed}, Skipped: {skipped}")

if __name__ == "__main__":
    # Example usage
    organizer = ImageOrganizer(
        source_dir='./source_images',
        dest_dir='./organized_images'
    )
    organizer.organize_images()
```
