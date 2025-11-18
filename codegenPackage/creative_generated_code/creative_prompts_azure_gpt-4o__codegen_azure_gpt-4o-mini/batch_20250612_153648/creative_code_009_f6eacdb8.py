"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://longhuigolf.com
Prompt: Generate code to track factory machine usage and maintenance schedules for molding and material processing machines, as described in Longhui Golf’s factory configuration details.
Generated: DETERMINISTIC_f6eacdb822c2b8ab
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict, Optional


class Machine:
    """Class representing a factory machine."""

    def __init__(self, machine_id: str, machine_type: str):
        """
        Initialize a Machine instance.

        :param machine_id: Unique identifier for the machine.
        :param machine_type: Type of the machine (e.g., 'Molding', 'Material Processing').
        """
        self.machine_id = machine_id
        self.machine_type = machine_type
        self.usage_records: List[Dict[str, datetime.datetime]] = []
        self.maintenance_records: List[Dict[str, datetime.datetime]] = []

    def log_usage(self):
        """
        Log the current usage timestamp for the machine.
        """
        self.usage_records.append({"start_time": datetime.datetime.now()})

    def end_usage(self):
        """
        End the current usage session for the machine.
        """
        if self.usage_records and "end_time" not in self.usage_records[-1]:
            self.usage_records[-1]["end_time"] = datetime.datetime.now()
        else:
            raise ValueError("No usage session found to end.")

    def schedule_maintenance(self, maintenance_date: datetime.date):
        """
        Schedule maintenance for the machine.

        :param maintenance_date: Date for scheduled maintenance.
        """
        self.maintenance_records.append({"maintenance_date": maintenance_date})

    def get_usage_report(self) -> List[Dict[str, Optional[datetime.datetime]]]:
        """
        Get usage report for the machine.

        :return: List of usage records with start and end times.
        """
        return self.usage_records

    def get_maintenance_schedule(self) -> List[Dict[str, datetime.date]]:
        """
        Get the maintenance schedule for the machine.

        :return: List of scheduled maintenance records.
        """
        return self.maintenance_records


class Factory:
    """Class representing a factory with multiple machines."""

    def __init__(self):
        """
        Initialize a Factory instance.
        """
        self.machines: Dict[str, Machine] = {}

    def add_machine(self, machine_id: str, machine_type: str):
        """
        Add a new machine to the factory.

        :param machine_id: Unique identifier for the machine.
        :param machine_type: Type of the machine.
        """
        if machine_id in self.machines:
            raise ValueError(f"Machine with ID {machine_id} already exists.")
        self.machines[machine_id] = Machine(machine_id, machine_type)

    def log_usage(self, machine_id: str):
        """
        Log usage for a specific machine.

        :param machine_id: Unique identifier for the machine.
        """
        if machine_id not in self.machines:
            raise ValueError(f"Machine with ID {machine_id} does not exist.")
        self.machines[machine_id].log_usage()

    def end_usage(self, machine_id: str):
        """
        End usage for a specific machine.

        :param machine_id: Unique identifier for the machine.
        """
        if machine_id not in self.machines:
            raise ValueError(f"Machine with ID {machine_id} does not exist.")
        self.machines[machine_id].end_usage()

    def schedule_maintenance(self, machine_id: str, maintenance_date: datetime.date):
        """
        Schedule maintenance for a specific machine.

        :param machine_id: Unique identifier for the machine.
        :param maintenance_date: Date for scheduled maintenance.
        """
        if machine_id not in self.machines:
            raise ValueError(f"Machine with ID {machine_id} does not exist.")
        self.machines[machine_id].schedule_maintenance(maintenance_date)

    def get_machine_usage_report(self, machine_id: str) -> List[Dict[str, Optional[datetime.datetime]]]:
        """
        Get usage report for a specific machine.

        :param machine_id: Unique identifier for the machine.
        :return: List of usage records for the machine.
        """
        if machine_id not in self.machines:
            raise ValueError(f"Machine with ID {machine_id} does not exist.")
        return self.machines[machine_id].get_usage_report()

    def get_machine_maintenance_schedule(self, machine_id: str) -> List[Dict[str, datetime.date]]:
        """
        Get maintenance schedule for a specific machine.

        :param machine_id: Unique identifier for the machine.
        :return: List of maintenance records for the machine.
        """
        if machine_id not in self.machines:
            raise ValueError(f"Machine with ID {machine_id} does not exist.")
        return self.machines[machine_id].get_maintenance_schedule()


# Example usage (commented out for production code)
# factory = Factory()
# factory.add_machine("M1", "Molding")
# factory.log_usage("M1")
# factory.end_usage("M1")
# factory.schedule_maintenance("M1", datetime.date(2023, 11, 10))
# usage_report = factory.get_machine_usage_report("M1")
# maintenance_schedule = factory.get_machine_maintenance_schedule("M1")
```
