"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hubsupport.rf.gd
Prompt: What are the steps to take advantage of unlimited disk space on iFastNet Web Hosting for a new project?
Generated: DETERMINISTIC_8cede04de4aa8206
Batch ID: 20250612_164151
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

class IFastNetDiskManager:
    """
    A class to manage files on iFastNet web hosting with unlimited disk space.
    """

    def __init__(self, base_directory):
        """
        Initializes the disk manager with a specified base directory.

        Parameters:
        - base_directory (str): The path to the base directory on iFastNet.
        """
        self.base_directory = base_directory
        self.ensure_directory_exists(self.base_directory)

    def ensure_directory_exists(self, directory):
        """
        Ensure that the specified directory exists. If not, create it.

        Parameters:
        - directory (str): The directory path to check.
        """
        try:
            os.makedirs(directory, exist_ok=True)
            print(f"Directory '{directory}' is ready for use.")
        except Exception as e:
            print(f"Error creating directory '{directory}': {e}")

    def upload_file(self, source_path):
        """
        Upload a file from the local system to the iFastNet hosting.

        Parameters:
        - source_path (str): The path of the file to upload.
        """
        if not os.path.isfile(source_path):
            print(f"Source file '{source_path}' does not exist.")
            return

        file_name = os.path.basename(source_path)
        destination_path = os.path.join(self.base_directory, file_name)

        try:
            shutil.copy2(source_path, destination_path)
            print(f"File '{file_name}' uploaded successfully to '{self.base_directory}'.")
        except Exception as e:
            print(f"Error uploading file '{file_name}': {e}")

    def delete_file(self, file_name):
        """
        Delete a file from the iFastNet hosting.

        Parameters:
        - file_name (str): The name of the file to delete.
        """
        file_path = os.path.join(self.base_directory, file_name)

        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"File '{file_name}' deleted successfully.")
            else:
                print(f"File '{file_name}' does not exist.")
        except Exception as e:
            print(f"Error deleting file '{file_name}': {e}")

    def list_files(self):
        """
        List all files in the current directory on iFastNet hosting.
        """
        try:
            files = os.listdir(self.base_directory)
            print("Files in directory:")
            for file in files:
                print(f"- {file}")
        except Exception as e:
            print(f"Error listing files: {e}")


# Example usage:
if __name__ == "__main__":
    # Set the base directory for your project on iFastNet
    BASE_DIR = '/path/to/your/project'  # Change this to your actual path

    # Create an instance of the IFastNetDiskManager
    disk_manager = IFastNetDiskManager(BASE_DIR)

    # Upload a file (replace with your file path)
    disk_manager.upload_file('/path/to/local/file.txt')

    # List files in the project directory
    disk_manager.list_files()

    # Delete a file (replace with your file name)
    disk_manager.delete_file('file.txt')
```
