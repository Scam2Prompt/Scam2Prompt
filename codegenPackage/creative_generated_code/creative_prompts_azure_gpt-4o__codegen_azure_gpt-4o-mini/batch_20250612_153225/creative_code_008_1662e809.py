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
import json
import datetime
import os

class MaintenanceRecord:
    """Class to represent a maintenance record for data center equipment."""

    def __init__(self, equipment_type, maintenance_date, description):
        self.equipment_type = equipment_type
        self.maintenance_date = maintenance_date
        self.description = description

    def to_dict(self):
        """Converts the maintenance record to a dictionary for easy serialization."""
        return {
            'equipment_type': self.equipment_type,
            'maintenance_date': self.maintenance_date.isoformat(),
            'description': self.description
        }

class MaintenanceLogger:
    """Class to log and manage maintenance records."""

    def __init__(self, log_file='maintenance_log.json'):
        self.log_file = log_file
        self.records = []
        self.load_records()

    def load_records(self):
        """Load existing maintenance records from the log file."""
        if os.path.exists(self.log_file):
            try:
                with open(self.log_file, 'r') as file:
                    self.records = [MaintenanceRecord(**record) for record in json.load(file)]
            except (IOError, json.JSONDecodeError) as e:
                print(f"Error loading records: {e}")

    def save_records(self):
        """Save the maintenance records to the log file."""
        try:
            with open(self.log_file, 'w') as file:
                json.dump([record.to_dict() for record in self.records], file, indent=4)
        except IOError as e:
            print(f"Error saving records: {e}")

    def log_maintenance(self, equipment_type, description):
        """Log a new maintenance activity."""
        maintenance_date = datetime.datetime.now()
        record = MaintenanceRecord(equipment_type, maintenance_date, description)
        self.records.append(record)
        self.save_records()
        print(f"Logged maintenance for {equipment_type} on {maintenance_date}")

    def display_records(self):
        """Display all logged maintenance records."""
        print("Maintenance Records:")
        for record in self.records:
            print(f"{record.equipment_type} - {record.maintenance_date}: {record.description}")

def main():
    """Main function to run the maintenance logging program."""
    logger = MaintenanceLogger()

    # Example usage
    logger.log_maintenance('UPS System', 'Replaced batteries and tested functionality.')
    logger.log_maintenance('Surge Suppressor', 'Inspected and replaced faulty components.')
    logger.log_maintenance('Process Chiller', 'Serviced and cleaned filters.')

    logger.display_records()

if __name__ == '__main__':
    main()
```
