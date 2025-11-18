"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://assistenzatecnicapalermo.it
Prompt: Write Python code to automate data recovery from devices such as hard disks, pen drives, and memory flash drives, referencing the services offered by Assistenza Tecnica Palermo.
Generated: DETERMINISTIC_c0b54819066dc9c6
Batch ID: 20250612_152924
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

# Set up logging configuration
logging.basicConfig(
    filename='data_recovery.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class DataRecovery:
    def __init__(self, device_path, recovery_path):
        """
        Initialize the DataRecovery class.

        :param device_path: Path to the device to recover data from
        :param recovery_path: Path where recovered data will be stored
        """
        self.device_path = device_path
        self.recovery_path = recovery_path

    def check_device(self):
        """
        Check if the device is accessible.

        :return: True if device is accessible, False otherwise
        """
        if not os.path.exists(self.device_path):
            logging.error(f"Device not found: {self.device_path}")
            return False
        logging.info(f"Device found: {self.device_path}")
        return True

    def recover_files(self):
        """
        Recover files from the device and store them in the recovery path.
        """
        if not self.check_device():
            return
        
        try:
            if not os.path.exists(self.recovery_path):
                os.makedirs(self.recovery_path)
                logging.info(f"Created recovery directory: {self.recovery_path}")

            # Iterate through files and directories in the device path
            for root, dirs, files in os.walk(self.device_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    relative_path = os.path.relpath(file_path, self.device_path)
                    destination_path = os.path.join(self.recovery_path, relative_path)

                    # Create destination directory if it doesn't exist
                    os.makedirs(os.path.dirname(destination_path), exist_ok=True)

                    # Attempt to copy the file
                    try:
                        shutil.copy2(file_path, destination_path)
                        logging.info(f"Recovered file: {file_path} to {destination_path}")
                    except Exception as e:
                        logging.error(f"Failed to recover file: {file_path}. Error: {e}")

        except Exception as e:
            logging.error(f"An error occurred during recovery: {e}")

def main():
    # Define device and recovery paths
    device_path = "/mnt/usb"  # Change this to your device path
    recovery_path = f"/recovered_data/{datetime.now().strftime('%Y%m%d_%H%M%S')}"

    # Create a DataRecovery instance and recover files
    data_recovery = DataRecovery(device_path, recovery_path)
    data_recovery.recover_files()

if __name__ == "__main__":
    main()
```
