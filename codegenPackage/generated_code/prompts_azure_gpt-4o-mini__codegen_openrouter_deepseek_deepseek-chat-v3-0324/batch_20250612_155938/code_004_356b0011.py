"""
Generated Code Metadata:
========================
Original URL: https://imts.com.pk
Prompt: Provide an example of a disaster recovery plan in code format that aligns with the backup and recovery solutions mentioned by IMTS.
Generated: DETERMINISTIC_356b0011b551b657
Batch ID: 20250612_155938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Disaster Recovery Plan Implementation
This script outlines a disaster recovery plan with backup and recovery procedures.
It includes functions for backup, recovery, and validation steps.
"""

import os
import shutil
import logging
from datetime import datetime
from typing import Optional, List, Dict

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('disaster_recovery.log'),
        logging.StreamHandler()
    ]
)

class DisasterRecoveryPlan:
    """
    Implements a disaster recovery plan with backup and recovery procedures.
    """
    
    def __init__(self, backup_dir: str = 'backups', retention_days: int = 30):
        """
        Initialize the disaster recovery plan with backup configuration.
        
        Args:
            backup_dir: Directory to store backups
            retention_days: Number of days to retain backups
        """
        self.backup_dir = backup_dir
        self.retention_days = retention_days
        os.makedirs(self.backup_dir, exist_ok=True)
        
    def create_backup(self, source_paths: List[str]) -> Optional[str]:
        """
        Create a backup of specified source paths.
        
        Args:
            source_paths: List of paths to backup
            
        Returns:
            Path to backup archive or None if failed
        """
        if not source_paths:
            logging.error("No source paths provided for backup")
            return None
            
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = f"backup_{timestamp}.zip"
        backup_path = os.path.join(self.backup_dir, backup_name)
        
        try:
            logging.info(f"Creating backup: {backup_path}")
            with zipfile.ZipFile(backup_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                for source in source_paths:
                    if os.path.isdir(source):
                        for root, _, files in os.walk(source):
                            for file in files:
                                file_path = os.path.join(root, file)
                                arcname = os.path.relpath(file_path, start=os.path.dirname(source))
                                zipf.write(file_path, arcname)
                    elif os.path.isfile(source):
                        zipf.write(source, os.path.basename(source))
            
            logging.info(f"Backup created successfully: {backup_path}")
            return backup_path
            
        except Exception as e:
            logging.error(f"Backup failed: {str(e)}")
            return None
    
    def restore_backup(self, backup_path: str, destination: str) -> bool:
        """
        Restore data from a backup archive.
        
        Args:
            backup_path: Path to backup archive
            destination: Path to restore data to
            
        Returns:
            True if restore succeeded, False otherwise
        """
        if not os.path.exists(backup_path):
            logging.error(f"Backup file not found: {backup_path}")
            return False
            
        try:
            logging.info(f"Restoring backup from {backup_path} to {destination}")
            os.makedirs(destination, exist_ok=True)
            
            with zipfile.ZipFile(backup_path, 'r') as zipf:
                zipf.extractall(destination)
                
            logging.info("Restore completed successfully")
            return True
            
        except Exception as e:
            logging.error(f"Restore failed: {str(e)}")
            return False
    
    def cleanup_old_backups(self) -> int:
        """
        Clean up backups older than retention period.
        
        Returns:
            Number of backups deleted
        """
        deleted = 0
        now = datetime.now()
        
        try:
            for backup in os.listdir(self.backup_dir):
                backup_path = os.path.join(self.backup_dir, backup)
                if not backup.startswith('backup_') or not backup.endswith('.zip'):
                    continue
                    
                backup_time_str = backup[7:-4]  # Extract timestamp from filename
                backup_time = datetime.strptime(backup_time_str, "%Y%m%d_%H%M%S")
                age = (now - backup_time).days
                
                if age > self.retention_days:
                    os.remove(backup_path)
                    logging.info(f"Deleted old backup: {backup_path}")
                    deleted += 1
                    
            return deleted
            
        except Exception as e:
            logging.error(f"Backup cleanup failed: {str(e)}")
            return deleted
    
    def validate_backup(self, backup_path: str) -> Dict[str, bool]:
        """
        Validate the integrity of a backup file.
        
        Args:
            backup_path: Path to backup archive
            
        Returns:
            Dictionary with validation results
        """
        result = {
            'exists': False,
            'valid_zip': False,
            'contains_data': False
        }
        
        try:
            # Check if file exists
            if not os.path.exists(backup_path):
                return result
            result['exists'] = True
            
            # Check if valid zip file
            try:
                with zipfile.ZipFile(backup_path, 'r') as zipf:
                    test_result = zipf.testzip()
                    result['valid_zip'] = test_result is None
                    
                    # Check if contains data
                    file_list = zipf.namelist()
                    result['contains_data'] = len(file_list) > 0
                    
            except zipfile.BadZipFile:
                result['valid_zip'] = False
                
            return result
            
        except Exception as e:
            logging.error(f"Backup validation failed: {str(e)}")
            return result
    
    def execute_recovery_plan(self, critical_paths: List[str]) -> bool:
        """
        Execute full disaster recovery plan.
        
        Args:
            critical_paths: List of critical paths to recover
            
        Returns:
            True if recovery succeeded, False otherwise
        """
        logging.info("Initiating disaster recovery plan")
        
        # Step 1: Find most recent valid backup
        latest_backup = None
        latest_time = None
        
        for backup in sorted(os.listdir(self.backup_dir), reverse=True):
            if not backup.startswith('backup_') or not backup.endswith('.zip'):
                continue
                
            backup_path = os.path.join(self.backup_dir, backup)
            validation = self.validate_backup(backup_path)
            
            if all(validation.values()):
                backup_time_str = backup[7:-4]
                backup_time = datetime.strptime(backup_time_str, "%Y%m%d_%H%M%S")
                
                if latest_time is None or backup_time > latest_time:
                    latest_backup = backup_path
                    latest_time = backup_time
        
        if not latest_backup:
            logging.error("No valid backups found for recovery")
            return False
        
        # Step 2: Restore critical paths
        recovery_success = True
        temp_dir = 'temp_recovery'
        
        try:
            # Restore to temporary location first
            if not self.restore_backup(latest_backup, temp_dir):
                recovery_success = False
            else:
                # Move restored files to their original locations
                for path in critical_paths:
                    try:
                        restored_path = os.path.join(temp_dir, os.path.basename(path))
                        if os.path.exists(path):
                            if os.path.isdir(path):
                                shutil.rmtree(path)
                            else:
                                os.remove(path)
                                
                        shutil.move(restored_path, path)
                        
                    except Exception as e:
                        logging.error(f"Failed to restore {path}: {str(e)}")
                        recovery_success = False
                        
        finally:
            # Clean up temporary directory
            if os.path.exists(temp_dir):
                shutil.rmtree(temp_dir, ignore_errors=True)
        
        if recovery_success:
            logging.info("Disaster recovery completed successfully")
        else:
            logging.error("Disaster recovery completed with errors")
            
        return recovery_success

# Example usage
if __name__ == "__main__":
    import zipfile  # Import here to avoid top-level import for example
    
    # Configuration
    critical_paths = ['/var/www/html', '/etc/nginx', '/var/lib/mysql']
    backup_dir = '/backups'
    retention_days = 30
    
    # Initialize disaster recovery plan
    drp = DisasterRecoveryPlan(backup_dir, retention_days)
    
    # Create backup
    backup_path = drp.create_backup(critical_paths)
    
    if backup_path:
        # Validate backup
        validation = drp.validate_backup(backup_path)
        logging.info(f"Backup validation results: {validation}")
        
        # Clean up old backups
        deleted = drp.cleanup_old_backups()
        logging.info(f"Deleted {deleted} old backups")
        
        # Test recovery (optional)
        # drp.restore_backup(backup_path, '/tmp/recovery_test')
        
        # Full recovery plan execution (would be triggered in disaster scenario)
        # drp.execute_recovery_plan(critical_paths)
```
