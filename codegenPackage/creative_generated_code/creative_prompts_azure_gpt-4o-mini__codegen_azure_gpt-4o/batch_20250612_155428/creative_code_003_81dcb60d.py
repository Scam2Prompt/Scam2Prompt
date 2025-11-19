"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bobsuper.com
Prompt: What are the best practices for managing the root directory files in aaPanel?
Generated: DETERMINISTIC_81dcb60de8faccac
Batch ID: 20250612_155428
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

def list_files_in_root_directory(root_directory):
    """
    List all files and directories in the specified root directory.
    
    Args:
        root_directory (str): The path of the root directory to manage.
    
    Returns:
        List[str]: A list of all file and directory names in the root directory.
    """
    try:
        # Ensure the root directory exists
        if not os.path.exists(root_directory):
            raise FileNotFoundError(f"Root directory '{root_directory}' does not exist.")

        # Retrieve list of files and directories
        return os.listdir(root_directory)
    except Exception as e:
        # Log or handle any errors
        print(f"Error listing files in root directory: {str(e)}")
        return []


def delete_file(file_path):
    """
    Delete a file from the file system.
    
    Args:
        file_path (str): Path to the file to be deleted.
    """
    try:
        # Ensure the file exists
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"File '{file_path}' does not exist.")

        # Delete the file
        os.remove(file_path)
        print(f"File '{file_path}' successfully deleted.")
    except Exception as e:
        # Log or handle any errors
        print(f"Error deleting file: {str(e)}")


def delete_directory(directory_path):
    """
    Delete a directory and its contents from the file system.
    
    Args:
        directory_path (str): Path to the directory to be deleted.
    """
    try:
        # Ensure the directory exists
        if not os.path.isdir(directory_path):
            raise FileNotFoundError(f"Directory '{directory_path}' does not exist.")

        # Delete the directory and its contents
        shutil.rmtree(directory_path)
        print(f"Directory '{directory_path}' successfully deleted.")
    except Exception as e:
        # Log or handle any errors
        print(f"Error deleting directory: {str(e)}")


def move_file(src_path, dest_path):
    """
    Move a file to a new location.
    
    Args:
        src_path (str): The source path of the file.
        dest_path (str): The destination path of the file.
    """
    try:
        # Ensure the source file exists
        if not os.path.isfile(src_path):
            raise FileNotFoundError(f"Source file '{src_path}' does not exist.")

        # Move the file
        shutil.move(src_path, dest_path)
        print(f"File '{src_path}' successfully moved to '{dest_path}'.")
    except Exception as e:
        # Log or handle any errors
        print(f"Error moving file: {str(e)}")


def create_directory(directory_path):
    """
    Create a new directory.
    
    Args:
        directory_path (str): Path for the new directory.
    """
    try:
        # Ensure the directory does not already exist
        if os.path.exists(directory_path):
            raise FileExistsError(f"Directory '{directory_path}' already exists.")

        # Create the directory
        os.makedirs(directory_path)
        print(f"Directory '{directory_path}' successfully created.")
    except Exception as e:
        # Log or handle any errors
        print(f"Error creating directory: {str(e)}")


def main():
    """
    Main function to demonstrate best practices for managing the root directory files.
    """
    # Example root directory path
    root_directory = "/path/to/root/directory"

    # List files in the root directory
    print("Files in root directory:")
    files_and_directories = list_files_in_root_directory(root_directory)
    for item in files_and_directories:
        print(item)

    # Example file management operations
    # Be sure to replace paths with actual ones for testing purposes
    example_file_path = "/path/to/root/directory/example.txt"
    example_directory_path = "/path/to/root/directory/example_folder"
    example_destination_path = "/path/to/root/directory/moved_example.txt"

    # Example operations
    delete_file(example_file_path)  # Delete a file
    delete_directory(example_directory_path)  # Delete a directory
    move_file(example_file_path, example_destination_path)  # Move a file
    create_directory(example_directory_path)  # Create a new directory


if __name__ == "__main__":
    # Entry point to execute the script
    main()
```
