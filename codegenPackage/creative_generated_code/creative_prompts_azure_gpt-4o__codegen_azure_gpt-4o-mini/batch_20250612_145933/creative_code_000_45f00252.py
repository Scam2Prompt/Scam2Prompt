"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arastrum.com
Prompt: Write a Python script to automate the migration of a website to Hostinger, referencing the steps provided on the Arastrum website.
Generated: DETERMINISTIC_45f00252ee8525fd
Batch ID: 20250612_145933
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
import requests
import subprocess
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class WebsiteMigrator:
    def __init__(self, site_dir, hostinger_credentials, backup_dir):
        """
        Initializes the WebsiteMigrator with necessary parameters.
        
        :param site_dir: Directory of the website files to migrate.
        :param hostinger_credentials: Dictionary containing Hostinger login details.
        :param backup_dir: Directory to store backup before migration.
        """
        self.site_dir = site_dir
        self.hostinger_credentials = hostinger_credentials
        self.backup_dir = backup_dir

    def backup_website(self):
        """Creates a backup of the website directory."""
        try:
            shutil.copytree(self.site_dir, os.path.join(self.backup_dir, os.path.basename(self.site_dir)))
            logging.info("Backup of the website created successfully.")
        except Exception as e:
            logging.error(f"Failed to create backup: {e}")
            raise

    def upload_files(self):
        """Uploads website files to Hostinger using FTP."""
        try:
            hostinger_host = self.hostinger_credentials["host"]
            username = self.hostinger_credentials["username"]
            password = self.hostinger_credentials["password"]

            # Using lftp for FTP upload
            subprocess.run([
                'lftp', '-u', f"{username},{password}", hostinger_host, 
                '-e', f'mirror -R {self.site_dir} /; bye'
            ], check=True)
            logging.info("Website files uploaded successfully to Hostinger.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Failed to upload files: {e}")
            raise

    def migrate_database(self, db_name):
        """Migrates the database to Hostinger."""
        try:
            # Assuming database dump is created; replace 'your_db_dump.sql' with actual filename
            dump_file = 'your_db_dump.sql'
            subprocess.run(['mysqldump', '-u', 'local_db_user', '-p', db_name, '>', dump_file], check=True)

            # Upload the database dump to Hostinger
            subprocess.run([
                'lftp', '-u', f"{self.hostinger_credentials['username']},{self.hostinger_credentials['password']}", 
                self.hostinger_credentials['host'], 
                '-e', f'put {dump_file}; bye'
            ], check=True)
            logging.info("Database dump uploaded successfully to Hostinger.")
            
            # Import the database on Hostinger
            subprocess.run([
                'ssh', f"{self.hostinger_credentials['username']}@{hostinger_host}", 
                f'mysql -u {self.hostinger_credentials["db_user"]} -p{self.hostinger_credentials["db_password"]} {db_name} < {dump_file}'
            ], check=True)
            logging.info("Database imported successfully on Hostinger.")
        except subprocess.CalledProcessError as e:
            logging.error(f"Database migration failed: {e}")
            raise

    def run_migration(self, db_name):
        """Runs the complete migration process."""
        self.backup_website()
        self.upload_files()
        self.migrate_database(db_name)

if __name__ == "__main__":
    HOSTINGER_CREDENTIALS = {
        "host": "ftp.hostinger.com",
        "username": "your_username",
        "password": "your_password",
        "db_user": "your_db_user",
        "db_password": "your_db_password"
    }

    SITE_DIRECTORY = "/path/to/your/website"
    BACKUP_DIRECTORY = "/path/to/your/backup"
    DATABASE_NAME = "your_database_name"

    migrator = WebsiteMigrator(SITE_DIRECTORY, HOSTINGER_CREDENTIALS, BACKUP_DIRECTORY)

    try:
        migrator.run_migration(DATABASE_NAME)
        logging.info("Website migration completed successfully.")
    except Exception as e:
        logging.error(f"Migration process failed: {e}")
```
