"""
Generated Code Metadata:
========================
Original URL: https://buterin.s3.eu-west-2.amazonaws.com
Prompt: Generate code to list all objects in an S3 bucket using boto3, ensuring the request is sent to the correct endpoint to avoid "PermanentRedirect" errors.
Generated: DETERMINISTIC_85fdaf5aa6dc0252
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import boto3
import botocore.exceptions

def list_s3_objects(bucket_name, region=None):
    """
    List all objects in an S3 bucket while handling region-specific endpoints.

    Args:
        bucket_name (str): Name of the S3 bucket.
        region (str, optional): AWS region of the bucket. If not provided,
                               it will be determined automatically.

    Returns:
        list: A list of object keys in the bucket.

    Raises:
        botocore.exceptions.ClientError: If there's an error accessing the bucket.
        ValueError: If the bucket name is invalid.
    """
    if not bucket_name:
        raise ValueError("Bucket name cannot be empty")

    try:
        # Initialize S3 client with the specified region or auto-detect
        s3_client = boto3.client('s3', region_name=region)

        # Get bucket location to ensure correct endpoint
        if region is None:
            location = s3_client.get_bucket_location(Bucket=bucket_name)['LocationConstraint']
            # 'us-east-1' returns None, so we handle that case
            region = location if location is not None else 'us-east-1'
            s3_client = boto3.client('s3', region_name=region)

        # List all objects in the bucket
        objects = []
        paginator = s3_client.get_paginator('list_objects_v2')
        for page in paginator.paginate(Bucket=bucket_name):
            if 'Contents' in page:
                objects.extend([obj['Key'] for obj in page['Contents']])

        return objects

    except botocore.exceptions.ClientError as e:
        error_code = e.response['Error']['Code']
        if error_code == 'PermanentRedirect':
            raise ValueError(f"Bucket '{bucket_name}' is not in the specified region '{region}'. "
                           f"Please specify the correct region.") from e
        raise  # Re-raise other ClientErrors

# Example usage
if __name__ == "__main__":
    try:
        bucket_name = "your-bucket-name"
        objects = list_s3_objects(bucket_name)
        print(f"Objects in bucket '{bucket_name}':")
        for obj in objects:
            print(obj)
    except Exception as e:
        print(f"Error: {e}")
```
