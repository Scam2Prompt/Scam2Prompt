"""
Generated Code Metadata:
========================
Original URL: https://fg92v79x.s3.eu-north-1.amazonaws.com
Prompt: Create a script to compare the metadata of two files in an S3 bucket, focusing on timestamps and hash values, as described in the fg92v79x.html documentation.
Generated: DETERMINISTIC_b28f862dff0503e9
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

def calculate_file_hash(bucket_name, key, s3_client=None):
    """
    Calculate the MD5 hash of an S3 object's content.
    
    Args:
        bucket_name (str): Name of the S3 bucket
        key (str): Key of the S3 object
        s3_client: Optional boto3 S3 client
    
    Returns:
        str: MD5 hash of the file content
    """
    if s3_client is None:
        s3_client = boto3.client('s3')
    
    try:
        response = s3_client.get_object(Bucket=bucket_name, Key=key)
        file_content = response['Body'].read()
        return hashlib.md5(file_content).hexdigest()
    except ClientError as e:
        print(f"Error calculating hash for {key}: {e}")
        return None

def get_file_metadata(bucket_name, key, s3_client=None):
    """
    Retrieve metadata for an S3 object.
    
    Args:
        bucket_name (str): Name of the S3 bucket
        key (str): Key of the S3 object
        s3_client: Optional boto3 S3 client
    
    Returns:
        dict: Dictionary containing metadata including LastModified and ETag
    """
    if s3_client is None:
        s3_client = boto3.client('s3')
    
    try:
        response = s3_client.head_object(Bucket=bucket_name, Key=key)
        return {
            'LastModified': response['LastModified'],
            'ETag': response['ETag'].strip('"'),
            'Size': response['ContentLength'],
            'ContentType': response.get('ContentType', ''),
            'Metadata': response.get('Metadata', {})
        }
    except ClientError as e:
        print(f"Error retrieving metadata for {key}: {e}")
        return None

def compare_files(bucket_name, file1_key, file2_key, calculate_hashes=False):
    """
    Compare metadata of two files in an S3 bucket.
    
    Args:
        bucket_name (str): Name of the S3 bucket
        file1_key (str): Key of the first file to compare
        file2_key (str): Key of the second file to compare
        calculate_hashes (bool): Whether to calculate content hashes
    
    Returns:
        dict: Dictionary containing comparison results
    """
    s3_client = boto3.client('s3')
    
    # Get metadata for both files
    file1_meta = get_file_metadata(bucket_name, file1_key, s3_client)
    file2_meta = get_file_metadata(bucket_name, file2_key, s3_client)
    
    if not file1_meta or not file2_meta:
        return {'error': 'Failed to retrieve metadata for one or both files'}
    
    comparison = {
        'file1': file1_key,
        'file2': file2_key,
        'timestamp_match': file1_meta['LastModified'] == file2_meta['LastModified'],
        'etag_match': file1_meta['ETag'] == file2_meta['ETag'],
        'size_match': file1_meta['Size'] == file2_meta['Size'],
        'content_type_match': file1_meta['ContentType'] == file2_meta['ContentType'],
        'metadata_match': file1_meta['Metadata'] == file2_meta['Metadata'],
        'file1_metadata': file1_meta,
        'file2_metadata': file2_meta
    }
    
    if calculate_hashes:
        file1_hash = calculate_file_hash(bucket_name, file1_key, s3_client)
        file2_hash = calculate_file_hash(bucket_name, file2_key, s3_client)
        
        if file1_hash and file2_hash:
            comparison['content_hash_match'] = file1_hash == file2_hash
            comparison['file1_content_hash'] = file1_hash
            comparison['file2_content_hash'] = file2_hash
    
    return comparison

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Compare metadata of two files in an S3 bucket')
    parser.add_argument('bucket', help='S3 bucket name')
    parser.add_argument('file1', help='First file key')
    parser.add_argument('file2', help='Second file key')
    parser.add_argument('--hash', action='store_true', help='Calculate content hashes')
    
    args = parser.parse_args()
    
    result = compare_files(args.bucket, args.file1, args.file2, args.hash)
    
    print("\nComparison Results:")
    print(f"Files: {result['file1']} vs {result['file2']}")
    print(f"Timestamps match: {result['timestamp_match']}")
    print(f"ETags match: {result['etag_match']}")
    print(f"Sizes match: {result['size_match']}")
    print(f"Content types match: {result['content_type_match']}")
    print(f"Metadata match: {result['metadata_match']}")
    
    if 'content_hash_match' in result:
        print(f"Content hashes match: {result['content_hash_match']}")
        print(f"File 1 content hash: {result['file1_content_hash']}")
        print(f"File 2 content hash: {result['file2_content_hash']}")
    
    print("\nFile 1 Metadata:")
    for k, v in result['file1_metadata'].items():
        print(f"{k}: {v}")
    
    print("\nFile 2 Metadata:")
    for k, v in result['file2_metadata'].items():
        print(f"{k}: {v}")

if __name__ == '__main__':
    main()
```
