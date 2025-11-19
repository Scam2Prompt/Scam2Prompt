"""
Generated Code Metadata:
========================
Original URL: https://cryptogifts.s3.us-east-2.amazonaws.com
Prompt: Explain how to troubleshoot S3 bucket access issues related to endpoint misconfigurations, using the cryptogifts example.
Generated: DETERMINISTIC_ce2439d6560a533a
Batch ID: 20250612_160703
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

def troubleshoot_s3_access(bucket_name, region_name):
    """
    Troubleshoot S3 bucket access issues related to endpoint misconfigurations.

    Parameters:
    - bucket_name: str - The name of the S3 bucket to troubleshoot.
    - region_name: str - The AWS region where the S3 bucket is located.

    Returns:
    - None
    """
    # Create a session using the specified region
    session = boto3.Session(region_name=region_name)
    
    # Create an S3 client
    s3_client = session.client('s3')

    try:
        # Attempt to retrieve the bucket location
        response = s3_client.get_bucket_location(Bucket=bucket_name)
        print(f"Bucket '{bucket_name}' is located in region: {response['LocationConstraint']}")
        
        # Check if the region matches the expected region
        if response['LocationConstraint'] != region_name:
            print(f"Warning: The bucket is in region '{response['LocationConstraint']}', "
                  f"but you are trying to access it in region '{region_name}'.")
            print("Ensure you are using the correct endpoint for the bucket's region.")
        
        # Attempt to list objects in the bucket
        objects = s3_client.list_objects_v2(Bucket=bucket_name)
        if 'Contents' in objects:
            print(f"Objects in bucket '{bucket_name}':")
            for obj in objects['Contents']:
                print(f" - {obj['Key']}")
        else:
            print(f"No objects found in bucket '{bucket_name}'.")

    except ClientError as e:
        # Handle specific S3 errors
        if e.response['Error']['Code'] == 'NoSuchBucket':
            print(f"Error: The bucket '{bucket_name}' does not exist.")
        elif e.response['Error']['Code'] == 'AccessDenied':
            print(f"Error: Access denied to bucket '{bucket_name}'. Check your permissions.")
        else:
            print(f"Unexpected error: {e.response['Error']['Message']}")

    except Exception as e:
        # Handle any other exceptions
        print(f"An error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Replace with your S3 bucket name and region
    bucket_name = 'cryptogifts'
    region_name = 'us-west-2'  # Example region
    troubleshoot_s3_access(bucket_name, region_name)
```
