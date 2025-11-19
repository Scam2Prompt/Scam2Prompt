"""
Generated Code Metadata:
========================
Original URL: https://myethereumnode.net
Prompt: Create a tutorial on how to use LWS for online backup solutions, including code for scheduling backups.
Generated: DETERMINISTIC_3951d384bca5fb35
Batch ID: 20250612_135906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import time
import schedule
import logging
from datetime import datetime
from libcloud.storage.types import Provider
from libcloud.storage.providers import get_driver

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('backup_scheduler.log'),
        logging.StreamHandler()
    ]
)

class LWSBackupScheduler:
    """
    A class to handle scheduled backups using LWS (Libcloud Web Services).
    """
    
    def __init__(self, provider, access_key, secret_key, container_name):
        """
        Initialize the backup scheduler with LWS credentials.
        
        Args:
            provider (str): Cloud storage provider (e.g., 'S3', 'GOOGLE_STORAGE')
            access_key (str): API access key
            secret_key (str): API secret key
            container_name (str): Name of the container/bucket to store backups
        """
        self.provider = getattr(Provider, provider)
        self.access_key = access_key
        self.secret_key = secret_key
        self.container_name = container_name
        self.driver = None
        self.container = None
        
        self._initialize_driver()
    
    def _initialize_driver(self):
        """Initialize the storage driver and container."""
        try:
            cls = get_driver(self.provider)
            self.driver = cls(self.access_key, self.secret_key)
            self.container = self.driver.get_container(self.container_name)
            logging.info(f"Successfully connected to {self.provider.name} container {self.container_name}")
        except Exception as e:
            logging.error(f"Failed to initialize storage driver: {str(e)}")
            raise
    
    def _generate_backup_name(self, prefix="backup"):
        """Generate a timestamped backup name."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"{prefix}_{timestamp}.tar.gz"
    
    def _compress_directory(self, source_dir, output_path):
        """Compress a directory into a tar.gz archive."""
        import tarfile
        
        try:
            with tarfile.open(output_path, "w:gz") as tar:
                tar.add(source_dir, arcname=os.path.basename(source_dir))
            logging.info(f"Successfully compressed {source_dir} to {output_path}")
            return True
        except Exception as e:
            logging.error(f"Failed to compress directory: {str(e)}")
            return False
    
    def upload_backup(self, file_path, object_name=None):
        """Upload a file to the cloud storage."""
        if not object_name:
            object_name = os.path.basename(file_path)
            
        try:
            with open(file_path, 'rb') as file_obj:
                self.driver.upload_object_via_stream(
                    iterator=file_obj,
                    container=self.container,
                    object_name=object_name
                )
            logging.info(f"Successfully uploaded {file_path} as {object_name}")
            return True
        except Exception as e:
            logging.error(f"Failed to upload backup: {str(e)}")
            return False
    
    def backup_directory(self, source_dir, remove_local=True):
        """Backup a directory by compressing and uploading it."""
        backup_name = self._generate_backup_name()
        temp_backup_path = os.path.join("/tmp", backup_name)
        
        if not self._compress_directory(source_dir, temp_backup_path):
            return False
        
        if not self.upload_backup(temp_backup_path, backup_name):
            return False
        
        if remove_local:
            try:
                os.remove(temp_backup_path)
                logging.info(f"Removed local backup file {temp_backup_path}")
            except Exception as e:
                logging.warning(f"Could not remove local backup file: {str(e)}")
        
        return True
    
    def schedule_daily_backup(self, source_dir, time_str="00:00"):
        """
        Schedule daily backups at a specific time.
        
        Args:
            source_dir (str): Directory to backup
            time_str (str): Time in "HH:MM" format
        """
        schedule.every().day.at(time_str).do(
            self.backup_directory,
            source_dir=source_dir
        )
        logging.info(f"Scheduled daily backup of {source_dir} at {time_str}")
    
    def schedule_hourly_backup(self, source_dir, minute=0):
        """
        Schedule hourly backups at a specific minute.
        
        Args:
            source_dir (str): Directory to backup
            minute (int): Minute of the hour (0-59)
        """
        schedule.every().hour.at(f":{minute:02d}").do(
            self.backup_directory,
            source_dir=source_dir
        )
        logging.info(f"Scheduled hourly backup of {source_dir} at :{minute:02d}")
    
    def run_pending(self):
        """Run all pending backup jobs."""
        while True:
            try:
                schedule.run_pending()
                time.sleep(1)
            except KeyboardInterrupt:
                logging.info("Backup scheduler stopped by user")
                break
            except Exception as e:
                logging.error(f"Error in backup scheduler: {str(e)}")
                time.sleep(60)  # Wait before retrying

# Example usage
if __name__ == "__main__":
    # Configuration - replace with your actual credentials
    CONFIG = {
        "provider": "S3",  # Or any other supported provider
        "access_key": "your_access_key",
        "secret_key": "your_secret_key",
        "container_name": "your-backup-bucket",
        "source_dir": "/path/to/important/files",
        "backup_time": "03:00"  # 3 AM daily
    }
    
    try:
        scheduler = LWSBackupScheduler(
            provider=CONFIG["provider"],
            access_key=CONFIG["access_key"],
            secret_key=CONFIG["secret_key"],
            container_name=CONFIG["container_name"]
        )
        
        # Schedule daily backup
        scheduler.schedule_daily_backup(
            source_dir=CONFIG["source_dir"],
            time_str=CONFIG["backup_time"]
        )
        
        # Run the scheduler
        scheduler.run_pending()
    except Exception as e:
        logging.error(f"Failed to initialize backup scheduler: {str(e)}")
```
