"""
Generated Code Metadata:
========================
Original URL: https://5mev69v8.s3.us-east-2.amazonaws.com
Prompt: Develop a script to download files from an S3 bucket based on their metadata, such as file name and timestamp, as described in the webpage content.
Generated: DETERMINISTIC_eea2bcbb18439837
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
import os
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError
from datetime import datetime

# Initialize the S3 client
s3_client = boto3.client('s3')

def download_files_from_s3(bucket_name, prefix='', file_name=None, timestamp=None, download_dir='./downloads'):
    """
    Download files from an S3 bucket based on specified metadata.

    :param bucket_name: Name of the S3 bucket
    :param prefix: Prefix to filter files in the bucket
    :param file_name: Specific file name to download (optional)
    :param timestamp: Timestamp to filter files (optional, format: 'YYYY-MM-DD HH:MM:SS')
    :param download_dir: Local directory to save downloaded files
    """
    # Ensure the download directory exists
    os.makedirs(download_dir, exist_ok=True)

    try:
        # List objects in the specified S3 bucket
        response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=prefix)

        # Check if the response contains any contents
        if 'Contents' not in response:
            print("No files found in the specified bucket and prefix.")
            return

        for obj in response['Contents']:
            # Extract file metadata
            s3_file_name = obj['Key']
            last_modified = obj['LastModified']

            # Filter by file name if specified
            if file_name and file_name not in s3_file_name:
                continue

            # Filter by timestamp if specified
            if timestamp:
                timestamp_dt = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
                if last_modified < timestamp_dt:
                    continue

            # Define the local file path
            local_file_path = os.path.join(download_dir, os.path.basename(s3_file_name))

            # Download the file
            print(f"Downloading {s3_file_name} to {local_file_path}...")
            s3_client.download_file(bucket_name, s3_file_name, local_file_path)

    except NoCredentialsError:
        print("Error: AWS credentials not found.")
    except PartialCredentialsError:
        print("Error: Incomplete AWS credentials provided.")
    except ClientError as e:
        print(f"Error: {e.response['Error']['Message']}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    download_files_from_s3(
        bucket_name='your-bucket-name',
        prefix='your/prefix/',
        file_name='specific_file.txt',
        timestamp='2023-01-01 00:00:00',
        download_dir='./downloads'
    )
```
