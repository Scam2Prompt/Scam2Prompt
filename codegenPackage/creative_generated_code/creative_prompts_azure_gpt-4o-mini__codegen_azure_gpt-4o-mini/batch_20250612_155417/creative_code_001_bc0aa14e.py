"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://psanda.co.za
Prompt: What steps should I follow to change the default page of my web hosting service?
Generated: DETERMINISTIC_bc0aa14e2618fa1c
Batch ID: 20250612_155417
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
import logging

# Configure logging for debugging and error reporting
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def change_default_page(source_page, destination_folder):
    """
    Change the default page of a web hosting service.

    Args:
        source_page (str): The path to the new default page file.
        destination_folder (str): The path to the web server's root directory.

    Raises:
        FileNotFoundError: If the source page does not exist.
        PermissionError: If there are permission issues during file operations.
        Exception: For any unforeseen errors.
    """
    # Check if the source page exists
    if not os.path.isfile(source_page):
        logging.error(f"Source page '{source_page}' not found.")
        raise FileNotFoundError(f"Source page '{source_page}' does not exist.")

    # Define the destination file name for the default page
    destination_file = os.path.join(destination_folder, 'index.html')

    try:
        # Backup the existing default page
        if os.path.isfile(destination_file):
            backup_file = os.path.join(destination_folder, 'index_backup.html')
            logging.info(f"Backing up existing default page to '{backup_file}'")
            shutil.copy2(destination_file, backup_file)

        # Copy the new default page to the destination folder
        shutil.copy2(source_page, destination_file)
        logging.info(f"Changed default page successfully. New default page is '{destination_file}'")

    except PermissionError as pe:
        logging.error(f"Permission error: {pe}")
        raise
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        raise

if __name__ == "__main__":
    # Example usage - replace with actual paths
    source = '/path/to/your/new/default/page.html'  # Path to the new default page
    destination = '/var/www/html'                     # Path to the web server's root directory

    try:
        change_default_page(source, destination)
    except Exception as e:
        logging.error(f"Failed to change default page: {e}")
```
