"""
Generated Code Metadata:
========================
Original URL: https://5mev69v8.s3.us-east-2.amazonaws.com
Prompt: Write code to compare hash values of files in an S3 bucket to detect duplicates, using the hash format shown on the webpage.
Generated: DETERMINISTIC_559a0aae86dfe652
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
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def calculate_file_hash(file_content, hash_algorithm='md5'):
    """
    Calculate the hash of a file.

    Args:
        file_content (bytes): The content of the file.
        hash_algorithm (str): The algorithm to use for hashing. Defaults to 'md5'.

    Returns:
        str: The hash value of the file.
    """
    if hash_algorithm == 'md5':
        hash_object = hashlib.md5()
    elif hash_algorithm == 'sha1':
        hash_object = hashlib.sha1()
    elif hash_algorithm == 'sha256':
        hash_object = hashlib.sha256()
    else:
        raise ValueError("Invalid hash algorithm")

    hash_object.update(file_content)
    return hash_object.hexdigest()

def get_s3_file_content(s3_client, bucket_name, file_key):
    """
    Get the content of a file from an S3 bucket.

    Args:
        s3_client (boto3.client): The S3 client.
        bucket_name (str): The name of the S3 bucket.
        file_key (str): The key of the file.

    Returns:
        bytes: The content of the file.

    Raises:
        Exception: If there is an error getting the file content.
    """
    try:
        response = s3_client.get_object(Bucket=bucket_name, Key=file_key)
        return response['Body'].read()
    except Exception as e:
        logger.error(f"Error getting file content: {e}")
        raise

def compare_file_hashes_in_s3_bucket(bucket_name, hash_algorithm='md5'):
    """
    Compare the hash values of files in an S3 bucket to detect duplicates.

    Args:
        bucket_name (str): The name of the S3 bucket.
        hash_algorithm (str): The algorithm to use for hashing. Defaults to 'md5'.

    Returns:
        dict: A dictionary where the keys are the hash values and the values are lists of file keys.
    """
    s3_client = boto3.client('s3')
    file_hashes = {}

    try:
        response = s3_client.list_objects_v2(Bucket=bucket_name)
        for file in response.get('Contents', []):
            file_key = file['Key']
            file_content = get_s3_file_content(s3_client, bucket_name, file_key)
            file_hash = calculate_file_hash(file_content, hash_algorithm)

            if file_hash in file_hashes:
                file_hashes[file_hash].append(file_key)
            else:
                file_hashes[file_hash] = [file_key]

        # Get additional files if there are more than 1000 files in the bucket
        while 'NextContinuationToken' in response:
            response = s3_client.list_objects_v2(Bucket=bucket_name, ContinuationToken=response['NextContinuationToken'])
            for file in response.get('Contents', []):
                file_key = file['Key']
                file_content = get_s3_file_content(s3_client, bucket_name, file_key)
                file_hash = calculate_file_hash(file_content, hash_algorithm)

                if file_hash in file_hashes:
                    file_hashes[file_hash].append(file_key)
                else:
                    file_hashes[file_hash] = [file_key]

    except Exception as e:
        logger.error(f"Error comparing file hashes: {e}")

    # Filter out files that are not duplicates
    duplicate_hashes = {file_hash: file_keys for file_hash, file_keys in file_hashes.items() if len(file_keys) > 1}

    return duplicate_hashes

def main():
    bucket_name = 'your-bucket-name'
    duplicate_hashes = compare_file_hashes_in_s3_bucket(bucket_name)

    if duplicate_hashes:
        logger.info("Duplicate files found:")
        for file_hash, file_keys in duplicate_hashes.items():
            logger.info(f"Hash: {file_hash}, Files: {file_keys}")
    else:
        logger.info("No duplicate files found")

if __name__ == "__main__":
    main()
```
