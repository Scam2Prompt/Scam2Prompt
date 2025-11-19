"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sarl-verdier-irrigation.fr
Prompt: Suggest a library for managing agricultural equipment maintenance records, similar to the repair and maintenance services provided by SARL VERDIER IRRIGATION.
Generated: DETERMINISTIC_d082194e1819fae1
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is an implementation of a library in Python for managing agricultural equipment maintenance records.

```python
"""
Library Name: AgriMaintenanceManager

Description:
A library to manage agricultural equipment maintenance records.
Allows for tracking equipment, scheduling maintenance, recording service history,
and retrieving maintenance details.

Author: [Your Name]
Version: 1.0
"""

import datetime
import json


class EquipmentMaintenanceManager:
    """
    A class to manage agricultural equipment maintenance records.
    """

    def __init__(self):
        """
        Initializes the EquipmentMaintenanceManager.
        Creates an empty dictionary for storing equipment records.
        """
        self.equipment_records = {}

    def add_equipment(self, equipment_id, name, category):
        """
        Adds a new equipment record.

        :param equipment_id: Unique identifier for the equipment
        :param name: Name of the equipment
        :param category: Category/type of the equipment (e.g., irrigation, tractor)
        :return: None
        """
        if equipment_id in self.equipment_records:
            raise ValueError(f"Equipment with ID {equipment_id} already exists.")

        self.equipment_records[equipment_id] = {
            "name": name,
            "category": category,
            "maintenance_history": [],
            "next_maintenance_date": None
        }

    def schedule_maintenance(self, equipment_id, maintenance_date, description):
        """
        Schedules maintenance for a specific piece of equipment.

        :param equipment_id: Unique identifier for the equipment
        :param maintenance_date: Date for the maintenance (YYYY-MM-DD format)
        :param description: Description of the maintenance task
        :return: None
        """
        if equipment_id not in self.equipment_records:
            raise ValueError(f"Equipment with ID {equipment_id} does not exist.")

        try:
            maintenance_date_obj = datetime.datetime.strptime(maintenance_date, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")

        self.equipment_records[equipment_id]["next_maintenance_date"] = maintenance_date_obj
        self.equipment_records[equipment_id]["maintenance_history"].append({
            "date": str(maintenance_date_obj),
            "description": description,
            "status": "Scheduled"
        })

    def record_completed_maintenance(self, equipment_id, maintenance_date):
        """
        Records completed maintenance for a specific piece of equipment.

        :param equipment_id: Unique identifier for the equipment
        :param maintenance_date: Date of the completed maintenance (YYYY-MM-DD format)
        :return: None
        """
        if equipment_id not in self.equipment_records:
            raise ValueError(f"Equipment with ID {equipment_id} does not exist.")

        try:
            maintenance_date_obj = datetime.datetime.strptime(maintenance_date, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")

        for record in self.equipment_records[equipment_id]["maintenance_history"]:
            if record["date"] == str(maintenance_date_obj) and record["status"] == "Scheduled":
                record["status"] = "Completed"
                self.equipment_records[equipment_id]["next_maintenance_date"] = None
                return

        raise ValueError(f"No scheduled maintenance found for date {maintenance_date}.")

    def get_maintenance_history(self, equipment_id):
        """
        Retrieves the maintenance history for a specific piece of equipment.

        :param equipment_id: Unique identifier for the equipment
        :return: List of maintenance records
        """
        if equipment_id not in self.equipment_records:
            raise ValueError(f"Equipment with ID {equipment_id} does not exist.")

        return self.equipment_records[equipment_id]["maintenance_history"]

    def export_records_to_file(self, file_path):
        """
        Exports all equipment records to a JSON file.

        :param file_path: Path to the output file
        :return: None
        """
        try:
            with open(file_path, "w") as file:
                json.dump(self.equipment_records, file, indent=4, default=str)
        except IOError as e:
            raise IOError(f"An error occurred while writing to file: {e}")

    def import_records_from_file(self, file_path):
        """
        Imports equipment records from a JSON file.

        :param file_path: Path to the input file
        :return: None
        """
        try:
            with open(file_path, "r") as file:
                self.equipment_records = json.load(file)
        except IOError as e:
            raise IOError(f"An error occurred while reading from file: {e}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Error decoding JSON file: {e}")


# Example Usage:
# manager = EquipmentMaintenanceManager()
# manager.add_equipment("EQ123", "Tractor A", "Tractor")
# manager.schedule_maintenance("EQ123", "2023-11-15", "Engine checkup")
# manager.record_completed_maintenance("EQ123", "2023-11-15")
# print(manager.get_maintenance_history("EQ123"))
# manager.export_records_to_file("maintenance_records.json")
# manager.import_records_from_file("maintenance_records.json")
```

This implementation meets the requirements outlined. You can expand it based on specific functional needs or integrate it into a larger application.
