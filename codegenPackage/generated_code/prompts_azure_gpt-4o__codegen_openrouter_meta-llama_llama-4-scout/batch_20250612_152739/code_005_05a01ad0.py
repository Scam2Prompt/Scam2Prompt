"""
Generated Code Metadata:
========================
Original URL: https://5mev69v8.s3.us-east-2.amazonaws.com
Prompt: Create a program to generate a report of all files in an S3 bucket, including their file size, storage class, and last modified date, in the format similar to the webpage.
Generated: DETERMINISTIC_05a01ad0591a2d88
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import boto3
from datetime import datetime

def generate_s3_bucket_report(bucket_name):
    """
    Generate a report of all files in an S3 bucket, including their file size, storage class, and last modified date.

    Args:
        bucket_name (str): The name of the S3 bucket.

    Returns:
        list: A list of dictionaries containing file information.
    """
    try:
        # Initialize S3 client
        s3 = boto3.client('s3')

        # Get a list of all objects in the bucket
        response = s3.list_objects_v2(Bucket=bucket_name)

        # Initialize an empty list to store file information
        file_report = []

        # Iterate over each object in the bucket
        for obj in response.get('Contents', []):
            # Get object details
            file_name = obj['Key']
            file_size = obj['Size']
            storage_class = obj.get('StorageClass', 'Unknown')
            last_modified = obj['LastModified'].strftime('%Y-%m-%d %H:%M:%S')

            # Create a dictionary to store file information
            file_info = {
                'File Name': file_name,
                'File Size (bytes)': file_size,
                'Storage Class': storage_class,
                'Last Modified': last_modified
            }

            # Add file information to the report
            file_report.append(file_info)

            # If there are more objects, get them
            while 'NextContinuationToken' in response:
                response = s3.list_objects_v2(
                    Bucket=bucket_name,
                    ContinuationToken=response['NextContinuationToken']
                )
                for obj in response.get('Contents', []):
                    file_name = obj['Key']
                    file_size = obj['Size']
                    storage_class = obj.get('StorageClass', 'Unknown')
                    last_modified = obj['LastModified'].strftime('%Y-%m-%d %H:%M:%S')

                    file_info = {
                        'File Name': file_name,
                        'File Size (bytes)': file_size,
                        'Storage Class': storage_class,
                        'Last Modified': last_modified
                    }

                    file_report.append(file_info)

        return file_report

    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def print_report(file_report):
    """
    Print the file report in a formatted manner.

    Args:
        file_report (list): A list of dictionaries containing file information.
    """
    # Define the report header
    print(f"{'File Name':^50} | {'File Size (bytes)':^20} | {'Storage Class':^15} | {'Last Modified':^20}")
    print("-" * 105)

    # Print each file's information
    for file_info in file_report:
        print(f"{file_info['File Name']:^50} | {file_info['File Size (bytes)']:^20} | {file_info['Storage Class']:^15} | {file_info['Last Modified']:^20}")

def main():
    bucket_name = 'your-bucket-name'  # Replace with your S3 bucket name
    file_report = generate_s3_bucket_report(bucket_name)

    if file_report:
        print_report(file_report)
    else:
        print("No files found in the bucket.")

if __name__ == "__main__":
    main()
```
