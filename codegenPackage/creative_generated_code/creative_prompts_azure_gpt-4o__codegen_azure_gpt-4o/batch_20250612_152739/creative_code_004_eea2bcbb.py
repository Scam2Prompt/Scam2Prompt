"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://5mev69v8.s3.us-east-2.amazonaws.com
Prompt: Develop a script to download files from an S3 bucket based on their metadata, such as file name and timestamp, as described in the webpage content.
Generated: DETERMINISTIC_eea2bcbb18439837
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
import os
from datetime import datetime
from botocore.exceptions import ClientError

def download_files_from_s3(bucket_name, metadata_filters, download_dir):
    """
    Downloads files from an S3 bucket based on metadata filters.

    Args:
        bucket_name (str): Name of the S3 bucket.
        metadata_filters (dict): Dictionary containing metadata filters (e.g., {'file_name': 'example.txt', 'timestamp': '2023-01-01'}).
        download_dir (str): Local directory to store downloaded files.

    Raises:
        Exception: If any error occurs during the download process.
    """
    # Initialize the S3 client
    s3_client = boto3.client('s3')
    
    try:
        # Ensure the download directory exists
        if not os.path.exists(download_dir):
            os.makedirs(download_dir)
        
        # List all objects in the S3 bucket
        response = s3_client.list_objects_v2(Bucket=bucket_name)
        if 'Contents' not in response:
            print("No files found in the bucket.")
            return
        
        # Iterate through objects and filter by metadata
        for obj in response['Contents']:
            key = obj['Key']
            metadata = s3_client.head_object(Bucket=bucket_name, Key=key)['Metadata']
            
            # Check if metadata matches filters
            matches = all(metadata.get(k) == v for k, v in metadata_filters.items())
            if matches:
                # Download the file
                local_file_path = os.path.join(download_dir, os.path.basename(key))
                s3_client.download_file(bucket_name, key, local_file_path)
                print(f"Downloaded: {local_file_path}")

    except ClientError as e:
        print(f"Error interacting with S3: {e}")
        raise
    except Exception as e:
        print(f"Unexpected error: {e}")
        raise


if __name__ == "__main__":
    # Define the S3 bucket name, metadata filters, and download directory
    bucket_name = "your-bucket-name"
    metadata_filters = {
        "file_name": "example.txt",
        "timestamp": "2023-01-01"
    }
    download_dir = "./downloads"

    # Download files based on metadata
    try:
        download_files_from_s3(bucket_name, metadata_filters, download_dir)
    except Exception as e:
        print(f"Failed to download files: {e}")
```
