"""
Generated Code Metadata:
========================
Original URL: https://5mev69v8.s3.us-east-2.amazonaws.com
Prompt: Write a script to convert S3 file metadata into a CSV file, including columns for file name, timestamp, hash value, and storage class.
Generated: DETERMINISTIC_4d9767d8dba3b8a0
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
import csv
import logging
from datetime import datetime
from botocore.exceptions import ClientError

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_s3_file_metadata(bucket_name, prefix=''):
    """
    Retrieve metadata for files in an S3 bucket.
    
    Args:
        bucket_name (str): Name of the S3 bucket
        prefix (str): Optional prefix to filter files
    
    Returns:
        list: List of dictionaries containing file metadata
    """
    s3 = boto3.client('s3')
    file_metadata = []
    
    try:
        paginator = s3.get_paginator('list_objects_v2')
        page_iterator = paginator.paginate(Bucket=bucket_name, Prefix=prefix)
        
        for page in page_iterator:
            if 'Contents' not in page:
                continue
                
            for obj in page['Contents']:
                # Get additional metadata including storage class
                head_object = s3.head_object(Bucket=bucket_name, Key=obj['Key'])
                
                metadata = {
                    'file_name': obj['Key'],
                    'timestamp': obj['LastModified'].isoformat(),
                    'size_bytes': obj['Size'],
                    'storage_class': obj.get('StorageClass', 'STANDARD'),
                    'etag': head_object['ETag'].strip('"'),
                    'content_type': head_object.get('ContentType', ''),
                }
                file_metadata.append(metadata)
                
    except ClientError as e:
        logger.error(f"Error accessing S3 bucket {bucket_name}: {e}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise
        
    return file_metadata

def write_metadata_to_csv(metadata_list, output_file):
    """
    Write file metadata to a CSV file.
    
    Args:
        metadata_list (list): List of file metadata dictionaries
        output_file (str): Path to output CSV file
    """
    if not metadata_list:
        logger.warning("No metadata to write to CSV")
        return
        
    fieldnames = ['file_name', 'timestamp', 'size_bytes', 'storage_class', 'etag', 'content_type']
    
    try:
        with open(output_file, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(metadata_list)
        logger.info(f"Successfully wrote metadata to {output_file}")
    except IOError as e:
        logger.error(f"Error writing to CSV file {output_file}: {e}")
        raise

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Convert S3 file metadata to CSV')
    parser.add_argument('--bucket', required=True, help='S3 bucket name')
    parser.add_argument('--prefix', default='', help='Optional prefix filter')
    parser.add_argument('--output', default='s3_metadata.csv', help='Output CSV file path')
    
    args = parser.parse_args()
    
    try:
        metadata = get_s3_file_metadata(args.bucket, args.prefix)
        write_metadata_to_csv(metadata, args.output)
    except Exception as e:
        logger.error(f"Script failed: {e}")
        exit(1)

if __name__ == '__main__':
    main()
```
