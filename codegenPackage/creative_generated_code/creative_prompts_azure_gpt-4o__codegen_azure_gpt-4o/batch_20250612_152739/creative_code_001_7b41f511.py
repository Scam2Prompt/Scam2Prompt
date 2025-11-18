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
from botocore.exceptions import NoCredentialsError, PartialCredentialsError


def filter_files_by_storage_class(bucket_name, storage_class):
    """
    Filters files in the specified S3 bucket based on their storage class and outputs their metadata.

    Args:
        bucket_name (str): Name of the S3 bucket.
        storage_class (str): Storage class to filter files (e.g., 'STANDARD', 'GLACIER').
    
    Returns:
        list: List of dictionaries containing metadata of the filtered files.
    """
    try:
        # Initialize the S3 client
        s3_client = boto3.client('s3')

        # Get the list of objects in the bucket
        response = s3_client.list_objects_v2(Bucket=bucket_name)
        
        if 'Contents' not in response:
            print("No files found in the bucket.")
            return []

        # Filter files based on the specified storage class
        filtered_files = []
        for obj in response['Contents']:
            # Retrieve metadata for each object
            metadata = s3_client.head_object(Bucket=bucket_name, Key=obj['Key'])
            
            # Check the storage class
            if metadata.get('StorageClass', 'STANDARD') == storage_class:
                # Add relevant metadata to the list
                filtered_files.append({
                    'FileName': obj['Key'],
                    'Size': obj['Size'],
                    'LastModified': obj['LastModified'].strftime('%Y-%m-%d %H:%M:%S'),
                    'StorageClass': metadata['StorageClass']
                })

        return filtered_files

    except NoCredentialsError:
        print("Error: AWS credentials not found.")
    except PartialCredentialsError:
        print("Error: Incomplete AWS credentials provided.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Replace these with appropriate values
    BUCKET_NAME = 'your-bucket-name'
    STORAGE_CLASS = 'STANDARD'

    # Call the function and get metadata of filtered files
    metadata = filter_files_by_storage_class(BUCKET_NAME, STORAGE_CLASS)

    # Output the metadata
    if metadata:
        print("Filtered Files Metadata:")
        for file_info in metadata:
            print(file_info)
    else:
        print("No files matched the specified storage class.")
```
