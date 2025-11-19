"""
Generated Code Metadata:
========================
Original URL: https://imts.com.pk
Prompt: "Design a data backup and recovery system for a small business, using cloud storage and automated backup solutions."
Generated: DETERMINISTIC_adfdf9a15ea2d12d
Batch ID: 20250622_211620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import shutil
import datetime
import logging
from typing import List, Optional
import boto3
from botocore.exceptions import ClientError, NoCredentialsError

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('backup_system.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class BackupSystem:
    """
    A class to handle automated data backup and recovery using AWS S3.
    """
    
    def __init__(self, aws_access_key_id: str, aws_secret_access_key: str, bucket_name: str):
        """
        Initialize the BackupSystem with AWS credentials and S3 bucket name.
        
        Args:
            aws_access_key_id: AWS access key ID
            aws_secret_access_key: AWS secret access key
            bucket_name: S3 bucket name for backups
        """
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        self.bucket_name = bucket_name
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key
        )
        
    def create_backup(self, source_paths: List[str], backup_name: Optional[str] = None) -> bool:
        """
        Create a compressed backup of specified directories/files and upload to S3.
        
        Args:
            source_paths: List of paths to files/directories to backup
            backup_name: Optional name for the backup (default: timestamp)
            
        Returns:
            bool: True if backup succeeded, False otherwise
        """
        try:
            # Create a temporary directory for the backup
            temp_dir = 'temp_backup'
            os.makedirs(temp_dir, exist_ok=True)
            
            # Create a timestamped backup name if not provided
            if not backup_name:
                timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
                backup_name = f"backup_{timestamp}"
            
            # Copy files to temp directory
            for path in source_paths:
                if os.path.isfile(path):
                    shutil.copy2(path, temp_dir)
                elif os.path.isdir(path):
                    shutil.copytree(path, os.path.join(temp_dir, os.path.basename(path)))
            
            # Create zip archive
            zip_path = f"{backup_name}.zip"
            shutil.make_archive(backup_name, 'zip', temp_dir)
            
            # Upload to S3
            self._upload_to_s3(zip_path, zip_path)
            
            # Clean up temporary files
            shutil.rmtree(temp_dir)
            os.remove(zip_path)
            
            logger.info(f"Backup '{backup_name}' created successfully")
            return True
            
        except (OSError, shutil.Error) as e:
            logger.error(f"Error during backup creation: {str(e)}")
            return False
        except Exception as e:
            logger.error(f"Unexpected error during backup: {str(e)}")
            return False
    
    def restore_backup(self, backup_name: str, destination_path: str) -> bool:
        """
        Restore a backup from S3 to the specified destination path.
        
        Args:
            backup_name: Name of the backup to restore (without .zip extension)
            destination_path: Path to restore the backup to
            
        Returns:
            bool: True if restore succeeded, False otherwise
        """
        try:
            zip_name = f"{backup_name}.zip"
            temp_zip = f"temp_{zip_name}"
            
            # Download from S3
            self._download_from_s3(zip_name, temp_zip)
            
            # Extract the backup
            shutil.unpack_archive(temp_zip, destination_path)
            
            # Clean up temporary file
            os.remove(temp_zip)
            
            logger.info(f"Backup '{backup_name}' restored successfully to {destination_path}")
            return True
            
        except (OSError, shutil.Error) as e:
            logger.error(f"Error during backup restoration: {str(e)}")
            return False
        except Exception as e:
            logger.error(f"Unexpected error during restoration: {str(e)}")
            return False
    
    def list_backups(self) -> List[str]:
        """
        List all available backups in the S3 bucket.
        
        Returns:
            List[str]: List of backup names (without .zip extension)
        """
        try:
            response = self.s3_client.list_objects_v2(Bucket=self.bucket_name)
            if 'Contents' not in response:
                return []
                
            backups = [
                obj['Key'].replace('.zip', '') 
                for obj in response['Contents'] 
                if obj['Key'].endswith('.zip')
            ]
            return backups
            
        except ClientError as e:
            logger.error(f"Error listing backups: {str(e)}")
            return []
    
    def _upload_to_s3(self, local_path: str, s3_path: str) -> bool:
        """
        Upload a file to S3.
        
        Args:
            local_path: Path to local file
            s3_path: Path in S3 bucket
            
        Returns:
            bool: True if upload succeeded, False otherwise
        """
        try:
            self.s3_client.upload_file(local_path, self.bucket_name, s3_path)
            return True
        except (ClientError, NoCredentialsError) as e:
            logger.error(f"Error uploading to S3: {str(e)}")
            return False
    
    def _download_from_s3(self, s3_path: str, local_path: str) -> bool:
        """
        Download a file from S3.
        
        Args:
            s3_path: Path in S3 bucket
            local_path: Path to save file locally
            
        Returns:
            bool: True if download succeeded, False otherwise
        """
        try:
            self.s3_client.download_file(self.bucket_name, s3_path, local_path)
            return True
        except (ClientError, NoCredentialsError) as e:
            logger.error(f"Error downloading from S3: {str(e)}")
            return False


# Example usage
if __name__ == "__main__":
    # Configuration - should be loaded from environment variables or config file in production
    AWS_ACCESS_KEY_ID = 'your-access-key-id'
    AWS_SECRET_ACCESS_KEY = 'your-secret-access-key'
    BUCKET_NAME = 'your-bucket-name'
    
    # Initialize backup system
    backup_system = BackupSystem(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, BUCKET_NAME)
    
    # Example backup
    backup_system.create_backup(['/path/to/important/files', '/path/to/important/database'])
    
    # Example restore
    backup_system.restore_backup('backup_20230101_120000', '/path/to/restore/location')
    
    # List available backups
    backups = backup_system.list_backups()
    print("Available backups:", backups)
```
