"""
Generated Code Metadata:
========================
Original URL: https://2e76k7pt.s3.us-east-2.amazonaws.com
Prompt: "Generate a Python code snippet to list objects in an AWS S3 bucket using the AWS SDK, assuming the bucket is located in the us-east-2 region."
Generated: DETERMINISTIC_d512b650f51fc762
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
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError

def list_s3_objects(bucket_name, region_name='us-east-2'):
    """
    Lists objects in an AWS S3 bucket.

    :param bucket_name: Name of the S3 bucket
    :param region_name: AWS region where the bucket is located (default: 'us-east-2')
    :return: List of object keys in the bucket
    """
    try:
        # Initialize the S3 client
        s3_client = boto3.client('s3', region_name=region_name)

        # Fetch the list of objects in the bucket
        response = s3_client.list_objects_v2(Bucket=bucket_name)

        # Check if the bucket contains any objects
        if 'Contents' in response:
            # Extract and return the list of object keys
            return [obj['Key'] for obj in response['Contents']]
        else:
            print(f"The bucket '{bucket_name}' is empty.")
            return []

    except NoCredentialsError:
        print("Error: No AWS credentials found. Please configure your credentials.")
    except PartialCredentialsError:
        print("Error: Incomplete AWS credentials found. Please check your configuration.")
    except ClientError as e:
        print(f"Error: Unable to access the bucket '{bucket_name}'. Details: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    # Return an empty list in case of any error
    return []

# Example usage
if __name__ == "__main__":
    bucket_name = "your-bucket-name"  # Replace with your bucket name
    objects = list_s3_objects(bucket_name)
    if objects:
        print(f"Objects in bucket '{bucket_name}':")
        for obj in objects:
            print(f" - {obj}")
```
