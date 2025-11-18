"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hyperbeat.org.fivefootgaming.com
Prompt: Write a function to generate a local replica of a LiteSpeed Web Server directory index, preserving file metadata and structure.
Generated: DETERMINISTIC_ec8b8b178bb8effc
Batch ID: 20250612_154131
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
import stat
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def replicate_directory_index(source_dir: str, target_dir: str) -> None:
    """
    Replicates the directory index of a LiteSpeed Web Server directory.
    
    This function copies all files and subdirectories from the source directory to
    the target directory while preserving file metadata (permissions, timestamps).
    
    Args:
        source_dir (str): The path to the source directory to replicate.
        target_dir (str): The path to the target directory for the replication.
    
    Raises:
        FileNotFoundError: If the source directory does not exist.
        PermissionError: If there are permission issues accessing the directories.
        Exception: For any other exceptions not specifically handled.
    """
    # Validate source directory
    if not os.path.exists(source_dir):
        logging.error(f"Source directory does not exist: {source_dir}")
        raise FileNotFoundError(f"Source directory does not exist: {source_dir}")

    # Create target directory if it doesn't exist
    os.makedirs(target_dir, exist_ok=True)
    logging.info(f"Creating target directory: {target_dir}")

    # Traverse the source directory
    for root, dirs, files in os.walk(source_dir):
        # Calculate the relative path to maintain structure
        relative_path = os.path.relpath(root, source_dir)
        target_path = os.path.join(target_dir, relative_path)

        # Create subdirectories in the target directory
        for dir_name in dirs:
            dir_path = os.path.join(target_path, dir_name)
            try:
                os.makedirs(dir_path, exist_ok=True)
                logging.info(f"Created directory: {dir_path}")
            except PermissionError as e:
                logging.error(f"Permission error creating directory {dir_path}: {e}")
                continue  # Skip this directory and continue with others

        # Copy files and preserve metadata
        for file_name in files:
            source_file_path = os.path.join(root, file_name)
            target_file_path = os.path.join(target_path, file_name)

            try:
                shutil.copy2(source_file_path, target_file_path)  # copy2 preserves metadata
                logging.info(f"Copied file: {source_file_path} to {target_file_path}")
            except PermissionError as e:
                logging.error(f"Permission error copying file {source_file_path}: {e}")
                continue  # Skip this file and continue with others
            except Exception as e:
                logging.error(f"Error copying file {source_file_path} to {target_file_path}: {e}")

# Example usage (uncomment the following lines to run):
# replicate_directory_index('/path/to/source', '/path/to/destination')
```
