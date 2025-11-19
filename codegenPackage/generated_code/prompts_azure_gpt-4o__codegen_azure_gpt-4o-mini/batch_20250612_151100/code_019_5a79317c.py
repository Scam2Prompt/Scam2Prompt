"""
Generated Code Metadata:
========================
Original URL: https://aptrongurgaon.in
Prompt: Generate a Python script for cloud-based data storage and retrieval, incorporating concepts from APTRON Gurgaon’s Google Cloud training.
Generated: DETERMINISTIC_5a79317cba46a355
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from google.cloud import storage
from google.cloud.exceptions import NotFound

# Set up Google Cloud Storage client
def initialize_storage_client():
    """Initializes the Google Cloud Storage client."""
    try:
        client = storage.Client()
        return client
    except Exception as e:
        print(f"Error initializing Google Cloud Storage client: {e}")
        raise

# Upload a file to a specified bucket
def upload_file(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the specified Google Cloud Storage bucket.

    Args:
        bucket_name (str): The name of the bucket to upload to.
        source_file_name (str): The path to the file to upload.
        destination_blob_name (str): The name of the blob in the bucket.
    """
    client = initialize_storage_client()
    bucket = client.bucket(bucket_name)

    try:
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_filename(source_file_name)
        print(f"File {source_file_name} uploaded to {destination_blob_name}.")
    except Exception as e:
        print(f"Error uploading file: {e}")
        raise

# Download a file from a specified bucket
def download_file(bucket_name, source_blob_name, destination_file_name):
    """Downloads a file from the specified Google Cloud Storage bucket.

    Args:
        bucket_name (str): The name of the bucket to download from.
        source_blob_name (str): The name of the blob in the bucket.
        destination_file_name (str): The path to save the downloaded file.
    """
    client = initialize_storage_client()
    bucket = client.bucket(bucket_name)

    try:
        blob = bucket.blob(source_blob_name)
        blob.download_to_filename(destination_file_name)
        print(f"Blob {source_blob_name} downloaded to {destination_file_name}.")
    except NotFound:
        print(f"Blob {source_blob_name} not found in bucket {bucket_name}.")
    except Exception as e:
        print(f"Error downloading file: {e}")
        raise

# List all files in a specified bucket
def list_blobs(bucket_name):
    """Lists all the blobs in the specified Google Cloud Storage bucket.

    Args:
        bucket_name (str): The name of the bucket to list blobs from.
    """
    client = initialize_storage_client()
    blobs = client.list_blobs(bucket_name)

    print(f"Blobs in bucket {bucket_name}:")
    for blob in blobs:
        print(blob.name)

# Main function to demonstrate functionality
if __name__ == "__main__":
    # Set your bucket name and file paths
    BUCKET_NAME = "your-bucket-name"
    SOURCE_FILE = "path/to/your/file.txt"
    DESTINATION_BLOB = "uploaded_file.txt"
    DOWNLOAD_FILE = "path/to/downloaded/file.txt"

    # Upload a file
    upload_file(BUCKET_NAME, SOURCE_FILE, DESTINATION_BLOB)

    # List files in the bucket
    list_blobs(BUCKET_NAME)

    # Download a file
    download_file(BUCKET_NAME, DESTINATION_BLOB, DOWNLOAD_FILE)
```

Make sure to replace `"your-bucket-name"`, `"path/to/your/file.txt"`, and `"path/to/downloaded/file.txt"` with actual values before running the script. Additionally, ensure that the Google Cloud SDK is installed and properly configured with the necessary permissions to access the specified bucket.
