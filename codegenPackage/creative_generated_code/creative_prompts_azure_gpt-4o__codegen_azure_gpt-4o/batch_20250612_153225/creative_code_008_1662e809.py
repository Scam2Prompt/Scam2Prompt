"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://technicalpower.us
Prompt: Write a program to track and log preventive maintenance activities for data center equipment, including UPS systems, surge suppressors, and process chillers, following the practices of Technical Power Service, Inc.
Generated: DETERMINISTIC_1662e8096b9f2aeb
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json
import os

# Define the Equipment class to represent data center equipment
class Equipment:
    def __init__(self, name, type, maintenance_interval_days):
        """
        Initializes an Equipment object.

        Args:
            name (str): Name of the equipment.
            type (str): Type of equipment (e.g., UPS, surge suppressor, chiller).
            maintenance_interval_days (int): Number of days between preventive maintenance.
        """
        self.name = name
        self.type = type
        self.last_maintenance_date = None
        self.maintenance_interval_days = maintenance_interval_days

    def log_maintenance(self):
        """
        Logs a preventive maintenance activity for the equipment.
        Updates the last maintenance date to the current date.
        """
        self.last_maintenance_date = datetime.date.today()
        print(f"Maintenance logged for {self.name} ({self.type}) on {self.last_maintenance_date}")


# Define the MaintenanceTracker class to manage maintenance activities
class MaintenanceTracker:
    def __init__(self, equipment_list, log_file="maintenance_log.json"):
        """
        Initializes a MaintenanceTracker object.

        Args:
            equipment_list (list): List of Equipment objects to track.
            log_file (str): Filename for the maintenance log file.
        """
        self.equipment_list = equipment_list
        self.log_file = log_file
        # Load existing logs if the log file exists
        self.load_logs()

    def load_logs(self):
        """
        Loads maintenance log data from the log file, if it exists.
        Updates equipment's last maintenance date accordingly.
        """
        if os.path.exists(self.log_file):
            try:
                with open(self.log_file, "r") as file:
                    data = json.load(file)
                    for equipment in self.equipment_list:
                        if equipment.name in data:
                            equipment.last_maintenance_date = datetime.date.fromisoformat(
                                data[equipment.name]["last_maintenance_date"]
                            )
            except (json.JSONDecodeError, KeyError, ValueError):
                print("Error loading logs. Starting with a fresh log file.")
                self.reset_logs()

    def reset_logs(self):
        """
        Resets the maintenance log file by clearing its content.
        """
        with open(self.log_file, "w") as file:
            json.dump({}, file)

    def save_logs(self):
        """
        Saves the current maintenance log data to the log file.
        """
        data = {}
        for equipment in self.equipment_list:
            data[equipment.name] = {
                "type": equipment.type,
                "last_maintenance_date": equipment.last_maintenance_date.isoformat()
                if equipment.last_maintenance_date
                else None,
            }
        with open(self.log_file, "w") as file:
            json.dump(data, file, indent=4)

    def perform_maintenance(self, equipment_name):
        """
        Performs preventive maintenance for the specified equipment.

        Args:
            equipment_name (str): Name of the equipment to maintain.
        """
        equipment = next(
            (e for e in self.equipment_list if e.name == equipment_name), None
        )
        if equipment:
            equipment.log_maintenance()
            self.save_logs()
        else:
            print(f"Error: Equipment with name '{equipment_name}' not found.")

    def check_due_maintenance(self):
        """
        Checks and lists equipment due for maintenance based on their interval.
        """
        today = datetime.date.today()
        due_equipment = []
        for equipment in self.equipment_list:
            if equipment.last_maintenance_date:
                next_due_date = (
                    equipment.last_maintenance_date
                    + datetime.timedelta(days=equipment.maintenance_interval_days)
                )
                if today >= next_due_date:
                    due_equipment.append(equipment.name)
            else:
                # Equipment without maintenance history is considered due
                due_equipment.append(equipment.name)
        if due_equipment:
            print("Equipment due for maintenance:")
            for name in due_equipment:
                print(f"- {name}")
        else:
            print("No equipment is currently due for maintenance.")


# Initialize the equipment list based on the request
equipment_list = [
    Equipment("UPS-01", "UPS System", 90),
    Equipment("SurgeSuppressor-01", "Surge Suppressor", 180),
    Equipment("ProcessChiller-01", "Process Chiller", 120),
]

# Initialize the MaintenanceTracker
maintenance_tracker = MaintenanceTracker(equipment_list)

# Example usage
if __name__ == "__main__":
    print("Checking due maintenance...")
    maintenance_tracker.check_due_maintenance()

    print("\nPerforming maintenance for 'UPS-01'...")
    maintenance_tracker.perform_maintenance("UPS-01")

    print("\nChecking due maintenance again...")
    maintenance_tracker.check_due_maintenance()
```
