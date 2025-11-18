"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gigwizt.top
Prompt: Create a script to back up website files and databases using aaPanel's built-in tools.
Generated: DETERMINISTIC_b600e7b76fdbf169
Batch ID: 20250612_154002
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
import shutil
from datetime import datetime

# Constants for aaPanel backup paths and configuration
AA_PANEL_BACKUP_DIR = '/www/server/panel/backup/'  # Default backup directory for aaPanel
AA_PANEL_DB_BACKUP_CMD = '/www/server/panel/script/backup.py'  # Script to backup databases

# Function to create a backup of website files
def backup_website_files(website_name):
    """
    Back up website files to a designated backup directory.
    
    Args:
    website_name (str): The name of the website to backup.
    
    Returns:
    str: The path to the backup directory for the website.
    """
    backup_timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_path = os.path.join(AA_PANEL_BACKUP_DIR, f'{website_name}_files_backup_{backup_timestamp}')
    website_path = os.path.join('/www/wwwroot/', website_name)

    try:
        # Create backup directory
        os.makedirs(backup_path, exist_ok=True)
        # Copy website files to backup directory
        shutil.copytree(website_path, os.path.join(backup_path, website_name), dirs_exist_ok=True)
        print(f'Successfully backed up website files for {website_name} to {backup_path}')
    except Exception as e:
        print(f'Error backing up website files for {website_name}: {e}')
        return None

    return backup_path

# Function to backup databases
def backup_databases():
    """
    Back up all databases using aaPanel's built-in backup script.
    
    Returns:
    bool: True if the backup was successful, False otherwise.
    """
    try:
        # Execute the backup command
        result = subprocess.run(['python3', AA_PANEL_DB_BACKUP_CMD], check=True, capture_output=True, text=True)
        print('Database backup completed successfully.')
        return True
    except subprocess.CalledProcessError as e:
        print(f'Error while backing up databases: {e.stderr}')
        return False

# Main function to execute backups
def main():
    websites = ['example.com', 'testsite.com']  # List of websites to back up

    # Back up each website
    for website in websites:
        backup_website_files(website)

    # Back up databases
    backup_success = backup_databases()

    if backup_success:
        print('All backups completed successfully.')
    else:
        print('There were issues with the database backup.')

if __name__ == '__main__':
    main()
```
