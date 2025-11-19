"""
Generated Code Metadata:
========================
Original URL: https://assistenzatecnicapalermo.it
Prompt: Write Python code to automate data recovery from devices such as hard disks, pen drives, and memory flash drives, referencing the services offered by Assistenza Tecnica Palermo.
Generated: DETERMINISTIC_c0b54819066dc9c6
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import shutil
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='data_recovery.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class DataRecovery:
    def __init__(self, source_device, recovery_location):
        """
        Initialize the DataRecovery class.

        :param source_device: Path to the source device (e.g., hard disk, pen drive)
        :param recovery_location: Path to the location where recovered data will be stored
        """
        self.source_device = source_device
        self.recovery_location = recovery_location

    def validate_device(self):
        """
        Validate if the source device exists and is accessible.

        :return: True if valid, False otherwise
        """
        if not os.path.exists(self.source_device):
            logging.error(f"Source device {self.source_device} does not exist.")
            return False
        if not os.access(self.source_device, os.R_OK):
            logging.error(f"Source device {self.source_device} is not readable.")
            return False
        return True

    def recover_data(self):
        """
        Recover data from the source device to the recovery location.
        """
        if not self.validate_device():
            logging.error("Data recovery aborted due to invalid source device.")
            return

        try:
            # Create recovery location if it doesn't exist
            os.makedirs(self.recovery_location, exist_ok=True)
            logging.info(f"Starting data recovery from {self.source_device} to {self.recovery_location}")

            # Copy files from source device to recovery location
            for item in os.listdir(self.source_device):
                source_path = os.path.join(self.source_device, item)
                destination_path = os.path.join(self.recovery_location, item)

                if os.path.isdir(source_path):
                    shutil.copytree(source_path, destination_path)
                    logging.info(f"Recovered directory: {source_path} to {destination_path}")
                else:
                    shutil.copy2(source_path, destination_path)
                    logging.info(f"Recovered file: {source_path} to {destination_path}")

            logging.info("Data recovery completed successfully.")

        except Exception as e:
            logging.error(f"An error occurred during data recovery: {e}")

if __name__ == "__main__":
    # Example usage
    source_device = "/path/to/source/device"  # Replace with actual device path
    recovery_location = f"/path/to/recovery/location/{datetime.now().strftime('%Y%m%d_%H%M%S')}"  # Unique recovery folder

    data_recovery = DataRecovery(source_device, recovery_location)
    data_recovery.recover_data()
```

**Note:** Replace `"/path/to/source/device"` and `"/path/to/recovery/location/"` with actual paths before running the code.
