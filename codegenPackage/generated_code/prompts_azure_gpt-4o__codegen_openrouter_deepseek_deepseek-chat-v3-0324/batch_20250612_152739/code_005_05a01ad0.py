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
import csv
import os

def generate_s3_report(bucket_name, output_file):
    """
    Generates a report of all files in an S3 bucket with their metadata.
    
    Args:
        bucket_name (str): Name of the S3 bucket to scan
        output_file (str): Path to the output CSV file
    """
    try:
        # Initialize S3 client
        s3 = boto3.client('s3')
        
        # Open CSV file for writing
        with open(output_file, 'w', newline='') as csvfile:
            fieldnames = ['Key', 'Size (Bytes)', 'Storage Class', 'Last Modified']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            # Paginate through all objects in the bucket
            paginator = s3.get_paginator('list_objects_v2')
            for page in paginator.paginate(Bucket=bucket_name):
                if 'Contents' not in page:
                    continue
                    
                for obj in page['Contents']:
                    writer.writerow({
                        'Key': obj['Key'],
                        'Size (Bytes)': obj['Size'],
                        'Storage Class': obj.get('StorageClass', 'STANDARD'),
                        'Last Modified': obj['LastModified'].strftime('%Y-%m-%d %H:%M:%S')
                    })
        
        print(f"Report generated successfully at: {os.path.abspath(output_file)}")
    
    except boto3.exceptions.Boto3Error as e:
        print(f"Error accessing S3: {str(e)}")
    except IOError as e:
        print(f"Error writing to file: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Generate S3 bucket report')
    parser.add_argument('bucket', help='Name of the S3 bucket')
    parser.add_argument('--output', default='s3_report.csv', 
                       help='Output CSV file path (default: s3_report.csv)')
    
    args = parser.parse_args()
    
    generate_s3_report(args.bucket, args.output)
```
