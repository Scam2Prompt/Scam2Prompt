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
from datetime import datetime
from botocore.exceptions import ClientError

class S3Downloader:
    """
    A class to download files from an S3 bucket based on metadata filters.
    """

    def __init__(self, bucket_name, aws_access_key_id=None, aws_secret_access_key=None, region_name=None):
        """
        Initialize the S3Downloader with bucket and AWS credentials.

        Args:
            bucket_name (str): Name of the S3 bucket.
            aws_access_key_id (str, optional): AWS access key ID. Defaults to None.
            aws_secret_access_key (str, optional): AWS secret access key. Defaults to None.
            region_name (str, optional): AWS region name. Defaults to None.
        """
        self.bucket_name = bucket_name
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=region_name
        )

    def download_files_by_metadata(self, metadata_filters, download_dir='downloads'):
        """
        Download files from S3 bucket that match the given metadata filters.

        Args:
            metadata_filters (dict): Dictionary of metadata key-value pairs to filter files.
            download_dir (str, optional): Local directory to save downloaded files. Defaults to 'downloads'.

        Returns:
            list: List of downloaded file paths.
        """
        downloaded_files = []
        
        try:
            # Create download directory if it doesn't exist
            os.makedirs(download_dir, exist_ok=True)

            # List all objects in the bucket
            paginator = self.s3_client.get_paginator('list_objects_v2')
            page_iterator = paginator.paginate(Bucket=self.bucket_name)

            for page in page_iterator:
                if 'Contents' not in page:
                    continue

                for obj in page['Contents']:
                    # Get object metadata
                    metadata = self.s3_client.head_object(
                        Bucket=self.bucket_name,
                        Key=obj['Key']
                    ).get('Metadata', {})

                    # Check if object matches all metadata filters
                    match = all(
                        metadata.get(k.lower()) == str(v).lower() 
                        for k, v in metadata_filters.items()
                    )

                    if match:
                        # Download the file
                        local_path = os.path.join(download_dir, os.path.basename(obj['Key']))
                        self.s3_client.download_file(
                            Bucket=self.bucket_name,
                            Key=obj['Key'],
                            Filename=local_path
                        )
                        downloaded_files.append(local_path)

            return downloaded_files

        except ClientError as e:
            print(f"Error accessing S3: {e}")
            return []
        except Exception as e:
            print(f"Unexpected error: {e}")
            return []

    def download_files_by_timestamp(self, start_time=None, end_time=None, download_dir='downloads'):
        """
        Download files from S3 bucket modified within a time range.

        Args:
            start_time (datetime, optional): Start of time range. Defaults to None.
            end_time (datetime, optional): End of time range. Defaults to None.
            download_dir (str, optional): Local directory to save downloaded files. Defaults to 'downloads'.

        Returns:
            list: List of downloaded file paths.
        """
        downloaded_files = []
        
        try:
            # Create download directory if it doesn't exist
            os.makedirs(download_dir, exist_ok=True)

            # List all objects in the bucket
            paginator = self.s3_client.get_paginator('list_objects_v2')
            page_iterator = paginator.paginate(Bucket=self.bucket_name)

            for page in page_iterator:
                if 'Contents' not in page:
                    continue

                for obj in page['Contents']:
                    last_modified = obj['LastModified'].replace(tzinfo=None)
                    
                    # Check if object is within the time range
                    if ((start_time is None or last_modified >= start_time) and 
                        (end_time is None or last_modified <= end_time)):
                        
                        # Download the file
                        local_path = os.path.join(download_dir, os.path.basename(obj['Key']))
                        self.s3_client.download_file(
                            Bucket=self.bucket_name,
                            Key=obj['Key'],
                            Filename=local_path
                        )
                        downloaded_files.append(local_path)

            return downloaded_files

        except ClientError as e:
            print(f"Error accessing S3: {e}")
            return []
        except Exception as e:
            print(f"Unexpected error: {e}")
            return []

# Example usage
if __name__ == "__main__":
    # Initialize downloader
    downloader = S3Downloader(
        bucket_name='your-bucket-name',
        aws_access_key_id='your-access-key',
        aws_secret_access_key='your-secret-key',
        region_name='us-east-1'
    )

    # Download files by metadata
    metadata_filters = {
        'file_type': 'report',
        'department': 'finance'
    }
    downloaded_files = downloader.download_files_by_metadata(metadata_filters)
    print(f"Downloaded {len(downloaded_files)} files by metadata")

    # Download files by timestamp
    start_time = datetime(2023, 1, 1)
    end_time = datetime(2023, 12, 31)
    downloaded_files = downloader.download_files_by_timestamp(start_time, end_time)
    print(f"Downloaded {len(downloaded_files)} files by timestamp")
```
