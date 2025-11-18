"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://5mev69v8.s3.us-east-2.amazonaws.com
Prompt: Create a program to generate a report of all files in an S3 bucket, including their file size, storage class, and last modified date, in the format similar to the webpage.
Generated: DETERMINISTIC_05a01ad0591a2d88
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the Python code for the requested functionality using the `boto3` library:

```python
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
from datetime import datetime
import sys

def get_s3_bucket_report(bucket_name):
    """
    Generates a report of all files in the specified S3 bucket.
    The report includes the file name, file size (in bytes), storage class, 
    and the last modified date.

    :param bucket_name: Name of the S3 bucket.
    :return: None. Prints the report to the console.
    """
    try:
        # Create an S3 client
        s3_client = boto3.client('s3')

        # List objects in the bucket
        response = s3_client.list_objects_v2(Bucket=bucket_name)

        if 'Contents' not in response:
            print(f"The bucket '{bucket_name}' is empty or does not exist.")
            return

        # Generate report header
        print(f"Report for S3 bucket: {bucket_name}")
        print("------------------------------------------------------------")
        print(f"{'File Name':<50} {'Size (Bytes)':<15} {'Storage Class':<15} {'Last Modified':<20}")
        print("------------------------------------------------------------")

        # Iterate through each file in the bucket
        for item in response['Contents']:
            file_name = item['Key']
            file_size = item['Size']
            storage_class = item.get('StorageClass', 'STANDARD')  # Default to STANDARD if not provided
            last_modified = item['LastModified'].strftime('%Y-%m-%d %H:%M:%S')

            # Print file details
            print(f"{file_name:<50} {file_size:<15} {storage_class:<15} {last_modified:<20}")

    except NoCredentialsError:
        print("AWS credentials not found. Please configure your credentials.")
    except PartialCredentialsError:
        print("Incomplete AWS credentials. Ensure both Access Key and Secret Key are provided.")
    except s3_client.exceptions.NoSuchBucket:
        print(f"The bucket '{bucket_name}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Ensure bucket name is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <bucket_name>")
        sys.exit(1)

    bucket_name = sys.argv[1]
    get_s3_bucket_report(bucket_name)
```

### Notes:
1. Save this script as `s3_bucket_report.py`.
2. Run it using the command: `python s3_bucket_report.py <bucket_name>`.
3. Ensure the AWS credentials are properly configured using environment variables or the `~/.aws/credentials` file.
