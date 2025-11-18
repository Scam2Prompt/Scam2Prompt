"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://5mev69v8.s3.us-east-2.amazonaws.com
Prompt: Write Python code to list all files in an Amazon S3 bucket and retrieve their metadata, including file names, timestamps, and hash values, similar to the structure shown on the webpage.
Generated: DETERMINISTIC_36673521e8ea97fd
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

def list_s3_files_with_metadata(bucket_name):
    """
    Lists all files in an S3 bucket along with their metadata.
    
    Args:
        bucket_name (str): The name of the S3 bucket.
    
    Returns:
        list of dict: A list of dictionaries containing file metadata (file name, last modified timestamp, and hash value).
    """
    try:
        # Initialize S3 client
        s3_client = boto3.client('s3')

        # Fetch all objects in the bucket
        response = s3_client.list_objects_v2(Bucket=bucket_name)

        # Check if the bucket is empty
        if 'Contents' not in response:
            print(f"The bucket '{bucket_name}' is empty.")
            return []

        # List to store file metadata
        file_metadata_list = []

        # Iterate through each object in the bucket
        for obj in response['Contents']:
            file_metadata = {
                'FileName': obj['Key'],                       # The name of the file
                'LastModified': obj['LastModified'],          # Timestamp of last modification
                'HashValue': obj['ETag'].strip('"')           # The ETag (hash value) of the file
            }
            file_metadata_list.append(file_metadata)

        return file_metadata_list

    except NoCredentialsError:
        print("Error: No AWS credentials were provided.")
    except PartialCredentialsError:
        print("Error: Incomplete AWS credentials were provided.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

# Example usage:
if __name__ == "__main__":
    bucket_name = "your-bucket-name"  # Replace with your S3 bucket name
    files = list_s3_files_with_metadata(bucket_name)
    for file in files:
        print(file)
```

Note:
- Ensure that AWS credentials are properly configured in your environment (via `~/.aws/credentials` or environment variables).
- Replace `"your-bucket-name"` with the actual name of your S3 bucket.
