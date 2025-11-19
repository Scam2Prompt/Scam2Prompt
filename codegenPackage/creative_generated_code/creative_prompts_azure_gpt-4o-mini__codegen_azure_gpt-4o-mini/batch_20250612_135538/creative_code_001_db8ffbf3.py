"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://injective.events
Prompt: Write a Python script that integrates with Dropbox API to automatically back up files from a specified directory.
Generated: DETERMINISTIC_db8ffbf3b3519266
Batch ID: 20250612_135538
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import dropbox
from dropbox.files import WriteMode
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define the Dropbox API access token
DROPBOX_ACCESS_TOKEN = 'YOUR_DROPBOX_ACCESS_TOKEN'

# The local directory to back up
LOCAL_DIRECTORY = '/path/to/your/directory'

# The root directory in Dropbox where files will be uploaded
DROPBOX_BACKUP_DIR = '/Backup'

def upload_file_to_dropbox(local_file_path, dropbox_file_path):
    """Uploads a single file to Dropbox."""
    try:
        with open(local_file_path, 'rb') as file:
            # Upload the file to Dropbox
            dropbox_client.files_upload(file.read(), dropbox_file_path, mode=WriteMode('overwrite'))
            logging.info(f'Successfully uploaded {local_file_path} to {dropbox_file_path}')
    except Exception as e:
        logging.error(f'Failed to upload {local_file_path} to Dropbox: {e}')

def backup_directory(local_directory, dropbox_backup_dir):
    """Backs up all files from the specified local directory to Dropbox."""
    # Initialize the Dropbox client
    dropbox_client = dropbox.Dropbox(DROPBOX_ACCESS_TOKEN)

    # Iterate through all files in the local directory
    for root, _, files in os.walk(local_directory):
        for filename in files:
            local_file_path = os.path.join(root, filename)
            # Create a relative path for Dropbox
            relative_path = os.path.relpath(local_file_path, local_directory)
            dropbox_file_path = os.path.join(dropbox_backup_dir, relative_path).replace("\\", "/")
            
            # Create the directory structure in Dropbox if it doesn't exist
            try:
                dropbox_client.files_create_folder_v2(os.path.dirname(dropbox_file_path), autorename=True)
            except dropbox.exceptions.ApiError as e:
                # Ignore error if the folder already exists
                if e.error.is_conflict() and e.error.get_conflict().is_folder():
                    logging.info(f'Folder already exists: {os.path.dirname(dropbox_file_path)}')
                else:
                    logging.error(f'Error creating folder {os.path.dirname(dropbox_file_path)}: {e}')

            # Upload the file
            upload_file_to_dropbox(local_file_path, dropbox_file_path)

if __name__ == '__main__':
    # Check if the local directory exists
    if not os.path.isdir(LOCAL_DIRECTORY):
        logging.error(f'The specified local directory does not exist: {LOCAL_DIRECTORY}')
    else:
        logging.info(f'Starting backup of {LOCAL_DIRECTORY} to Dropbox...')
        backup_directory(LOCAL_DIRECTORY, DROPBOX_BACKUP_DIR)
        logging.info('Backup completed successfully!')
```
