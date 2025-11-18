"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.cenvirmarketingdigital.com
Prompt: Create a script to validate the integrity of WordPress core files, including `wp-load.php` and `wp-blog-header.php`, using the directory listing as a reference.
Generated: DETERMINISTIC_8edbe311345c2773
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import hashlib

def calculate_file_hash(file_path):
    """
    Calculate the SHA256 hash of a file.

    Args:
        file_path (str): Path to the file.

    Returns:
        str: Hexadecimal SHA256 hash of the file.
    """
    try:
        hasher = hashlib.sha256()
        with open(file_path, 'rb') as f:
            while chunk := f.read(8192):
                hasher.update(chunk)
        return hasher.hexdigest()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"Error: Unable to calculate hash for '{file_path}'. Reason: {e}")
        return None

def validate_wp_core_files(directory):
    """
    Validate the integrity of WordPress core files.

    Args:
        directory (str): Path to the WordPress installation directory.

    Returns:
        None
    """
    # List of important WordPress core files to validate
    core_files = ['wp-load.php', 'wp-blog-header.php']
    validation_results = {}

    for core_file in core_files:
        file_path = os.path.join(directory, core_file)
        if os.path.isfile(file_path):
            file_hash = calculate_file_hash(file_path)
            if file_hash:
                validation_results[core_file] = file_hash
        else:
            print(f"Warning: '{core_file}' is missing in the directory '{directory}'.")

    # Summarize validation results
    print("\nWordPress Core File Validation Results:")
    for file, file_hash in validation_results.items():
        print(f"{file}: {file_hash}")

def main():
    """
    Entry point for the script.
    """
    # Prompt user for the WordPress directory path
    wp_directory = input("Enter the path to your WordPress installation directory: ").strip()

    if not os.path.isdir(wp_directory):
        print(f"Error: Directory '{wp_directory}' does not exist or is not accessible.")
        return

    print(f"Validating WordPress core files in: {wp_directory}")
    validate_wp_core_files(wp_directory)

if __name__ == "__main__":
    main()
```
