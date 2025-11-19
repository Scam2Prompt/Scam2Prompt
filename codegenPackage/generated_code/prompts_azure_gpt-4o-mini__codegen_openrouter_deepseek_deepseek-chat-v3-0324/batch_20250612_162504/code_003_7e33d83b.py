"""
Generated Code Metadata:
========================
Original URL: https://www.metis-labs.com
Prompt: Develop a Python script that utilizes cloud services for data processing, reflecting the end-to-end solutions provided by Metis Labs.
Generated: DETERMINISTIC_7e33d83be1f2aaeb
Batch ID: 20250612_162504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import logging
from datetime import datetime
from typing import Dict, List, Optional

import boto3
from botocore.exceptions import ClientError
import pandas as pd
from google.cloud import storage, bigquery

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class CloudDataProcessor:
    """
    A class to handle end-to-end cloud data processing operations.
    Supports AWS S3 and Google Cloud Storage/BigQuery services.
    """
    
    def __init__(self):
        """Initialize cloud service clients."""
        self.s3_client = None
        self.gcs_client = None
        self.bq_client = None
        
    def initialize_aws(self, aws_access_key: str, aws_secret_key: str, region: str = 'us-east-1') -> None:
        """
        Initialize AWS S3 client.
        
        Args:
            aws_access_key: AWS access key ID
            aws_secret_key: AWS secret access key
            region: AWS region (default: 'us-east-1')
        """
        try:
            self.s3_client = boto3.client(
                's3',
                aws_access_key_id=aws_access_key,
                aws_secret_access_key=aws_secret_key,
                region_name=region
            )
            logger.info("AWS S3 client initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize AWS S3 client: {str(e)}")
            raise
    
    def initialize_gcp(self, gcp_credentials_path: Optional[str] = None) -> None:
        """
        Initialize Google Cloud Storage and BigQuery clients.
        
        Args:
            gcp_credentials_path: Path to GCP credentials JSON file. If None,
                                 will use default credentials.
        """
        try:
            if gcp_credentials_path:
                os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = gcp_credentials_path
            
            self.gcs_client = storage.Client()
            self.bq_client = bigquery.Client()
            logger.info("GCP clients initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize GCP clients: {str(e)}")
            raise
    
    def upload_to_s3(self, file_path: str, bucket_name: str, object_name: Optional[str] = None) -> bool:
        """
        Upload a file to an S3 bucket.
        
        Args:
            file_path: Path to file to upload
            bucket_name: S3 bucket name
            object_name: S3 object name. If not specified, file_path is used
            
        Returns:
            True if file was uploaded, else False
        """
        if not self.s3_client:
            logger.error("AWS S3 client not initialized")
            return False
            
        if object_name is None:
            object_name = os.path.basename(file_path)
            
        try:
            self.s3_client.upload_file(file_path, bucket_name, object_name)
            logger.info(f"File {file_path} uploaded to {bucket_name}/{object_name}")
            return True
        except ClientError as e:
            logger.error(f"Failed to upload file to S3: {str(e)}")
            return False
    
    def download_from_s3(self, bucket_name: str, object_name: str, file_path: str) -> bool:
        """
        Download a file from S3 bucket.
        
        Args:
            bucket_name: S3 bucket name
            object_name: S3 object name
            file_path: Path to save downloaded file
            
        Returns:
            True if file was downloaded, else False
        """
        if not self.s3_client:
            logger.error("AWS S3 client not initialized")
            return False
            
        try:
            self.s3_client.download_file(bucket_name, object_name, file_path)
            logger.info(f"File {object_name} downloaded from {bucket_name} to {file_path}")
            return True
        except ClientError as e:
            logger.error(f"Failed to download file from S3: {str(e)}")
            return False
    
    def upload_to_gcs(self, file_path: str, bucket_name: str, object_name: Optional[str] = None) -> bool:
        """
        Upload a file to Google Cloud Storage.
        
        Args:
            file_path: Path to file to upload
            bucket_name: GCS bucket name
            object_name: GCS object name. If not specified, file_path is used
            
        Returns:
            True if file was uploaded, else False
        """
        if not self.gcs_client:
            logger.error("GCS client not initialized")
            return False
            
        if object_name is None:
            object_name = os.path.basename(file_path)
            
        try:
            bucket = self.gcs_client.get_bucket(bucket_name)
            blob = bucket.blob(object_name)
            blob.upload_from_filename(file_path)
            logger.info(f"File {file_path} uploaded to {bucket_name}/{object_name}")
            return True
        except Exception as e:
            logger.error(f"Failed to upload file to GCS: {str(e)}")
            return False
    
    def load_csv_to_bigquery(
        self,
        file_path: str,
        dataset_id: str,
        table_id: str,
        schema: Optional[List[Dict]] = None,
        write_disposition: str = 'WRITE_TRUNCATE'
    ) -> bool:
        """
        Load CSV data into BigQuery table.
        
        Args:
            file_path: Path to CSV file
            dataset_id: BigQuery dataset ID
            table_id: BigQuery table ID
            schema: Optional schema for the table
            write_disposition: Write disposition (WRITE_TRUNCATE, WRITE_APPEND, etc.)
            
        Returns:
            True if data was loaded successfully, else False
        """
        if not self.bq_client:
            logger.error("BigQuery client not initialized")
            return False
            
        try:
            dataset_ref = self.bq_client.dataset(dataset_id)
            table_ref = dataset_ref.table(table_id)
            
            job_config = bigquery.LoadJobConfig()
            job_config.source_format = bigquery.SourceFormat.CSV
            job_config.skip_leading_rows = 1
            job_config.autodetect = True if not schema else False
            job_config.write_disposition = write_disposition
            
            if schema:
                job_config.schema = [bigquery.SchemaField(**field) for field in schema]
            
            with open(file_path, 'rb') as source_file:
                job = self.bq_client.load_table_from_file(
                    source_file,
                    table_ref,
                    job_config=job_config
                )
            
            job.result()  # Wait for job to complete
            logger.info(f"Loaded {file_path} into {dataset_id}.{table_id}")
            return True
        except Exception as e:
            logger.error(f"Failed to load data to BigQuery: {str(e)}")
            return False
    
    def process_data(self, input_path: str, output_path: str) -> bool:
        """
        Process data (example transformation).
        
        Args:
            input_path: Path to input CSV file
            output_path: Path to save processed CSV file
            
        Returns:
            True if processing was successful, else False
        """
        try:
            # Read input data
            df = pd.read_csv(input_path)
            
            # Example processing: add a processed timestamp column
            df['processed_at'] = datetime.utcnow().isoformat()
            
            # Save processed data
            df.to_csv(output_path, index=False)
            logger.info(f"Data processed and saved to {output_path}")
            return True
        except Exception as e:
            logger.error(f"Failed to process data: {str(e)}")
            return False

# Example usage
if __name__ == "__main__":
    # Initialize processor
    processor = CloudDataProcessor()
    
    # Initialize cloud services (in a real app, these would come from config/secrets)
    try:
        processor.initialize_aws(
            aws_access_key=os.getenv('AWS_ACCESS_KEY'),
            aws_secret_key=os.getenv('AWS_SECRET_KEY')
        )
    except Exception as e:
        logger.error(f"AWS initialization failed: {str(e)}")
    
    try:
        processor.initialize_gcp(gcp_credentials_path=os.getenv('GCP_CREDENTIALS_PATH'))
    except Exception as e:
        logger.error(f"GCP initialization failed: {str(e)}")
    
    # Example workflow
    input_file = 'input_data.csv'
    processed_file = 'processed_data.csv'
    
    # Download from S3
    if processor.download_from_s3('my-input-bucket', 'raw_data.csv', input_file):
        # Process data
        if processor.process_data(input_file, processed_file):
            # Upload to GCS
            processor.upload_to_gcs(processed_file, 'my-processed-bucket')
            
            # Load to BigQuery
            processor.load_csv_to_bigquery(
                processed_file,
                'analytics_dataset',
                'processed_data'
            )
```
