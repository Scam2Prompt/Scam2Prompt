"""
Generated Code Metadata:
========================
Original URL: https://fg92v79x.s3.eu-north-1.amazonaws.com
Prompt: Create a script to compare the metadata of two files in an S3 bucket, focusing on timestamps and hash values, as described in the fg92v79x.html documentation.
Generated: DETERMINISTIC_b28f862dff0503e9
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import boto3
import hashlib
import botocore

def calculate_file_hash(file_path):
    """
    Calculate the hash of a file.

    Args:
        file_path (str): The path to the file.

    Returns:
        str: The hash of the file.
    """
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def get_s3_file_metadata(bucket_name, file_name):
    """
    Get the metadata of a file in an S3 bucket.

    Args:
        bucket_name (str): The name of the S3 bucket.
        file_name (str): The name of the file.

    Returns:
        dict: The metadata of the file.
    """
    try:
        s3 = boto3.client('s3')
        metadata = s3.head_object(Bucket=bucket_name, Key=file_name)
        return metadata
    except botocore.exceptions.ClientError as e:
        print(f"Error getting metadata for {file_name}: {e}")
        return None


def compare_file_metadata(bucket_name, file_name1, file_name2):
    """
    Compare the metadata of two files in an S3 bucket.

    Args:
        bucket_name (str): The name of the S3 bucket.
        file_name1 (str): The name of the first file.
        file_name2 (str): The name of the second file.

    Returns:
        dict: A dictionary containing the comparison results.
    """
    metadata1 = get_s3_file_metadata(bucket_name, file_name1)
    metadata2 = get_s3_file_metadata(bucket_name, file_name2)

    if metadata1 is None or metadata2 is None:
        return None

    # Download files from S3 to calculate hash
    try:
        s3 = boto3.client('s3')
        s3.download_file(bucket_name, file_name1, '/tmp/' + file_name1)
        s3.download_file(bucket_name, file_name2, '/tmp/' + file_name2)
    except botocore.exceptions.ClientError as e:
        print(f"Error downloading files: {e}")
        return None

    hash1 = calculate_file_hash('/tmp/' + file_name1)
    hash2 = calculate_file_hash('/tmp/' + file_name2)

    # Clean up temporary files
    import os
    os.remove('/tmp/' + file_name1)
    os.remove('/tmp/' + file_name2)

    comparison_results = {
        'timestamps': {
            'file1_last_modified': metadata1.get('LastModified'),
            'file2_last_modified': metadata2.get('LastModified')
        },
        'hash_values': {
            'file1_hash': hash1,
            'file2_hash': hash2
        },
        'hash_match': hash1 == hash2,
        'timestamp_match': metadata1.get('LastModified') == metadata2.get('LastModified')
    }

    return comparison_results


if __name__ == "__main__":
    bucket_name = 'your-bucket-name'
    file_name1 = 'file1.txt'
    file_name2 = 'file2.txt'

    comparison_results = compare_file_metadata(bucket_name, file_name1, file_name2)

    if comparison_results:
        print("Comparison Results:")
        print(f"Timestamps - File 1: {comparison_results['timestamps']['file1_last_modified']}")
        print(f"Timestamps - File 2: {comparison_results['timestamps']['file2_last_modified']}")
        print(f"Hash - File 1: {comparison_results['hash_values']['file1_hash']}")
        print(f"Hash - File 2: {comparison_results['hash_values']['file2_hash']}")
        print(f"Hash Match: {comparison_results['hash_match']}")
        print(f"Timestamp Match: {comparison_results['timestamp_match']}")
```
