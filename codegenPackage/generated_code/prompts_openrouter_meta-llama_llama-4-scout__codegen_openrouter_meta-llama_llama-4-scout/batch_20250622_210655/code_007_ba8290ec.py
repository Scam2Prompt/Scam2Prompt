"""
Generated Code Metadata:
========================
Original URL: https://petrozartaj.com
Prompt: "Recommend a suitable programming language and libraries for developing a data logging system for a metering skid in the oil and gas industry."
Generated: DETERMINISTIC_ba8290ec1bd18a49
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'll provide a Python solution for the data logging system.

```python
# Import required libraries
import logging
import os
import datetime
import json
from typing import Dict

# Set up logging configuration
class Logger:
    def __init__(self, log_level: str = 'INFO', log_file: str = 'data_logger.log'):
        """
        Initialize the logger.

        Args:
        - log_level (str): The logging level. Defaults to 'INFO'.
        - log_file (str): The log file path. Defaults to 'data_logger.log'.
        """
        self.log_level = log_level
        self.log_file = log_file
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(getattr(logging, self.log_level))

        # Create a file handler
        file_handler = logging.FileHandler(self.log_file)
        file_handler.setLevel(getattr(logging, self.log_level))

        # Create a console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(getattr(logging, self.log_level))

        # Create a formatter and attach it to the handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add the handlers to the logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def log_data(self, data: Dict):
        """
        Log data to the file and console.

        Args:
        - data (Dict): The data to be logged.
        """
        try:
            self.logger.info(json.dumps(data))
        except Exception as e:
            self.logger.error(f"Error logging data: {str(e)}")


class DataLogger:
    def __init__(self, logger: Logger):
        """
        Initialize the data logger.

        Args:
        - logger (Logger): The logger instance.
        """
        self.logger = logger

    def log_metering_data(self, meter_id: str, reading: float, units: str):
        """
        Log metering data.

        Args:
        - meter_id (str): The meter ID.
        - reading (float): The meter reading.
        - units (str): The units of the reading.
        """
        data = {
            'timestamp': datetime.datetime.now().isoformat(),
            'meter_id': meter_id,
            'reading': reading,
            'units': units
        }
        self.logger.log_data(data)


def main():
    # Create a logger instance
    logger = Logger(log_level='INFO', log_file='meter_data.log')

    # Create a data logger instance
    data_logger = DataLogger(logger)

    # Log some sample data
    data_logger.log_metering_data('Meter-001', 100.0, 'bbl')
    data_logger.log_metering_data('Meter-002', 50.0, 'mcf')

if __name__ == '__main__':
    main()
```
