"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://icopages.pw
Prompt: What steps should I follow to delete or overwrite the automatically generated index.html page on my site?
Generated: DETERMINISTIC_657b69106d754ec9
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

def delete_or_overwrite_index_html(target_directory, new_file_path=None):
    """
    Deletes or overwrites the automatically generated index.html page
    in the specified directory.

    Parameters:
    target_directory (str): The directory where index.html is located.
    new_file_path (str): Optional path to the new file to overwrite the existing index.html.

    Raises:
    FileNotFoundError: If the target directory does not exist.
    Exception: For any other unexpected errors.
    """
    try:
        # Check if the target directory exists
        if not os.path.exists(target_directory):
            raise FileNotFoundError(f"The directory '{target_directory}' does not exist.")
        
        index_file_path = os.path.join(target_directory, 'index.html')

        # Check if index.html exists
        if os.path.exists(index_file_path):
            # If a new file path is provided, overwrite index.html
            if new_file_path:
                if os.path.exists(new_file_path):
                    shutil.copy2(new_file_path, index_file_path)
                    print(f"Overwritten 'index.html' with '{new_file_path}'.")
                else:
                    raise FileNotFoundError(f"The new file '{new_file_path}' does not exist.")
            else:
                # If no new file is provided, delete index.html
                os.remove(index_file_path)
                print("'index.html' has been deleted.")
        else:
            print("'index.html' does not exist in the specified directory.")

    except FileNotFoundError as fnf_error:
        print(f"FileNotFoundError: {fnf_error}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
# delete_or_overwrite_index_html('/path/to/your/website', '/path/to/new/file.html')
```
