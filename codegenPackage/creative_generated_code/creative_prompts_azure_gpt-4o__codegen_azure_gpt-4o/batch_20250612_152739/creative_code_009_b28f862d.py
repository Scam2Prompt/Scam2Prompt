"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fg92v79x.s3.eu-north-1.amazonaws.com
Prompt: Create a script to compare the metadata of two files in an S3 bucket, focusing on timestamps and hash values, as described in the fg92v79x.html documentation.
Generated: DETERMINISTIC_b28f862dff0503e9
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
import sys
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError

def get_file_metadata(bucket_name, file_key):
    """
    Retrieves the metadata for a given file in an S3 bucket.

    :param bucket_name: Name of the S3 bucket
    :param file_key: Key (path) of the file in the S3 bucket
    :return: Dictionary containing metadata or None if an error occurs
    """
    try:
        s3_client = boto3.client('s3')
        response = s3_client.head_object(Bucket=bucket_name, Key=file_key)
        
        # Extract relevant metadata
        metadata = {
            'LastModified': response.get('LastModified'),
            'ETag': response.get('ETag').strip('"')  # ETag is typically the hash value in quotes
        }
        return metadata
    except NoCredentialsError:
        print("Error: No AWS credentials found.")
    except PartialCredentialsError:
        print("Error: Incomplete AWS credentials.")
    except ClientError as e:
        print(f"Error accessing S3: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return None


def compare_file_metadata(bucket_name, file_key_1, file_key_2):
    """
    Compares the metadata (timestamps and hash values) of two files in an S3 bucket.

    :param bucket_name: Name of the S3 bucket
    :param file_key_1: Key of the first file in the S3 bucket
    :param file_key_2: Key of the second file in the S3 bucket
    :return: None
    """
    metadata_1 = get_file_metadata(bucket_name, file_key_1)
    metadata_2 = get_file_metadata(bucket_name, file_key_2)

    if not metadata_1 or not metadata_2:
        print("Unable to retrieve metadata for one or both files.")
        return

    print("Metadata Comparison:")
    print(f"File 1: {file_key_1}, LastModified: {metadata_1['LastModified']}, ETag: {metadata_1['ETag']}")
    print(f"File 2: {file_key_2}, LastModified: {metadata_2['LastModified']}, ETag: {metadata_2['ETag']}")

    # Compare timestamps
    if metadata_1['LastModified'] == metadata_2['LastModified']:
        print("The files have the same LastModified timestamp.")
    else:
        print("The files have different LastModified timestamps.")

    # Compare hash values
    if metadata_1['ETag'] == metadata_2['ETag']:
        print("The files have the same hash value (ETag).")
    else:
        print("The files have different hash values (ETag).")


if __name__ == "__main__":
    # Example usage: python script.py <bucket_name> <file_key_1> <file_key_2>
    if len(sys.argv) != 4:
        print("Usage: python script.py <bucket_name> <file_key_1> <file_key_2>")
        sys.exit(1)

    bucket_name = sys.argv[1]
    file_key_1 = sys.argv[2]
    file_key_2 = sys.argv[3]

    compare_file_metadata(bucket_name, file_key_1, file_key_2)
```
