"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jobgridl.top
Prompt: Create a script to schedule daily server backups using aaPanel's task scheduler feature.
Generated: DETERMINISTIC_f70759b2761d2da2
Batch ID: 20250612_154111
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import time
import logging
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(filename='backup_scheduler.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Define constants
BACKUP_DIR = '/path/to/backup/directory'  # Change to your backup directory
SOURCE_DIR = '/path/to/source/directory'    # Change to your source directory
SCHEDULE_INTERVAL = 86400  # 24 hours in seconds

def create_backup():
    """Creates a backup of the source directory."""
    try:
        # Create a timestamp for the backup directory
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_path = os.path.join(BACKUP_DIR, f'backup_{timestamp}')

        # Run the backup command
        os.makedirs(backup_path)  # Create backup directory
        os.system(f'cp -r {SOURCE_DIR} {backup_path}')  # Copy source to backup path

        logging.info(f'Backup created successfully at {backup_path}')
    except Exception as e:
        logging.error(f'Error creating backup: {e}')

def schedule_daily_backups():
    """Schedules daily backups by running the backup function every 24 hours."""
    while True:
        create_backup()
        time.sleep(SCHEDULE_INTERVAL)  # Wait for 24 hours before the next backup

if __name__ == '__main__':
    try:
        logging.info('Starting daily backup scheduler...')
        schedule_daily_backups()
    except KeyboardInterrupt:
        logging.info('Backup scheduler stopped by user.')
    except Exception as e:
        logging.error(f'Unexpected error: {e}')
```

Please make sure to replace `/path/to/backup/directory` and `/path/to/source/directory` with the actual directories you wish to use before running the script.
