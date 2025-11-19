"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://binanceclub.rf.gd
Prompt: Create a tutorial on transferring an existing website to iFastNet hosting, highlighting the unlimited bandwidth and disk space features.
Generated: DETERMINISTIC_1e28adee53ee2bce
Batch ID: 20250612_161119
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

class WebsiteTransfer:
    """
    A class to handle the transfer of a website to iFastNet hosting.
    """

    def __init__(self, source_directory, destination_directory):
        """
        Initializes the WebsiteTransfer class.

        :param source_directory: str: The local path to the existing website files.
        :param destination_directory: str: The iFastNet hosting directory path.
        """
        self.source_directory = source_directory
        self.destination_directory = destination_directory

    def verify_directories(self):
        """
        Verifies that the source and destination directories exist.

        :raises FileNotFoundError: If the source directory does not exist.
        :raises NotADirectoryError: If the destination directory is not a directory.
        """
        if not os.path.exists(self.source_directory):
            raise FileNotFoundError(f"Source directory '{self.source_directory}' does not exist.")
        
        if not os.path.isdir(self.destination_directory):
            raise NotADirectoryError(f"Destination directory '{self.destination_directory}' is not a directory.")

    def transfer_files(self):
        """
        Transfers files from the source directory to the destination directory.

        :raises Exception: If an error occurs during the file transfer.
        """
        try:
            # Copy the entire website directory to the new destination
            shutil.copytree(self.source_directory, self.destination_directory, dirs_exist_ok=True)
            print(f"Successfully transferred files from '{self.source_directory}' to '{self.destination_directory}'.")
        except Exception as e:
            raise Exception(f"An error occurred during file transfer: {e}")

    def run(self):
        """
        Executes the file transfer process.
        """
        try:
            self.verify_directories()
            self.transfer_files()
        except Exception as e:
            print(f"Transfer failed: {e}")

if __name__ == "__main__":
    # Define source and destination paths
    source = "/path/to/existing/website"  # Replace with the actual path to the website files
    destination = "/path/to/ifastnet/hosting"  # Replace with the actual destination path on iFastNet

    # Create a WebsiteTransfer object and run the transfer
    transfer = WebsiteTransfer(source, destination)
    transfer.run()
```
