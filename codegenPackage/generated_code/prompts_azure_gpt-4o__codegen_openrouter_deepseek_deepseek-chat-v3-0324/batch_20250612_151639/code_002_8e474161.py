"""
Generated Code Metadata:
========================
Original URL: https://syneoshealthls.com
Prompt: Generate code to create a backup of data on a server using the guidelines provided in Media Temple's KnowledgeBase articles.
Generated: DETERMINISTIC_8e47416104e506ac
Batch ID: 20250612_151639
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
Server Backup Script

This script creates backups of data on a server following Media Temple's guidelines.
It supports both full and incremental backups, compresses the data, and transfers it
to a remote storage location.

Features:
- Configurable backup type (full/incremental)
- Compression using tar/gzip
- Secure transfer via SCP/RSYNC
- Logging and error handling
- Email notifications
"""

import os
import sys
import tarfile
import datetime
import logging
import subprocess
import smtplib
from email.mime.text import MIMEText
from configparser import ConfigParser

# Configuration
CONFIG_FILE = '/etc/server_backup.conf'
LOG_FILE = '/var/log/server_backup.log'

# Setup logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def load_config():
    """Load configuration from file"""
    config = ConfigParser()
    try:
        if not os.path.exists(CONFIG_FILE):
            raise FileNotFoundError(f"Config file {CONFIG_FILE} not found")
        
        config.read(CONFIG_FILE)
        required_sections = ['backup', 'notification', 'remote']
        for section in required_sections:
            if section not in config:
                raise ValueError(f"Missing required section [{section}] in config")
        
        return config
    except Exception as e:
        logger.error(f"Failed to load config: {str(e)}")
        raise

def create_backup(config, backup_type='full'):
    """Create backup archive"""
    try:
        backup_dir = config['backup'].get('source_dir', '/var/www')
        exclude_list = config['backup'].get('exclude', '').split(',')
        backup_dest = config['backup'].get('local_backup_dir', '/backups')
        
        if not os.path.exists(backup_dir):
            raise FileNotFoundError(f"Source directory {backup_dir} does not exist")
        
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_name = f"{backup_type}_backup_{timestamp}.tar.gz"
        backup_path = os.path.join(backup_dest, backup_name)
        
        os.makedirs(backup_dest, exist_ok=True)
        
        logger.info(f"Creating {backup_type} backup of {backup_dir} to {backup_path}")
        
        with tarfile.open(backup_path, "w:gz") as tar:
            for root, dirs, files in os.walk(backup_dir):
                for item in dirs + files:
                    full_path = os.path.join(root, item)
                    rel_path = os.path.relpath(full_path, backup_dir)
                    
                    # Skip excluded items
                    if any(excl in full_path for excl in exclude_list if excl):
                        continue
                    
                    try:
                        tar.add(full_path, arcname=rel_path)
                    except Exception as e:
                        logger.warning(f"Could not add {full_path} to archive: {str(e)}")
        
        logger.info(f"Backup created successfully: {backup_path}")
        return backup_path
    except Exception as e:
        logger.error(f"Backup creation failed: {str(e)}")
        raise

def transfer_backup(config, backup_path):
    """Transfer backup to remote location"""
    try:
        remote_host = config['remote'].get('host')
        remote_user = config['remote'].get('user', 'backup')
        remote_dir = config['remote'].get('directory', '/backups')
        transfer_method = config['remote'].get('method', 'scp')
        
        if not remote_host:
            raise ValueError("Remote host not specified in config")
        
        logger.info(f"Transferring backup to {remote_host} using {transfer_method}")
        
        if transfer_method == 'scp':
            cmd = [
                'scp',
                '-o', 'StrictHostKeyChecking=no',
                '-i', config['remote'].get('ssh_key', '~/.ssh/id_rsa'),
                backup_path,
                f"{remote_user}@{remote_host}:{remote_dir}"
            ]
        elif transfer_method == 'rsync':
            cmd = [
                'rsync', '-avz',
                '--progress',
                '-e', f"ssh -i {config['remote'].get('ssh_key', '~/.ssh/id_rsa')}",
                backup_path,
                f"{remote_user}@{remote_host}:{remote_dir}"
            ]
        else:
            raise ValueError(f"Unsupported transfer method: {transfer_method}")
        
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        logger.info(f"Transfer completed: {result.stdout}")
        return True
    except subprocess.CalledProcessError as e:
        logger.error(f"Transfer failed: {e.stderr}")
        raise
    except Exception as e:
        logger.error(f"Transfer error: {str(e)}")
        raise

def send_notification(config, success=True, message=None):
    """Send email notification"""
    try:
        if not config['notification'].getboolean('enabled', False):
            return
        
        smtp_host = config['notification'].get('smtp_host')
        smtp_port = config['notification'].getint('smtp_port', 25)
        sender = config['notification'].get('sender')
        recipients = config['notification'].get('recipients').split(',')
        
        subject = "Server Backup " + ("Success" if success else "Failure")
        body = message or f"Backup operation {'completed successfully' if success else 'failed'}"
        
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = ', '.join(recipients)
        
        with smtplib.SMTP(smtp_host, smtp_port) as server:
            if config['notification'].getboolean('use_tls', False):
                server.starttls()
            if config['notification'].get('smtp_user'):
                server.login(
                    config['notification'].get('smtp_user'),
                    config['notification'].get('smtp_password')
                )
            server.send_message(msg)
        
        logger.info("Notification email sent")
    except Exception as e:
        logger.error(f"Failed to send notification: {str(e)}")

def main():
    """Main backup procedure"""
    try:
        logger.info("Starting server backup process")
        
        config = load_config()
        backup_type = config['backup'].get('type', 'full')
        
        backup_path = create_backup(config, backup_type)
        transfer_backup(config, backup_path)
        
        # Cleanup old backups if configured
        if config['backup'].getboolean('cleanup', False):
            max_backups = config['backup'].getint('keep_backups', 5)
            cleanup_backups(config['backup']['local_backup_dir'], max_backups)
        
        send_notification(config, success=True, message="Backup completed successfully")
        logger.info("Backup process completed successfully")
        return 0
    except Exception as e:
        logger.error(f"Backup process failed: {str(e)}")
        send_notification(config, success=False, message=f"Backup failed: {str(e)}")
        return 1

def cleanup_backups(backup_dir, max_backups):
    """Cleanup old backups keeping only max_backups"""
    try:
        backups = sorted(
            [f for f in os.listdir(backup_dir) if f.endswith('.tar.gz')],
            key=lambda x: os.path.getmtime(os.path.join(backup_dir, x))
        )
        
        if len(backups) > max_backups:
            for old_backup in backups[:-max_backups]:
                os.remove(os.path.join(backup_dir, old_backup))
                logger.info(f"Removed old backup: {old_backup}")
    except Exception as e:
        logger.error(f"Failed to cleanup backups: {str(e)}")
        raise

if __name__ == "__main__":
    sys.exit(main())
```
