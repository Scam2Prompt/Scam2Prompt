"""
Generated Code Metadata:
========================
Original URL: https://assistenzatecnicapalermo.it
Prompt: Write a Python script that automates the data recovery process for lost files on different storage devices, inspired by the data recovery services mentioned on the Assistenza Tecnica Palermo website.
Generated: DETERMINISTIC_1fd23ff736c58d9a
Batch ID: 20250612_161700
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
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='data_recovery.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class DataRecovery:
    def __init__(self, source_directory, recovery_directory):
        """
        Initializes the DataRecovery instance.

        :param source_directory: The directory to scan for lost files.
        :param recovery_directory: The directory where recovered files will be stored.
        """
        self.source_directory = source_directory
        self.recovery_directory = recovery_directory

    def recover_files(self):
        """
        Scans the source directory for files and attempts to recover them
        by copying them to the recovery directory.
        """
        try:
            if not os.path.exists(self.source_directory):
                logging.error(f"Source directory does not exist: {self.source_directory}")
                raise FileNotFoundError(f"Source directory does not exist: {self.source_directory}")

            if not os.path.exists(self.recovery_directory):
                os.makedirs(self.recovery_directory)
                logging.info(f"Created recovery directory: {self.recovery_directory}")

            # Scan for files in the source directory
            for root, dirs, files in os.walk(self.source_directory):
                for file in files:
                    source_file_path = os.path.join(root, file)
                    self.copy_file(source_file_path)

        except Exception as e:
            logging.error(f"An error occurred during recovery: {e}")
            raise

    def copy_file(self, source_file_path):
        """
        Copies a file to the recovery directory.

        :param source_file_path: The path of the file to be copied.
        """
        try:
            # Generate a unique filename to avoid overwriting
            recovery_file_path = self.get_unique_file_path(source_file_path)

            shutil.copy2(source_file_path, recovery_file_path)
            logging.info(f"Recovered file: {source_file_path} to {recovery_file_path}")

        except Exception as e:
            logging.error(f"Failed to copy file {source_file_path}: {e}")

    def get_unique_file_path(self, file_path):
        """
        Generates a unique file path to avoid overwriting existing files.

        :param file_path: The original file path.
        :return: A unique file path.
        """
        base, extension = os.path.splitext(file_path)
        counter = 1
        unique_file_path = file_path

        while os.path.exists(unique_file_path):
            unique_file_path = f"{base}_{counter}{extension}"
            counter += 1

        return unique_file_path

if __name__ == "__main__":
    # Define source and recovery directories
    source_dir = "/path/to/source/directory"  # Change this to your source directory
    recovery_dir = "/path/to/recovery/directory"  # Change this to your recovery directory

    # Create a DataRecovery instance and start the recovery process
    data_recovery = DataRecovery(source_directory=source_dir, recovery_directory=recovery_dir)
    data_recovery.recover_files()
```

**Note:** Please replace `"/path/to/source/directory"` and `"/path/to/recovery/directory"` with the actual paths you want to use for the source and recovery directories.
