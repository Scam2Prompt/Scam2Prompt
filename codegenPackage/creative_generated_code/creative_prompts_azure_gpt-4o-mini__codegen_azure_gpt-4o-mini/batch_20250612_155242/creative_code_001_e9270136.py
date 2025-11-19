"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dwbridge.com
Prompt: Can you explain the structure of the dwbridge.com server index, including the cgi-bin and marmiton directories?
Generated: DETERMINISTIC_e92701366858b465
Batch ID: 20250612_155242
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import logging

# Configure logging for better error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ServerIndex:
    """
    Class to represent and manage the server index of dwbridge.com.
    Contains information about the cgi-bin and marmiton directories.
    """

    def __init__(self, base_directory):
        """
        Initializes the ServerIndex with a base directory.

        :param base_directory: The root directory of the server.
        """
        self.base_directory = base_directory
        self.cgi_bin_path = os.path.join(base_directory, 'cgi-bin')
        self.marmiton_path = os.path.join(base_directory, 'marmiton')

    def list_directory(self, directory):
        """
        List all files and subdirectories in the specified directory.

        :param directory: The directory to list.
        :return: A list of directory contents.
        """
        try:
            contents = os.listdir(directory)
            return contents
        except FileNotFoundError:
            logging.error(f"Directory not found: {directory}")
            return []
        except Exception as e:
            logging.error(f"Error accessing directory: {directory}. Error: {e}")
            return []

    def get_index_structure(self):
        """
        Get the structure of the server index including cgi-bin and marmiton directories.

        :return: A dictionary with directory structures.
        """
        index_structure = {
            'cgi-bin': {
                'path': self.cgi_bin_path,
                'contents': self.list_directory(self.cgi_bin_path)
            },
            'marmiton': {
                'path': self.marmiton_path,
                'contents': self.list_directory(self.marmiton_path)
            }
        }
        return index_structure

if __name__ == "__main__":
    # Specify the base directory for the server
    base_dir = "/path/to/dwbridge.com"  # Change this to the actual path

    # Create an instance of ServerIndex
    server_index = ServerIndex(base_directory=base_dir)

    # Get and print the index structure
    index_structure = server_index.get_index_structure()
    print("Server Index Structure:")
    for key, value in index_structure.items():
        print(f"{key}: {value['contents']}")
```
