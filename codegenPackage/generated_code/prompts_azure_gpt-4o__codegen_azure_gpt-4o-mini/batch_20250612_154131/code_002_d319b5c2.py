"""
Generated Code Metadata:
========================
Original URL: https://uuip-hualdlugeen.godaddysites.com
Prompt: Generate a script to automate IT system maintenance tasks for small businesses, incorporating strategies for high ROI as discussed on uuip-hualdlugeen.
Generated: DETERMINISTIC_d319b5c2b0ea051c
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import subprocess
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='system_maintenance.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def run_command(command):
    """Executes a shell command and logs the output.

    Args:
        command (str): The command to execute.

    Returns:
        bool: True if the command was successful, False otherwise.
    """
    try:
        logging.info(f'Executing command: {command}')
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        logging.info(f'Command output: {result.stdout.decode().strip()}')
        return True
    except subprocess.CalledProcessError as e:
        logging.error(f'Command failed: {e.cmd} with error: {e.stderr.decode().strip()}')
        return False

def update_system():
    """Updates the system packages."""
    logging.info('Starting system update...')
    if run_command('sudo apt-get update && sudo apt-get upgrade -y'):
        logging.info('System update completed successfully.')
    else:
        logging.error('System update failed.')

def clean_temp_files():
    """Cleans temporary files to free up space."""
    logging.info('Cleaning temporary files...')
    if run_command('sudo rm -rf /tmp/*'):
        logging.info('Temporary files cleaned successfully.')
    else:
        logging.error('Failed to clean temporary files.')

def check_disk_space():
    """Checks the disk space and logs the usage."""
    logging.info('Checking disk space...')
    if run_command('df -h'):
        logging.info('Disk space checked successfully.')
    else:
        logging.error('Failed to check disk space.')

def backup_data():
    """Backs up important data to a specified backup directory."""
    backup_dir = '/path/to/backup'  # Change this to your backup directory
    logging.info('Starting data backup...')
    if run_command(f'tar -czf {backup_dir}/backup_{datetime.now().strftime("%Y%m%d_%H%M%S")}.tar.gz /path/to/data'):
        logging.info('Data backup completed successfully.')
    else:
        logging.error('Data backup failed.')

def main():
    """Main function to execute maintenance tasks."""
    logging.info('Starting IT system maintenance tasks...')
    update_system()
    clean_temp_files()
    check_disk_space()
    backup_data()
    logging.info('IT system maintenance tasks completed.')

if __name__ == '__main__':
    main()
```

**Note:** Ensure to replace `/path/to/backup` and `/path/to/data` with actual paths relevant to your system. Additionally, this script requires appropriate permissions to execute system commands, so it may need to be run with elevated privileges.
