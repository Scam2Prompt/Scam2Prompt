"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fg92v79x.s3.eu-north-1.amazonaws.com
Prompt: Generate a script that lists all files in an S3 bucket and filters them based on a specific hash value, such as "71d4461c0a6091523478d077ec3830c51f8bbac410e96bf58c1059cf8396b094".
Generated: DETERMINISTIC_2e6e66069ae7c961
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
import botocore.exceptions

def get_s3_files_with_hash(bucket_name, hash_value):
    """
    List all files in an S3 bucket and filter them based on a specific hash value.
    
    :param bucket_name: Name of the S3 bucket
    :param hash_value: Hash value to filter the files
    :return: List of files matching the hash value
    """
    try:
        # Initialize the S3 client
        s3_client = boto3.client('s3')
        
        # Fetch the list of objects in the bucket
        response = s3_client.list_objects_v2(Bucket=bucket_name)
        
        # Ensure the response contains 'Contents' key
        if 'Contents' not in response:
            print(f"No files found in bucket '{bucket_name}'.")
            return []

        matching_files = []

        # Iterate over each object in the bucket
        for obj in response['Contents']:
            key = obj['Key']
            
            # Fetch the file content from S3
            file_obj = s3_client.get_object(Bucket=bucket_name, Key=key)
            file_content = file_obj['Body'].read()
            
            # Generate hash for file content
            file_hash = hashlib.sha256(file_content).hexdigest()
            
            # Compare generated hash with the given hash value
            if file_hash == hash_value:
                matching_files.append(key)

        return matching_files

    except botocore.exceptions.NoCredentialsError:
        print("AWS credentials not found. Please configure your credentials.")
        return []
    except botocore.exceptions.ClientError as e:
        print(f"An error occurred: {e}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

# Example usage
if __name__ == "__main__":
    bucket_name = "your-s3-bucket-name"
    hash_value = "71d4461c0a6091523478d077ec3830c51f8bbac410e96bf58c1059cf8396b094"
    
    files = get_s3_files_with_hash(bucket_name, hash_value)
    
    if files:
        print(f"Files matching hash '{hash_value}':")
        for file in files:
            print(f"- {file}")
    else:
        print(f"No files matching hash '{hash_value}' found.")
```
