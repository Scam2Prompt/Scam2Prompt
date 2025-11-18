"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aptrongurgaon.in
Prompt: Generate a Python script for cloud-based data storage and retrieval, incorporating concepts from APTRON Gurgaon’s Google Cloud training.
Generated: DETERMINISTIC_5a79317cba46a355
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from google.cloud import storage
from google.cloud.exceptions import NotFound

# Set up Google Cloud Storage client
def initialize_storage_client():
    """Initializes a Google Cloud Storage client."""
    try:
        client = storage.Client()
        return client
    except Exception as e:
        raise RuntimeError("Failed to initialize Google Cloud Storage client: {}".format(e))

# Upload a file to Google Cloud Storage
def upload_file(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the specified Google Cloud Storage bucket.

    Args:
        bucket_name (str): The name of the bucket to upload the file to.
        source_file_name (str): The local path of the file to be uploaded.
        destination_blob_name (str): The name of the destination blob in the bucket.

    Raises:
        RuntimeError: If the upload process fails.
    """
    client = initialize_storage_client()
    bucket = client.bucket(bucket_name)
    
    try:
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_filename(source_file_name)
        print(f"File {source_file_name} uploaded to {destination_blob_name}.")
    except Exception as e:
        raise RuntimeError("Failed to upload file to Google Cloud Storage: {}".format(e))

# Download a file from Google Cloud Storage
def download_file(bucket_name, source_blob_name, destination_file_name):
    """Downloads a file from the specified Google Cloud Storage bucket.

    Args:
        bucket_name (str): The name of the bucket to download from.
        source_blob_name (str): The name of the blob in the bucket.
        destination_file_name (str): The local path where the file will be saved.

    Raises:
        RuntimeError: If the download process fails.
    """
    client = initialize_storage_client()
    bucket = client.bucket(bucket_name)
    
    try:
        blob = bucket.blob(source_blob_name)
        blob.download_to_filename(destination_file_name)
        print(f"Blob {source_blob_name} downloaded to {destination_file_name}.")
    except NotFound:
        raise FileNotFoundError(f"The specified blob {source_blob_name} does not exist in bucket {bucket_name}.")
    except Exception as e:
        raise RuntimeError("Failed to download file from Google Cloud Storage: {}".format(e))

# List files in a Google Cloud Storage bucket
def list_blobs(bucket_name):
    """Lists all the blobs in the specified Google Cloud Storage bucket.

    Args:
        bucket_name (str): The name of the bucket to list blobs from.
    
    Returns:
        list: A list of blob names.

    Raises:
        RuntimeError: If the listing process fails.
    """
    client = initialize_storage_client()
    blobs = []
    
    try:
        bucket = client.bucket(bucket_name)
        for blob in bucket.list_blobs():
            blobs.append(blob.name)
        return blobs
    except Exception as e:
        raise RuntimeError("Failed to list blobs in Google Cloud Storage: {}".format(e))

if __name__ == "__main__":
    # Example usage of the functions
    BUCKET_NAME = 'your-bucket-name'

    # Upload a file
    try:
        upload_file(BUCKET_NAME, 'local/path/to/file.txt', 'storage/path/to/file.txt')
    except Exception as e:
        print(e)

    # Download a file
    try:
        download_file(BUCKET_NAME, 'storage/path/to/file.txt', 'local/path/to/downloaded_file.txt')
    except Exception as e:
        print(e)

    # List blobs
    try:
        blobs = list_blobs(BUCKET_NAME)
        print("Blobs in bucket:")
        for blob in blobs:
            print(blob)
    except Exception as e:
        print(e)
```
