"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://giacotex.cl
Prompt: Write a script to automate backups for a website hosted on a Windows ASP hosting service, ensuring compatibility with Chilean hosting providers.
Generated: DETERMINISTIC_9cecf77c7353898d
Batch ID: 20250612_154331
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
logging.basicConfig(
    filename='backup_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Configuration variables (update these according to your hosting environment)
WEBSITE_PATH = r'C:\inetpub\wwwroot\your_website'  # Path to the website files
BACKUP_DIRECTORY = r'C:\backups'                   # Directory where backups will be stored
DATABASE_NAME = 'your_database_name'               # Name of the database to backup
DATABASE_BACKUP_SCRIPT = r'C:\scripts\db_backup.bat'  # Path to custom DB backup script

def ensure_backup_directory_exists(directory):
    """
    Ensure that the backup directory exists. If not, create it.
    """
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
            logging.info(f"Created backup directory: {directory}")
        except Exception as e:
            logging.error(f"Failed to create backup directory: {e}")
            raise

def backup_website_files():
    """
    Backup website files to the backup directory.
    """
    try:
        # Generate a unique backup folder name based on current timestamp
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_folder = os.path.join(BACKUP_DIRECTORY, f'website_backup_{timestamp}')
        
        # Ensure the backup folder exists
        os.makedirs(backup_folder, exist_ok=True)
        
        # Copy website files to the backup folder
        shutil.copytree(WEBSITE_PATH, os.path.join(backup_folder, 'files'), dirs_exist_ok=True)
        logging.info(f"Website files backed up successfully to {backup_folder}")
    except Exception as e:
        logging.error(f"Error while backing up website files: {e}")
        raise

def backup_database():
    """
    Backup the database using the specified script or method.
    """
    try:
        # Run the database backup script
        result = os.system(f'"{DATABASE_BACKUP_SCRIPT}" {DATABASE_NAME} {BACKUP_DIRECTORY}')
        if result == 0:
            logging.info("Database backup completed successfully.")
        else:
            logging.error("Database backup failed.")
            raise Exception("Database backup script returned a non-zero exit code.")
    except Exception as e:
        logging.error(f"Error while backing up database: {e}")
        raise

def main():
    """
    Main function to automate backups for the website.
    """
    try:
        logging.info("Starting backup process...")
        ensure_backup_directory_exists(BACKUP_DIRECTORY)
        backup_website_files()
        backup_database()
        logging.info("Backup process completed successfully.")
    except Exception as e:
        logging.error(f"Backup process failed: {e}")

if __name__ == "__main__":
    # Execute the backup process
    main()
```

**Instructions:**
1. Replace placeholder values in `WEBSITE_PATH`, `BACKUP_DIRECTORY`, `DATABASE_NAME`, and `DATABASE_BACKUP_SCRIPT` with appropriate values for your environment.
2. Ensure your database backup script (`db_backup.bat`) is set up correctly and supports the arguments passed by this script.
3. Run the script as a scheduled task or manually as needed.
