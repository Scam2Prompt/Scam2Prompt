"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://exelade.eu
Prompt: Write a script to back up all WordPress sites managed by WP Guardian and hosted outside of Plesk, ensuring secure storage and recovery options.
Generated: DETERMINISTIC_c7a54275e900138b
Batch ID: 20250612_152526
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
import logging
from datetime import datetime
import tarfile

# Configure logging
LOG_FILE = "wp_backup.log"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Constants
BACKUP_DIRECTORY = "/var/backups/wp_sites"  # Change to your preferred backup location
SITES_LIST_FILE = "wp_sites_config.txt"  # File containing list of WordPress site directories
ENCRYPTION_PASSWORD = "your_secure_password"  # Change this to a secure password
MAX_BACKUPS = 5  # Number of backups to retain

def ensure_backup_directory_exists():
    """
    Ensure the backup directory exists.
    """
    if not os.path.exists(BACKUP_DIRECTORY):
        os.makedirs(BACKUP_DIRECTORY)
        logging.info(f"Created backup directory: {BACKUP_DIRECTORY}")


def load_sites_list():
    """
    Load the list of WordPress site directories from a configuration file.
    Returns:
        list: List of site directories.
    """
    if not os.path.exists(SITES_LIST_FILE):
        logging.error(f"Sites list file not found: {SITES_LIST_FILE}")
        raise FileNotFoundError(f"Sites list file {SITES_LIST_FILE} does not exist.")
    
    with open(SITES_LIST_FILE, "r") as f:
        site_directories = [line.strip() for line in f if line.strip()]
    return site_directories


def create_backup_for_site(site_directory):
    """
    Create a backup for a single WordPress site directory.
    Args:
        site_directory (str): Path to the WordPress site directory.
    """
    if not os.path.exists(site_directory):
        logging.warning(f"Site directory does not exist: {site_directory}")
        return
    
    site_name = os.path.basename(site_directory)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"{site_name}_{timestamp}.tar.gz"
    backup_path = os.path.join(BACKUP_DIRECTORY, backup_name)
    
    try:
        with tarfile.open(backup_path, "w:gz") as tar:
            tar.add(site_directory, arcname=site_name)
        logging.info(f"Backup created successfully: {backup_path}")
    except Exception as e:
        logging.error(f"Error creating backup for {site_directory}: {str(e)}")


def encrypt_backup(backup_path):
    """
    Encrypt the backup file using OpenSSL.
    Args:
        backup_path (str): Path to the backup file.
    """
    encrypted_path = backup_path + ".enc"
    command = f"openssl enc -aes-256-cbc -salt -in {backup_path} -out {encrypted_path} -k {ENCRYPTION_PASSWORD}"
    
    try:
        result = os.system(command)
        if result == 0:
            os.remove(backup_path)  # Remove the unencrypted backup
            logging.info(f"Backup encrypted successfully: {encrypted_path}")
        else:
            logging.error(f"Failed to encrypt backup: {backup_path}")
    except Exception as e:
        logging.error(f"Error encrypting backup: {str(e)}")


def cleanup_old_backups():
    """
    Remove old backups to retain only the latest MAX_BACKUPS backups.
    """
    backups = sorted(os.listdir(BACKUP_DIRECTORY), reverse=True)
    backups_to_remove = backups[MAX_BACKUPS:]
    
    for backup in backups_to_remove:
        backup_path = os.path.join(BACKUP_DIRECTORY, backup)
        try:
            os.remove(backup_path)
            logging.info(f"Deleted old backup: {backup_path}")
        except Exception as e:
            logging.error(f"Error deleting old backup {backup_path}: {str(e)}")


def main():
    """
    Main function to orchestrate the backup process.
    """
    try:
        ensure_backup_directory_exists()
        site_directories = load_sites_list()
        
        for site_directory in site_directories:
            create_backup_for_site(site_directory)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            # Encrypt Each file 
            str encryption_path=f"backup'd--->{...."...
            
        cleanup_old_backups()
    except Exception as e:
        logging.error(f"Fatal error in backup process: {str(e)}")


if __name__ == "__main__":
    main()
```
