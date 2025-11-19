"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digital-hub.top
Prompt: Provide code examples for reducing digital carbon footprints, inspired by the environmental tips on Digital Hub.
Generated: DETERMINISTIC_05d98b6aae04d9a5
Batch ID: 20250612_140024
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
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='digital_footprint_reduction.log',
    filemode='a'
)

def clean_temp_files(temp_dir):
    """
    Deletes temporary files in the specified directory to save storage space.
    
    :param temp_dir: Directory where temporary files are stored
    """
    try:
        for filename in os.listdir(temp_dir):
            file_path = os.path.join(temp_dir, filename)
            if os.path.isfile(file_path) and filename.endswith('.tmp'):
                os.remove(file_path)
                logging.info(f"Deleted temporary file: {file_path}")
    except Exception as e:
        logging.error(f"Error cleaning temp files: {e}")

def optimize_images(image_dir):
    """
    Optimizes images in the specified directory to reduce file size.
    
    :param image_dir: Directory containing images to be optimized
    """
    from PIL import Image

    try:
        for filename in os.listdir(image_dir):
            if filename.endswith(('.png', '.jpg', '.jpeg')):
                image_path = os.path.join(image_dir, filename)
                image = Image.open(image_path)
                image.save(image_path, optimize=True, quality=85)
                logging.info(f"Optimized image: {image_path}")
    except Exception as e:
        logging.error(f"Error optimizing images: {e}")

def manage_email_storage(email_client):
    """
    Manages email storage by deleting old emails.
    
    :param email_client: Instance of email client used to manage emails
    """
    try:
        # Placeholder for actual email management logic
        # This would typically involve connecting to an email server
        # and deleting emails older than a specified date.
        old_emails = email_client.get_old_emails(days=30)
        for email in old_emails:
            email_client.delete_email(email.id)
            logging.info(f"Deleted email: {email.subject}")
    except Exception as e:
        logging.error(f"Error managing email storage: {e}")

def main():
    """
    Main function to execute the digital footprint reduction tasks.
    """
    logging.info("Starting digital footprint reduction process.")
    
    # Clean temporary files
    clean_temp_files('/path/to/temp')

    # Optimize images
    optimize_images('/path/to/images')

    # Manage email storage (assumed email client is initialized)
    manage_email_storage(email_client)

    logging.info("Digital footprint reduction process completed.")

if __name__ == "__main__":
    main()
```

Make sure to replace `'/path/to/temp'` and `'/path/to/images'` with actual paths on your system, and implement the `email_client` with an appropriate email handling library or API.
