"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tibvanboxtel.nl
Prompt: Provide code to design a monitoring system for micro-inverters in a solar panel setup, following the installation standards (NEN 1010 and NEN 3140) mentioned on Technische Installatiebedrijf van Boxtel's webpage.
Generated: DETERMINISTIC_35c48a1293539ad7
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from datetime import datetime
from typing import List, Dict

# Configure logging for error tracking and debugging
logging.basicConfig(
    filename='monitoring_system.log',
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s'
)

class MicroInverter:
    """
    Class to represent a micro-inverter in a solar panel monitoring system.
    """

    def __init__(self, id: str, status: str, power_output: float):
        """
        Initialize a micro-inverter instance.

        :param id: Unique identifier for the micro-inverter
        :param status: Current operational status of the inverter
        :param power_output: Power output in watts
        """
        self.id = id
        self.status = status
        self.power_output = power_output

    def to_dict(self) -> Dict:
        """Convert the micro-inverter instance to a dictionary."""
        return {
            "id": self.id,
            "status": self.status,
            "power_output": self.power_output
        }


class MonitoringSystem:
    """
    Class to monitor multiple micro-inverters in a solar panel setup.
    """

    def __init__(self):
        """Initialize the monitoring system with an empty list of inverters."""
        self.inverters: List[MicroInverter] = []

    def add_inverter(self, inverter: MicroInverter):
        """
        Add a micro-inverter to the monitoring system.

        :param inverter: Instance of a MicroInverter to add
        """
        self.inverters.append(inverter)
        logging.info(f"Inverter {inverter.id} added with status {inverter.status}.")

    def update_inverter(self, id: str, status: str, power_output: float):
        """
        Update the status and power output of a micro-inverter.

        :param id: Unique identifier of the inverter to update
        :param status: New status of the inverter
        :param power_output: New power output in watts
        """
        try:
            inverter = next(inv for inv in self.inverters if inv.id == id)
            inverter.status = status
            inverter.power_output = power_output
            logging.info(f"Inverter {id} updated to status {status} with power output {power_output}W.")
        except StopIteration:
            logging.error(f"Inverter with ID {id} not found for update.")
            raise ValueError(f"Inverter with ID {id} not found.")

    def get_inverter_status(self, id: str) -> Dict:
        """
        Retrieve the status of a specific micro-inverter.

        :param id: Unique identifier of the inverter
        :return: Dictionary with inverter details
        """
        try:
            inverter = next(inv for inv in self.inverters if inv.id == id)
            logging.info(f"Retrieved status for inverter {id}.")
            return inverter.to_dict()
        except StopIteration:
            logging.error(f"Inverter with ID {id} not found.")
            raise ValueError(f"Inverter with ID {id} not found.")

    def save_report(self, filename: str):
        """
        Save the current state of all inverters to a JSON report.

        :param filename: Name of the file to save the report
        """
        try:
            report_data = [inverter.to_dict() for inverter in self.inverters]
            with open(filename, 'w') as f:
                json.dump(report_data, f, indent=4)
            logging.info(f"Report saved successfully to {filename}.")
        except Exception as e:
            logging.error(f"Failed to save report: {str(e)}")
            raise


# Example usage
if __name__ == "__main__":
    try:
        monitoring_system = MonitoringSystem()

        # Adding inverters
        monitoring_system.add_inverter(MicroInverter("INV001", "active", 250.0))
        monitoring_system.add_inverter(MicroInverter("INV002", "inactive", 0.0))

        # Updating an inverter
        monitoring_system.update_inverter("INV001", "active", 300.0)

        # Retrieving an inverter's status
        status = monitoring_system.get_inverter_status("INV001")
        print(status)

        # Saving the report
        monitoring_system.save_report("inverter_report.json")

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
```
