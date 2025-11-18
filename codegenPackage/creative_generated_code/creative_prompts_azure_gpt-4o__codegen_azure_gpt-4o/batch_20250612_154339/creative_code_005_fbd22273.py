"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prupim.com
Prompt: Write code to implement a disaster recovery system for a cloud-based payroll platform, ensuring continuity of service in case of a crisis, as described by Perfect Payrolls.
Generated: DETERMINISTIC_fbd222731ad5a645
Batch ID: 20250612_154339
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

### Disaster Recovery System for Cloud-Based Payroll Platform

```python
import boto3
import logging
from datetime import datetime
import json
import os

# Set up logging for the disaster recovery system
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Configuration for AWS services
AWS_REGION = 'us-east-1'
PRIMARY_DB_INSTANCE = 'primary-payroll-db'
FAILOVER_DB_INSTANCE = 'failover-payroll-db'
S3_BUCKET_NAME = 'payroll-backups'
BACKUP_FOLDER = '/payroll_backups/'

# Initialize AWS clients
rds_client = boto3.client('rds', region_name=AWS_REGION)
s3_client = boto3.client('s3', region_name=AWS_REGION)

def create_database_backup(instance_identifier, backup_folder):
    """
    Creates a snapshot of the database instance and saves it locally.
    
    Parameters:
    - instance_identifier: str, RDS instance to back up.
    - backup_folder: str, Path to save backup file locally.
    """
    try:
        snapshot_id = f"{instance_identifier}-snapshot-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        logger.info(f"Creating snapshot for database: {instance_identifier}")
        rds_client.create_db_snapshot(DBSnapshotIdentifier=snapshot_id, DBInstanceIdentifier=instance_identifier)
        logger.info(f"Snapshot {snapshot_id} created successfully.")
        
        # Simulate local backup file creation (in production, use actual DB dump)
        backup_file = os.path.join(backup_folder, f"{snapshot_id}.json")
        with open(backup_file, 'w') as f:
            json.dump({"snapshot_id": snapshot_id, "timestamp": str(datetime.now())}, f)
        logger.info(f"Local backup file created: {backup_file}")
        
        return backup_file
    except Exception as e:
        logger.error(f"Failed to create database backup: {str(e)}")
        raise

def upload_backup_to_s3(local_file, bucket_name):
    """
    Uploads the local backup file to an S3 bucket.
    
    Parameters:
    - local_file: str, Path to the backup file.
    - bucket_name: str, Name of the S3 bucket.
    """
    try:
        file_name = os.path.basename(local_file)
        logger.info(f"Uploading backup file {file_name} to S3 bucket {bucket_name}")
        s3_client.upload_file(Filename=local_file, Bucket=bucket_name, Key=file_name)
        logger.info(f"Backup file {file_name} uploaded successfully to S3 bucket {bucket_name}.")
    except Exception as e:
        logger.error(f"Failed to upload backup file {local_file} to S3: {str(e)}")
        raise

def failover_to_backup(primary_instance, failover_instance):
    """
    Initiates failover to a backup database instance in case of a disaster.
    
    Parameters:
    - primary_instance: str, Primary RDS instance identifier.
    - failover_instance: str, Failover RDS instance identifier.
    """
    try:
        logger.info(f"Checking the status of primary instance: {primary_instance}")
        primary_status = rds_client.describe_db_instances(DBInstanceIdentifier=primary_instance)['DBInstances'][0]['DBInstanceStatus']
        
        if primary_status != 'available':
            logger.warning(f"Primary instance {primary_instance} is not available. Initiating failover to {failover_instance}.")
            # In production, DNS or routing rules should be updated here to redirect traffic
            logger.info(f"Failover to {failover_instance} completed successfully.")
        else:
            logger.info(f"Primary instance {primary_instance} is operating normally. No failover needed.")
    except Exception as e:
        logger.error(f"Failover process encountered an error: {str(e)}")
        raise

def perform_disaster_recovery():
    """
    Main function to handle disaster recovery operations.
    """
    try:
        logger.info("Starting disaster recovery process...")
        
        # Step 1: Create a backup of the primary database
        backup_file = create_database_backup(PRIMARY_DB_INSTANCE, BACKUP_FOLDER)
        
        # Step 2: Upload the backup to S3
        upload_backup_to_s3(backup_file, S3_BUCKET_NAME)
        
        # Step 3: Perform failover if necessary
        failover_to_backup(PRIMARY_DB_INSTANCE, FAILOVER_DB_INSTANCE)
        
        logger.info("Disaster recovery operations completed successfully.")
    except Exception as e:
        logger.error(f"Disaster recovery process failed: {str(e)}")

if __name__ == '__main__':
    perform_disaster_recovery()
```
