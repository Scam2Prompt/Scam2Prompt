"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imts.com.pk
Prompt: Write a script to integrate a business's infrastructure with cloud platforms like AWS, Azure, and Google Cloud, following the cloud integration services mentioned on the IMTS website.
Generated: DETERMINISTIC_49b54ba44192d03e
Batch ID: 20250612_154344
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import boto3
from google.cloud import storage as gcs
from azure.storage.blob import BlobServiceClient
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

class CloudIntegration:
    def __init__(self, aws_access_key, aws_secret_key, azure_connection_string, gcp_project):
        # Initialize AWS S3 client
        self.aws_s3 = boto3.client(
            's3',
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key
        )
        
        # Initialize Azure Blob Service client
        self.azure_blob_service = BlobServiceClient.from_connection_string(azure_connection_string)
        
        # Initialize Google Cloud Storage client
        self.gcp_storage_client = gcs.Client(project=gcp_project)

    def upload_to_aws(self, file_name, bucket):
        """Upload a file to an AWS S3 bucket."""
        try:
            self.aws_s3.upload_file(file_name, bucket, file_name)
            logging.info(f'Successfully uploaded {file_name} to AWS S3 bucket {bucket}.')
        except Exception as e:
            logging.error(f'Failed to upload {file_name} to AWS S3: {e}')

    def upload_to_azure(self, file_name, container_name):
        """Upload a file to an Azure Blob Storage container."""
        try:
            blob_client = self.azure_blob_service.get_blob_client(container=container_name, blob=file_name)
            with open(file_name, "rb") as data:
                blob_client.upload_blob(data)
            logging.info(f'Successfully uploaded {file_name} to Azure container {container_name}.')
        except Exception as e:
            logging.error(f'Failed to upload {file_name} to Azure Blob Storage: {e}')

    def upload_to_gcp(self, file_name, bucket_name):
        """Upload a file to a Google Cloud Storage bucket."""
        try:
            bucket = self.gcp_storage_client.bucket(bucket_name)
            blob = bucket.blob(file_name)
            blob.upload_from_filename(file_name)
            logging.info(f'Successfully uploaded {file_name} to Google Cloud Storage bucket {bucket_name}.')
        except Exception as e:
            logging.error(f'Failed to upload {file_name} to Google Cloud Storage: {e}')

# Example usage
if __name__ == "__main__":
    # Replace these with your actual credentials and bucket/container names
    AWS_ACCESS_KEY = 'your_aws_access_key'
    AWS_SECRET_KEY = 'your_aws_secret_key'
    AZURE_CONNECTION_STRING = 'your_azure_connection_string'
    GCP_PROJECT = 'your_gcp_project'
    
    # Initialize the Cloud Integration with credentials
    cloud_integration = CloudIntegration(AWS_ACCESS_KEY, AWS_SECRET_KEY, AZURE_CONNECTION_STRING, GCP_PROJECT)
    
    # Upload files to respective cloud platforms
    cloud_integration.upload_to_aws('example_file.txt', 'your_aws_bucket')
    cloud_integration.upload_to_azure('example_file.txt', 'your_azure_container')
    cloud_integration.upload_to_gcp('example_file.txt', 'your_gcp_bucket')
```
