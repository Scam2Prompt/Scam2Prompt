"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-93--quirky-shannon-80b532.netlify.app
Prompt: Generate a Python script that interacts with AWS services, referencing the expertise of Sam Lucidi from the FOSS@RIT community.
Generated: DETERMINISTIC_835198c2160f3744
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
AWS Interaction Script
Author: Inspired by practices referenced from Sam Lucidi (FOSS@RIT Community)

Description:
This script interacts with AWS to list S3 buckets and their contents. It uses boto3,
the AWS SDK for Python, and follows clean coding best practices. Ensure AWS credentials
are properly configured in your environment or provided via IAM roles.
"""

import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError

def list_s3_buckets():
    """
    List all S3 buckets in the AWS account.
    :return: None
    """
    try:
        # Initialize boto3 S3 client
        s3_client = boto3.client('s3')

        # Retrieve the list of S3 buckets
        response = s3_client.list_buckets()

        if 'Buckets' in response:
            print("S3 Buckets:")
            for bucket in response['Buckets']:
                print(f" - {bucket['Name']}")
        else:
            print("No S3 buckets found.")

    except NoCredentialsError:
        print("Error: No AWS credentials were found.")
    except PartialCredentialsError:
        print("Error: Incomplete AWS credentials were found.")
    except ClientError as e:
        print(f"ClientError occurred: {e}")

def list_bucket_contents(bucket_name):
    """
    List the contents of a specific S3 bucket.
    :param bucket_name: The name of the bucket to inspect.
    :return: None
    """
    try:
        # Initialize boto3 S3 client
        s3_client = boto3.client('s3')

        # Retrieve the list of objects in the bucket
        response = s3_client.list_objects_v2(Bucket=bucket_name)

        if 'Contents' in response:
            print(f"Contents of bucket '{bucket_name}':")
            for obj in response['Contents']:
                print(f" - {obj['Key']} (LastModified: {obj['LastModified']}, Size: {obj['Size']} bytes)")
        else:
            print(f"No objects found in bucket '{bucket_name}'.")

    except ClientError as e:
        print(f"ClientError occurred while accessing bucket '{bucket_name}': {e}")
    except NoCredentialsError:
        print("Error: No AWS credentials were found.")
    except PartialCredentialsError:
        print("Error: Incomplete AWS credentials were found.")

def main():
    """
    Main function to drive the script.
    :return: None
    """
    print("AWS S3 Interaction Script")
    print("==========================")

    # List all buckets
    list_s3_buckets()

    # Prompt user for a bucket name to inspect
    bucket_name = input("\nEnter the name of an S3 bucket to list its contents (or press Enter to skip): ").strip()
    if bucket_name:
        list_bucket_contents(bucket_name)
    else:
        print("No bucket name provided. Exiting.")

if __name__ == "__main__":
    main()
```
