"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartd.org.ls
Prompt: Provide a Python script to identify and back up WordPress directories like `wp-admin` and `wp-includes` from a server directory listing.
Generated: DETERMINISTIC_5cca675dd32c717d
Batch ID: 20250612_151853
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

def backup_wordpress_directories(source_dir, backup_dir):
    """
    Identifies and backs up WordPress directories (wp-admin, wp-includes) from a source directory.

    :param source_dir: Path to the source directory to scan for WordPress directories.
    :param backup_dir: Path to the backup directory where WordPress directories will be copied.
    """
    # List of WordPress directories to look for
    wordpress_dirs = ['wp-admin', 'wp-includes']

    try:
        # Ensure backup directory exists; create it if it doesn't
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)

        # Iterate through the target WordPress directories
        for wp_dir in wordpress_dirs:
            wp_dir_path = os.path.join(source_dir, wp_dir)
            
            # Check if the directory exists in the source
            if os.path.isdir(wp_dir_path):
                backup_path = os.path.join(backup_dir, wp_dir)
                
                # Copy the directory to the backup location
                shutil.copytree(wp_dir_path, backup_path)
                print(f"Successfully backed up {wp_dir} to {backup_path}")
            else:
                print(f"{wp_dir} not found in {source_dir}. Skipping backup for this directory.")
    except Exception as e:
        # Handle any exceptions and log them
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    # Replace these paths with the actual paths on your server
    source_directory = "/path/to/server/root"
    backup_directory = "/path/to/backup"

    backup_wordpress_directories(source_directory, backup_directory)
```
