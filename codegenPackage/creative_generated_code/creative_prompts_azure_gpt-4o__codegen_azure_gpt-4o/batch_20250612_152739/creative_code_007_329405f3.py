"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://5mev69v8.s3.us-east-2.amazonaws.com
Prompt: Generate Python code to upload files to an S3 bucket and assign metadata tags, including hash values and storage class, as described in the webpage content.
Generated: DETERMINISTIC_329405f32747ecdc
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
import os
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def upload_file_to_s3(file_path, bucket_name, object_key, storage_class="STANDARD"):
    """
    Uploads a file to an S3 bucket and assigns metadata tags.
    
    Parameters:
        file_path (str): The local path to the file to be uploaded.
        bucket_name (str): The name of the S3 bucket.
        object_key (str): The key (path) for the object in the bucket.
        storage_class (str): The desired storage class for the object (default: STANDARD).
    
    Returns:
        None: Prints success or failure messages.
    """
    try:
        # Create an S3 client
        s3_client = boto3.client('s3')
        
        # Calculate the hash value of the file
        hash_value = calculate_file_hash(file_path)
        
        # Metadata tags to assign
        metadata = {
            "file-hash": hash_value,
            "storage-class": storage_class
        }
        
        # Upload the file to S3 with metadata and specified storage class
        s3_client.upload_file(
            Filename=file_path,
            Bucket=bucket_name,
            Key=object_key,
            ExtraArgs={
                "StorageClass": storage_class,  # Set storage class
                "Metadata": metadata            # Add custom metadata tags
            }
        )
        
        print(f"File '{file_path}' successfully uploaded to bucket '{bucket_name}' with key '{object_key}'.")
        
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except NoCredentialsError:
        print("Error: AWS credentials not found.")
    except PartialCredentialsError:
        print("Error: AWS credentials are incomplete.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")


def calculate_file_hash(file_path):
    """
    Calculates the SHA256 hash of a file.
    
    Parameters:
        file_path (str): The local path to the file.
    
    Returns:
        str: The hexadecimal SHA256 hash value of the file.
    """
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            # Read the file in chunks to avoid memory issues with large files
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        raise FileNotFoundError(f"Cannot calculate hash: File '{file_path}' not found.")
    except Exception as e:
        raise Exception(f"Error calculating hash: {str(e)}")


# Example usage:
if __name__ == "__main__":
    file_path = "example.txt"  # Local file to upload
    bucket_name = "my-example-bucket"  # Your S3 bucket name
    object_key = "uploads/example.txt"  # Path in the bucket
    storage_class = "STANDARD_IA"  # Choose storage class
    
    upload_file_to_s3(file_path, bucket_name, object_key, storage_class)
```
