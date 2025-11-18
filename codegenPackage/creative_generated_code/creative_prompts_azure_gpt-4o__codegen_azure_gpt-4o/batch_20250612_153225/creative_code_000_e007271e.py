"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://technicalpower.us
Prompt: Write Python code to monitor the status of UPS batteries and proactively replace any bad cells in a string to minimize data center downtime, as described by Technical Power Service, Inc.
Generated: DETERMINISTIC_e007271ec2496ba8
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
import time
from typing import List

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("ups_battery_monitor.log"),
        logging.StreamHandler()
    ]
)

class UPSBatteryMonitor:
    def __init__(self, battery_strings: List[List[float]], voltage_threshold: float):
        """
        Initializes the UPSBatteryMonitor object.

        :param battery_strings: A list of lists representing strings of battery cells and their voltages.
        :param voltage_threshold: The minimum voltage threshold considered healthy for a battery cell.
        """
        self.battery_strings = battery_strings
        self.voltage_threshold = voltage_threshold

    def check_batteries(self):
        """
        Checks the status of each battery cell and logs their status.
        If a cell is found below the voltage threshold, it is flagged for replacement.
        """
        logging.info("Starting UPS battery status check...")
        for string_index, battery_string in enumerate(self.battery_strings):
            for cell_index, cell_voltage in enumerate(battery_string):
                if cell_voltage < self.voltage_threshold:
                    logging.warning(
                        f"Battery cell in string {string_index + 1}, position {cell_index + 1} has failed "
                        f"(Voltage: {cell_voltage}V). Proactive replacement recommended."
                    )
                    self.replace_bad_cell(string_index, cell_index)
                else:
                    logging.info(
                        f"Battery cell in string {string_index + 1}, position {cell_index + 1} is healthy "
                        f"(Voltage: {cell_voltage}V)."
                    )

    def replace_bad_cell(self, string_index: int, cell_index: int):
        """
        Simulates the replacement of a bad battery cell.

        :param string_index: The index of the battery string containing the bad cell.
        :param cell_index: The index of the failed cell within the battery string.
        """
        try:
            # Replace the cell with a new one (simulated as assigning a new healthy voltage value)
            logging.info(f"Replacing battery cell in string {string_index + 1}, position {cell_index + 1}...")
            self.battery_strings[string_index][cell_index] = self.voltage_threshold + 0.5  # Assume 0.5V above threshold
            logging.info(f"Replacement complete for cell in string {string_index + 1}, position {cell_index + 1}.")
        except Exception as e:
            logging.error(f"Failed to replace battery cell: {e}")

    def run_monitoring(self, interval_seconds: int):
        """
        Starts continuous monitoring of UPS batteries at regular intervals.

        :param interval_seconds: Time interval between checks in seconds.
        """
        logging.info("UPS battery monitoring active. Press Ctrl+C to stop.")
        try:
            while True:
                self.check_batteries()
                time.sleep(interval_seconds)
        except KeyboardInterrupt:
            logging.info("UPS battery monitoring stopped by user.")

# Example usage:
if __name__ == "__main__":
    # Simulated battery strings: Each sublist represents a string of battery cell voltages
    battery_strings = [
        [13.2, 12.8, 11.9, 13.0],  # String 1
        [12.9, 12.7, 11.5, 13.1],  # String 2
        [13.5, 12.6, 12.0, 13.4],  # String 3
    ]
    
    # Voltage threshold below which a cell is considered bad
    voltage_threshold = 12.0
    
    # Initialize the monitor
    monitor = UPSBatteryMonitor(battery_strings, voltage_threshold)
    
    # Run monitoring every 10 seconds
    monitor.run_monitoring(interval_seconds=10)
```
