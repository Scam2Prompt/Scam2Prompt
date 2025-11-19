"""
Generated Code Metadata:
========================
Original URL: https://5mev69v8.s3.us-east-2.amazonaws.com
Prompt: "Recommend APIs or libraries for managing files on Amazon S3, considering the file types and metadata provided in the given S3 bucket content."
Generated: DETERMINISTIC_c87e4fa4bf11d1cf
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import boto3
from botocore.exceptions import ClientError
from typing import List, Dict, Optional

class S3FileManager:
    """
    A class to manage files on Amazon S3 with support for handling different file types and metadata.
    Uses boto3 library for AWS S3 operations.
    """

    def __init__(self, bucket_name: str, aws_access_key_id: str = None, aws_secret_access_key: str = None, region_name: str = None):
        """
        Initialize the S3FileManager with bucket name and optional AWS credentials.
        
        Args:
            bucket_name (str): Name of the S3 bucket
            aws_access_key_id (str, optional): AWS access key ID
            aws_secret_access_key (str, optional): AWS secret access key
            region_name (str, optional): AWS region name
        """
        self.bucket_name = bucket_name
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=region_name
        )

    def list_files(self, prefix: str = '') -> List[Dict]:
        """
        List all files in the bucket with optional prefix filter.
        
        Args:
            prefix (str, optional): Prefix to filter files
            
        Returns:
            List[Dict]: List of file objects with metadata
            
        Raises:
            ClientError: If AWS S3 operation fails
        """
        try:
            response = self.s3_client.list_objects_v2(
                Bucket=self.bucket_name,
                Prefix=prefix
            )
            return response.get('Contents', [])
        except ClientError as e:
            raise e

    def upload_file(self, file_path: str, object_name: str, metadata: Optional[Dict] = None) -> bool:
        """
        Upload a file to S3 bucket with optional metadata.
        
        Args:
            file_path (str): Local file path to upload
            object_name (str): S3 object name
            metadata (Dict, optional): Metadata to attach to the file
            
        Returns:
            bool: True if upload succeeded, False otherwise
            
        Raises:
            ClientError: If AWS S3 operation fails
        """
        try:
            extra_args = {}
            if metadata:
                extra_args['Metadata'] = metadata
            
            self.s3_client.upload_file(
                file_path,
                self.bucket_name,
                object_name,
                ExtraArgs=extra_args
            )
            return True
        except ClientError as e:
            raise e

    def download_file(self, object_name: str, file_path: str) -> bool:
        """
        Download a file from S3 bucket.
        
        Args:
            object_name (str): S3 object name to download
            file_path (str): Local file path to save to
            
        Returns:
            bool: True if download succeeded, False otherwise
            
        Raises:
            ClientError: If AWS S3 operation fails
        """
        try:
            self.s3_client.download_file(
                self.bucket_name,
                object_name,
                file_path
            )
            return True
        except ClientError as e:
            raise e

    def get_file_metadata(self, object_name: str) -> Dict:
        """
        Get metadata for a specific file in S3 bucket.
        
        Args:
            object_name (str): S3 object name
            
        Returns:
            Dict: File metadata
            
        Raises:
            ClientError: If AWS S3 operation fails
        """
        try:
            response = self.s3_client.head_object(
                Bucket=self.bucket_name,
                Key=object_name
            )
            return response.get('Metadata', {})
        except ClientError as e:
            raise e

    def delete_file(self, object_name: str) -> bool:
        """
        Delete a file from S3 bucket.
        
        Args:
            object_name (str): S3 object name to delete
            
        Returns:
            bool: True if deletion succeeded, False otherwise
            
        Raises:
            ClientError: If AWS S3 operation fails
        """
        try:
            self.s3_client.delete_object(
                Bucket=self.bucket_name,
                Key=object_name
            )
            return True
        except ClientError as e:
            raise e

# Example usage
if __name__ == "__main__":
    try:
        # Initialize with your bucket name and credentials
        s3_manager = S3FileManager(
            bucket_name='your-bucket-name',
            aws_access_key_id='your-access-key',
            aws_secret_access_key='your-secret-key',
            region_name='us-west-2'
        )
        
        # List files
        files = s3_manager.list_files()
        print("Files in bucket:", files)
        
        # Upload a file with metadata
        metadata = {'file_type': 'image', 'owner': 'user1'}
        s3_manager.upload_file('local_file.txt', 'remote_file.txt', metadata)
        
        # Get file metadata
        file_metadata = s3_manager.get_file_metadata('remote_file.txt')
        print("File metadata:", file_metadata)
        
        # Download file
        s3_manager.download_file('remote_file.txt', 'downloaded_file.txt')
        
        # Delete file
        s3_manager.delete_file('remote_file.txt')
        
    except ClientError as e:
        print(f"Error occurred: {e}")
```
