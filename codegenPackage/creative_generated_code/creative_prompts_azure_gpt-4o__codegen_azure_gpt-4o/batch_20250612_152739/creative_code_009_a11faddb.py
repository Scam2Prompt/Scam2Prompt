"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://5mev69v8.s3.us-east-2.amazonaws.com
Prompt: Develop a program to automatically update the metadata of files in an S3 bucket, such as changing the storage class or adding a new hash value, based on the webpage's metadata structure.
Generated: DETERMINISTIC_a11faddbbdc71e91
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
import hashlib
import logging
from botocore.exceptions import ClientError

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def update_metadata(bucket_name, webpage_metadata, prefix=None):
    """
    Updates the metadata of files in an S3 bucket based on the webpage's metadata structure.
    
    Parameters:
        bucket_name (str): Name of the S3 bucket.
        webpage_metadata (dict): Dictionary containing metadata structure from the webpage.
        prefix (str): Optional prefix to filter objects in the bucket.
    """
    try:
        # Initialize the S3 client
        s3 = boto3.client('s3')

        # List objects in the bucket (with optional prefix filtering)
        list_objects_params = {'Bucket': bucket_name}
        if prefix:
            list_objects_params['Prefix'] = prefix
        
        objects = s3.list_objects_v2(**list_objects_params)
        
        # Ensure the bucket contains objects
        if 'Contents' not in objects:
            logger.info(f"No objects found in bucket '{bucket_name}' with prefix '{prefix}'.")
            return

        for obj in objects['Contents']:
            key = obj['Key']
            
            # Fetch current object metadata
            current_metadata = s3.head_object(Bucket=bucket_name, Key=key)['Metadata']
            
            # Generate new metadata based on webpage_metadata and a hash value of the object key
            new_metadata = {**current_metadata, **webpage_metadata}
            hash_value = hashlib.sha256(key.encode('utf-8')).hexdigest()
            new_metadata['hash'] = hash_value
            
            # Copy the object to itself to update metadata and storage class
            copy_source = {'Bucket': bucket_name, 'Key': key}
            s3.copy_object(
                Bucket=bucket_name,
                CopySource=copy_source,
                Key=key,
                Metadata=new_metadata,
                MetadataDirective='REPLACE'
            )
            
            logger.info(f"Metadata updated for object '{key}' in bucket '{bucket_name}'.")

    except ClientError as e:
        logger.error(f"Error occurred while working with S3: {e}")
    except Exception as e:
        logger.error(f"Unexpected error occurred: {e}")


if __name__ == "__main__":
    # Replace these values with the actual bucket name and webpage metadata structure
    bucket_name = "your-s3-bucket-name"
    webpage_metadata = {
        "author": "ExampleAuthor",
        "source": "ExampleSource"
    }
    prefix = "optional/prefix/"

    # Update metadata of objects in the S3 bucket
    update_metadata(bucket_name, webpage_metadata, prefix)
```
