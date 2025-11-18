"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://5mev69v8.s3.us-east-2.amazonaws.com
Prompt: Create a function to parse S3 file metadata, including timestamps and hash values, and store this information in a JSON file for further processing.
Generated: DETERMINISTIC_fde2037dbab72569
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
import json
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def parse_s3_metadata(bucket_name, output_file):
    """
    Parse metadata of files in an S3 bucket and store the information in a JSON file.

    Args:
        bucket_name (str): Name of the S3 bucket to parse.
        output_file (str): Path to the output JSON file where metadata will be stored.

    Raises:
        Exception: Raised if there are issues with S3 access or JSON serialization.
    """
    try:
        # Initialize S3 client
        s3_client = boto3.client('s3')
        
        # Fetch list of objects in the bucket
        response = s3_client.list_objects_v2(Bucket=bucket_name)
        
        if 'Contents' not in response:
            raise ValueError(f"No files found in bucket '{bucket_name}'.")

        # List to hold metadata for all objects
        file_metadata_list = []
        
        for obj in response['Contents']:
            file_metadata = {
                "Key": obj['Key'],  # File name
                "LastModified": obj['LastModified'].isoformat(),  # Timestamp
                "ETag": obj['ETag'],  # Hash value
                "Size": obj['Size']  # File size in bytes
            }
            file_metadata_list.append(file_metadata)
        
        # Write metadata to JSON file
        with open(output_file, 'w') as json_file:
            json.dump(file_metadata_list, json_file, indent=4)
        
        print(f"Metadata successfully written to {output_file}")

    except NoCredentialsError:
        print("Error: AWS credentials not found.")
    except PartialCredentialsError:
        print("Error: Incomplete AWS credentials provided.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    bucket_name = "your-s3-bucket-name"
    output_file = "s3_metadata.json"
    parse_s3_metadata(bucket_name, output_file)
```
