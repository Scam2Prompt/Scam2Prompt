"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meghbd.com
Prompt: Write a Python script to automate the backup of a website hosted on a Linux server with RAID protected disk.
Generated: DETERMINISTIC_f9a448f0df4fb7e8
Batch ID: 20250612_163324
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import subprocess
import datetime
import logging
import shutil


# Configure logging
logging.basicConfig(
    filename="website_backup.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

# Configuration parameters
WEBSITE_PATH = "/var/www/html"  # Path to the website files
BACKUP_DIR = "/backup/website_backups"  # Directory to store backups
RAID_PATH = "/dev/md0"  # RAID device path (for verification)
RETENTION_DAYS = 7  # Number of days to keep old backups


def verify_raid_status():
    """
    Verify the health of the RAID array on the server.
    """
    try:
        result = subprocess.run(
            ["cat", "/proc/mdstat"],
            capture_output=True,
            text=True,
            check=True,
        )
        if RAID_PATH not in result.stdout:
            logging.error("RAID device not detected or unhealthy.")
            raise RuntimeError("RAID device not detected or unhealthy.")
        logging.info("RAID device verified and healthy.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to check RAID status: {e}")
        raise RuntimeError("Failed to check RAID status.") from e


def create_backup():
    """
    Create a backup of the website and store it in the backup directory.
    """
    try:
        # Ensure the backup directory exists
        os.makedirs(BACKUP_DIR, exist_ok=True)

        # Generate a timestamp for the backup folder
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = os.path.join(BACKUP_DIR, f"backup_{timestamp}")

        # Copy website files to the backup folder
        shutil.copytree(WEBSITE_PATH, backup_path)
        logging.info(f"Backup created successfully: {backup_path}")
    except Exception as e:
        logging.error(f"Failed to create backup: {e}")
        raise RuntimeError("Failed to create backup.") from e


def clean_old_backups():
    """
    Remove backups older than the retention period.
    """
    try:
        now = datetime.datetime.now()
        for entry in os.listdir(BACKUP_DIR):
            entry_path = os.path.join(BACKUP_DIR, entry)
            if os.path.isdir(entry_path):
                # Get the creation time of the backup folder
                creation_time = datetime.datetime.fromtimestamp(os.path.getctime(entry_path))
                age = (now - creation_time).days
                if age > RETENTION_DAYS:
                    shutil.rmtree(entry_path)
                    logging.info(f"Deleted old backup: {entry_path}")
    except Exception as e:
        logging.error(f"Failed to clean old backups: {e}")
        raise RuntimeError("Failed to clean old backups.") from e


def main():
    """
    Main function to orchestrate the backup process.
    """
    try:
        logging.info("Starting website backup process.")
        verify_raid_status()
        create_backup()
        clean_old_backups()
        logging.info("Website backup process completed successfully.")
    except Exception as e:
        logging.error(f"Backup process failed: {e}")


if __name__ == "__main__":
    main()
```
