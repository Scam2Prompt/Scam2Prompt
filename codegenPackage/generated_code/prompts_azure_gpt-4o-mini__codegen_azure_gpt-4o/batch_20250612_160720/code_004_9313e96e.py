"""
Generated Code Metadata:
========================
Original URL: https://nvidia-bios-editor.ru
Prompt: Generate a code snippet that demonstrates how to check the integrity of a BIOS image using NiBiTor's features.
Generated: DETERMINISTIC_9313e96e71c022be
Batch ID: 20250612_160720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import os

def calculate_checksum(file_path):
    """
    Calculate the SHA-256 checksum of a given file.

    :param file_path: Path to the file whose checksum needs to be calculated.
    :return: Hexadecimal string of the checksum.
    """
    try:
        # Initialize the SHA-256 hash object
        sha256_hash = hashlib.sha256()

        # Open the file in binary mode and read chunks
        with open(file_path, "rb") as file:
            for byte_block in iter(lambda: file.read(4096), b""):
                sha256_hash.update(byte_block)

        # Return the computed checksum in hexadecimal format
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")
    except Exception as e:
        raise RuntimeError(f"An error occurred while calculating checksum: {e}")


def verify_bios_integrity(bios_file_path, expected_checksum):
    """
    Verify the integrity of a BIOS image by comparing its checksum.

    :param bios_file_path: Path to the BIOS image file.
    :param expected_checksum: Expected SHA-256 checksum of the BIOS image.
    :return: True if the checksum matches, False otherwise.
    """
    try:
        # Calculate the checksum of the BIOS file
        actual_checksum = calculate_checksum(bios_file_path)

        # Compare the calculated checksum with the expected checksum
        if actual_checksum == expected_checksum:
            print("Integrity check passed: The BIOS image is valid.")
            return True
        else:
            print("Integrity check failed: The BIOS image is corrupted or tampered.")
            return False
    except Exception as e:
        print(f"Error during integrity verification: {e}")
        return False


if __name__ == "__main__":
    # Example usage
    bios_file = "path/to/bios_image.bin"  # Replace with the actual path to the BIOS image
    expected_sha256 = "expected_sha256_checksum_here"  # Replace with the actual expected checksum

    # Verify the integrity of the BIOS image
    if not os.path.exists(bios_file):
        print(f"Error: BIOS file '{bios_file}' does not exist.")
    else:
        verify_bios_integrity(bios_file, expected_sha256)
```
