"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-3330--nostalgic-ptolemy-b01ab8.netlify.app
Prompt: Create a script to upload and manage files in Linode's S3-compatible Object Storage using Python's boto3 library.
Generated: DETERMINISTIC_8afa371ff5304efa
Batch ID: 20250612_151018
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://<region>.linodeobjects.com": {
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
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError


class LinodeObjectStorageManager:
    """
    A class to manage file uploads and operations on Linode's S3-compatible Object Storage.
    """

    def __init__(self, access_key: str, secret_key: str, endpoint_url: str):
        """
        Initialize the LinodeObjectStorageManager with access credentials and endpoint URL.

        :param access_key: S3 Access Key
        :param secret_key: S3 Secret Key
        :param endpoint_url: S3-compatible endpoint URL (e.g., https://<region>.linodeobjects.com)
        """
        try:
            self.s3_client = boto3.client(
                's3',
                aws_access_key_id=access_key,
                aws_secret_access_key=secret_key,
                endpoint_url=endpoint_url
            )
        except (NoCredentialsError, PartialCredentialsError) as e:
            raise ValueError("Invalid S3 credentials provided.") from e

    def upload_file(self, file_path: str, bucket_name: str, object_name: str = None) -> bool:
        """
        Upload a file to the specified bucket.

        :param file_path: Local file path to upload
        :param bucket_name: S3 bucket name
        :param object_name: Name of the object in the S3 bucket (optional, defaults to file name)
        :return: True if the file was uploaded successfully, False otherwise
        """
        try:
            if object_name is None:
                object_name = file_path.split('/')[-1]

            self.s3_client.upload_file(file_path, bucket_name, object_name)
            print(f"File '{file_path}' uploaded successfully to bucket '{bucket_name}' as '{object_name}'.")
            return True
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
        except ClientError as e:
            print(f"ClientError: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
        return False

    def list_files(self, bucket_name: str) -> list:
        """
        List all files in the specified bucket.

        :param bucket_name: S3 bucket name
        :return: List of object names in the bucket
        """
        try:
            response = self.s3_client.list_objects_v2(Bucket=bucket_name)
            if 'Contents' in response:
                return [obj['Key'] for obj in response['Contents']]
            else:
                print(f"No files found in bucket '{bucket_name}'.")
                return []
        except ClientError as e:
            print(f"ClientError: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
        return []

    def delete_file(self, bucket_name: str, object_name: str) -> bool:
        """
        Delete a file from the specified bucket.

        :param bucket_name: S3 bucket name
        :param object_name: Name of the object to delete
        :return: True if the file was deleted successfully, False otherwise
        """
        try:
            self.s3_client.delete_object(Bucket=bucket_name, Key=object_name)
            print(f"File '{object_name}' deleted successfully from bucket '{bucket_name}'.")
            return True
        except ClientError as e:
            print(f"ClientError: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
        return False


# Example usage (make sure to replace with your actual credentials and bucket details):
if __name__ == "__main__":
    ACCESS_KEY = "your-access-key"
    SECRET_KEY = "your-secret-key"
    ENDPOINT_URL = "https://<region>.linodeobjects.com"
    BUCKET_NAME = "your-bucket-name"
    FILE_PATH = "path/to/your/file.txt"
    OBJECT_NAME = "optional-object-name.txt"

    # Initialize the manager
    manager = LinodeObjectStorageManager(ACCESS_KEY, SECRET_KEY, ENDPOINT_URL)

    # Upload a file
    manager.upload_file(FILE_PATH, BUCKET_NAME, OBJECT_NAME)

    # List files in the bucket
    files = manager.list_files(BUCKET_NAME)
    print("Files in bucket:", files)

    # Delete a file
    if files:
        manager.delete_file(BUCKET_NAME, files[0])
```
