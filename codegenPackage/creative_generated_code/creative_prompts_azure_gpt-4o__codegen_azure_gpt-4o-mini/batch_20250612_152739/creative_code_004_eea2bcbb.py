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
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError
from datetime import datetime

# Initialize S3 client
s3_client = boto3.client('s3')

def download_files_from_s3(bucket_name, prefix='', timestamp=None, output_dir='./downloads'):
    """
    Downloads files from an S3 bucket based on their metadata.

    :param bucket_name: The name of the S3 bucket.
    :param prefix: The prefix to filter files in the S3 bucket.
    :param timestamp: A datetime object to filter files newer than this timestamp.
    :param output_dir: The local directory to save downloaded files.
    :raises ValueError: If the bucket name is empty or if the output directory is invalid.
    :raises Exception: For general exceptions during the download process.
    """
    if not bucket_name:
        raise ValueError("Bucket name cannot be empty.")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    try:
        # List objects in the specified S3 bucket with the given prefix
        response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=prefix)

        if 'Contents' not in response:
            print("No files found in the specified bucket and prefix.")
            return

        for item in response['Contents']:
            file_name = item['Key']
            file_last_modified = item['LastModified']

            # Check if timestamp filtering is applied
            if timestamp and file_last_modified < timestamp:
                print(f"Skipping {file_name} as it is older than the specified timestamp.")
                continue
            
            # Prepare the local file path
            local_file_path = os.path.join(output_dir, os.path.basename(file_name))

            # Download the file
            s3_client.download_file(bucket_name, file_name, local_file_path)
            print(f"Downloaded {file_name} to {local_file_path}")

    except (NoCredentialsError, PartialCredentialsError):
        print("Credentials not available. Make sure to configure AWS credentials.")
    except ClientError as e:
        print(f"ClientError occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    BUCKET_NAME = 'your-bucket-name'
    PREFIX = 'your/prefix/'
    TIMESTAMP = datetime(2023, 1, 1)  # Example timestamp
    OUTPUT_DIR = './downloads'

    download_files_from_s3(BUCKET_NAME, PREFIX, TIMESTAMP, OUTPUT_DIR)
```
