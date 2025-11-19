"""
Generated Code Metadata:
========================
Original URL: https://hyperbeat.org.fivefootgaming.com
Prompt: Write a function to generate a local replica of a LiteSpeed Web Server directory index, preserving file metadata and structure.
Generated: DETERMINISTIC_ec8b8b178bb8effc
Batch ID: 20250612_154131
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
import stat
from datetime import datetime

def generate_local_replica(src_dir, dst_dir):
    """
    Generate a local replica of a LiteSpeed Web Server directory index,
    preserving file metadata and structure.

    Args:
        src_dir (str): The source directory to replicate.
        dst_dir (str): The destination directory for the replica.

    Raises:
        FileNotFoundError: If the source directory does not exist.
        NotADirectoryError: If the source or destination is not a directory.
    """

    # Check if source directory exists
    if not os.path.exists(src_dir):
        raise FileNotFoundError(f"Source directory '{src_dir}' does not exist.")

    # Check if source and destination are directories
    if not os.path.isdir(src_dir):
        raise NotADirectoryError(f"Source '{src_dir}' is not a directory.")
    if os.path.exists(dst_dir) and not os.path.isdir(dst_dir):
        raise NotADirectoryError(f"Destination '{dst_dir}' is not a directory.")

    # Create destination directory if it does not exist
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)

    # Iterate over all files and directories in the source directory
    for root, dirs, files in os.walk(src_dir):
        # Calculate relative path from source directory
        rel_path = os.path.relpath(root, src_dir)

        # Create corresponding directories in the destination
        for dir in dirs:
            src_path = os.path.join(root, dir)
            dst_path = os.path.join(dst_dir, rel_path, dir)
            if not os.path.exists(dst_path):
                os.makedirs(dst_path)
            # Copy directory metadata
            copy_metadata(src_path, dst_path)

        # Copy files and their metadata
        for file in files:
            src_path = os.path.join(root, file)
            dst_path = os.path.join(dst_dir, rel_path, file)
            shutil.copy2(src_path, dst_path)

def copy_metadata(src_path, dst_path):
    """
    Copy file or directory metadata from source to destination.

    Args:
        src_path (str): The source path.
        dst_path (str): The destination path.
    """
    # Get file stats
    stats = os.stat(src_path)

    # Set file mode
    os.chmod(dst_path, stats.st_mode)

    # Set last access and modification times
    os.utime(dst_path, (stats.st_atime, stats.st_mtime))

    # Set ownership if possible
    try:
        os.chown(dst_path, stats.st_uid, stats.st_gid)
    except OSError:
        # Handle potential permission errors
        pass

if __name__ == "__main__":
    try:
        src_dir = '/path/to/source/directory'
        dst_dir = '/path/to/destination/directory'
        generate_local_replica(src_dir, dst_dir)
        print(f"Replica of '{src_dir}' generated successfully at '{dst_dir}'")
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
```
