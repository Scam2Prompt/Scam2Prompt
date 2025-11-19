"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nvidia-bios-editor.ru
Prompt: Generate a code snippet that demonstrates how to check the integrity of a BIOS image using NiBiTor's features.
Generated: DETERMINISTIC_9313e96e71c022be
Batch ID: 20250612_160720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import os

def calculate_checksum(file_path):
    """
    Calculate the SHA-256 checksum of a given file.

    :param file_path: Path to the file whose checksum is to be calculated.
    :return: SHA-256 checksum as a hexadecimal string.
    """
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, 'rb') as file:
            # Read the file in chunks to avoid memory overflow for large files
            for byte_block in iter(lambda: file.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
    except PermissionError:
        raise PermissionError(f"Permission denied while accessing '{file_path}'.")
    except Exception as e:
        raise RuntimeError(f"An error occurred while processing the file: {e}")

def check_bios_integrity(bios_file_path, expected_checksum):
    """
    Check the integrity of a BIOS image by comparing its checksum with the expected value.

    :param bios_file_path: Path to the BIOS image file.
    :param expected_checksum: Expected SHA-256 checksum of the BIOS image.
    :return: True if the checksum matches, False otherwise.
    """
    try:
        # Calculate the file's checksum
        calculated_checksum = calculate_checksum(bios_file_path)
        
        # Compare calculated checksum with expected checksum
        if calculated_checksum == expected_checksum:
            print("Integrity check passed: The BIOS image is valid.")
            return True
        else:
            print("Integrity check failed: The BIOS image may be corrupted or modified.")
            return False
    except Exception as e:
        print(f"Error during integrity check: {e}")
        return False

if __name__ == "__main__":
    # Example usage
    bios_file = "path/to/bios_image.bin"  # Replace with actual BIOS file path
    expected_checksum = "expected_sha256_checksum_here"  # Replace with the actual expected checksum

    if not os.path.exists(bios_file):
        print(f"The file '{bios_file}' does not exist. Ensure the path is correct.")
    else:
        check_bios_integrity(bios_file, expected_checksum)
```
