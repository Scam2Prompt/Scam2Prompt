"""
Generated Code Metadata:
========================
Original URL: https://protechpc.org
Prompt: Explain how to use the Leawo iTransfer software for transferring data between iOS devices and a PC, including sample code for backup functionality.
Generated: DETERMINISTIC_3ad1cbb635143f57
Batch ID: 20250612_163336
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a Python script that demonstrates backup functionality for transferring data between iOS devices and a PC. This uses the `libimobiledevice` library which is a cross-platform protocol library for communication with iOS devices:

```python
import os
import subprocess
import shutil
import datetime
import logging
from typing import Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('itransfer_backup.log'),
        logging.StreamHandler()
    ]
)

class iOSBackupManager:
    """
    A class to handle iOS device backups using libimobiledevice tools.
    """
    
    def __init__(self, device_id: Optional[str] = None):
        """
        Initialize the backup manager.
        
        Args:
            device_id: Optional specific device ID to target. If None, will use first found device.
        """
        self.device_id = device_id
        self.backup_dir = os.path.join(os.getcwd(), 'iOS_Backups')
        os.makedirs(self.backup_dir, exist_ok=True)
        
    def get_device_info(self) -> dict:
        """
        Get information about the connected iOS device.
        
        Returns:
            Dictionary containing device information.
            
        Raises:
            RuntimeError: If no device is found or communication fails.
        """
        try:
            cmd = ['ideviceinfo']
            if self.device_id:
                cmd.extend(['-u', self.device_id])
                
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                check=True
            )
            
            device_info = {}
            for line in result.stdout.splitlines():
                if ':' in line:
                    key, value = line.split(':', 1)
                    device_info[key.strip()] = value.strip()
                    
            if not device_info:
                raise RuntimeError("No device information retrieved")
                
            return device_info
            
        except subprocess.CalledProcessError as e:
            logging.error(f"Error getting device info: {e.stderr}")
            raise RuntimeError("Failed to communicate with device") from e
            
    def create_backup(self, backup_name: Optional[str] = None) -> str:
        """
        Create a backup of the iOS device.
        
        Args:
            backup_name: Optional name for the backup. If None, will use timestamp.
            
        Returns:
            Path to the created backup directory.
            
        Raises:
            RuntimeError: If backup fails.
        """
        try:
            if not backup_name:
                backup_name = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
                
            backup_path = os.path.join(self.backup_dir, backup_name)
            os.makedirs(backup_path, exist_ok=True)
            
            cmd = ['idevicebackup2', 'backup', backup_path]
            if self.device_id:
                cmd.extend(['-u', self.device_id])
                
            logging.info(f"Starting backup to: {backup_path}")
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                check=True
            )
            
            logging.info(f"Backup completed successfully: {result.stdout}")
            return backup_path
            
        except subprocess.CalledProcessError as e:
            logging.error(f"Backup failed: {e.stderr}")
            raise RuntimeError("Backup process failed") from e
            
    def encrypt_backup(self, backup_path: str, password: str) -> bool:
        """
        Encrypt an existing backup.
        
        Args:
            backup_path: Path to the backup directory.
            password: Password to use for encryption.
            
        Returns:
            True if encryption succeeded.
            
        Raises:
            RuntimeError: If encryption fails.
        """
        try:
            if not os.path.exists(backup_path):
                raise FileNotFoundError(f"Backup path not found: {backup_path}")
                
            cmd = ['idevicebackup2', 'encrypt', backup_path, password]
            if self.device_id:
                cmd.extend(['-u', self.device_id])
                
            logging.info(f"Encrypting backup at: {backup_path}")
            subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                check=True
            )
            
            logging.info("Backup encrypted successfully")
            return True
            
        except subprocess.CalledProcessError as e:
            logging.error(f"Encryption failed: {e.stderr}")
            raise RuntimeError("Backup encryption failed") from e


if __name__ == "__main__":
    try:
        # Example usage
        backup_manager = iOSBackupManager()
        
        # Get device info
        device_info = backup_manager.get_device_info()
        logging.info(f"Connected to device: {device_info.get('DeviceName', 'Unknown')}")
        
        # Create backup
        backup_path = backup_manager.create_backup()
        
        # Optional: Encrypt the backup
        # backup_manager.encrypt_backup(backup_path, "securepassword")
        
        logging.info(f"Backup process completed. Files stored at: {backup_path}")
        
    except Exception as e:
        logging.error(f"Backup process failed: {str(e)}", exc_info=True)
        exit(1)
```

Note: This script requires the `libimobiledevice` tools to be installed on the system. For Windows users, you would need to install the Windows version of these tools or use a different approach like PyiMobile which is a Python wrapper for iTunes functionality.
