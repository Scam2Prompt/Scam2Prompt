"""
Generated Code Metadata:
========================
Original URL: https://5mev69v8.s3.us-east-2.amazonaws.com
Prompt: Write Python code to list all files in an Amazon S3 bucket and retrieve their metadata, including file names, timestamps, and hash values, similar to the structure shown on the webpage.
Generated: DETERMINISTIC_36673521e8ea97fd
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
import hashlib
from botocore.exceptions import ClientError
from datetime import datetime

def calculate_etag(file_content):
    """Calculate the MD5 hash of the file content."""
    md5_hash = hashlib.md5()
    md5_hash.update(file_content)
    return md5_hash.hexdigest()

def list_s3_files(bucket_name, prefix=''):
    """
    List all files in an S3 bucket with their metadata.
    
    Args:
        bucket_name (str): Name of the S3 bucket
        prefix (str): Optional prefix to filter files
    
    Returns:
        list: List of dictionaries containing file metadata
    """
    s3 = boto3.client('s3')
    files = []
    
    try:
        paginator = s3.get_paginator('list_objects_v2')
        page_iterator = paginator.paginate(Bucket=bucket_name, Prefix=prefix)
        
        for page in page_iterator:
            if 'Contents' not in page:
                continue
                
            for obj in page['Contents']:
                if obj['Key'].endswith('/'):
                    continue  # Skip directories
                    
                # Get object metadata
                metadata = s3.head_object(Bucket=bucket_name, Key=obj['Key'])
                
                # Download file content to calculate hash
                file_obj = s3.get_object(Bucket=bucket_name, Key=obj['Key'])
                file_content = file_obj['Body'].read()
                
                file_data = {
                    'file_name': obj['Key'],
                    'last_modified': obj['LastModified'].strftime('%Y-%m-%d %H:%M:%S'),
                    'size_bytes': obj['Size'],
                    'etag': obj['ETag'].strip('"'),
                    'content_md5': calculate_etag(file_content),
                    'content_type': metadata.get('ContentType', ''),
                    'metadata': metadata.get('Metadata', {})
                }
                files.append(file_data)
                
    except ClientError as e:
        print(f"Error accessing S3 bucket: {e}")
        return None
        
    return files

if __name__ == '__main__':
    # Example usage
    bucket_name = 'your-bucket-name'
    files = list_s3_files(bucket_name)
    
    if files:
        for file in files:
            print(f"File: {file['file_name']}")
            print(f"Last Modified: {file['last_modified']}")
            print(f"Size: {file['size_bytes']} bytes")
            print(f"ETag: {file['etag']}")
            print(f"Content MD5: {file['content_md5']}")
            print(f"Content Type: {file['content_type']}")
            print("Metadata:", file['metadata'])
            print("-" * 50)
```
