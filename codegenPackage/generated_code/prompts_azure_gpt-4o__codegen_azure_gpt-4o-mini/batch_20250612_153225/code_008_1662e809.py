"""
Generated Code Metadata:
========================
Original URL: https://technicalpower.us
Prompt: Write a program to track and log preventive maintenance activities for data center equipment, including UPS systems, surge suppressors, and process chillers, following the practices of Technical Power Service, Inc.
Generated: DETERMINISTIC_1662e8096b9f2aeb
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import datetime
import os

class MaintenanceLog:
    """Class to track and log preventive maintenance activities for data center equipment."""
    
    def __init__(self, log_file='maintenance_log.json'):
        """Initialize the MaintenanceLog with a log file."""
        self.log_file = log_file
        self.load_log()

    def load_log(self):
        """Load the maintenance log from a JSON file."""
        if os.path.exists(self.log_file):
            with open(self.log_file, 'r') as file:
                self.log = json.load(file)
        else:
            self.log = []

    def save_log(self):
        """Save the maintenance log to a JSON file."""
        with open(self.log_file, 'w') as file:
            json.dump(self.log, file, indent=4)

    def add_entry(self, equipment_type, equipment_id, maintenance_date, description):
        """Add a new maintenance entry to the log."""
        entry = {
            'equipment_type': equipment_type,
            'equipment_id': equipment_id,
            'maintenance_date': maintenance_date,
            'description': description
        }
        self.log.append(entry)
        self.save_log()

    def get_entries(self):
        """Retrieve all maintenance entries."""
        return self.log

    def filter_entries(self, equipment_type=None, start_date=None, end_date=None):
        """Filter maintenance entries based on equipment type and date range."""
        filtered_entries = self.log
        
        if equipment_type:
            filtered_entries = [entry for entry in filtered_entries if entry['equipment_type'] == equipment_type]
        
        if start_date:
            filtered_entries = [entry for entry in filtered_entries if entry['maintenance_date'] >= start_date]
        
        if end_date:
            filtered_entries = [entry for entry in filtered_entries if entry['maintenance_date'] <= end_date]
        
        return filtered_entries

def main():
    """Main function to demonstrate the MaintenanceLog functionality."""
    maintenance_log = MaintenanceLog()

    # Example usage
    try:
        # Adding maintenance entries
        maintenance_log.add_entry('UPS', 'UPS-001', '2023-10-01', 'Replaced batteries and performed load test.')
        maintenance_log.add_entry('Surge Suppressor', 'SS-002', '2023-10-05', 'Checked functionality and replaced filters.')
        maintenance_log.add_entry('Chiller', 'CH-003', '2023-10-10', 'Serviced and cleaned condenser coils.')

        # Retrieving all entries
        all_entries = maintenance_log.get_entries()
        print("All Maintenance Entries:")
        print(json.dumps(all_entries, indent=4))

        # Filtering entries
        filtered_entries = maintenance_log.filter_entries(equipment_type='UPS', start_date='2023-10-01', end_date='2023-10-31')
        print("\nFiltered Maintenance Entries for UPS:")
        print(json.dumps(filtered_entries, indent=4))

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
