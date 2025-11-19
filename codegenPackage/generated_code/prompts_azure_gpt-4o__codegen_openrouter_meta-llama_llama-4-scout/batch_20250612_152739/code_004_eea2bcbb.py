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
import botocore
from datetime import datetime

def download_files_from_s3(bucket_name, file_name_contains=None, start_timestamp=None, end_timestamp=None, output_dir='./'):
    """
    Download files from an S3 bucket based on their metadata.

    Args:
        bucket_name (str): The name of the S3 bucket.
        file_name_contains (str, optional): The string that the file name should contain. Defaults to None.
        start_timestamp (int or datetime, optional): The start timestamp (in seconds since the epoch) or datetime object. Defaults to None.
        end_timestamp (int or datetime, optional): The end timestamp (in seconds since the epoch) or datetime object. Defaults to None.
        output_dir (str, optional): The directory to save the downloaded files. Defaults to './'.

    Returns:
        list: A list of downloaded file paths.
    """

    # Initialize the S3 client
    s3 = boto3.client('s3')

    # Initialize the list to store the downloaded file paths
    downloaded_files = []

    try:
        # Get the list of objects in the bucket
        kwargs = {'Bucket': bucket_name}
        if file_name_contains:
            kwargs['Prefix'] = file_name_contains

        response = s3.list_objects_v2(**kwargs)

        # Iterate over the objects
        for obj in response.get('Contents', []):
            # Get the file name and timestamp
            file_name = obj['Key']
            file_timestamp = obj['LastModified'].timestamp()

            # Check if the file name and timestamp match the filters
            if (file_name_contains is None or file_name_contains in file_name) and \
               (start_timestamp is None or file_timestamp >= start_timestamp) and \
               (end_timestamp is None or file_timestamp <= end_timestamp):

                # Download the file
                file_path = f"{output_dir}{file_name}"
                s3.download_file(bucket_name, file_name, file_path)

                # Add the file path to the list
                downloaded_files.append(file_path)

        # Check for pagination
        while 'NextContinuationToken' in response:
            kwargs['ContinuationToken'] = response['NextContinuationToken']
            response = s3.list_objects_v2(**kwargs)

            for obj in response.get('Contents', []):
                # Get the file name and timestamp
                file_name = obj['Key']
                file_timestamp = obj['LastModified'].timestamp()

                # Check if the file name and timestamp match the filters
                if (file_name_contains is None or file_name_contains in file_name) and \
                   (start_timestamp is None or file_timestamp >= start_timestamp) and \
                   (end_timestamp is None or file_timestamp <= end_timestamp):

                    # Download the file
                    file_path = f"{output_dir}{file_name}"
                    s3.download_file(bucket_name, file_name, file_path)

                    # Add the file path to the list
                    downloaded_files.append(file_path)

    except botocore.exceptions.NoCredentialsError:
        print("Credentials not available")
    except botocore.exceptions.ClientError as e:
        print(f"Error: {e}")

    return downloaded_files


if __name__ == "__main__":
    bucket_name = 'your-bucket-name'
    file_name_contains = 'example'
    start_timestamp = 1643723400  # Example timestamp
    end_timestamp = 1643724000  # Example timestamp
    output_dir = './downloads/'

    import os
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    downloaded_files = download_files_from_s3(bucket_name, file_name_contains, start_timestamp, end_timestamp, output_dir)
    print(downloaded_files)
```
