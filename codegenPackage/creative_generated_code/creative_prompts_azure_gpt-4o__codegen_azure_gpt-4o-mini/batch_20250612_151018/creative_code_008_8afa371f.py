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
  "https://{region}.linodeobjects.com": {
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
import os

class LinodeS3Manager:
    """
    A class to manage file uploads and operations in Linode's S3-compatible Object Storage.
    """

    def __init__(self, access_key, secret_key, bucket_name, region):
        """
        Initializes the LinodeS3Manager with the necessary credentials and bucket information.

        :param access_key: The access key for Linode's Object Storage.
        :param secret_key: The secret key for Linode's Object Storage.
        :param bucket_name: The name of the S3 bucket to interact with.
        :param region: The region where the bucket is located.
        """
        self.access_key = access_key
        self.secret_key = secret_key
        self.bucket_name = bucket_name
        self.region = region

        # Creating a session with the given credentials
        self.session = boto3.session.Session()
        self.s3_client = self.session.client(
            's3',
            region_name=self.region,
            aws_access_key_id=self.access_key,
            aws_secret_access_key=self.secret_key,
            endpoint_url=f'https://{region}.linodeobjects.com'
        )

    def upload_file(self, file_path, object_name=None):
        """
        Uploads a file to the specified S3 bucket.

        :param file_path: The local path to the file to be uploaded.
        :param object_name: The name of the object in the S3 bucket. If None, same as file name.
        :raises FileNotFoundError: If the file does not exist.
        :raises ClientError: If there is an error during the upload.
        """
        if object_name is None:
            object_name = os.path.basename(file_path)

        try:
            self.s3_client.upload_file(file_path, self.bucket_name, object_name)
            print(f'Successfully uploaded {file_path} to {self.bucket_name}/{object_name}.')
        except FileNotFoundError:
            print(f'Error: The file {file_path} was not found.')
            raise
        except ClientError as e:
            print(f'Failed to upload {file_path}: {e}')
            raise

    def list_files(self):
        """
        Lists all files in the specified S3 bucket.

        :return: A list of object names in the bucket.
        :raises ClientError: If there is an error while listing the files.
        """
        try:
            response = self.s3_client.list_objects_v2(Bucket=self.bucket_name)
            if 'Contents' not in response:
                print('The bucket is empty.')
                return []

            file_names = [obj['Key'] for obj in response['Contents']]
            return file_names
        except ClientError as e:
            print(f'Failed to list files in bucket {self.bucket_name}: {e}')
            raise

    def delete_file(self, object_name):
        """
        Deletes a file from the specified S3 bucket.

        :param object_name: The name of the object to delete from the S3 bucket.
        :raises ClientError: If there is an error during the deletion.
        """
        try:
            response = self.s3_client.delete_object(Bucket=self.bucket_name, Key=object_name)
            if 'DeleteMarker' in response:
                print(f'Successfully deleted {object_name} from {self.bucket_name}.')
            else:
                print(f'Error: {object_name} could not be deleted.')
        except ClientError as e:
            print(f'Failed to delete {object_name}: {e}')
            raise


if __name__ == '__main__':
    # Replace with your Linode credentials and bucket information
    ACCESS_KEY = 'your_access_key'
    SECRET_KEY = 'your_secret_key'
    BUCKET_NAME = 'your_bucket_name'
    REGION = 'us-east-1'  # or your desired region

    # Create an instance of the LinodeS3Manager
    s3_manager = LinodeS3Manager(ACCESS_KEY, SECRET_KEY, BUCKET_NAME, REGION)

    # Example usage
    try:
        # Upload a file
        s3_manager.upload_file('path/to/your/file.txt')

        # List files in the bucket
        files = s3_manager.list_files()
        print(files)

        # Delete a file
        s3_manager.delete_file('file.txt')
    except (NoCredentialsError, PartialCredentialsError) as e:
        print(f'Credentials error: {e}')
```
