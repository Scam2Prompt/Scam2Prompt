"""
Generated Code Metadata:
========================
Original URL: https://zpv2g498.s3.us-west-2.amazonaws.com
Prompt: "Generate a Python script to list all objects in an Amazon S3 bucket that match a specific naming pattern, such as 'faphanoir150 STANDARD'."
Generated: DETERMINISTIC_95e4a213f2bf92c9
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
import re
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError

def list_matching_s3_objects(bucket_name, pattern):
    """
    List all objects in an S3 bucket that match a specific naming pattern.

    Args:
        bucket_name (str): Name of the S3 bucket.
        pattern (str): Regex pattern to match object names.

    Returns:
        list: A list of matching object keys.
    """
    # Initialize the S3 client
    s3_client = boto3.client('s3')

    try:
        # Compile the regex pattern
        regex = re.compile(pattern)

        # List objects in the bucket
        matching_objects = []
        paginator = s3_client.get_paginator('list_objects_v2')
        for page in paginator.paginate(Bucket=bucket_name):
            # Check if the page contains 'Contents' (objects)
            if 'Contents' in page:
                for obj in page['Contents']:
                    key = obj['Key']
                    # Match the object key against the regex pattern
                    if regex.match(key):
                        matching_objects.append(key)

        return matching_objects

    except NoCredentialsError:
        print("Error: No AWS credentials found. Please configure your credentials.")
    except PartialCredentialsError:
        print("Error: Incomplete AWS credentials. Please check your configuration.")
    except ClientError as e:
        print(f"Error: Unable to access bucket '{bucket_name}'. Details: {e}")
    except re.error as e:
        print(f"Error: Invalid regex pattern. Details: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return []

if __name__ == "__main__":
    # Example usage
    bucket_name = "your-bucket-name"  # Replace with your S3 bucket name
    pattern = r"faphanoir150 STANDARD"  # Replace with your desired regex pattern

    matching_objects = list_matching_s3_objects(bucket_name, pattern)
    if matching_objects:
        print("Matching objects:")
        for obj in matching_objects:
            print(obj)
    else:
        print("No matching objects found.")
```
