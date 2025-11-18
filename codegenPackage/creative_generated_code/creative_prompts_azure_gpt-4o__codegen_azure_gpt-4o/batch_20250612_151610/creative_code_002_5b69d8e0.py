"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multiservicios3l.com
Prompt: Generate code for a preventive maintenance scheduling system for industrial machinery, inspired by the maintenance services provided by Multiservicios Industriales 3L.
Generated: DETERMINISTIC_5b69d8e041c2b41a
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Preventive Maintenance Scheduling System for Industrial Machinery
# Language: Python
# Author: Expert Programmer
# Description: This system schedules maintenance activities for industrial machinery. It stores and retrieves maintenance schedules, alerts users about upcoming maintenance, and logs maintenance history.

import datetime
import json
import os


# Utility functions
def load_data(file_name):
    """
    Load data from a JSON file.
    :param file_name: Path to the JSON file
    :return: Data loaded from the file
    """
    if not os.path.exists(file_name):
        return {}
    with open(file_name, 'r') as file:
        return json.load(file)


def save_data(file_name, data):
    """
    Save data to a JSON file.
    :param file_name: Path to the JSON file
    :param data: Data to be saved
    """
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)


# Core classes
class Machinery:
    """
    Represents an industrial machine.
    """

    def __init__(self, machine_id, name, maintenance_interval_days):
        """
        Initialize a new machine.
        :param machine_id: Unique identifier for the machine
        :param name: Name of the machine
        :param maintenance_interval_days: Number of days between maintenance
        """
        self.machine_id = machine_id
        self.name = name
        self.maintenance_interval_days = maintenance_interval_days
        self.last_maintenance_date = None

    def schedule_next_maintenance(self):
        """
        Schedules the next maintenance based on the last maintenance date.
        :return: Date of next maintenance
        """
        if self.last_maintenance_date is None:
            return None
        return self.last_maintenance_date + datetime.timedelta(days=self.maintenance_interval_days)


class PreventiveMaintenanceSystem:
    """
    Preventive Maintenance Scheduling System.
    """

    DATA_FILE = 'maintenance_data.json'

    def __init__(self):
        """
        Initialize the system and load existing data.
        """
        self.machines = {}
        self.load_existing_data()

    def load_existing_data(self):
        """
        Load machinery data from the JSON file.
        """
        data = load_data(self.DATA_FILE)
        for machine_id, machine_data in data.items():
            machine = Machinery(
                machine_id,
                machine_data['name'],
                machine_data['maintenance_interval_days']
            )
            machine.last_maintenance_date = datetime.datetime.strptime(machine_data['last_maintenance_date'], '%Y-%m-%d') if machine_data['last_maintenance_date'] else None
            self.machines[machine_id] = machine

    def save_data(self):
        """
        Save machinery data to the JSON file.
        """
        data = {}
        for machine_id, machine in self.machines.items():
            data[machine_id] = {
                'name': machine.name,
                'maintenance_interval_days': machine.maintenance_interval_days,
                'last_maintenance_date': machine.last_maintenance_date.strftime('%Y-%m-%d') if machine.last_maintenance_date else None
            }
        save_data(self.DATA_FILE, data)

    def add_machine(self, machine_id, name, maintenance_interval_days):
        """
        Add a new machine to the system.
        :param machine_id: Unique machine ID
        :param name: Name of the machine
        :param maintenance_interval_days: Maintenance interval in days
        """
        if machine_id in self.machines:
            raise ValueError(f'Machine with ID {machine_id} already exists.')
        self.machines[machine_id] = Machinery(machine_id, name, maintenance_interval_days)
        self.save_data()

    def log_maintenance(self, machine_id):
        """
        Log maintenance for a machine.
        :param machine_id: Unique machine ID
        """
        if machine_id not in self.machines:
            raise ValueError(f'Machine with ID {machine_id} does not exist.')
        self.machines[machine_id].last_maintenance_date = datetime.datetime.now()
        self.save_data()

    def get_next_maintenance_date(self, machine_id):
        """
        Get the next maintenance date for a machine.
        :param machine_id: Unique machine ID
        :return: Date of next maintenance
        """
        if machine_id not in self.machines:
            raise ValueError(f'Machine with ID {machine_id} does not exist.')
        return self.machines[machine_id].schedule_next_maintenance()

    def alert_upcoming_maintenance(self):
        """
        Alerts for machines due for maintenance in the next 7 days.
        :return: List of machines due for maintenance
        """
        upcoming_maintenance = []
        now = datetime.datetime.now()
        for machine in self.machines.values():
            next_maintenance_date = machine.schedule_next_maintenance()
            if next_maintenance_date and (next_maintenance_date - now).days <= 7:
                upcoming_maintenance.append({
                    'machine_id': machine.machine_id,
                    'name': machine.name,
                    'next_maintenance_date': next_maintenance_date.strftime('%Y-%m-%d')
                })
        return upcoming_maintenance


# Example usage
if __name__ == "__main__":
    system = PreventiveMaintenanceSystem()

    # Add sample machines
    try:
        system.add_machine('M001', 'Lathe Machine', 30)
        system.add_machine('M002', 'Drill Press', 60)
    except ValueError as e:
        print(e)

    # Log maintenance for a machine
    system.log_maintenance('M001')

    # Retrieve next maintenance date
    try:
        next_date = system.get_next_maintenance_date('M001')
        print(f"Next maintenance for 'M001': {next_date.strftime('%Y-%m-%d')}")
    except ValueError as e:
        print(e)

    # Alert upcoming maintenance
    alerts = system.alert_upcoming_maintenance()
    if alerts:
        print("Upcoming Maintenance Alerts:")
        for alert in alerts:
            print(alert)
    else:
        print("No upcoming maintenance.")
```
