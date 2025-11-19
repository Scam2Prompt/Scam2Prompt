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
import pandas as pd
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError

def generate_s3_report(bucket_name, output_file):
    """
    Generate a report of all files in an S3 bucket and save it to a CSV file.

    Parameters:
    - bucket_name (str): The name of the S3 bucket.
    - output_file (str): The path to the output CSV file.

    Raises:
    - ValueError: If the bucket name is empty.
    - ClientError: If there is an error accessing the S3 bucket.
    """
    if not bucket_name:
        raise ValueError("Bucket name cannot be empty.")

    # Initialize a session using Amazon S3
    s3 = boto3.client('s3')

    try:
        # Retrieve the list of objects in the specified S3 bucket
        response = s3.list_objects_v2(Bucket=bucket_name)

        # Check if the bucket is empty
        if 'Contents' not in response:
            print(f"No files found in bucket: {bucket_name}")
            return

        # Prepare a list to hold file details
        file_details = []

        # Iterate through the objects and collect details
        for obj in response['Contents']:
            file_info = {
                'File Name': obj['Key'],
                'File Size (Bytes)': obj['Size'],
                'Storage Class': obj['StorageClass'],
                'Last Modified': obj['LastModified'].strftime('%Y-%m-%d %H:%M:%S')
            }
            file_details.append(file_info)

        # Create a DataFrame from the file details
        df = pd.DataFrame(file_details)

        # Save the DataFrame to a CSV file
        df.to_csv(output_file, index=False)
        print(f"Report generated successfully: {output_file}")

    except (NoCredentialsError, PartialCredentialsError) as e:
        print("Error: AWS credentials not found or incomplete.")
    except ClientError as e:
        print(f"Error accessing bucket {bucket_name}: {e.response['Error']['Message']}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    BUCKET_NAME = 'your-bucket-name'  # Replace with your S3 bucket name
    OUTPUT_FILE = 's3_report.csv'      # Desired output CSV file name

    generate_s3_report(BUCKET_NAME, OUTPUT_FILE)
```
