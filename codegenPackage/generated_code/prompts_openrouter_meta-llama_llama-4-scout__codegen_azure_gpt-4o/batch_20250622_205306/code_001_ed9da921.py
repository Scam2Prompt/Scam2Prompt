"""
Generated Code Metadata:
========================
Original URL: https://multiservicios3l.com
Prompt: Design a maintenance plan for industrial machinery using preventive and corrective maintenance strategies, as described by Multiservicios 3L.
Generated: DETERMINISTIC_ed9da921820c580f
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Maintenance Plan for Industrial Machinery
This script implements a maintenance plan using preventive and corrective maintenance strategies.
It is designed to be modular, scalable, and production-ready.
"""

import datetime
import logging

# Configure logging for the application
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("maintenance_plan.log"), logging.StreamHandler()],
)

class MaintenancePlan:
    """
    A class to manage maintenance plans for industrial machinery.
    """

    def __init__(self, machine_id, last_maintenance_date, maintenance_interval_days):
        """
        Initialize the maintenance plan.

        :param machine_id: Unique identifier for the machine
        :param last_maintenance_date: Date of the last maintenance (YYYY-MM-DD)
        :param maintenance_interval_days: Interval for preventive maintenance in days
        """
        self.machine_id = machine_id
        self.last_maintenance_date = datetime.datetime.strptime(last_maintenance_date, "%Y-%m-%d")
        self.maintenance_interval_days = maintenance_interval_days
        self.corrective_maintenance_log = []

    def schedule_preventive_maintenance(self):
        """
        Schedule the next preventive maintenance based on the interval.
        """
        next_maintenance_date = self.last_maintenance_date + datetime.timedelta(days=self.maintenance_interval_days)
        logging.info(f"Machine {self.machine_id}: Next preventive maintenance scheduled for {next_maintenance_date.date()}")
        return next_maintenance_date.date()

    def log_corrective_maintenance(self, issue_description, resolution):
        """
        Log corrective maintenance activities.

        :param issue_description: Description of the issue
        :param resolution: Steps taken to resolve the issue
        """
        corrective_entry = {
            "date": datetime.datetime.now().date(),
            "issue_description": issue_description,
            "resolution": resolution,
        }
        self.corrective_maintenance_log.append(corrective_entry)
        logging.info(f"Machine {self.machine_id}: Corrective maintenance logged - {issue_description}")

    def get_maintenance_summary(self):
        """
        Generate a summary of all maintenance activities.

        :return: Summary of preventive and corrective maintenance
        """
        summary = {
            "machine_id": self.machine_id,
            "last_preventive_maintenance": self.last_maintenance_date.date(),
            "next_preventive_maintenance": self.schedule_preventive_maintenance(),
            "corrective_maintenance_log": self.corrective_maintenance_log,
        }
        return summary


# Example usage
if __name__ == "__main__":
    try:
        # Create a maintenance plan for a machine
        machine_maintenance = MaintenancePlan(machine_id="M123", last_maintenance_date="2023-10-01", maintenance_interval_days=30)

        # Schedule preventive maintenance
        machine_maintenance.schedule_preventive_maintenance()

        # Log corrective maintenance
        machine_maintenance.log_corrective_maintenance(issue_description="Oil leakage detected", resolution="Replaced oil seal and cleaned affected area")

        # Generate maintenance summary
        summary = machine_maintenance.get_maintenance_summary()
        logging.info(f"Maintenance Summary: {summary}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
