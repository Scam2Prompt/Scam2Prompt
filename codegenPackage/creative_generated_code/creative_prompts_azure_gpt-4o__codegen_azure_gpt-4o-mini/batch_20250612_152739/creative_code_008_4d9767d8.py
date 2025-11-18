"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://5mev69v8.s3.us-east-2.amazonaws.com
Prompt: Write a script to convert S3 file metadata into a CSV file, including columns for file name, timestamp, hash value, and storage class.
Generated: DETERMINISTIC_4d9767d8dba3b8a0
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
import csv
import os
from botocore.exceptions import ClientError

def fetch_s3_file_metadata(bucket_name):
    """
    Fetches metadata for all objects in the specified S3 bucket.

    Args:
        bucket_name (str): The name of the S3 bucket.

    Returns:
        list: A list of dictionaries containing file metadata.
    """
    s3_client = boto3.client('s3')
    file_metadata = []

    try:
        # Paginate through all objects in the bucket
        paginator = s3_client.get_paginator('list_objects_v2')
        for page in paginator.paginate(Bucket=bucket_name):
            if 'Contents' in page:
                for obj in page['Contents']:
                    file_metadata.append({
                        'file_name': obj['Key'],
                        'last_modified': obj['LastModified'].isoformat(),
                        'e_tag': obj['ETag'].strip('"'),  # Remove quotes around ETag
                        'storage_class': obj['StorageClass']
                    })
    except ClientError as e:
        print(f"Error fetching metadata: {e}")
    
    return file_metadata

def write_metadata_to_csv(metadata, output_file):
    """
    Writes the provided metadata to a CSV file.

    Args:
        metadata (list): List of dictionaries containing file metadata.
        output_file (str): Path to the output CSV file.
    """
    try:
        # Define the CSV column names
        fieldnames = ['file_name', 'last_modified', 'e_tag', 'storage_class']
        
        # Write metadata to CSV
        with open(output_file, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(metadata)
        print(f"Metadata successfully written to {output_file}")
    except IOError as e:
        print(f"Error writing to CSV file: {e}")

def main():
    # Set your S3 bucket name and output CSV file path
    bucket_name = 'your-s3-bucket-name'
    output_file = 's3_file_metadata.csv'

    # Fetch S3 file metadata
    metadata = fetch_s3_file_metadata(bucket_name)
    
    # Check if metadata is not empty before writing to CSV
    if metadata:
        write_metadata_to_csv(metadata, output_file)
    else:
        print("No metadata found to write.")

if __name__ == "__main__":
    main()
```
