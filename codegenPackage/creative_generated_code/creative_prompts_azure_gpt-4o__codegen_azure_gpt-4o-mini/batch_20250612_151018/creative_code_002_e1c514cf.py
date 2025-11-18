"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-3346--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Provide a step-by-step guide to integrate Linode Object Storage with an application using the S3-compatible API.
Generated: DETERMINISTIC_e1c514cff4927d9f
Batch ID: 20250612_151018
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://{self.region}.linodeobjects.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

class LinodeObjectStorage:
    """
    A class to interact with Linode Object Storage using the S3-compatible API.
    
    Attributes:
        access_key (str): The access key for Linode Object Storage.
        secret_key (str): The secret key for Linode Object Storage.
        region (str): The region for the Linode Object Storage.
        bucket_name (str): The name of the storage bucket.
    """
    
    def __init__(self, access_key: str, secret_key: str, region: str, bucket_name: str):
        """
        Initializes the LinodeObjectStorage class with the provided credentials and bucket name.
        
        Args:
            access_key (str): Linode Object Storage access key.
            secret_key (str): Linode Object Storage secret key.
            region (str): Region for Linode Object Storage.
            bucket_name (str): Name of the bucket to interact with.
        """
        self.access_key = access_key
        self.secret_key = secret_key
        self.region = region
        self.bucket_name = bucket_name
        
        # Initialize the S3 client
        self.s3_client = self._initialize_s3_client()
    
    def _initialize_s3_client(self):
        """Initializes the S3 client using provided credentials."""
        try:
            s3_client = boto3.client(
                's3',
                region_name=self.region,
                aws_access_key_id=self.access_key,
                aws_secret_access_key=self.secret_key,
                endpoint_url=f"https://{self.region}.linodeobjects.com"
            )
            return s3_client
        except (NoCredentialsError, PartialCredentialsError) as e:
            raise ValueError("Invalid AWS credentials provided.") from e
    
    def upload_file(self, file_path: str, object_name: str):
        """
        Uploads a file to the specified bucket in Linode Object Storage.
        
        Args:
            file_path (str): The path to the file to be uploaded.
            object_name (str): The name of the object in the bucket.
        
        Raises:
            FileNotFoundError: If the file does not exist.
            ValueError: For any issues encountered during the upload.
        """
        try:
            self.s3_client.upload_file(file_path, self.bucket_name, object_name)
        except FileNotFoundError:
            raise FileNotFoundError(f"The file '{file_path}' was not found.")
        except Exception as e:
            raise ValueError(f"Failed to upload '{file_path}' to '{self.bucket_name}': {str(e)}")
    
    def download_file(self, object_name: str, file_path: str):
        """
        Downloads a file from the specified bucket in Linode Object Storage.
        
        Args:
            object_name (str): The name of the object in the bucket.
            file_path (str): The path where the file will be saved.
        
        Raises:
            ValueError: For any issues encountered during the download.
        """
        try:
            self.s3_client.download_file(self.bucket_name, object_name, file_path)
        except Exception as e:
            raise ValueError(f"Failed to download '{object_name}' from '{self.bucket_name}': {str(e)}")
    
    def list_files(self):
        """
        Lists all the files in the specified bucket.
        
        Returns:
            list: A list of object keys in the bucket.
        
        Raises:
            ValueError: For any issues encountered while listing files.
        """
        try:
            response = self.s3_client.list_objects_v2(Bucket=self.bucket_name)
            if 'Contents' in response:
                return [obj['Key'] for obj in response['Contents']]
            else:
                return []
        except Exception as e:
            raise ValueError(f"Failed to list files in '{self.bucket_name}': {str(e)}")

# Example usage:
if __name__ == "__main__":
    ACCESS_KEY = 'your_access_key'
    SECRET_KEY = 'your_secret_key'
    REGION = 'us-east-1'
    BUCKET_NAME = 'your_bucket_name'
    
    # Create instance of LinodeObjectStorage
    linode_storage = LinodeObjectStorage(ACCESS_KEY, SECRET_KEY, REGION, BUCKET_NAME)

    # Upload a file
    linode_storage.upload_file('path/to/local/file.txt', 'uploaded_file.txt')

    # List files in the bucket
    files = linode_storage.list_files()
    print("Files in bucket:", files)

    # Download a file
    linode_storage.download_file('uploaded_file.txt', 'path/to/downloaded/file.txt')
```
