"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.metis-labs.com
Prompt: Develop a Python script that utilizes cloud services for data processing, reflecting the end-to-end solutions provided by Metis Labs.
Generated: DETERMINISTIC_7e33d83be1f2aaeb
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import boto3
import pandas as pd
import logging
import os
from botocore.exceptions import BotoCoreError, ClientError

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# AWS S3 Bucket Name
S3_BUCKET_NAME = 'your-s3-bucket-name'
# Output S3 Bucket for processed data
OUTPUT_S3_BUCKET_NAME = 'your-output-s3-bucket-name'
# AWS Region
AWS_REGION = 'us-west-2'

def upload_to_s3(file_name, bucket):
    """Uploads a file to an S3 bucket."""
    try:
        s3_client = boto3.client('s3', region_name=AWS_REGION)
        s3_client.upload_file(file_name, bucket, os.path.basename(file_name))
        logger.info(f'Successfully uploaded {file_name} to {bucket}')
    except (BotoCoreError, ClientError) as e:
        logger.error(f'Failed to upload {file_name} to {bucket}: {e}')
        raise

def download_from_s3(file_name, bucket):
    """Downloads a file from an S3 bucket."""
    try:
        s3_client = boto3.client('s3', region_name=AWS_REGION)
        s3_client.download_file(bucket, file_name, file_name)
        logger.info(f'Successfully downloaded {file_name} from {bucket}')
    except (BotoCoreError, ClientError) as e:
        logger.error(f'Failed to download {file_name} from {bucket}: {e}')
        raise

def process_data(file_name):
    """Processes the data from a CSV file and returns a DataFrame."""
    try:
        logger.info(f'Starting data processing for {file_name}')
        # Load CSV data into a DataFrame
        data = pd.read_csv(file_name)
        # Perform some transformation (example: removing NaN values)
        processed_data = data.dropna()
        logger.info('Data processing completed successfully')
        return processed_data
    except Exception as e:
        logger.error(f'Error processing {file_name}: {e}')
        raise

def save_processed_data(data_frame, output_file_name):
    """Saves the processed DataFrame to a CSV file."""
    try:
        data_frame.to_csv(output_file_name, index=False)
        logger.info(f'Successfully saved processed data to {output_file_name}')
    except Exception as e:
        logger.error(f'Failed to save processed data to {output_file_name}: {e}')
        raise

def main():
    """Main function to execute the end-to-end data processing."""
    input_file_name = 'input_data.csv'  # Name of the file to be processed
    output_file_name = 'processed_data.csv'  # Name of the output file

    # Step 1: Download the input data from S3
    download_from_s3(input_file_name, S3_BUCKET_NAME)

    # Step 2: Process the data
    processed_data = process_data(input_file_name)

    # Step 3: Save the processed data locally
    save_processed_data(processed_data, output_file_name)

    # Step 4: Upload the processed data back to S3
    upload_to_s3(output_file_name, OUTPUT_S3_BUCKET_NAME)

if __name__ == '__main__':
    main()
```
