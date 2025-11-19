"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://icolast.top
Prompt: What steps should I follow to overwrite the automatically generated index.html file in my site root directory?
Generated: DETERMINISTIC_7251eac8266e51c5
Batch ID: 20250612_162854
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

def overwrite_index_html(source_file: str, destination_dir: str) -> None:
    """
    Overwrite the automatically generated index.html file in the specified directory.

    Parameters:
    source_file (str): The path to the new index.html file that will replace the existing one.
    destination_dir (str): The directory where the index.html file should be overwritten.

    Raises:
    FileNotFoundError: If the source_file does not exist.
    OSError: If the destination directory does not exist or cannot be accessed.
    Exception: For any other unexpected errors.
    """
    
    try:
        # Check if the source file exists
        if not os.path.isfile(source_file):
            raise FileNotFoundError(f"Source file '{source_file}' does not exist.")

        # Check if the destination directory exists
        if not os.path.isdir(destination_dir):
            raise OSError(f"Destination directory '{destination_dir}' does not exist or cannot be accessed.")

        # Define the full path of the destination file
        destination_file = os.path.join(destination_dir, 'index.html')

        # Overwrite the existing index.html file with the source file
        shutil.copyfile(source_file, destination_file)
        print(f"Successfully overwritten '{destination_file}' with '{source_file}'.")

    except FileNotFoundError as fnf_error:
        print(f"Error: {fnf_error}")
    except OSError as os_error:
        print(f"Error: {os_error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
# overwrite_index_html('path/to/new/index.html', '/path/to/site/root')
```
