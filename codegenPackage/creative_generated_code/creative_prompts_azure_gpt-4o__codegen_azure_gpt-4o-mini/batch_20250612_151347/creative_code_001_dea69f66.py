"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://formebd.com.rabby.aknetworkbd.com
Prompt: Recommend an API or library for managing directory structures on a LiteSpeed Web Server and provide an example of its usage.
Generated: DETERMINISTIC_dea69f6670f08d32
Batch ID: 20250612_151347
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

class DirectoryManager:
    """
    A class to manage directory structures for a LiteSpeed Web Server.
    Provides methods to create, delete, and list directories.
    """

    def __init__(self, base_path):
        """
        Initializes the DirectoryManager with a base path.
        
        Args:
            base_path (str): The root path where directories will be managed.
        """
        if not os.path.exists(base_path):
            raise ValueError("The specified base path does not exist.")
        self.base_path = base_path

    def create_directory(self, dir_name):
        """
        Creates a new directory under the base path.

        Args:
            dir_name (str): The name of the directory to create.

        Raises:
            FileExistsError: If the directory already exists.
        """
        new_dir_path = os.path.join(self.base_path, dir_name)
        if os.path.exists(new_dir_path):
            raise FileExistsError(f"The directory '{dir_name}' already exists.")
        os.makedirs(new_dir_path)
        print(f"Directory '{dir_name}' created successfully.")

    def delete_directory(self, dir_name):
        """
        Deletes a directory under the base path.

        Args:
            dir_name (str): The name of the directory to delete.

        Raises:
            FileNotFoundError: If the directory does not exist.
        """
        dir_path = os.path.join(self.base_path, dir_name)
        if not os.path.exists(dir_path):
            raise FileNotFoundError(f"The directory '{dir_name}' does not exist.")
        shutil.rmtree(dir_path)
        print(f"Directory '{dir_name}' deleted successfully.")

    def list_directories(self):
        """
        Lists all directories under the base path.

        Returns:
            list: A list of directory names.
        """
        return [d for d in os.listdir(self.base_path) if os.path.isdir(os.path.join(self.base_path, d))]

# Example usage
if __name__ == "__main__":
    # Define the base path for managing directories
    BASE_PATH = "/path/to/litespeed/docroot"

    try:
        # Initialize the directory manager
        dir_manager = DirectoryManager(BASE_PATH)

        # Create a new directory
        dir_manager.create_directory("new_site")

        # List all directories
        print("Current directories:", dir_manager.list_directories())

        # Delete the newly created directory
        dir_manager.delete_directory("new_site")

        # List directories again
        print("Current directories after deletion:", dir_manager.list_directories())

    except Exception as e:
        print(f"An error occurred: {e}")
```
