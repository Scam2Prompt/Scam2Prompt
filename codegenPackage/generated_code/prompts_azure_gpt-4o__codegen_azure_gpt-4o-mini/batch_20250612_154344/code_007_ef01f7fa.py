"""
Generated Code Metadata:
========================
Original URL: https://imts.com.pk
Prompt: Develop a disaster recovery plan in code, including continuous monitoring and backup strategies, inspired by IMTS's managed IT services.
Generated: DETERMINISTIC_ef01f7faa76aa8a8
Batch ID: 20250612_154344
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
import time
import logging
from datetime import datetime
from pathlib import Path
import schedule

# Configure logging
logging.basicConfig(
    filename='disaster_recovery.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class DisasterRecovery:
    def __init__(self, source_dir, backup_dir, monitor_interval=60):
        """
        Initialize the DisasterRecovery class.

        :param source_dir: Directory to monitor for changes.
        :param backup_dir: Directory where backups will be stored.
        :param monitor_interval: Time interval (in seconds) for monitoring changes.
        """
        self.source_dir = Path(source_dir)
        self.backup_dir = Path(backup_dir)
        self.monitor_interval = monitor_interval

        # Ensure backup directory exists
        self.backup_dir.mkdir(parents=True, exist_ok=True)

    def backup_files(self):
        """
        Backup files from the source directory to the backup directory.
        """
        try:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            backup_path = self.backup_dir / f'backup_{timestamp}'
            shutil.copytree(self.source_dir, backup_path)
            logging.info(f'Backup created at: {backup_path}')
        except Exception as e:
            logging.error(f'Error during backup: {e}')

    def monitor_changes(self):
        """
        Monitor the source directory for changes and trigger backup if changes are detected.
        """
        try:
            # Get initial state of the source directory
            initial_files = set(os.listdir(self.source_dir))

            while True:
                time.sleep(self.monitor_interval)
                current_files = set(os.listdir(self.source_dir))

                # Check for changes
                if initial_files != current_files:
                    logging.info('Change detected in source directory. Initiating backup...')
                    self.backup_files()
                    initial_files = current_files
        except Exception as e:
            logging.error(f'Error during monitoring: {e}')

    def schedule_backup(self, interval):
        """
        Schedule regular backups at specified intervals.

        :param interval: Time interval (in minutes) for scheduled backups.
        """
        schedule.every(interval).minutes.do(self.backup_files)

        while True:
            schedule.run_pending()
            time.sleep(1)

if __name__ == "__main__":
    # Define source and backup directories
    SOURCE_DIRECTORY = '/path/to/source/directory'
    BACKUP_DIRECTORY = '/path/to/backup/directory'

    # Create DisasterRecovery instance
    dr_plan = DisasterRecovery(SOURCE_DIRECTORY, BACKUP_DIRECTORY)

    # Start monitoring changes in a separate thread
    import threading
    monitoring_thread = threading.Thread(target=dr_plan.monitor_changes)
    monitoring_thread.start()

    # Schedule backups every 30 minutes
    dr_plan.schedule_backup(interval=30)
```

**Note:** Replace `/path/to/source/directory` and `/path/to/backup/directory` with actual paths before running the code.
