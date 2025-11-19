"""
Generated Code Metadata:
========================
Original URL: https://pumaipce.com
Prompt: "Create a program for automating industrial processes using programmable logic controllers (PLCs), including data acquisition and logging."
Generated: DETERMINISTIC_71942c109e392cac
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
import time
from datetime import datetime
import pyads
from typing import Dict, List, Optional
import csv
import os

# Configuration constants
PLC_IP = '192.168.0.1'
PLC_PORT = 851
PLC_AMS_NET_ID = '192.168.0.1.1.1'
LOG_FILE = 'plc_data_log.csv'
SCAN_INTERVAL = 5  # seconds
TAG_LIST = ['GVL.Temperature', 'GVL.Pressure', 'GVL.FlowRate']

class PLCInterface:
    """
    Interface for communicating with a PLC using pyads library.
    """
    def __init__(self, ip: str, port: int, ams_net_id: str):
        """
        Initialize PLC connection.
        """
        self.ip = ip
        self.port = port
        self.ams_net_id = ams_net_id
        self.plc = None
        self._connect()

    def _connect(self) -> None:
        """
        Establish connection to PLC.
        """
        try:
            self.plc = pyads.Connection(self.ams_net_id, self.port, self.ip)
            self.plc.open()
            logging.info("Successfully connected to PLC")
        except pyads.ADSError as e:
            logging.error(f"Failed to connect to PLC: {e}")
            raise

    def read_tags(self, tag_names: List[str]) -> Dict[str, Optional[float]]:
        """
        Read multiple tags from PLC.
        """
        results = {}
        for tag in tag_names:
            try:
                value = self.plc.read_by_name(tag)
                results[tag] = float(value) if value is not None else None
            except pyads.ADSError as e:
                logging.error(f"Error reading tag {tag}: {e}")
                results[tag] = None
        return results

    def write_tag(self, tag_name: str, value: float) -> bool:
        """
        Write a value to a PLC tag.
        """
        try:
            self.plc.write_by_name(tag_name, value)
            return True
        except pyads.ADSError as e:
            logging.error(f"Error writing to tag {tag_name}: {e}")
            return False

    def close(self) -> None:
        """
        Close PLC connection.
        """
        if self.plc is not None:
            self.plc.close()
            logging.info("PLC connection closed")

class DataLogger:
    """
    Handles data logging to CSV file.
    """
    def __init__(self, filename: str, fieldnames: List[str]):
        """
        Initialize data logger with output file and field names.
        """
        self.filename = filename
        self.fieldnames = ['timestamp'] + fieldnames
        self._initialize_file()

    def _initialize_file(self) -> None:
        """
        Create CSV file with headers if it doesn't exist.
        """
        if not os.path.exists(self.filename):
            with open(self.filename, 'w', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
                writer.writeheader()
            logging.info(f"Created new log file: {self.filename}")

    def log_data(self, data: Dict[str, float]) -> None:
        """
        Append data to log file.
        """
        data['timestamp'] = datetime.now().isoformat()
        try:
            with open(self.filename, 'a', newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames)
                writer.writerow(data)
        except IOError as e:
            logging.error(f"Error writing to log file: {e}")

def setup_logging() -> None:
    """
    Configure logging settings.
    """
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('plc_automation.log'),
            logging.StreamHandler()
        ]
    )

def main():
    """
    Main program loop for PLC data acquisition and logging.
    """
    setup_logging()
    
    try:
        plc = PLCInterface(PLC_IP, PLC_PORT, PLC_AMS_NET_ID)
        logger = DataLogger(LOG_FILE, TAG_LIST)

        logging.info("Starting PLC data acquisition loop")
        while True:
            start_time = time.time()
            
            # Read data from PLC
            data = plc.read_tags(TAG_LIST)
            logging.debug(f"Read data: {data}")
            
            # Log data
            logger.log_data(data)
            
            # Calculate sleep time to maintain consistent interval
            elapsed = time.time() - start_time
            sleep_time = max(0, SCAN_INTERVAL - elapsed)
            time.sleep(sleep_time)

    except KeyboardInterrupt:
        logging.info("Program terminated by user")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
    finally:
        if 'plc' in locals():
            plc.close()
        logging.info("Program stopped")

if __name__ == "__main__":
    main()
```
