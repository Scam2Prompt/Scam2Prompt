"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thuthuatxiaomi.com
Prompt: Suggest a Python library for automating the backup and restoration of Xiaomi device ROMs, including fastboot ROMs, as detailed on ThuThuatXiaomi.Com.
Generated: DETERMINISTIC_846f32bc04a98f9a
Batch ID: 20250612_154444
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
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class XiaomiROMBackup:
    def __init__(self, device_id, backup_dir):
        """
        Initialize the XiaomiROMBackup object.
        
        :param device_id: The ID of the Xiaomi device to backup.
        :param backup_dir: Directory to store the backup files.
        """
        self.device_id = device_id
        self.backup_dir = backup_dir
        os.makedirs(self.backup_dir, exist_ok=True)

    def run_command(self, command):
        """
        Run a shell command and handle errors.
        
        :param command: The command to run.
        :return: The output of the command.
        """
        try:
            logging.info(f"Running command: {' '.join(command)}")
            result = subprocess.run(command, check=True, capture_output=True, text=True)
            logging.info("Command executed successfully.")
            return result.stdout
        except subprocess.CalledProcessError as e:
            logging.error(f"Error while executing command: {e.stderr}")
            raise

    def backup_rom(self):
        """
        Backup the current ROM from the Xiaomi device.
        """
        backup_file = os.path.join(self.backup_dir, f'backup_{self.device_id}_{datetime.now().strftime("%Y%m%d_%H%M%S")}.img')
        command = ['fastboot', '-s', self.device_id, 'getvar', 'all']
        
        try:
            self.run_command(command)
            # Dummy command to simulate creating a backup image
            # Replace with actual backup command
            shutil.copy('/path/to/original/rom.img', backup_file)
            logging.info(f"Backup created successfully at {backup_file}")
        except Exception as e:
            logging.error(f"Failed to backup ROM: {e}")

    def restore_rom(self, backup_file):
        """
        Restore the ROM from a backup file.
        
        :param backup_file: The path to the backup file to restore.
        """
        if not os.path.exists(backup_file):
            logging.error(f"Backup file does not exist: {backup_file}")
            return
        command = ['fastboot', '-s', self.device_id, 'flash', 'system', backup_file]
        
        try:
            self.run_command(command)
            logging.info(f"Restored ROM from {backup_file} successfully.")
        except Exception as e:
            logging.error(f"Failed to restore ROM: {e}")

# Example usage:
if __name__ == '__main__':
    device_id = 'YOUR_DEVICE_ID'
    backup_directory = './xiaomi_backups'
    
    backup_tool = XiaomiROMBackup(device_id, backup_directory)
    backup_tool.backup_rom()
    # To restore, uncomment the line below and provide the appropriate path
    # backup_tool.restore_rom('/path/to/backup/file.img')
```
