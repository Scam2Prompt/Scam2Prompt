"""
Generated Code Metadata:
========================
Original URL: https://ohclift.com
Prompt: Provide an example of a maintenance scheduling system for hydraulic lifts that ensures compliance with safety standards.
Generated: DETERMINISTIC_35ad6705978d4e92
Batch ID: 20250612_160628
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json

class HydraulicLiftMaintenanceScheduler:
    """
    A class to manage maintenance scheduling for hydraulic lifts.
    Ensures compliance with safety standards.
    """

    def __init__(self, maintenance_interval_days=90):
        """
        Initialize the scheduler with a default maintenance interval.

        :param maintenance_interval_days: Number of days between maintenance checks.
        """
        self.maintenance_interval_days = maintenance_interval_days
        self.lifts = {}  # Dictionary to store lift data

    def add_lift(self, lift_id, last_maintenance_date):
        """
        Add a hydraulic lift to the system.

        :param lift_id: Unique identifier for the lift.
        :param last_maintenance_date: Date of the last maintenance (YYYY-MM-DD).
        """
        try:
            last_maintenance_date = datetime.datetime.strptime(last_maintenance_date, "%Y-%m-%d").date()
            self.lifts[lift_id] = {
                "last_maintenance_date": last_maintenance_date,
                "next_maintenance_date": last_maintenance_date + datetime.timedelta(days=self.maintenance_interval_days)
            }
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")

    def update_maintenance(self, lift_id, maintenance_date):
        """
        Update the maintenance record for a lift.

        :param lift_id: Unique identifier for the lift.
        :param maintenance_date: Date of the maintenance (YYYY-MM-DD).
        """
        if lift_id not in self.lifts:
            raise KeyError(f"Lift ID {lift_id} not found.")
        
        try:
            maintenance_date = datetime.datetime.strptime(maintenance_date, "%Y-%m-%d").date()
            self.lifts[lift_id]["last_maintenance_date"] = maintenance_date
            self.lifts[lift_id]["next_maintenance_date"] = maintenance_date + datetime.timedelta(days=self.maintenance_interval_days)
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")

    def get_next_maintenance_date(self, lift_id):
        """
        Get the next scheduled maintenance date for a lift.

        :param lift_id: Unique identifier for the lift.
        :return: Next maintenance date (YYYY-MM-DD).
        """
        if lift_id not in self.lifts:
            raise KeyError(f"Lift ID {lift_id} not found.")
        
        return self.lifts[lift_id]["next_maintenance_date"]

    def list_lifts_due_for_maintenance(self):
        """
        List all lifts that are due for maintenance.

        :return: List of lift IDs due for maintenance.
        """
        today = datetime.date.today()
        due_lifts = [lift_id for lift_id, data in self.lifts.items() if data["next_maintenance_date"] <= today]
        return due_lifts

    def save_to_file(self, filename):
        """
        Save the lift data to a file in JSON format.

        :param filename: Name of the file to save the data.
        """
        try:
            with open(filename, "w") as file:
                json.dump(self.lifts, file, default=str, indent=4)
        except IOError:
            raise IOError("Failed to save data to file.")

    def load_from_file(self, filename):
        """
        Load lift data from a file in JSON format.

        :param filename: Name of the file to load the data from.
        """
        try:
            with open(filename, "r") as file:
                self.lifts = json.load(file)
                # Convert string dates back to datetime.date objects
                for lift_id, data in self.lifts.items():
                    data["last_maintenance_date"] = datetime.datetime.strptime(data["last_maintenance_date"], "%Y-%m-%d").date()
                    data["next_maintenance_date"] = datetime.datetime.strptime(data["next_maintenance_date"], "%Y-%m-%d").date()
        except (IOError, json.JSONDecodeError):
            raise IOError("Failed to load data from file.")

# Example usage:
if __name__ == "__main__":
    scheduler = HydraulicLiftMaintenanceScheduler()

    # Add lifts
    scheduler.add_lift("Lift1", "2023-01-01")
    scheduler.add_lift("Lift2", "2023-02-15")

    # Update maintenance
    scheduler.update_maintenance("Lift1", "2023-04-01")

    # Get next maintenance date
    print(f"Next maintenance for Lift1: {scheduler.get_next_maintenance_date('Lift1')}")

    # List lifts due for maintenance
    print(f"Lifts due for maintenance: {scheduler.list_lifts_due_for_maintenance()}")

    # Save and load data
    scheduler.save_to_file("lifts_data.json")
    scheduler.load_from_file("lifts_data.json")
```
