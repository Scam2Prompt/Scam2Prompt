"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fg92v79x.s3.eu-north-1.amazonaws.com
Prompt: Create a program that scans an S3 bucket for files with the "STANDARD" storage class and logs their metadata, including timestamps and hash values.
Generated: DETERMINISTIC_6480329c10f97ae1
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import boto3
import logging
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("s3_files_metadata.log"),
        logging.StreamHandler()
    ]
)

def initialize_s3_client():
    """
    Initializes and returns an S3 client using boto3.
    """
    try:
        return boto3.client("s3")
    except NoCredentialsError:
        logging.error("No AWS credentials found. Ensure they are properly configured.")
        raise
    except PartialCredentialsError:
        logging.error("Incomplete AWS credentials provided.")
        raise
    except Exception as e:
        logging.error(f"Error initializing S3 client: {str(e)}")
        raise

def scan_s3_bucket(bucket_name):
    """
    Scans an S3 bucket for objects with the "STANDARD" storage class
    and logs their metadata including timestamps and hash values.

    :param bucket_name: Name of the S3 bucket to scan.
    """
    try:
        s3_client = initialize_s3_client()
        
        # Paginate through bucket contents
        paginator = s3_client.get_paginator("list_objects_v2")
        response_iterator = paginator.paginate(Bucket=bucket_name)

        for page in response_iterator:
            if "Contents" not in page:
                logging.info(f"No files found in bucket: {bucket_name}")
                continue

            for obj in page["Contents"]:
                # Fetch object metadata
                key = obj["Key"]

                try:
                    # Get metadata of the object
                    metadata = s3_client.head_object(Bucket=bucket_name, Key=key)
                    
                    # Check for the STANDARD storage class
                    if metadata.get("StorageClass", "STANDARD") == "STANDARD":
                        logging.info(f"File: {key}")
                        logging.info(f"  Last Modified: {obj['LastModified']}")
                        logging.info(f"  ETag (MD5 Hash): {metadata['ETag']}")
                        logging.info(f"  Size: {obj['Size']} bytes")
                except ClientError as e:
                    logging.error(f"Error retrieving metadata for {key}: {str(e)}")
                    continue
    except ClientError as e:
        logging.error(f"Error accessing bucket {bucket_name}: {str(e)}")
        raise
    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")
        raise

def main():
    """
    Main entry point of the program. Change the bucket_name to your target bucket name.
    """
    bucket_name = "your-bucket-name"  # Replace with your bucket name
    
    try:
        logging.info(f"Starting scan for bucket: {bucket_name}")
        scan_s3_bucket(bucket_name)
        logging.info(f"Scan completed for bucket: {bucket_name}")
    except Exception as e:
        logging.error(f"Failed to complete scan: {str(e)}")

if __name__ == "__main__":
    main()
```
