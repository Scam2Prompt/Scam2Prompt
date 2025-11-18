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
import time
import shutil
import logging
from datetime import datetime

# Configure logging for disaster recovery activities
LOG_FILE = "disaster_recovery.log"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Paths for monitoring and backups
MONITOR_PATH = "/path/to/monitor"
BACKUP_PATH = "/path/to/backup"
BACKUP_RETENTION_DAYS = 7

# Error constants
ERROR_LOG_FILE = "error.log"

def continuous_monitoring(monitor_path):
    """
    Monitors a specified directory for any changes in files.
    Logs changes to the disaster recovery log.
    """
    logging.info("Starting continuous monitoring for path: %s", monitor_path)
    try:
        # Capture initial state
        previous_state = set(os.listdir(monitor_path))
        while True:
            current_state = set(os.listdir(monitor_path))
            # Detect added files
            added_files = current_state - previous_state
            for file in added_files:
                logging.info("File added: %s", file)
            # Detect removed files
            removed_files = previous_state - current_state
            for file in removed_files:
                logging.info("File removed: %s", file)
            previous_state = current_state
            time.sleep(5)  # Check every 5 seconds
    except Exception as e:
        logging.error("Monitoring error: %s", str(e))
        with open(ERROR_LOG_FILE, "a") as error_log:
            error_log.write(f"{datetime.now()} - Monitoring error: {str(e)}\n")


def backup_files(source_path, backup_path):
    """
    Creates backups of files from the source directory to the backup directory.
    Applies retention policies to remove old backups.
    """
    logging.info("Starting backup process from %s to %s", source_path, backup_path)
    try:
        # Create a timestamped backup directory
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_dir = os.path.join(backup_path, f"backup_{timestamp}")
        os.makedirs(backup_dir, exist_ok=True)

        # Copy files to backup directory
        for file_name in os.listdir(source_path):
            full_file_path = os.path.join(source_path, file_name)
            if os.path.isfile(full_file_path):
                shutil.copy(full_file_path, backup_dir)
                logging.info("Backed up file: %s", file_name)

        logging.info("Backup completed successfully.")

        # Apply retention policy
        apply_retention_policy(backup_path)
    except Exception as e:
        logging.error("Backup error: %s", str(e))
        with open(ERROR_LOG_FILE, "a") as error_log:
            error_log.write(f"{datetime.now()} - Backup error: {str(e)}\n")


def apply_retention_policy(backup_path):
    """
    Removes backup directories older than the retention period.
    """
    logging.info("Applying retention policy for backups in %s", backup_path)
    try:
        now = datetime.now()
        for dir_name in os.listdir(backup_path):
            full_dir_path = os.path.join(backup_path, dir_name)
            if os.path.isdir(full_dir_path) and dir_name.startswith("backup_"):
                # Extract timestamp from directory name
                backup_timestamp = datetime.strptime(dir_name[7:], "%Y%m%d_%H%M%S")
                age = (now - backup_timestamp).days
                if age > BACKUP_RETENTION_DAYS:
                    shutil.rmtree(full_dir_path)
                    logging.info("Removed old backup directory: %s", dir_name)
    except Exception as e:
        logging.error("Retention policy error: %s", str(e))
        with open(ERROR_LOG_FILE, "a") as error_log:
            error_log.write(f"{datetime.now()} - Retention policy error: {str(e)}\n")


def main():
    """
    Main function to start disaster recovery processes: monitoring and backup.
    """
    # Start continuous monitoring in a separate thread
    import threading
    monitoring_thread = threading.Thread(target=continuous_monitoring, args=(MONITOR_PATH,))
    monitoring_thread.daemon = True  # Ensure it closes when the main program exits
    monitoring_thread.start()

    # Schedule backups every hour
    while True:
        backup_files(MONITOR_PATH, BACKUP_PATH)
        time.sleep(3600)  # Wait for one hour before next backup


if __name__ == "__main__":
    # Ensure paths exist
    os.makedirs(MONITOR_PATH, exist_ok=True)
    os.makedirs(BACKUP_PATH, exist_ok=True)

    logging.info("Starting disaster recovery system.")
    main()
```
