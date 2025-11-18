"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://5mev69v8.s3.us-east-2.amazonaws.com
Prompt: Generate a script to filter files in an S3 bucket based on their storage class, such as "STANDARD," and output their metadata in the format provided on the webpage.
Generated: DETERMINISTIC_7b41f5115e9a18ee
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def filter_s3_files_by_storage_class(bucket_name, storage_class):
    """
    Filters files in an S3 bucket based on their storage class.

    :param bucket_name: Name of the S3 bucket to filter files from
    :param storage_class: Storage class to filter by (e.g., 'STANDARD')
    :return: List of dictionaries containing metadata for each filtered file
    """
    # Initialize a session using Boto3
    s3_client = boto3.client('s3')

    # Initialize a list to hold the filtered metadata
    filtered_files_metadata = []

    try:
        # List objects in the specified S3 bucket
        paginator = s3_client.get_paginator('list_objects_v2')
        for page in paginator.paginate(Bucket=bucket_name):
            for obj in page.get('Contents', []):
                # Check if the object's storage class matches the specified class
                if obj.get('StorageClass') == storage_class:
                    # Create a dictionary to hold the metadata
                    file_metadata = {
                        'Key': obj['Key'],
                        'LastModified': obj['LastModified'].isoformat(),
                        'Size': obj['Size'],
                        'StorageClass': obj['StorageClass'],
                    }
                    # Append the metadata to the list
                    filtered_files_metadata.append(file_metadata)

        # Log the number of files found
        logger.info(f"Found {len(filtered_files_metadata)} files with storage class '{storage_class}' in bucket '{bucket_name}'.")
        
    except Exception as e:
        logger.error(f"Error retrieving files from bucket '{bucket_name}': {e}")
        return []

    return filtered_files_metadata

def main():
    # Define the S3 bucket name and the storage class to filter by
    bucket_name = 'your-bucket-name'  # Replace with your S3 bucket name
    storage_class = 'STANDARD'          # Replace with desired storage class

    # Call the function to filter files and retrieve their metadata
    filtered_files = filter_s3_files_by_storage_class(bucket_name, storage_class)

    # Print the filtered file metadata
    for file in filtered_files:
        print(file)

if __name__ == "__main__":
    main()
```
