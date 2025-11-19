"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptogifts.s3.us-east-2.amazonaws.com
Prompt: Write a Python script that uploads files to an S3 bucket and ensures requests are directed to the correct endpoint as indicated in the error message.
Generated: DETERMINISTIC_e746fc0b8a28c35c
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
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError
import os


def upload_file_to_s3(file_path, bucket_name, object_name=None, region_name="us-east-1"):
    """
    Uploads a file to an S3 bucket.

    :param file_path: Path to the file on the local file system.
    :param bucket_name: Name of the target S3 bucket.
    :param object_name: Key name for the object in the S3 bucket. Defaults to the filename.
    :param region_name: AWS region for the S3 bucket. Defaults to 'us-east-1'.
    :return: True if file upload was successful, False otherwise.
    """
    # Set object_name to file name if not provided
    if object_name is None:
        object_name = os.path.basename(file_path)

    try:
        # Create an S3 client with the specified region
        s3_client = boto3.client('s3', region_name=region_name)
        
        # Upload the file
        s3_client.upload_file(file_path, bucket_name, object_name)
        print(f"File '{file_path}' successfully uploaded to '{bucket_name}/{object_name}'")
        return True

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except NoCredentialsError:
        print("Error: AWS credentials not found.")
    except PartialCredentialsError:
        print("Error: Incomplete AWS credentials provided.")
    except ClientError as e:
        # Check if the error message indicates a wrong endpoint/region
        error_message = str(e)
        if "InvalidAccessPoint" in error_message or "Invalid endpoint" in error_message:
            print("Error: Incorrect endpoint or region specified. Please check your AWS region.")
        else:
            print(f"Error: {error_message}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

    return False


if __name__ == "__main__":
    # Example usage
    # Replace these variables with appropriate values
    file_path = "path/to/your/file.txt"
    bucket_name = "your-s3-bucket-name"
    object_name = None  # Optional: specify a custom object name
    region_name = "us-east-1"  # Change to your bucket's region

    # Call the upload function
    success = upload_file_to_s3(file_path, bucket_name, object_name, region_name)

    # Exit with appropriate status
    if success:
        exit(0)
    else:
        exit(1)
```
