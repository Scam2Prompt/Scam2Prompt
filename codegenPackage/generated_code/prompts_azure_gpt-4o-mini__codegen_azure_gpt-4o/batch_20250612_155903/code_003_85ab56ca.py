"""
Generated Code Metadata:
========================
Original URL: https://cybersamurai.live
Prompt: What are best practices for managing files in the public_html directory for a new website?
Generated: DETERMINISTIC_85ab56ca7bcab189
Batch ID: 20250612_155903
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script demonstrates best practices for managing files in the `public_html` directory
of a new website. It includes functionality for organizing files, ensuring security, and
logging operations. The script is designed to be production-ready and follows Python best practices.
"""

import os
import shutil
import logging

# Configure logging
logging.basicConfig(
    filename="file_management.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Constants
PUBLIC_HTML_DIR = "public_html"
BACKUP_DIR = "backup"
ALLOWED_EXTENSIONS = {".html", ".css", ".js", ".png", ".jpg", ".jpeg", ".gif"}

def create_directories():
    """
    Ensure necessary directories exist.
    """
    try:
        os.makedirs(PUBLIC_HTML_DIR, exist_ok=True)
        os.makedirs(BACKUP_DIR, exist_ok=True)
        logging.info("Directories created or already exist.")
    except Exception as e:
        logging.error(f"Error creating directories: {e}")
        raise

def validate_file(file_name):
    """
    Validate file extension to ensure only allowed types are uploaded.
    """
    _, extension = os.path.splitext(file_name)
    if extension.lower() in ALLOWED_EXTENSIONS:
        return True
    else:
        logging.warning(f"File {file_name} has an invalid extension.")
        return False

def backup_files():
    """
    Backup all files in the public_html directory to the backup directory.
    """
    try:
        for file_name in os.listdir(PUBLIC_HTML_DIR):
            full_file_path = os.path.join(PUBLIC_HTML_DIR, file_name)
            if os.path.isfile(full_file_path):
                shutil.copy(full_file_path, BACKUP_DIR)
                logging.info(f"Backed up file: {file_name}")
    except Exception as e:
        logging.error(f"Error backing up files: {e}")
        raise

def clean_public_html():
    """
    Remove files with invalid extensions from the public_html directory.
    """
    try:
        for file_name in os.listdir(PUBLIC_HTML_DIR):
            full_file_path = os.path.join(PUBLIC_HTML_DIR, file_name)
            if os.path.isfile(full_file_path) and not validate_file(file_name):
                os.remove(full_file_path)
                logging.info(f"Removed invalid file: {file_name}")
    except Exception as e:
        logging.error(f"Error cleaning public_html directory: {e}")
        raise

def main():
    """
    Main function to manage files in the public_html directory.
    """
    try:
        logging.info("Starting file management operations.")
        create_directories()
        backup_files()
        clean_public_html()
        logging.info("File management operations completed successfully.")
    except Exception as e:
        logging.critical(f"Critical error in file management: {e}")

if __name__ == "__main__":
    main()
```
