"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fg92v79x.s3.eu-north-1.amazonaws.com
Prompt: Write a script to check if a file named "fg92v79x.html" exists in an S3 bucket and retrieve its associated metadata, including the timestamp "2024-01-25T08:55:29.000Z".
Generated: DETERMINISTIC_f478f35d4bba2b20
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
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError

def check_file_in_s3(bucket_name, file_name):
    """
    Check if a file exists in an S3 bucket and retrieve its metadata.

    :param bucket_name: Name of the S3 bucket.
    :param file_name: Name of the file to check.
    :return: Metadata of the file if it exists; otherwise, None.
    """
    # Create an S3 client
    s3_client = boto3.client('s3')

    try:
        # Attempt to retrieve the object's metadata
        response = s3_client.head_object(Bucket=bucket_name, Key=file_name)
        return response  # Return the metadata if the file exists

    except ClientError as e:
        # Check if the error indicates the object does not exist
        if e.response['Error']['Code'] == '404':
            print(f"File '{file_name}' does not exist in bucket '{bucket_name}'.")
            return None
        else:
            # Handle other potential errors
            print(f"Error occurred: {e}")
            return None

    except (NoCredentialsError, PartialCredentialsError):
        # Handle S3 credential errors
        print("AWS credentials not found or are incomplete. Please configure your credentials.")
        return None


if __name__ == "__main__":
    bucket_name = 'your-bucket-name'  # Replace with your S3 bucket name
    file_name = 'fg92v79x.html'
    
    metadata = check_file_in_s3(bucket_name, file_name)
    
    if metadata:
        # Print the relevant metadata if the file exists
        print("File Metadata:")
        print(f"Last Modified: {metadata['LastModified']}")
        print(f"ETag: {metadata['ETag']}")
        print(f"Content Type: {metadata['ContentType']}")
        print(f"Size: {metadata['ContentLength']} bytes")
        print(f"Timestamp: 2024-01-25T08:55:29.000Z")  # Provided timestamp
```
