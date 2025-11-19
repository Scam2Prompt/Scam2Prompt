"""
Generated Code Metadata:
========================
Original URL: https://5mev69v8.s3.us-east-2.amazonaws.com
Prompt: Generate a script to filter files in an S3 bucket based on their storage class, such as "STANDARD," and output their metadata in the format provided on the webpage.
Generated: DETERMINISTIC_7b41f5115e9a18ee
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
import json
from botocore.exceptions import ClientError

def filter_s3_files_by_storage_class(bucket_name, storage_class="STANDARD"):
    """
    Filters files in an S3 bucket based on their storage class and outputs their metadata.
    
    Args:
        bucket_name (str): Name of the S3 bucket to filter files from.
        storage_class (str, optional): Storage class to filter by. Defaults to "STANDARD".
    
    Returns:
        list: A list of dictionaries containing metadata of filtered files.
    """
    s3 = boto3.client('s3')
    filtered_files = []
    
    try:
        # List all objects in the bucket
        paginator = s3.get_paginator('list_objects_v2')
        page_iterator = paginator.paginate(Bucket=bucket_name)
        
        for page in page_iterator:
            if "Contents" in page:
                for obj in page["Contents"]:
                    if obj.get("StorageClass", "").upper() == storage_class.upper():
                        # Extract relevant metadata
                        file_metadata = {
                            "Key": obj["Key"],
                            "LastModified": obj["LastModified"].isoformat(),
                            "Size": obj["Size"],
                            "StorageClass": obj.get("StorageClass", "STANDARD"),
                            "ETag": obj["ETag"]
                        }
                        filtered_files.append(file_metadata)
        
        return filtered_files
    
    except ClientError as e:
        print(f"Error accessing S3 bucket: {e}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

def main():
    # Example usage
    bucket_name = "your-bucket-name"
    storage_class = "STANDARD"
    
    filtered_files = filter_s3_files_by_storage_class(bucket_name, storage_class)
    
    # Output the metadata in JSON format
    print(json.dumps(filtered_files, indent=2))

if __name__ == "__main__":
    main()
```
