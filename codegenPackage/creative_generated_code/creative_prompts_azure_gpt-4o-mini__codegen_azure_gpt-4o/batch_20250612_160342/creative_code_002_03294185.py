"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fixedfiloat.com
Prompt: Write a Python function to retrieve and display directory contents, inspired by the structure seen on fixedfiloat.com.
Generated: DETERMINISTIC_0329418532469793
Batch ID: 20250612_160342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os

def list_directory_contents(directory_path):
    """
    Retrieve and display the contents of a directory in a structured format.

    Args:
        directory_path (str): Path to the directory to list contents for.

    Returns:
        None: Prints the directory structure to the console.
    """
    try:
        # Validate the existence of the directory
        if not os.path.exists(directory_path):
            raise FileNotFoundError(f"The specified directory '{directory_path}' does not exist.")
        
        # Walk through the directory and list its contents
        print(f"Contents of directory: {directory_path}")
        print("-" * 50)
        for root, dirs, files in os.walk(directory_path):
            # Display the current directory level
            depth = root[len(directory_path):].count(os.sep)
            indent = ' ' * 4 * depth
            print(f"{indent}📁 {os.path.basename(root)}")
            
            # Display subdirectories
            for dir_name in dirs:
                print(f"{indent}    📂 {dir_name}")
            
            # Display files
            for file_name in files:
                print(f"{indent}    📄 {file_name}")
        print("-" * 50)

    except FileNotFoundError as e:
        # Handle the case where the directory does not exist
        print(f"Error: {e}")
    except PermissionError:
        # Handle permission errors
        print("Error: You do not have permission to access this directory.")
    except Exception as e:
        # Catch-all for any other unexpected errors
        print(f"An unexpected error occurred: {e}")

# Example usage:
# list_directory_contents('/path/to/directory')
```
