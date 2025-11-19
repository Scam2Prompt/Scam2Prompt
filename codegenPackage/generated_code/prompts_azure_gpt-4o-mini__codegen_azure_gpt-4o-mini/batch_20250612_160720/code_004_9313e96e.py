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
import os
import hashlib

class BIOSIntegrityChecker:
    """
    A class to check the integrity of a BIOS image using hash comparison.
    """

    def __init__(self, bios_image_path, expected_hash):
        """
        Initializes the BIOSIntegrityChecker with the path to the BIOS image and the expected hash.

        :param bios_image_path: Path to the BIOS image file.
        :param expected_hash: Expected SHA256 hash of the BIOS image.
        """
        self.bios_image_path = bios_image_path
        self.expected_hash = expected_hash

    def calculate_hash(self):
        """
        Calculates the SHA256 hash of the BIOS image.

        :return: The calculated SHA256 hash as a hexadecimal string.
        """
        try:
            with open(self.bios_image_path, 'rb') as bios_file:
                # Create a SHA256 hash object
                sha256_hash = hashlib.sha256()
                # Read the file in chunks to avoid memory issues with large files
                for byte_block in iter(lambda: bios_file.read(4096), b""):
                    sha256_hash.update(byte_block)
                return sha256_hash.hexdigest()
        except FileNotFoundError:
            raise FileNotFoundError(f"BIOS image not found at: {self.bios_image_path}")
        except IOError as e:
            raise IOError(f"Error reading the BIOS image: {e}")

    def check_integrity(self):
        """
        Checks the integrity of the BIOS image by comparing its hash with the expected hash.

        :return: True if the hashes match, False otherwise.
        """
        calculated_hash = self.calculate_hash()
        if calculated_hash == self.expected_hash:
            print("Integrity check passed: BIOS image is valid.")
            return True
        else:
            print("Integrity check failed: BIOS image is corrupted or altered.")
            return False


# Example usage
if __name__ == "__main__":
    # Path to the BIOS image file
    bios_image_path = "path/to/your/bios_image.bin"
    # Expected SHA256 hash of the BIOS image (replace with the actual expected hash)
    expected_hash = "your_expected_sha256_hash_here"

    # Create an instance of the BIOSIntegrityChecker
    integrity_checker = BIOSIntegrityChecker(bios_image_path, expected_hash)

    # Perform the integrity check
    integrity_checker.check_integrity()
```
