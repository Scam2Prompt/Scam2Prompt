"""
Generated Code Metadata:
========================
Original URL: https://feedoy.org
Prompt: Create a function that checks for the presence of documentation files (.DOC, .RTF, .TXT) in a screen saver package, inspired by the content from Dick Lee's Screen Saver Page.
Generated: DETERMINISTIC_f371a81a40c0c386
Batch ID: 20250612_135617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os

def check_documentation_files(directory_path):
    """
    Checks for the presence of documentation files (.DOC, .RTF, .TXT) 
    in the specified directory.

    Args:
        directory_path (str): The path to the directory to check.

    Returns:
        dict: A dictionary with file extensions as keys and lists of found files as values.
              Example: {'DOC': ['file1.doc'], 'RTF': ['file2.rtf'], 'TXT': ['file3.txt']}
    """
    # Supported documentation file extensions
    supported_extensions = ['.DOC', '.RTF', '.TXT']
    
    # Dictionary to store found files by extension
    found_files = {ext.strip('.').upper(): [] for ext in supported_extensions}

    try:
        # Check if the directory exists
        if not os.path.isdir(directory_path):
            raise FileNotFoundError(f"The directory '{directory_path}' does not exist.")

        # Iterate through files in the directory
        for file_name in os.listdir(directory_path):
            # Get the file extension
            _, file_extension = os.path.splitext(file_name)
            
            # Check if the file extension matches supported extensions
            if file_extension.upper() in supported_extensions:
                found_files[file_extension.strip('.').upper()].append(file_name)
    
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except PermissionError as perm_error:
        print(f"Permission denied: {perm_error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return found_files


# Example usage:
if __name__ == "__main__":
    # Replace 'path_to_directory' with the actual path to the screen saver package directory
    directory = "path_to_directory"
    result = check_documentation_files(directory)
    print("Documentation files found:", result)
```
