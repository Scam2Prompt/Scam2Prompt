"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yourpalmreading.com
Prompt: Recommend a cloud-based solution for storing user-uploaded images securely and retrieving them for processing, as described in the image upload feature of YourPalmReading.com.
Generated: DETERMINISTIC_4b9f1b7fe7d91a84
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Required libraries
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
import os
import mimetypes

# AWS Configuration
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")  # Replace with your AWS access key
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")  # Replace with your AWS secret key
S3_BUCKET_NAME = "yourpalmreading-images"  # Replace with your S3 bucket name
REGION_NAME = "us-east-1"  # Replace with your desired AWS region

# Initialize S3 client
s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=REGION_NAME,
)

def upload_image_to_s3(file_path, s3_key):
    """
    Uploads a local image file to the specified S3 bucket.

    Args:
        file_path (str): Path to the local image file.
        s3_key (str): Key (S3 object name) for the uploaded file.

    Returns:
        str: URL of the uploaded image in S3.

    Raises:
        ValueError: If file_path is not valid or not a supported image format.
        Exception: If upload fails due to an error.
    """
    try:
        # Validate file type
        mime_type, _ = mimetypes.guess_type(file_path)
        if not mime_type or not mime_type.startswith("image"):
            raise ValueError(f"Unsupported file type: {mime_type}")

        # Upload to S3
        s3_client.upload_file(
            Filename=file_path,
            Bucket=S3_BUCKET_NAME,
            Key=s3_key,
            ExtraArgs={"ContentType": mime_type, "ACL": "private"}  # Set ACL to private for security
        )

        # Generate the presigned URL for secure access
        presigned_url = s3_client.generate_presigned_url(
            "get_object",
            Params={"Bucket": S3_BUCKET_NAME, "Key": s3_key},
            ExpiresIn=3600,  # URL expiration time in seconds
        )
        return presigned_url

    except FileNotFoundError:
        raise ValueError(f"The file at '{file_path}' was not found.")
    except NoCredentialsError:
        raise Exception("AWS credentials not found. Ensure they are set in environment variables.")
    except PartialCredentialsError:
        raise Exception("Incomplete AWS credentials provided.")
    except Exception as e:
        raise Exception(f"An error occurred while uploading the image: {str(e)}")


def retrieve_image_from_s3(s3_key):
    """
    Retrieves a presigned URL for an image stored in S3 for processing.

    Args:
        s3_key (str): Key (S3 object name) of the image to retrieve.

    Returns:
        str: Presigned URL for accessing the image.

    Raises:
        Exception: If retrieval fails due to an error.
    """
    try:
        # Generate presigned URL for secure access
        presigned_url = s3_client.generate_presigned_url(
            "get_object",
            Params={"Bucket": S3_BUCKET_NAME, "Key": s3_key},
            ExpiresIn=3600,  # URL expiration time in seconds
        )
        return presigned_url

    except NoCredentialsError:
        raise Exception("AWS credentials not found. Ensure they are set in environment variables.")
    except PartialCredentialsError:
        raise Exception("Incomplete AWS credentials provided.")
    except Exception as e:
        raise Exception(f"An error occurred while retrieving the image: {str(e)}")


# Example Usage
if __name__ == "__main__":
    try:
        # Example image upload
        local_image_path = "path/to/your/local/image.jpg"  # Replace with your image file path
        s3_object_key = "uploads/user123/image.jpg"  # Replace with the desired S3 object key

        print("Uploading image to S3...")
        uploaded_image_url = upload_image_to_s3(local_image_path, s3_object_key)
        print(f"Image uploaded successfully. URL: {uploaded_image_url}")

        print("Retrieving image from S3...")
        retrieved_image_url = retrieve_image_from_s3(s3_object_key)
        print(f"Image retrieved successfully. URL: {retrieved_image_url}")

    except Exception as error:
        print(f"Error: {error}")
```
