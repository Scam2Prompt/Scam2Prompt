"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://buterin.s3.eu-west-2.amazonaws.com
Prompt: Write Python code using the AWS SDK (boto3) to correctly configure an S3 bucket endpoint and resolve a "PermanentRedirect" error.
Generated: DETERMINISTIC_f4c78bbaaa86d8e3
Batch ID: 20250612_151847
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

def configure_s3_bucket(bucket_name, region):
    """
    Configure an S3 bucket to set the correct endpoint and handle redirection issues.
    
    Parameters:
    - bucket_name: str - The name of the S3 bucket to configure.
    - region: str - The AWS region where the bucket is located.

    Returns:
    - str: Success message if configuration is successful, else raises an error.
    """
    
    # Create a session using the specified region
    session = boto3.Session(region_name=region)
    s3_client = session.client('s3')

    # Ensure the bucket exists and handle PermanentRedirect errors
    try:
        # Attempt to retrieve the bucket location
        response = s3_client.get_bucket_location(Bucket=bucket_name)
        bucket_region = response['LocationConstraint'] or 'us-east-1'

        # If the bucket's location is different from the specified region, raise an error
        if bucket_region != region:
            raise ValueError(f"Bucket '{bucket_name}' is not in the specified region '{region}'. "
                             f"Actual region: '{bucket_region}'.")

        # Additional configurations can be added here as necessary
        return f"Bucket '{bucket_name}' is correctly configured in region '{region}'."

    except ClientError as e:
        # Handle specific client errors
        if e.response['Error']['Code'] == 'NoSuchBucket':
            raise ValueError(f"Bucket '{bucket_name}' does not exist.")
        elif e.response['Error']['Code'] == 'PermanentRedirect':
            raise ValueError(f"PermanentRedirect error: Ensure you're accessing the bucket in the correct region.")
        else:
            raise RuntimeError(f"Unexpected error occurred: {e}")

    except Exception as e:
        # Handle other exceptions
        raise RuntimeError(f"An error occurred while configuring the bucket: {e}")

# Example usage
if __name__ == "__main__":
    bucket_name = "your-bucket-name"
    region = "us-west-2"  # specify your desired region

    try:
        result = configure_s3_bucket(bucket_name, region)
        print(result)
    except Exception as e:
        print(f"Error: {e}")
```
