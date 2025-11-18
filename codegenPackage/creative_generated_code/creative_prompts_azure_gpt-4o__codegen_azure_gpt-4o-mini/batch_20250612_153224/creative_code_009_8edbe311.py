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

# Define the directory where WordPress is installed
WP_DIRECTORY = '/path/to/your/wordpress'
# Define a reference file containing the expected file hashes
REFERENCE_FILE = 'wp_core_hashes.txt'

def load_reference_hashes(reference_file):
    """
    Load the expected file hashes from the reference file.

    :param reference_file: Path to the file containing expected hashes
    :return: Dictionary of file names and their corresponding hashes
    """
    hashes = {}
    try:
        with open(reference_file, 'r') as file:
            for line in file:
                if line.strip():  # Avoid empty lines
                    parts = line.strip().split()
                    if len(parts) == 2:
                        hashes[parts[0]] = parts[1]
    except FileNotFoundError:
        raise FileNotFoundError(f"Reference file not found: {reference_file}")
    except Exception as e:
        raise RuntimeError(f"An error occurred while reading the reference file: {e}")
    
    return hashes

def calculate_file_hash(file_path):
    """
    Calculate the SHA256 hash of a file.

    :param file_path: Path to the file to hash
    :return: SHA256 hash of the file as a hexadecimal string
    """
    hash_sha256 = hashlib.sha256()
    
    try:
        with open(file_path, 'rb') as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                hash_sha256.update(byte_block)
    except Exception as e:
        raise RuntimeError(f"An error occurred while hashing the file {file_path}: {e}")
    
    return hash_sha256.hexdigest()

def validate_wordpress_files(wp_directory, reference_hashes):
    """
    Validate the integrity of WordPress core files by comparing their hashes to a reference.

    :param wp_directory: Directory where WordPress is installed
    :param reference_hashes: Dictionary of expected file hashes
    """
    for file_name, expected_hash in reference_hashes.items():
        file_path = os.path.join(wp_directory, file_name)
        
        if os.path.exists(file_path):
            file_hash = calculate_file_hash(file_path)
            if file_hash != expected_hash:
                print(f"File integrity check failed for {file_name}. Expected: {expected_hash}, Found: {file_hash}")
            else:
                print(f"File integrity check passed for {file_name}.")
        else:
            print(f"File not found: {file_name}")

if __name__ == "__main__":
    # Load expected file hashes
    try:
        reference_hashes = load_reference_hashes(REFERENCE_FILE)
        
        # Validate the integrity of WordPress core files
        validate_wordpress_files(WP_DIRECTORY, reference_hashes)
    except Exception as e:
        print(f"An error occurred: {e}")
```

> Note: Please ensure to update `WP_DIRECTORY` and `REFERENCE_FILE` with appropriate paths before running the code. The `wp_core_hashes.txt` should be formatted with each line containing a filename followed by its expected SHA256 hash.
