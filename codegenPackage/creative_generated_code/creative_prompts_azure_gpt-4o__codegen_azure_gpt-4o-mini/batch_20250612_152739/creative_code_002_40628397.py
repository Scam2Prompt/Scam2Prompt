"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fg92v79x.s3.eu-north-1.amazonaws.com
Prompt: Create a function in Python that validates the integrity of files stored in an S3 bucket by comparing their hash values with "ed25235c150785b6ceea017e09f191bb".
Generated: DETERMINISTIC_4062839752b38953
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import boto3
import hashlib
import botocore

def calculate_file_hash(file_path):
    """
    Calculate the MD5 hash of a file.

    :param file_path: Path to the file to hash.
    :return: MD5 hash of the file in hexadecimal format.
    """
    hash_md5 = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File not found: {file_path}") from e
    except IOError as e:
        raise IOError(f"Error reading file: {file_path}") from e
    return hash_md5.hexdigest()

def validate_s3_file_integrity(bucket_name, file_key, expected_hash):
    """
    Validate the integrity of a file stored in an S3 bucket by comparing its hash value.

    :param bucket_name: S3 bucket name.
    :param file_key: S3 object key (file name in the bucket).
    :param expected_hash: Expected MD5 hash of the file.
    :return: Boolean indicating whether the file's hash matches the expected hash.
    """
    s3 = boto3.client('s3')

    try:
        # Download the file from S3 to a temporary location
        temp_file_path = f"/tmp/{file_key}"
        s3.download_file(bucket_name, file_key, temp_file_path)

        # Calculate the hash of the downloaded file
        file_hash = calculate_file_hash(temp_file_path)

        # Compare the calculated hash with the expected hash
        return file_hash == expected_hash
    except botocore.exceptions.ClientError as e:
        raise RuntimeError(f"Error accessing S3 bucket: {bucket_name}, file: {file_key}") from e
    except Exception as e:
        raise RuntimeError("An unexpected error occurred") from e

# Example of usage
if __name__ == "__main__":
    BUCKET_NAME = 'your-bucket-name'
    FILE_KEY = 'your-file-key'
    EXPECTED_HASH = 'ed25235c150785b6ceea017e09f191bb'

    is_valid = validate_s3_file_integrity(BUCKET_NAME, FILE_KEY, EXPECTED_HASH)
    if is_valid:
        print("File integrity validated successfully.")
    else:
        print("File integrity validation failed.")
```
