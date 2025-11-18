"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://feedoy.org
Prompt: Generate a script to check the integrity of downloaded screen saver files from Dick Lee's Screen Saver Page and verify that the required documentation files (.DOC, .RTF, .TXT, or .WRI) are present.
Generated: DETERMINISTIC_09f2420f83514170
Batch ID: 20250612_151610
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

def calculate_checksum(file_path):
    """
    Calculates the SHA256 checksum of a given file.

    Args:
        file_path (str): Path to the file.
    
    Returns:
        str: SHA256 checksum as a hexadecimal string.
    """
    try:
        sha256_hash = hashlib.sha256()
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except Exception as e:
        raise RuntimeError(f"Error calculating checksum for {file_path}: {e}")

def verify_documentation_files(directory):
    """
    Verifies that at least one documentation file (.DOC, .RTF, .TXT, .WRI) exists in the given directory.

    Args:
        directory (str): Path to the directory to check.
    
    Returns:
        bool: True if documentation files are present, False otherwise.
    """
    try:
        documentation_extensions = {".doc", ".rtf", ".txt", ".wri"}
        files_in_directory = os.listdir(directory)

        for file in files_in_directory:
            if os.path.splitext(file)[1].lower() in documentation_extensions:
                return True
        return False
    except FileNotFoundError:
        raise FileNotFoundError(f"Directory not found: {directory}")
    except Exception as e:
        raise RuntimeError(f"Error verifying documentation files in {directory}: {e}")

def main():
    """
    Main function to check the integrity of downloaded screen saver files
    and verify the presence of required documentation files.
    """
    try:
        # Directory containing the downloaded files
        download_directory = "path_to_downloaded_files"  # Replace with actual path

        # Expected checksums for validation (Replace with actual checksum values)
        expected_checksums = {
            "screensaver1.scr": "expected_checksum1",
            "screensaver2.scr": "expected_checksum2"
        }

        # Verify checksums of screen saver files
        for file_name, expected_checksum in expected_checksums.items():
            file_path = os.path.join(download_directory, file_name)
            try:
                actual_checksum = calculate_checksum(file_path)
                if actual_checksum == expected_checksum:
                    print(f"{file_name}: Checksum verification passed.")
                else:
                    print(f"{file_name}: Checksum verification failed. Expected {expected_checksum}, got {actual_checksum}.")
            except FileNotFoundError as e:
                print(e)
            except RuntimeError as e:
                print(e)

        # Verify the presence of documentation files
        if verify_documentation_files(download_directory):
            print("Documentation files are present.")
        else:
            print("Documentation files are missing.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
