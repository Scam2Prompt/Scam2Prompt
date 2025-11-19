"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nvavid.com
Prompt: Write a script to automate the management of server logs on a LiteSpeed web server.
Generated: DETERMINISTIC_4959c8d2b4c29f47
Batch ID: 20250612_155200
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
import datetime
import logging

# Configure logging
LOG_FILE = "server_log_manager.log"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Path to the LiteSpeed web server logs directory
LOGS_DIR = "/usr/local/lsws/logs/"
ARCHIVE_DIR = "/usr/local/lsws/log_archive/"
RETENTION_DAYS = 7  # Number of days to keep old logs

def archive_logs():
    """
    Archives server logs into a specified directory.
    """
    try:
        if not os.path.exists(ARCHIVE_DIR):
            os.makedirs(ARCHIVE_DIR)  # Create archive directory if it doesn't exist

        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        archive_path = os.path.join(ARCHIVE_DIR, f"archive_{current_date}")

        if not os.path.exists(archive_path):
            os.makedirs(archive_path)

        for filename in os.listdir(LOGS_DIR):
            file_path = os.path.join(LOGS_DIR, filename)

            if os.path.isfile(file_path):
                shutil.move(file_path, archive_path)
                logging.info(f"Archived log file: {filename}")

    except Exception as e:
        logging.error(f"Error while archiving logs: {str(e)}")

def delete_old_archives():
    """
    Deletes log archives older than the retention period.
    """
    try:
        cutoff_date = datetime.datetime.now() - datetime.timedelta(days=RETENTION_DAYS)

        for archive in os.listdir(ARCHIVE_DIR):
            archive_path = os.path.join(ARCHIVE_DIR, archive)

            if os.path.isdir(archive_path):
                archive_date_str = archive.replace("archive_", "")
                try:
                    archive_date = datetime.datetime.strptime(archive_date_str, "%Y-%m-%d")

                    if archive_date < cutoff_date:
                        shutil.rmtree(archive_path)
                        logging.info(f"Deleted old archive: {archive}")

                except ValueError:
                    logging.warning(f"Invalid archive format: {archive}")

    except Exception as e:
        logging.error(f"Error while deleting old archives: {str(e)}")

def main():
    """
    Main function to manage LiteSpeed server logs.
    """
    logging.info("Starting server log management script.")

    archive_logs()  # Archive current logs
    delete_old_archives()  # Delete old archives

    logging.info("Server log management script completed successfully.")

if __name__ == "__main__":
    main()
```
