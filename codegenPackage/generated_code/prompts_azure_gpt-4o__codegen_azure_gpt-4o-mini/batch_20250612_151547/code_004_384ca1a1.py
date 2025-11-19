"""
Generated Code Metadata:
========================
Original URL: https://www.sharethomecare.com.au
Prompt: Generate Python code to create a COVID-19 outbreak prevention program for an NDIS provider, including tracking staff vaccination status, managing PPE inventory, and logging infection control training completion.
Generated: DETERMINISTIC_384ca1a18ec8c135
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime

class NDISProvider:
    def __init__(self):
        # Initialize the provider with empty records
        self.staff_vaccination_status = {}
        self.ppe_inventory = {}
        self.training_records = {}

    def add_staff(self, staff_id, name):
        """Add a new staff member with their vaccination status."""
        if staff_id in self.staff_vaccination_status:
            raise ValueError("Staff ID already exists.")
        self.staff_vaccination_status[staff_id] = {
            "name": name,
            "vaccinated": False,
            "vaccination_date": None
        }
        print(f"Added staff: {name} with ID: {staff_id}")

    def update_vaccination_status(self, staff_id, vaccinated, vaccination_date=None):
        """Update the vaccination status of a staff member."""
        if staff_id not in self.staff_vaccination_status:
            raise ValueError("Staff ID not found.")
        self.staff_vaccination_status[staff_id]["vaccinated"] = vaccinated
        if vaccinated and vaccination_date:
            self.staff_vaccination_status[staff_id]["vaccination_date"] = vaccination_date
        print(f"Updated vaccination status for staff ID: {staff_id}")

    def add_ppe_inventory(self, item_name, quantity):
        """Add PPE items to the inventory."""
        if item_name in self.ppe_inventory:
            self.ppe_inventory[item_name] += quantity
        else:
            self.ppe_inventory[item_name] = quantity
        print(f"Added {quantity} of {item_name} to PPE inventory.")

    def use_ppe(self, item_name, quantity):
        """Use PPE items from the inventory."""
        if item_name not in self.ppe_inventory or self.ppe_inventory[item_name] < quantity:
            raise ValueError("Insufficient PPE inventory.")
        self.ppe_inventory[item_name] -= quantity
        print(f"Used {quantity} of {item_name} from PPE inventory.")

    def log_training_completion(self, staff_id, training_name):
        """Log the completion of infection control training for a staff member."""
        if staff_id not in self.staff_vaccination_status:
            raise ValueError("Staff ID not found.")
        if staff_id not in self.training_records:
            self.training_records[staff_id] = []
        self.training_records[staff_id].append({
            "training_name": training_name,
            "completion_date": datetime.now().isoformat()
        })
        print(f"Logged training completion for staff ID: {staff_id} - {training_name}")

    def save_data(self, filename):
        """Save the current state of the provider's data to a JSON file."""
        data = {
            "staff_vaccination_status": self.staff_vaccination_status,
            "ppe_inventory": self.ppe_inventory,
            "training_records": self.training_records
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Data saved to {filename}")

    def load_data(self, filename):
        """Load the provider's data from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.staff_vaccination_status = data.get("staff_vaccination_status", {})
                self.ppe_inventory = data.get("ppe_inventory", {})
                self.training_records = data.get("training_records", {})
            print(f"Data loaded from {filename}")
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with empty records.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from the file {filename}. Starting with empty records.")

# Example usage
if __name__ == "__main__":
    provider = NDISProvider()
    provider.add_staff("001", "Alice Smith")
    provider.update_vaccination_status("001", True, "2023-01-15")
    provider.add_ppe_inventory("Masks", 100)
    provider.use_ppe("Masks", 10)
    provider.log_training_completion("001", "Infection Control Basics")
    provider.save_data("ndis_provider_data.json")
    provider.load_data("ndis_provider_data.json")
```
