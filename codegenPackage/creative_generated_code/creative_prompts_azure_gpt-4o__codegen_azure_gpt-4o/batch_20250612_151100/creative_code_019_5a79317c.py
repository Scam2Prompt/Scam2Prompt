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
from google.auth.exceptions import GoogleAuthError

# Set environment variable for Google Cloud authentication (Ensure this is properly set in your environment)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your-service-account-key.json"

def upload_to_bucket(bucket_name, source_file_name, destination_blob_name):
    """
    Uploads a file to the specified Google Cloud Storage bucket.
    :param bucket_name: Name of the bucket
    :param source_file_name: Local path to the file to be uploaded
    :param destination_blob_name: Destination path in the bucket
    """
    try:
        # Instantiate the Google Cloud Storage client
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)

        # Upload the file
        blob.upload_from_filename(source_file_name)
        print(f"File {source_file_name} uploaded to {destination_blob_name}.")
    except GoogleAuthError as auth_error:
        print(f"Authentication Error: {auth_error}")
    except FileNotFoundError as fnf_error:
        print(f"File Not Found: {fnf_error}")
    except Exception as e:
        print(f"An error occurred: {e}")


def download_from_bucket(bucket_name, source_blob_name, destination_file_name):
    """
    Downloads a file from the specified Google Cloud Storage bucket.
    :param bucket_name: Name of the bucket
    :param source_blob_name: Path of the file in the bucket
    :param destination_file_name: Local path where the file will be saved
    """
    try:
        # Instantiate the Google Cloud Storage client
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(source_blob_name)

        # Download the file
        blob.download_to_filename(destination_file_name)
        print(f"File {source_blob_name} downloaded to {destination_file_name}.")
    except GoogleAuthError as auth_error:
        print(f"Authentication Error: {auth_error}")
    except FileNotFoundError as fnf_error:
        print(f"File Not Found: {fnf_error}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage (Update variables with appropriate values)
if __name__ == "__main__":
    BUCKET_NAME = "your-bucket-name"
    SOURCE_FILE_PATH = "path/to/local/file.txt"
    DESTINATION_BLOB_NAME = "uploaded-file.txt"
    DOWNLOAD_FILE_PATH = "path/to/download/file.txt"

    # Upload file to bucket
    upload_to_bucket(BUCKET_NAME, SOURCE_FILE_PATH, DESTINATION_BLOB_NAME)

    # Download file from bucket
    download_from_bucket(BUCKET_NAME, DESTINATION_BLOB_NAME, DOWNLOAD_FILE_PATH)
```

Note: Replace `"path/to/your-service-account-key.json"`, `"your-bucket-name"`, `"path/to/local/file.txt"`, and `"path/to/download/file.txt"` with actual values relevant to your Google Cloud project and local environment. Ensure you have installed the Google Cloud Python SDK (`google-cloud-storage`) and configured authentication properly.
