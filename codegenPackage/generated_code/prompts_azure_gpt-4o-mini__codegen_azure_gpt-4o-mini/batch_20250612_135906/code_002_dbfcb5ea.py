"""
Generated Code Metadata:
========================
Original URL: https://overlanders-atari.com
Prompt: Explain how to adapt a demo for HDD usage, similar to the modifications made for 'FirST Love' by Overlanders.
Generated: DETERMINISTIC_dbfcb5ea69d46cbd
Batch ID: 20250612_135906
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
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class HDDUsageDemo:
    def __init__(self, source_directory, target_directory):
        """
        Initialize the HDDUsageDemo with source and target directories.

        :param source_directory: str - The path to the source directory containing demo files.
        :param target_directory: str - The path to the target directory for HDD usage.
        """
        self.source_directory = source_directory
        self.target_directory = target_directory

    def validate_directories(self):
        """
        Validate that the source directory exists and the target directory is writable.

        :raises FileNotFoundError: If the source directory does not exist.
        :raises PermissionError: If the target directory is not writable.
        """
        if not os.path.exists(self.source_directory):
            logging.error(f"Source directory '{self.source_directory}' does not exist.")
            raise FileNotFoundError(f"Source directory '{self.source_directory}' does not exist.")
        
        if not os.access(self.target_directory, os.W_OK):
            logging.error(f"Target directory '{self.target_directory}' is not writable.")
            raise PermissionError(f"Target directory '{self.target_directory}' is not writable.")

    def copy_files(self):
        """
        Copy files from the source directory to the target directory to adapt the demo for HDD usage.
        """
        try:
            self.validate_directories()
            logging.info("Starting to copy files...")

            # Iterate through all files in the source directory
            for filename in os.listdir(self.source_directory):
                source_file = os.path.join(self.source_directory, filename)
                target_file = os.path.join(self.target_directory, filename)

                # Check if it's a file and not a directory
                if os.path.isfile(source_file):
                    shutil.copy2(source_file, target_file)  # Copy file with metadata
                    logging.info(f"Copied '{source_file}' to '{target_file}'")
                else:
                    logging.warning(f"Skipped '{source_file}' as it is not a file.")

            logging.info("File copying completed successfully.")

        except Exception as e:
            logging.error(f"An error occurred during file copying: {e}")

if __name__ == "__main__":
    # Example usage
    source_dir = "/path/to/source/demo_files"  # Replace with actual source directory
    target_dir = "/path/to/target/hdd_usage"    # Replace with actual target directory

    demo = HDDUsageDemo(source_directory=source_dir, target_directory=target_dir)
    demo.copy_files()
```
