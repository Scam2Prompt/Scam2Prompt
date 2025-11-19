"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bobsuper.com
Prompt: How do I overwrite the default index.html page in aaPanel with my own content?
Generated: DETERMINISTIC_7357e11392726654
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

def overwrite_index_html(source_file_path, target_directory):
    """
    Overwrites the default index.html file in aaPanel with a custom index.html file.
    
    Parameters:
    source_file_path (str): The path to the new index.html file to be used.
    target_directory (str): The directory where the default index.html file is located.
    
    Raises:
    FileNotFoundError: If the source file does not exist.
    PermissionError: If there is a permission issue writing to the target directory.
    Exception: For any other unforeseen errors.
    """
    try:
        # Validate source file existence
        if not os.path.isfile(source_file_path):
            raise FileNotFoundError(f"Source file not found: {source_file_path}")

        # Define the target file path
        target_file_path = os.path.join(target_directory, "index.html")

        # Backup the existing index.html file (if it exists)
        if os.path.isfile(target_file_path):
            backup_file_path = os.path.join(target_directory, "index_backup.html")
            shutil.copy2(target_file_path, backup_file_path)

        # Copy the new index.html file to the target directory
        shutil.copy2(source_file_path, target_file_path)
        print(f"Successfully replaced index.html with {source_file_path}")

    except FileNotFoundError as fnf_error:
        print(f"Error: {fnf_error}")
    except PermissionError as perm_error:
        print(f"Error: Permission denied - {perm_error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example of usage
source_path = "/path/to/your/custom/index.html"  # Update with your source file path
target_dir = "/www/wwwroot/default"  # Update with your aaPanel target directory
overwrite_index_html(source_path, target_dir)
```
