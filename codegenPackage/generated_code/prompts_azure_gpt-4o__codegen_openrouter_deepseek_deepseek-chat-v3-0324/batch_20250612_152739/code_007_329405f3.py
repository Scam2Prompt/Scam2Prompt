"""
Generated Code Metadata:
========================
Original URL: https://5mev69v8.s3.us-east-2.amazonaws.com
Prompt: Generate Python code to upload files to an S3 bucket and assign metadata tags, including hash values and storage class, as described in the webpage content.
Generated: DETERMINISTIC_329405f32747ecdc
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
import os
from botocore.exceptions import ClientError

class S3Uploader:
    """
    A class to handle file uploads to Amazon S3 with metadata and tags.
    """

    def __init__(self, aws_access_key_id=None, aws_secret_access_key=None, region_name=None):
        """
        Initialize the S3 client with optional credentials and region.
        If no credentials are provided, the client will use the default AWS configuration.
        """
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=region_name
        )

    def calculate_file_hash(self, file_path, hash_algorithm='sha256'):
        """
        Calculate the hash of a file using the specified algorithm.
        """
        hash_obj = hashlib.new(hash_algorithm)
        with open(file_path, 'rb') as file:
            for chunk in iter(lambda: file.read(4096), b''):
                hash_obj.update(chunk)
        return hash_obj.hexdigest()

    def upload_file_to_s3(
        self,
        file_path,
        bucket_name,
        object_name=None,
        storage_class='STANDARD',
        metadata=None,
        tags=None
    ):
        """
        Upload a file to an S3 bucket with metadata and tags.

        :param file_path: Path to the file to upload
        :param bucket_name: Name of the S3 bucket
        :param object_name: S3 object name. If not specified, file_path is used
        :param storage_class: Storage class for the object (e.g., STANDARD, INTELLIGENT_TIERING)
        :param metadata: Dictionary of metadata to attach to the object
        :param tags: Dictionary of tags to attach to the object
        :return: True if file was uploaded, else False
        """
        try:
            # If object_name was not specified, use the file name
            if object_name is None:
                object_name = os.path.basename(file_path)

            # Calculate file hashes
            md5_hash = self.calculate_file_hash(file_path, 'md5')
            sha256_hash = self.calculate_file_hash(file_path, 'sha256')

            # Prepare metadata
            if metadata is None:
                metadata = {}
            metadata.update({
                'md5': md5_hash,
                'sha256': sha256_hash
            })

            # Prepare tags
            if tags is None:
                tags = {}
            tags.update({
                'md5': md5_hash,
                'sha256': sha256_hash
            })

            # Convert tags to the format expected by S3
            tag_set = [{'Key': k, 'Value': v} for k, v in tags.items()]
            tag_string = '&'.join([f"{k}={v}" for k, v in tags.items()])

            # Upload the file
            extra_args = {
                'Metadata': metadata,
                'StorageClass': storage_class,
                'Tagging': tag_string
            }

            self.s3_client.upload_file(
                file_path,
                bucket_name,
                object_name,
                ExtraArgs=extra_args
            )

            return True

        except ClientError as e:
            print(f"Error uploading file to S3: {e}")
            return False
        except Exception as e:
            print(f"Unexpected error: {e}")
            return False

# Example usage
if __name__ == "__main__":
    # Initialize the uploader (uses default AWS credentials if none provided)
    uploader = S3Uploader()

    # Example file upload
    success = uploader.upload_file_to_s3(
        file_path='example.txt',
        bucket_name='your-bucket-name',
        object_name='uploaded_example.txt',
        storage_class='INTELLIGENT_TIERING',
        metadata={'author': 'John Doe', 'description': 'Sample file'},
        tags={'environment': 'production', 'department': 'IT'}
    )

    if success:
        print("File uploaded successfully")
    else:
        print("File upload failed")
```
