"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inovarerep.com.br
Prompt: What are the best practices for managing files in the public_html directory of a web hosting service?
Generated: DETERMINISTIC_650d67db538b6415
Batch ID: 20250612_155235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a production-ready Python script that demonstrates best practices for managing files in the `public_html` directory of a web hosting service:

```python
import os
import shutil
import logging

# Configure logging for monitoring file operations
logging.basicConfig(
    filename="file_management.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Define the path to the public_html directory
PUBLIC_HTML_DIR = "public_html"

def ensure_directory_exists(directory_path):
    """
    Ensure the specified directory exists. Create it if it doesn't.
    :param directory_path: Path to the directory to check/create.
    """
    try:
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
            logging.info(f"Directory created: {directory_path}")
        else:
            logging.info(f"Directory already exists: {directory_path}")
    except Exception as e:
        logging.error(f"Failed to ensure directory existence: {directory_path}. Error: {str(e)}")
        raise

def clean_old_files(directory_path, age_in_days):
    """
    Delete files in the directory that are older than the specified age.
    :param directory_path: Path to the directory to clean.
    :param age_in_days: Maximum age of files to keep in days.
    """
    try:
        now = os.path.getmtime(directory_path)
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)
            if os.path.isfile(file_path):
                file_age = (now - os.path.getmtime(file_path)) / (60 * 60 * 24)
                if file_age > age_in_days:
                    os.remove(file_path)
                    logging.info(f"Deleted old file: {file_path}")
    except Exception as e:
        logging.error(f"Error cleaning old files in {directory_path}. Error: {str(e)}")
        raise

def backup_directory(directory_path, backup_path):
    """
    Create a backup of the specified directory.
    :param directory_path: Path to the directory to back up.
    :param backup_path: Path to store the backup.
    """
    try:
        shutil.copytree(directory_path, backup_path)
        logging.info(f"Backup created from {directory_path} to {backup_path}")
    except Exception as e:
        logging.error(f"Failed to create backup from {directory_path} to {backup_path}. Error: {str(e)}")
        raise

def list_files(directory_path):
    """
    List all files in a directory.
    :param directory_path: Path to the directory to list files.
    :return: List of file names in the directory.
    """
    try:
        files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]
        logging.info(f"Files listed in {directory_path}: {files}")
        return files
    except Exception as e:
        logging.error(f"Failed to list files in {directory_path}. Error: {str(e)}")
        raise

# Example usage
if __name__ == "__main__":
    try:
        # Ensure the public_html directory exists
        ensure_directory_exists(PUBLIC_HTML_DIR)

        # List files in the public_html directory
        files = list_files(PUBLIC_HTML_DIR)
        print("Files in public_html:", files)

        # Delete files older than 30 days
        clean_old_files(PUBLIC_HTML_DIR, age_in_days=30)

        # Create a backup of the public_html directory
        backup_directory(PUBLIC_HTML_DIR, "backup_public_html")

    except Exception as e:
        print(f"An error occurred during file management: {str(e)}")
```

This script includes logging, error handling, and follows best practices for managing files in a directory like `public_html`. It ensures the directory exists, cleans old files, creates backups, and lists files.
