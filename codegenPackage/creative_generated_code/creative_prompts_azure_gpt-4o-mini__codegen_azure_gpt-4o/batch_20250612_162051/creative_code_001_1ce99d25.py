"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arpgroupcorp.com
Prompt: Write a code snippet for a cloud migration tool that aligns with the tailored solutions offered by ARP Group Corporation.
Generated: DETERMINISTIC_1ce99d25758e0c1c
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import shutil
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

class CloudMigrationTool:
    """
    A tool to migrate local files to an S3 bucket, aligning with tailored solutions 
    offered by ARP Group Corporation.
    """

    def __init__(self, aws_access_key, aws_secret_key, bucket_name, region_name='us-east-1'):
        """
        Initializes the CloudMigrationTool with AWS credentials and bucket details.
        Args:
            aws_access_key (str): AWS access key ID.
            aws_secret_key (str): AWS secret access key.
            bucket_name (str): The name of the S3 bucket.
            region_name (str): AWS region name. Default: 'us-east-1'
        """
        self.aws_access_key = aws_access_key
        self.aws_secret_key = aws_secret_key
        self.bucket_name = bucket_name
        self.region_name = region_name
        self.s3_client = self._initialize_s3_client()

    def _initialize_s3_client(self):
        """
        Creates and returns an S3 client using provided credentials.
        Returns:
            boto3.client: S3 client instance.
        Raises:
            ValueError: If credentials are missing or invalid.
        """
        try:
            return boto3.client(
                's3',
                aws_access_key_id=self.aws_access_key,
                aws_secret_access_key=self.aws_secret_key,
                region_name=self.region_name
            )
        except (NoCredentialsError, PartialCredentialsError) as e:
            raise ValueError("Invalid AWS credentials provided.") from e

    def migrate_files_to_s3(self, local_directory):
        """
        Migrates all files from a local directory to the specified S3 bucket.
        Args:
            local_directory (str): Path to the local directory to migrate files from.
        Raises:
            ValueError: If the local directory does not exist.
        """
        if not os.path.exists(local_directory):
            raise ValueError(f"Local directory '{local_directory}' does not exist.")

        for root, _, files in os.walk(local_directory):
            for file in files:
                local_file_path = os.path.join(root, file)
                s3_key = os.path.relpath(local_file_path, local_directory)  # Preserve directory structure in S3
                
                try:
                    self._upload_file_to_s3(local_file_path, s3_key)
                except Exception as e:
                    print(f"Failed to upload '{local_file_path}' to S3: {e}")

    def _upload_file_to_s3(self, local_file_path, s3_key):
        """
        Uploads a single file to the specified S3 bucket.
        Args:
            local_file_path (str): Path to the local file.
            s3_key (str): Key for the file in the S3 bucket.
        """
        print(f"Uploading '{local_file_path}' to bucket '{self.bucket_name}' as key '{s3_key}'...")
        self.s3_client.upload_file(local_file_path, self.bucket_name, s3_key)
        print(f"Successfully uploaded '{local_file_path}' to S3.")

# Example usage:
if __name__ == "__main__":
    # Replace with your AWS credentials and S3 bucket info
    AWS_ACCESS_KEY = "your_access_key"
    AWS_SECRET_KEY = "your_secret_key"
    BUCKET_NAME = "your_bucket_name"

    # Local directory containing files to migrate
    LOCAL_DIR = "/path/to/local/directory"

    try:
        # Initialize migration tool and migrate files
        migration_tool = CloudMigrationTool(AWS_ACCESS_KEY, AWS_SECRET_KEY, BUCKET_NAME)
        migration_tool.migrate_files_to_s3(LOCAL_DIR)
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
