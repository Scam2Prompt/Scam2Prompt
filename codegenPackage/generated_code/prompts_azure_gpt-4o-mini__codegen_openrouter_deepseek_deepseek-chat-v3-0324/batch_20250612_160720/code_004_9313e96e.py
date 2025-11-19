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

def calculate_file_hash(file_path, hash_algorithm='sha256'):
    """
    Calculate the hash of a file using the specified algorithm.
    
    Args:
        file_path (str): Path to the file to be hashed.
        hash_algorithm (str): Hash algorithm to use (default: 'sha256').
    
    Returns:
        str: Hexadecimal digest of the file's hash.
    
    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the hash algorithm is not supported.
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    if hash_algorithm not in hashlib.algorithms_available:
        raise ValueError(f"Unsupported hash algorithm: {hash_algorithm}")
    
    hash_func = hashlib.new(hash_algorithm)
    
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            hash_func.update(chunk)
    
    return hash_func.hexdigest()

def verify_bios_integrity(bios_file_path, expected_hash, hash_algorithm='sha256'):
    """
    Verify the integrity of a BIOS image by comparing its hash with an expected value.
    
    Args:
        bios_file_path (str): Path to the BIOS image file.
        expected_hash (str): Expected hash value to compare against.
        hash_algorithm (str): Hash algorithm used (default: 'sha256').
    
    Returns:
        bool: True if the hash matches, False otherwise.
    
    Raises:
        FileNotFoundError: If the BIOS file does not exist.
        ValueError: If the hash algorithm is not supported.
    """
    try:
        actual_hash = calculate_file_hash(bios_file_path, hash_algorithm)
        return actual_hash == expected_hash.lower()
    except Exception as e:
        print(f"Error verifying BIOS integrity: {e}")
        return False

# Example usage
if __name__ == "__main__":
    BIOS_FILE = "bios_image.rom"
    EXPECTED_HASH = "a1b2c3d4e5f6..."  # Replace with actual expected hash
    
    try:
        is_valid = verify_bios_integrity(BIOS_FILE, EXPECTED_HASH)
        if is_valid:
            print("BIOS image integrity verified successfully.")
        else:
            print("BIOS image integrity check failed. Hashes do not match.")
    except Exception as e:
        print(f"Error during BIOS verification: {e}")
```
