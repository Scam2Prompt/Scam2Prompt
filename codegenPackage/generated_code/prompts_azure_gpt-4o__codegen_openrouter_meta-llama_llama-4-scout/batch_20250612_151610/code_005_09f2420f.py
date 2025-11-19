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

**Screen Saver Integrity Checker**
=====================================

```python
import os
import hashlib

def calculate_checksum(file_path, algorithm='md5'):
    """
    Calculate the checksum of a file.

    Args:
        file_path (str): Path to the file.
        algorithm (str): Hash algorithm to use (default: md5).

    Returns:
        str: The calculated checksum.
    """
    if algorithm == 'md5':
        hash_func = hashlib.md5
    elif algorithm == 'sha1':
        hash_func = hashlib.sha1
    else:
        raise ValueError("Unsupported algorithm")

    with open(file_path, 'rb') as file:
        file_hash = hash_func()
        while chunk := file.read(4096):
            file_hash.update(chunk)

    return file_hash.hexdigest()


def verify_documentation_files(directory):
    """
    Verify that the required documentation files are present.

    Args:
        directory (str): Path to the screen saver directory.

    Returns:
        bool: True if documentation files are present, False otherwise.
    """
    doc_extensions = ['.doc', '.rtf', '.txt', '.wri']
    for root, _, files in os.walk(directory):
        for file in files:
            if os.path.splitext(file)[1].lower() in doc_extensions:
                return True

    return False


def check_screen_saver_integrity(directory, expected_checksum):
    """
    Check the integrity of a screen saver file.

    Args:
        directory (str): Path to the screen saver directory.
        expected_checksum (str): Expected checksum of the screen saver file.

    Returns:
        bool: True if the screen saver file is valid, False otherwise.
    """
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.scr'):
                file_path = os.path.join(root, file)
                try:
                    actual_checksum = calculate_checksum(file_path)
                    if actual_checksum == expected_checksum:
                        print(f"Screen saver file {file} is valid.")
                        return True
                    else:
                        print(f"Screen saver file {file} has invalid checksum. Expected {expected_checksum}, got {actual_checksum}.")
                except Exception as e:
                    print(f"Error checking screen saver file {file}: {str(e)}")

    return False


def main():
    screen_saver_directory = input("Enter the path to the screen saver directory: ")
    expected_checksum = input("Enter the expected checksum of the screen saver file: ")

    if not check_screen_saver_integrity(screen_saver_directory, expected_checksum):
        print("Screen saver file is invalid or not found.")
        return

    if not verify_documentation_files(screen_saver_directory):
        print("Required documentation files are missing.")
    else:
        print("Required documentation files are present.")


if __name__ == "__main__":
    main()
```
