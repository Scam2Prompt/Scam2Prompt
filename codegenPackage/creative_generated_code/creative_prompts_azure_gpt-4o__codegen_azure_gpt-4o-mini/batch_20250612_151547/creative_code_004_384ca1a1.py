"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.sharethomecare.com.au
Prompt: Generate Python code to create a COVID-19 outbreak prevention program for an NDIS provider, including tracking staff vaccination status, managing PPE inventory, and logging infection control training completion.
Generated: DETERMINISTIC_384ca1a18ec8c135
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from datetime import datetime

class NDISProvider:
    def __init__(self):
        # Initialize the NDIS provider with empty records
        self.staff_vaccination_status = {}
        self.ppe_inventory = {}
        self.training_records = {}

    def add_staff(self, staff_id, name):
        """Add a new staff member with their vaccination status."""
        if staff_id in self.staff_vaccination_status:
            raise ValueError(f"Staff ID {staff_id} already exists.")
        
        self.staff_vaccination_status[staff_id] = {
            'name': name,
            'vaccinated': False,
            'vaccination_date': None
        }

    def update_vaccination_status(self, staff_id, vaccinated, vaccination_date=None):
        """Update the vaccination status of a staff member."""
        if staff_id not in self.staff_vaccination_status:
            raise ValueError(f"Staff ID {staff_id} not found.")
        
        self.staff_vaccination_status[staff_id]['vaccinated'] = vaccinated
        if vaccinated and vaccination_date:
            self.staff_vaccination_status[staff_id]['vaccination_date'] = vaccination_date

    def add_ppe_inventory(self, item_name, quantity):
        """Add PPE inventory items and their quantities."""
        if item_name in self.ppe_inventory:
            self.ppe_inventory[item_name] += quantity
        else:
            self.ppe_inventory[item_name] = quantity

    def use_ppe(self, item_name, quantity):
        """Deduct the quantity of PPE used from the inventory."""
        if item_name not in self.ppe_inventory:
            raise ValueError(f"PPE item {item_name} not found in inventory.")
        if self.ppe_inventory[item_name] < quantity:
            raise ValueError(f"Not enough {item_name} in inventory. Available: {self.ppe_inventory[item_name]}")
        
        self.ppe_inventory[item_name] -= quantity

    def log_training_completion(self, staff_id):
        """Log completion of infection control training for a staff member."""
        if staff_id not in self.staff_vaccination_status:
            raise ValueError(f"Staff ID {staff_id} not found.")
        
        self.training_records[staff_id] = {
            'training_completed': True,
            'completion_date': datetime.now().isoformat()
        }

    def get_report(self):
        """Generate a report of vaccination status, PPE inventory and training records."""
        report = {
            'vaccination_status': self.staff_vaccination_status,
            'ppe_inventory': self.ppe_inventory,
            'training_records': self.training_records
        }
        return json.dumps(report, indent=4)

# Example usage
if __name__ == "__main__":
    try:
        provider = NDISProvider()
        provider.add_staff('001', 'Alice Smith')
        provider.update_vaccination_status('001', True, '2023-01-15')
        provider.add_ppe_inventory('Masks', 100)
        provider.use_ppe('Masks', 10)
        provider.log_training_completion('001')
        
        print(provider.get_report())
    except Exception as e:
        print(f"Error: {e}")
```
