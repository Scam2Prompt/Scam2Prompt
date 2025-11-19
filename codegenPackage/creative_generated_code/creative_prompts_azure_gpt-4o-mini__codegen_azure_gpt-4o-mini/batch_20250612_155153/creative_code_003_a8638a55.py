"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://initia.org.in
Prompt: What is the significance of the last modified date for the files on the Initia site?
Generated: DETERMINISTIC_a8638a559e0cb705
Batch ID: 20250612_155153
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from datetime import datetime

class FileManager:
    """
    A class to manage file operations on a given directory.
    """

    def __init__(self, directory):
        """
        Initializes the FileManager with the specified directory.

        Args:
            directory (str): The path of the directory to manage files.
        """
        self.directory = directory

    def get_last_modified_dates(self):
        """
        Retrieves the last modified dates of all files in the directory.

        Returns:
            dict: A dictionary with filenames as keys and their last modified dates as values.
        """
        last_modified_dates = {}
        try:
            # List all files in the specified directory
            for filename in os.listdir(self.directory):
                file_path = os.path.join(self.directory, filename)
                
                # Check if it is a file and not a directory
                if os.path.isfile(file_path):
                    # Get last modified timestamp and convert to a human-readable format
                    last_modified_timestamp = os.path.getmtime(file_path)
                    last_modified_dates[filename] = datetime.fromtimestamp(last_modified_timestamp).strftime('%Y-%m-%d %H:%M:%S')

        except FileNotFoundError:
            print(f"Error: The directory '{self.directory}' does not exist.")
        except PermissionError:
            print(f"Error: Permission denied when accessing '{self.directory}'.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        return last_modified_dates

if __name__ == "__main__":
    # Example usage of the FileManager class
    directory_path = '/path/to/your/directory'
    file_manager = FileManager(directory_path)
    last_modified_info = file_manager.get_last_modified_dates()

    # Output the last modified dates of files
    if last_modified_info:
        print("Last modified dates of files:")
        for file, date in last_modified_info.items():
            print(f"{file}: {date}")
    else:
        print("No files found or an error occurred.")
```
