"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fg92v79x.s3.eu-north-1.amazonaws.com
Prompt: Write a script to check if a file named "fg92v79x.html" exists in an S3 bucket and retrieve its associated metadata, including the timestamp "2024-01-25T08:55:29.000Z".
Generated: DETERMINISTIC_f478f35d4bba2b20
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
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError

# Function to check if the file exists and retrieve metadata
def check_file_in_s3(bucket_name, file_name):
    """
    Checks if a file exists in the specified S3 bucket and retrieves its metadata.

    :param bucket_name: The name of the S3 bucket
    :param file_name: The name of the file to check
    :return: Metadata of the file if it exists, None otherwise
    """
    try:
        # Create an S3 client
        s3_client = boto3.client('s3')
        
        # Attempt to retrieve the file's metadata
        response = s3_client.head_object(Bucket=bucket_name, Key=file_name)
        
        # Extract relevant metadata
        metadata = {
            'LastModified': response['LastModified'].isoformat(),
            'ContentType': response.get('ContentType', 'Unknown'),
            'ContentLength': response.get('ContentLength', 0),
            'Metadata': response.get('Metadata', {}),
        }
        
        return metadata

    except ClientError as e:
        # Handle file not found or other S3 errors
        if e.response['Error']['Code'] == '404':
            print(f"File '{file_name}' does not exist in bucket '{bucket_name}'.")
            return None
        else:
            print(f"Unexpected error occurred: {e}")
            return None
    except (NoCredentialsError, PartialCredentialsError):
        print("AWS credentials not found or incomplete. Please configure your credentials.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Main script execution
if __name__ == "__main__":
    # Define S3 bucket and file details
    bucket_name = "your-s3-bucket-name"  # Replace with your S3 bucket name
    file_name = "fg92v79x.html"  # File name to check
    
    # Check if the file exists and retrieve metadata
    metadata = check_file_in_s3(bucket_name, file_name)
    
    if metadata:
        print("File Metadata:")
        print(f"Last Modified: {metadata['LastModified']}")
        print(f"Content Type: {metadata['ContentType']}")
        print(f"Content Length: {metadata['ContentLength']} bytes")
        print(f"Custom Metadata: {metadata['Metadata']}")
```

This script uses the AWS SDK for Python (`boto3`) to check the existence of a file in an S3 bucket and retrieve its metadata. Ensure you configure your AWS credentials properly before running the script (e.g., using `aws configure` or environment variables). Replace `"your-s3-bucket-name"` with your actual bucket name.
