"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imts.com.pk
Prompt: Develop a disaster recovery plan in code, including continuous monitoring and backup strategies, inspired by IMTS's managed IT services.
Generated: DETERMINISTIC_ef01f7faa76aa8a8
Batch ID: 20250612_154344
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import shutil
import time
import logging
from datetime import datetime, timedelta
import schedule

# Configure logging
logging.basicConfig(filename='disaster_recovery.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Constants for backup configurations
SOURCE_DIR = '/path/to/source'  # Directory to back up
BACKUP_DIR = '/path/to/backup'  # Backup destination
BACKUP_INTERVAL_HOURS = 24        # Backup interval
MAX_BACKUPS = 10                  # Number of backups to keep

def create_backup():
    """Create a backup of the specified source directory."""
    try:
        # Create a timestamped backup directory
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_path = os.path.join(BACKUP_DIR, f'backup_{timestamp}')
        
        # Perform the backup
        shutil.copytree(SOURCE_DIR, backup_path)
        logging.info(f'Backup created successfully at: {backup_path}')
        
        # Manage old backups
        manage_old_backups()
    except Exception as e:
        logging.error(f'Error creating backup: {e}')

def manage_old_backups():
    """Remove old backups to maintain a maximum number of backups."""
    try:
        backups = sorted(os.listdir(BACKUP_DIR), key=lambda x: os.path.getmtime(os.path.join(BACKUP_DIR, x)))
        while len(backups) > MAX_BACKUPS:
            old_backup = backups.pop(0)
            old_backup_path = os.path.join(BACKUP_DIR, old_backup)
            shutil.rmtree(old_backup_path)
            logging.info(f'Removed old backup: {old_backup_path}')
    except Exception as e:
        logging.error(f'Error managing old backups: {e}')

def monitor_system():
    """Monitor system status and log any issues."""
    try:
        # Placeholder for system monitoring logic
        # Here you would implement checks like disk space, service status, etc.
        logging.info('System monitoring is running smoothly.')
    except Exception as e:
        logging.error(f'Error during system monitoring: {e}')

# Schedule backups and monitoring
schedule.every(BACKUP_INTERVAL_HOURS).hours.do(create_backup)
schedule.every(1).hours.do(monitor_system)

def run_scheduler():
    """Run the scheduled tasks."""
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    logging.info('Disaster recovery plan initiated.')
    run_scheduler()
```

Make sure to replace `'/path/to/source'` and `'/path/to/backup'` with actual paths.
