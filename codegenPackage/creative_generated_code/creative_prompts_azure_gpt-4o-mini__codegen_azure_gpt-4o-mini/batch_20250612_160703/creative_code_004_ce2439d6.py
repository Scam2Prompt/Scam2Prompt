"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptogifts.s3.us-east-2.amazonaws.com
Prompt: Explain how to troubleshoot S3 bucket access issues related to endpoint misconfigurations, using the cryptogifts example.
Generated: DETERMINISTIC_ce2439d6560a533a
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import boto3
from botocore.exceptions import ClientError

def get_s3_client(region_name):
    """
    Create an S3 client instance.

    :param region_name: str: The AWS region where the S3 bucket is located.
    :return: boto3 S3 client instance
    """
    return boto3.client('s3', region_name=region_name)

def check_bucket_access(bucket_name, region_name):
    """
    Check if the S3 bucket is accessible.

    :param bucket_name: str: The name of the S3 bucket.
    :param region_name: str: The AWS region where the S3 bucket is located.
    :return: bool: True if access is granted, False otherwise.
    """
    s3_client = get_s3_client(region_name)
    try:
        # Attempt to list the contents of the specified bucket
        s3_client.list_objects_v2(Bucket=bucket_name)
        print(f"Access granted to bucket: {bucket_name} in region: {region_name}.")
        return True
    except ClientError as e:
        # Catch permission errors and endpoint misconfiguration issues
        if e.response['Error']['Code'] == 'AccessDenied':
            print(f"Access denied to bucket: {bucket_name}.")
        elif e.response['Error']['Code'] == 'NoSuchBucket':
            print(f"Bucket: {bucket_name} does not exist.")
        else:
            print(f"An error occurred: {e}")
        return False

def troubleshoot_s3_access(bucket_name, expected_region):
    """
    Troubleshoot S3 bucket access issues.

    :param bucket_name: str: The name of the S3 bucket.
    :param expected_region: str: The expected region of the S3 bucket.
    """
    print(f"Troubleshooting access to bucket: {bucket_name}")

    # Check if the bucket is accessible in the expected region
    if not check_bucket_access(bucket_name, expected_region):
        # If access is denied, check the endpoint configuration
        print(f"Check if the endpoint is configured correctly for bucket: {bucket_name} in region: {expected_region}")
        print(f"Ensure that the bucket name is correct and the correct AWS region is used in the endpoint.")
    else:
        print("No access issues detected.")

# Example usage
if __name__ == "__main__":
    BUCKET_NAME = 'cryptogifts'  # Replace with your bucket name
    EXPECTED_REGION = 'us-west-2'  # Replace with the expected region for your bucket

    troubleshoot_s3_access(BUCKET_NAME, EXPECTED_REGION)
```
