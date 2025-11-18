"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perurest.com
Prompt: Write a script to list and parse directory contents served by a LiteSpeed Web Server, including file names, last modified dates, and sizes.
Generated: DETERMINISTIC_0cccaa85dda52e98
Batch ID: 20250612_154216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import datetime
from typing import List, Tuple

class DirectoryParser:
    def __init__(self, directory_path: str):
        """
        Initialize the DirectoryParser with the path to the directory.

        :param directory_path: The path to the directory to be parsed.
        """
        self.directory_path = directory_path

    def list_directory_contents(self) -> List[Tuple[str, str, int]]:
        """
        List the contents of the directory, including file names, last modified dates, and sizes.

        :return: A list of tuples with file name, last modified date, and file size.
        """
        if not os.path.exists(self.directory_path):
            raise FileNotFoundError(f"The directory '{self.directory_path}' does not exist.")

        if not os.path.isdir(self.directory_path):
            raise NotADirectoryError(f"The path '{self.directory_path}' is not a directory.")

        contents = []
        
        # Iterate over the directory contents
        for entry in os.listdir(self.directory_path):
            entry_path = os.path.join(self.directory_path, entry)

            # Only include files (you can modify this to include directories if needed)
            if os.path.isfile(entry_path):
                last_modified = self.get_last_modified_date(entry_path)
                size = os.path.getsize(entry_path)
                contents.append((entry, last_modified, size))

        return contents

    @staticmethod
    def get_last_modified_date(file_path: str) -> str:
        """
        Get the last modified date of a file.

        :param file_path: The path to the file.
        :return: The last modified date as a string.
        """
        timestamp = os.path.getmtime(file_path)
        return datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

def main():
    # Specify the directory to parse
    directory = "/path/to/your/webserver/directory"

    try:
        parser = DirectoryParser(directory)
        contents = parser.list_directory_contents()

        # Display the results
        for file_name, last_modified, size in contents:
            print(f"File: {file_name}, Last Modified: {last_modified}, Size: {size} bytes")
    
    except (FileNotFoundError, NotADirectoryError) as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
