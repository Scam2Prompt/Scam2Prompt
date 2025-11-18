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
import logging
from botocore.exceptions import ClientError
from datetime import datetime

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_s3_file_metadata(bucket_name, file_key):
    """
    Retrieve the metadata of a file stored in an S3 bucket.

    Args:
        bucket_name (str): The name of the S3 bucket.
        file_key (str): The key of the file in the S3 bucket.

    Returns:
        dict: A dictionary containing the file metadata including
              last modified timestamp and ETag (hash value).
    """
    s3_client = boto3.client('s3')
    
    try:
        # Fetch the object's metadata from S3
        response = s3_client.head_object(Bucket=bucket_name, Key=file_key)

        # Extract relevant metadata
        metadata = {
            'FileName': file_key,
            'LastModified': response['LastModified'].isoformat(),
            'ETag': response['ETag'].strip('"'),  # Remove quotes from ETag
            'Size': response['ContentLength']  # Size in bytes
        }
        
        return metadata

    except ClientError as e:
        logging.error(f"Failed to retrieve metadata for {file_key} in bucket {bucket_name}: {e}")
        return None

def save_metadata_to_json(metadata, output_file):
    """
    Save the parsed metadata to a JSON file.

    Args:
        metadata (dict): The metadata to be saved.
        output_file (str): Path to the output JSON file.
    """
    try:
        with open(output_file, 'w') as json_file:
            json.dump(metadata, json_file, indent=4)
        logging.info(f"Metadata saved successfully to {output_file}")

    except IOError as e:
        logging.error(f"Failed to write metadata to {output_file}: {e}")

def main():
    """
    Main function to execute the metadata extraction and saving process.
    """
    bucket_name = 'your-bucket-name'  # Replace with your S3 bucket name
    file_key = 'your/file/key.txt'      # Replace with the S3 file key
    output_file = 'metadata.json'        # JSON output file name
    
    # Get file metadata from S3
    metadata = get_s3_file_metadata(bucket_name, file_key)
    
    # Check if metadata retrieval was successful
    if metadata:
        # Save the metadata to a JSON file
        save_metadata_to_json(metadata, output_file)

if __name__ == "__main__":
    main()
```
