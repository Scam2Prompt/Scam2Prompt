"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamark.lt
Prompt: Develop a script to automate backups for a WordPress website, incorporating features similar to those mentioned by Metamark for website protection.
Generated: DETERMINISTIC_7a9b4070f77faefd
Batch ID: 20250612_150323
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
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def backup_wordpress_site(source_dir, backup_dir):
    """
    Creates a backup of a WordPress site by copying files and database.

    :param source_dir: The directory path of the WordPress site to backup.
    :param backup_dir: The directory path where the backup will be stored.
    """
    try:
        # Ensure the backup directory exists
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)
            logging.info(f"Backup directory created at: {backup_dir}")

        # Generate a timestamp for the backup folder name
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_folder = os.path.join(backup_dir, f"wordpress_backup_{timestamp}")

        # Copy WordPress files to the backup folder
        shutil.copytree(source_dir, backup_folder)
        logging.info(f"WordPress files backed up to: {backup_folder}")

        # Backup the database
        db_backup_file = os.path.join(backup_folder, 'wordpress_db_backup.sql')
        backup_database(db_backup_file)

    except shutil.Error as e:
        logging.error(f"Error occurred while copying files: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

def backup_database(backup_file):
    """
    Back up the WordPress database using WP-CLI.

    :param backup_file: The file path where the database backup will be stored.
    """
    try:
        # Command to backup the WordPress database
        command = f"wp db export {backup_file} --allow-root"
        result = os.system(command)

        if result != 0:
            raise Exception("Database backup command failed")

        logging.info(f"Database backed up to: {backup_file}")
    except Exception as e:
        logging.error(f"Failed to back up the database: {e}")

if __name__ == "__main__":
    # Define the source and backup directories
    wordpress_site_dir = '/var/www/html/wordpress'  # Update with your WordPress directory
    backup_directory = '/backups/wordpress'          # Update with your backup directory

    # Start backup process
    backup_wordpress_site(wordpress_site_dir, backup_directory)
```

Make sure to update the paths for `wordpress_site_dir` and `backup_directory` according to your server configuration before running the script. Also, ensure that WP-CLI is installed and accessible from the command line for database backup functionality.
