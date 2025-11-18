"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://buterin.s3.eu-west-2.amazonaws.com
Prompt: Generate code to list all objects in an S3 bucket using boto3, ensuring the request is sent to the correct endpoint to avoid "PermanentRedirect" errors.
Generated: DETERMINISTIC_85fdaf5aa6dc0252
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
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError

def list_s3_objects(bucket_name, region_name):
    """
    Lists all objects in the specified S3 bucket.

    Args:
        bucket_name (str): Name of the S3 bucket.
        region_name (str): AWS region where the S3 bucket is located.

    Returns:
        list: A list of object keys in the bucket, or an empty list if bucket is empty.
    """
    try:
        # Create an S3 client with the specified region
        s3_client = boto3.client('s3', region_name=region_name)

        # Initialize an empty list for storing object keys
        object_keys = []

        # Use paginator to handle buckets with many objects
        paginator = s3_client.get_paginator('list_objects_v2')
        operation_parameters = {'Bucket': bucket_name}
        page_iterator = paginator.paginate(**operation_parameters)

        # Iterate through paginated results and gather object keys
        for page in page_iterator:
            if 'Contents' in page:
                for obj in page['Contents']:
                    object_keys.append(obj['Key'])

        return object_keys

    except NoCredentialsError:
        print("ERROR: No AWS credentials found. Please configure your credentials.")
    except PartialCredentialsError:
        print("ERROR: Incomplete AWS credentials. Please verify your configuration.")
    except ClientError as e:
        print(f"ERROR: Failed to list objects in bucket '{bucket_name}'. Reason: {e.response['Error']['Message']}")
    except Exception as e:
        print(f"ERROR: An unexpected error occurred. {str(e)}")

    return []


# Example usage
if __name__ == "__main__":
    # Replace with your bucket name and region
    bucket_name = "your-bucket-name"
    region_name = "your-region-name"

    objects = list_s3_objects(bucket_name, region_name)
    if objects:
        print(f"Objects in bucket '{bucket_name}':")
        for obj_key in objects:
            print(f"  - {obj_key}")
    else:
        print(f"No objects found in bucket '{bucket_name}'.")
```
