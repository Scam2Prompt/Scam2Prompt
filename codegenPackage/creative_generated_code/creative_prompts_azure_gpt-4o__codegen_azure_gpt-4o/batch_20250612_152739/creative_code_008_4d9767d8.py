"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://5mev69v8.s3.us-east-2.amazonaws.com
Prompt: Write a script to convert S3 file metadata into a CSV file, including columns for file name, timestamp, hash value, and storage class.
Generated: DETERMINISTIC_4d9767d8dba3b8a0
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
import csv
import sys

def fetch_s3_metadata(bucket_name, prefix=''):
    """
    Fetch metadata of files in an S3 bucket.

    Args:
        bucket_name (str): Name of the S3 bucket.
        prefix (str): Prefix to filter objects in the bucket (optional).

    Returns:
        list: List of dictionaries containing file metadata.
    """
    s3_client = boto3.client('s3')

    try:
        # List objects in the bucket under the specified prefix
        response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=prefix)

        if 'Contents' not in response:
            print(f"No files found in bucket '{bucket_name}' with prefix '{prefix}'.")
            return []

        metadata = []
        for obj in response['Contents']:
            metadata.append({
                'FileName': obj['Key'],
                'Timestamp': obj['LastModified'].isoformat(),
                'HashValue': obj['ETag'].strip('"'),
                'StorageClass': obj.get('StorageClass', 'STANDARD')  # Default storage class
            })
        return metadata

    except Exception as e:
        print(f"Error fetching metadata from S3: {e}")
        sys.exit(1)

def write_metadata_to_csv(metadata, output_file):
    """
    Write file metadata to a CSV file.

    Args:
        metadata (list): List of dictionaries containing file metadata.
        output_file (str): Path to the output CSV file.
    """
    try:
        with open(output_file, mode='w', newline='', encoding='utf-8') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=['FileName', 'Timestamp', 'HashValue', 'StorageClass'])
            writer.writeheader()
            writer.writerows(metadata)
    except Exception as e:
        print(f"Error writing metadata to CSV file '{output_file}': {e}")
        sys.exit(1)

if __name__ == '__main__':
    # Define the S3 bucket name and optional prefix
    BUCKET_NAME = 'your-s3-bucket-name'
    PREFIX = ''  # Change this if you want to filter by prefix
    OUTPUT_CSV = 's3_metadata.csv'

    # Fetch metadata from S3
    file_metadata = fetch_s3_metadata(BUCKET_NAME, PREFIX)

    # Write metadata to a CSV file
    if file_metadata:
        write_metadata_to_csv(file_metadata, OUTPUT_CSV)
        print(f"Metadata successfully written to '{OUTPUT_CSV}'.")
    else:
        print("No metadata to write.")
```
