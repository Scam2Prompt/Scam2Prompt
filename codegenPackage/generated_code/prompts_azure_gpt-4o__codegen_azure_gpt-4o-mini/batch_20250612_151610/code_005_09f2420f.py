"""
Generated Code Metadata:
========================
Original URL: https://feedoy.org
Prompt: Generate a script to check the integrity of downloaded screen saver files from Dick Lee's Screen Saver Page and verify that the required documentation files (.DOC, .RTF, .TXT, or .WRI) are present.
Generated: DETERMINISTIC_09f2420f83514170
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import hashlib

# Define the directory containing the screen saver files
SCREEN_SAVER_DIR = 'path/to/screen_savers'
# Define the required documentation file extensions
REQUIRED_EXTENSIONS = {'.doc', '.rtf', '.txt', '.wri'}

def calculate_file_hash(file_path):
    """Calculate the SHA-256 hash of a file."""
    hash_sha256 = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                hash_sha256.update(byte_block)
    except IOError as e:
        print(f"Error reading file {file_path}: {e}")
        return None
    return hash_sha256.hexdigest()

def check_integrity_and_documentation(directory):
    """Check the integrity of screen saver files and verify documentation presence."""
    if not os.path.isdir(directory):
        print(f"Error: The directory {directory} does not exist.")
        return

    # List to hold results
    results = []

    # Iterate through files in the specified directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Check if the file is a screen saver (assuming .scr as the extension)
        if filename.endswith('.scr'):
            file_hash = calculate_file_hash(file_path)
            if file_hash:
                results.append((filename, file_hash))

            # Check for required documentation files
            documentation_present = any(
                os.path.isfile(os.path.join(directory, f"{os.path.splitext(filename)[0]}{ext}"))
                for ext in REQUIRED_EXTENSIONS
            )

            if not documentation_present:
                print(f"Warning: Documentation files for {filename} are missing.")

    # Print the integrity check results
    print("\nIntegrity Check Results:")
    for file_name, file_hash in results:
        print(f"{file_name}: {file_hash}")

if __name__ == "__main__":
    check_integrity_and_documentation(SCREEN_SAVER_DIR)
```
