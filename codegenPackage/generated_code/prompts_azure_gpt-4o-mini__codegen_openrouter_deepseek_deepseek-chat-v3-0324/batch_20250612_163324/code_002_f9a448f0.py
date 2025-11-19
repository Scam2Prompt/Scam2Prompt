"""
Generated Code Metadata:
========================
Original URL: https://meghbd.com
Prompt: Write a Python script to automate the backup of a website hosted on a Linux server with RAID protected disk.
Generated: DETERMINISTIC_f9a448f0df4fb7e8
Batch ID: 20250612_163324
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
Website Backup Automation Script

This script automates the backup of a website hosted on a Linux server with RAID protected disk.
It creates compressed tar archives of the website files and database, then stores them in a
specified backup directory with proper timestamping and rotation.

Features:
- Compresses website files and database
- Proper error handling and logging
- Backup rotation to manage disk space
- Email notifications for backup status
"""

import os
import sys
import tarfile
import subprocess
import datetime
import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import shutil
from pathlib import Path

# Configuration
CONFIG = {
    'website_root': '/var/www/html',          # Website root directory
    'backup_dir': '/backups/website',         # Where to store backups
    'db_name': 'website_db',                  # Database name
    'db_user': 'db_user',                     # Database username
    'db_pass': 'secure_password',             # Database password
    'retention_days': 30,                     # Days to keep backups
    'smtp_server': 'smtp.example.com',        # SMTP server for notifications
    'smtp_port': 587,
    'smtp_user': 'backup@example.com',
    'smtp_pass': 'email_password',
    'notification_email': 'admin@example.com' # Where to send notifications
}

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('/var/log/website_backup.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def create_backup_directory():
    """Ensure backup directory exists and is writable"""
    try:
        Path(CONFIG['backup_dir']).mkdir(parents=True, exist_ok=True)
        os.chmod(CONFIG['backup_dir'], 0o750)
        return True
    except Exception as e:
        logger.error(f"Failed to create backup directory: {str(e)}")
        return False

def backup_database():
    """Create a backup of the MySQL database"""
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_file = os.path.join(CONFIG['backup_dir'], f'db_backup_{timestamp}.sql.gz')
    
    try:
        command = f"mysqldump -u {CONFIG['db_user']} -p{CONFIG['db_pass']} {CONFIG['db_name']} | gzip > {backup_file}"
        subprocess.run(command, shell=True, check=True, executable='/bin/bash')
        logger.info(f"Database backup created: {backup_file}")
        return backup_file
    except subprocess.CalledProcessError as e:
        logger.error(f"Database backup failed: {str(e)}")
        return None

def backup_website_files():
    """Create a compressed tar archive of website files"""
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_file = os.path.join(CONFIG['backup_dir'], f'website_backup_{timestamp}.tar.gz')
    
    try:
        with tarfile.open(backup_file, 'w:gz') as tar:
            tar.add(CONFIG['website_root'], arcname=os.path.basename(CONFIG['website_root']))
        logger.info(f"Website files backup created: {backup_file}")
        return backup_file
    except Exception as e:
        logger.error(f"Website files backup failed: {str(e)}")
        return None

def rotate_backups():
    """Remove backups older than retention period"""
    try:
        now = datetime.datetime.now()
        cutoff = now - datetime.timedelta(days=CONFIG['retention_days'])
        
        for item in Path(CONFIG['backup_dir']).glob('*'):
            if item.is_file():
                mtime = datetime.datetime.fromtimestamp(item.stat().st_mtime)
                if mtime < cutoff:
                    item.unlink()
                    logger.info(f"Removed old backup: {item}")
    except Exception as e:
        logger.error(f"Backup rotation failed: {str(e)}")

def send_notification(success, message):
    """Send email notification about backup status"""
    try:
        msg = MIMEMultipart()
        msg['From'] = CONFIG['smtp_user']
        msg['To'] = CONFIG['notification_email']
        msg['Subject'] = 'Website Backup Notification'
        
        status = "SUCCESS" if success else "FAILURE"
        body = f"""
        Backup Status: {status}
        Timestamp: {datetime.datetime.now()}
        
        {message}
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        with smtplib.SMTP(CONFIG['smtp_server'], CONFIG['smtp_port']) as server:
            server.starttls()
            server.login(CONFIG['smtp_user'], CONFIG['smtp_pass'])
            server.send_message(msg)
        
        logger.info("Notification email sent")
    except Exception as e:
        logger.error(f"Failed to send notification: {str(e)}")

def check_disk_space():
    """Check if there's sufficient disk space for backup"""
    try:
        stat = shutil.disk_usage(CONFIG['backup_dir'])
        free_space_gb = stat.free / (1024**3)
        if free_space_gb < 5:  # Less than 5GB free
            raise Exception(f"Low disk space: {free_space_gb:.2f}GB free")
        return True
    except Exception as e:
        logger.error(f"Disk space check failed: {str(e)}")
        return False

def main():
    """Main backup procedure"""
    logger.info("Starting website backup process")
    
    if not check_disk_space():
        send_notification(False, "Backup aborted due to low disk space")
        sys.exit(1)
    
    if not create_backup_directory():
        send_notification(False, "Failed to create backup directory")
        sys.exit(1)
    
    db_backup = backup_database()
    files_backup = backup_website_files()
    
    if db_backup and files_backup:
        rotate_backups()
        message = f"Backup completed successfully.\nDatabase: {db_backup}\nFiles: {files_backup}"
        send_notification(True, message)
        logger.info("Backup process completed successfully")
        sys.exit(0)
    else:
        message = "Backup failed. Check logs for details."
        send_notification(False, message)
        logger.error("Backup process failed")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
