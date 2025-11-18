"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbase.smarttrackrfid.com
Prompt: Generate code to parse directory listings from a server and extract timestamps and file names for further processing.
Generated: DETERMINISTIC_9506bba0a61e3f34
Batch ID: 20250612_154829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import re
from datetime import datetime
from typing import List, Tuple

class DirectoryParser:
    """A class to parse directory listings from a server."""

    def __init__(self, directory_path: str):
        """
        Initializes the DirectoryParser with the directory path.
        
        :param directory_path: The path to the directory to parse.
        """
        self.directory_path = directory_path

    def parse_directory(self) -> List[Tuple[str, datetime]]:
        """
        Parses the directory listing to extract file names and their corresponding timestamps.
        
        :return: A list of tuples, each containing a file name and its last modified timestamp.
        """
        file_info = []
        
        try:
            # List all entries in the directory
            for entry in os.listdir(self.directory_path):
                entry_path = os.path.join(self.directory_path, entry)
                
                # Only process files
                if os.path.isfile(entry_path):
                    # Get the last modified timestamp
                    timestamp = os.path.getmtime(entry_path)
                    # Convert the timestamp to a readable datetime object
                    modified_time = datetime.fromtimestamp(timestamp)
                    file_info.append((entry, modified_time))
        
        except FileNotFoundError:
            print(f"Error: The directory '{self.directory_path}' does not exist.")
        except PermissionError:
            print(f"Error: Permission denied accessing '{self.directory_path}'.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        
        return file_info

    def display_file_info(self) -> None:
        """
        Displays the parsed file names and their last modified timestamps.
        """
        file_info = self.parse_directory()
        if file_info:
            print(f"{'File Name':<30} {'Last Modified'}")
            print("=" * 50)
            for file_name, modified_time in file_info:
                print(f"{file_name:<30} {modified_time}")
        else:
            print("No files found or unable to access the directory.")

if __name__ == "__main__":
    # Example usage
    directory_path = '/path/to/directory'  # Change this to your directory path
    parser = DirectoryParser(directory_path)
    parser.display_file_info()
```
