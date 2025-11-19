"""
Generated Code Metadata:
========================
Original URL: https://zpv2g498.s3.us-west-2.amazonaws.com
Prompt: "Write a Python script to download and save a list of files from an S3 bucket, specified by their keys and metadata, similar to those listed on this webpage."
Generated: DETERMINISTIC_27ba842128180c06
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import boto3
import os
import logging
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def download_files_from_s3(bucket_name, file_keys, download_dir):
    """
    Downloads files from an S3 bucket based on the provided keys and saves them locally.

    Args:
        bucket_name (str): Name of the S3 bucket.
        file_keys (list): List of file keys to download from the bucket.
        download_dir (str): Local directory to save the downloaded files.

    Raises:
        Exception: If any error occurs during the download process.
    """
    # Initialize the S3 client
    s3_client = boto3.client('s3')

    # Ensure the download directory exists
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    for file_key in file_keys:
        try:
            # Define the local file path
            local_file_path = os.path.join(download_dir, os.path.basename(file_key))

            # Download the file from S3
            logging.info(f"Downloading {file_key} from bucket {bucket_name}...")
            s3_client.download_file(bucket_name, file_key, local_file_path)
            logging.info(f"File {file_key} downloaded successfully to {local_file_path}")

        except NoCredentialsError:
            logging.error("AWS credentials not found. Please configure your credentials.")
            raise
        except PartialCredentialsError:
            logging.error("Incomplete AWS credentials. Please check your configuration.")
            raise
        except ClientError as e:
            logging.error(f"Failed to download {file_key}: {e}")
            raise
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            raise

if __name__ == "__main__":
    # Example usage
    try:
        # Define the S3 bucket name
        bucket_name = "your-s3-bucket-name"

        # List of file keys to download
        file_keys = [
            "path/to/file1.txt",
            "path/to/file2.jpg",
            "path/to/file3.pdf"
        ]

        # Local directory to save the downloaded files
        download_dir = "./downloads"

        # Download files
        download_files_from_s3(bucket_name, file_keys, download_dir)

    except Exception as e:
        logging.error(f"Script failed: {e}")
```
