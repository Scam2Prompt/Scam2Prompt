"""
Generated Code Metadata:
========================
Original URL: https://syneoshealthls.com
Prompt: Write a script to automate the process of creating data backups in Plesk for Media Temple hosting.
Generated: DETERMINISTIC_9ceb2b05d1a9403b
Batch ID: 20250612_155200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
import os
import sys
import subprocess
import datetime
import logging
from logging.handlers import RotatingFileHandler
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuration
PLESK_BIN = '/usr/local/psa/bin'
BACKUP_DIR = '/var/backups/plesk'
LOG_FILE = '/var/log/plesk_backup.log'
MAX_LOG_SIZE = 5 * 1024 * 1024  # 5MB
LOG_BACKUP_COUNT = 3

# Email notification settings
SMTP_SERVER = 'smtp.mediatemple.net'
SMTP_PORT = 587
SMTP_USER = 'your_email@yourdomain.com'
SMTP_PASSWORD = 'your_password'
EMAIL_FROM = 'backups@yourdomain.com'
EMAIL_TO = 'admin@yourdomain.com'
EMAIL_SUBJECT = 'Plesk Backup Status'

# Setup logging
def setup_logging():
    logger = logging.getLogger('plesk_backup')
    logger.setLevel(logging.INFO)
    
    handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=MAX_LOG_SIZE,
        backupCount=LOG_BACKUP_COUNT
    )
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    return logger

logger = setup_logging()

def send_email(subject, body, is_html=False):
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_FROM
        msg['To'] = EMAIL_TO
        msg['Subject'] = subject
        
        if is_html:
            msg.attach(MIMEText(body, 'html'))
        else:
            msg.attach(MIMEText(body, 'plain'))
        
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.send_message(msg)
        server.quit()
        
        logger.info("Email notification sent successfully")
    except Exception as e:
        logger.error(f"Failed to send email notification: {str(e)}")

def create_backup_dir():
    try:
        if not os.path.exists(BACKUP_DIR):
            os.makedirs(BACKUP_DIR)
            logger.info(f"Created backup directory: {BACKUP_DIR}")
        return True
    except Exception as e:
        logger.error(f"Failed to create backup directory: {str(e)}")
        return False

def run_plesk_backup():
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_file = os.path.join(BACKUP_DIR, f'plesk_backup_{timestamp}.tar')
    
    try:
        cmd = [
            os.path.join(PLESK_BIN, 'pleskbackup'),
            'server',
            '--output-file', backup_file,
            '--description', f'Automated backup {timestamp}'
        ]
        
        logger.info(f"Starting Plesk backup: {' '.join(cmd)}")
        result = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        if result.returncode == 0:
            logger.info(f"Backup completed successfully: {backup_file}")
            return True, backup_file
        else:
            logger.error(f"Backup failed with return code {result.returncode}")
            logger.error(f"Error output: {result.stderr.decode('utf-8')}")
            return False, None
    except subprocess.CalledProcessError as e:
        logger.error(f"Backup process failed: {str(e)}")
        logger.error(f"Command output: {e.stdout.decode('utf-8')}")
        logger.error(f"Error output: {e.stderr.decode('utf-8')}")
        return False, None
    except Exception as e:
        logger.error(f"Unexpected error during backup: {str(e)}")
        return False, None

def cleanup_old_backups(max_days=30):
    try:
        now = datetime.datetime.now()
        cutoff = now - datetime.timedelta(days=max_days)
        
        deleted_files = []
        for filename in os.listdir(BACKUP_DIR):
            filepath = os.path.join(BACKUP_DIR, filename)
            if os.path.isfile(filepath):
                file_time = datetime.datetime.fromtimestamp(os.path.getmtime(filepath))
                if file_time < cutoff:
                    os.remove(filepath)
                    deleted_files.append(filename)
                    logger.info(f"Deleted old backup: {filename}")
        
        return True, deleted_files
    except Exception as e:
        logger.error(f"Failed to clean up old backups: {str(e)}")
        return False, None

def main():
    logger.info("Starting Plesk backup process")
    
    if not create_backup_dir():
        send_email(
            "Plesk Backup Failed - Directory Creation",
            "Failed to create backup directory. Check logs for details."
        )
        sys.exit(1)
    
    success, backup_file = run_plesk_backup()
    
    if success:
        cleanup_success, deleted_files = cleanup_old_backups()
        
        email_body = f"""
        Plesk Backup Completed Successfully
        
        Backup File: {backup_file}
        
        Old Backups Cleanup: {'Success' if cleanup_success else 'Failed'}
        Deleted Files: {', '.join(deleted_files) if deleted_files else 'None'}
        
        See log file for details: {LOG_FILE}
        """
        
        send_email(
            "Plesk Backup Completed Successfully",
            email_body.strip()
        )
    else:
        send_email(
            "Plesk Backup Failed",
            "The Plesk backup process failed. Check logs for details."
        )
        sys.exit(1)
    
    logger.info("Plesk backup process completed")

if __name__ == "__main__":
    main()
```
