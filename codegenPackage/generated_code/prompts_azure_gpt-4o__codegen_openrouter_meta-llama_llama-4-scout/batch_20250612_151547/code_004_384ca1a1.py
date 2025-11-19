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
# covid19_prevention_program.py

import datetime
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class StaffMember:
    """Represents an NDIS staff member."""

    def __init__(self, staff_id, name):
        self.staff_id = staff_id
        self.name = name
        self.vaccination_status = False
        self.training_completion = False

    def update_vaccination_status(self, status):
        """Updates the staff member's vaccination status."""
        self.vaccination_status = status

    def update_training_completion(self, completion):
        """Updates the staff member's training completion status."""
        self.training_completion = completion


class PPEInventory:
    """Manages PPE inventory."""

    def __init__(self):
        self.inventory = {
            "masks": 0,
            "gloves": 0,
            "gowns": 0,
            "sanitizer": 0
        }

    def update_inventory(self, item, quantity):
        """Updates the PPE inventory."""
        if item in self.inventory:
            self.inventory[item] += quantity
        else:
            logging.error(f"Invalid PPE item: {item}")

    def get_inventory(self):
        """Returns the current PPE inventory."""
        return self.inventory


class InfectionControlTraining:
    """Manages infection control training completion."""

    def __init__(self):
        self.training_completion_log = []

    def log_training_completion(self, staff_member):
        """Logs infection control training completion for a staff member."""
        self.training_completion_log.append({
            "staff_id": staff_member.staff_id,
            "completion_date": datetime.date.today()
        })
        staff_member.update_training_completion(True)


class COVID19PreventionProgram:
    """Manages COVID-19 outbreak prevention program."""

    def __init__(self):
        self.staff_members = {}
        self.ppe_inventory = PPEInventory()
        self.infection_control_training = InfectionControlTraining()

    def add_staff_member(self, staff_id, name):
        """Adds a new staff member."""
        self.staff_members[staff_id] = StaffMember(staff_id, name)

    def update_staff_vaccination_status(self, staff_id, status):
        """Updates a staff member's vaccination status."""
        if staff_id in self.staff_members:
            self.staff_members[staff_id].update_vaccination_status(status)
        else:
            logging.error(f"Staff member not found: {staff_id}")

    def update_ppe_inventory(self, item, quantity):
        """Updates the PPE inventory."""
        self.ppe_inventory.update_inventory(item, quantity)

    def log_infection_control_training(self, staff_id):
        """Logs infection control training completion for a staff member."""
        if staff_id in self.staff_members:
            self.infection_control_training.log_training_completion(self.staff_members[staff_id])
        else:
            logging.error(f"Staff member not found: {staff_id}")

    def get_staff_vaccination_status(self, staff_id):
        """Returns a staff member's vaccination status."""
        if staff_id in self.staff_members:
            return self.staff_members[staff_id].vaccination_status
        else:
            logging.error(f"Staff member not found: {staff_id}")
            return None

    def get_ppe_inventory(self):
        """Returns the current PPE inventory."""
        return self.ppe_inventory.get_inventory()

    def get_infection_control_training_log(self):
        """Returns the infection control training completion log."""
        return self.infection_control_training.training_completion_log


def main():
    program = COVID19PreventionProgram()

    # Add staff members
    program.add_staff_member("S001", "John Doe")
    program.add_staff_member("S002", "Jane Smith")

    # Update staff vaccination status
    program.update_staff_vaccination_status("S001", True)
    program.update_staff_vaccination_status("S002", False)

    # Update PPE inventory
    program.update_ppe_inventory("masks", 100)
    program.update_ppe_inventory("gloves", 500)

    # Log infection control training completion
    program.log_infection_control_training("S001")
    program.log_infection_control_training("S002")

    # Print staff vaccination status
    print("Staff Vaccination Status:")
    for staff_id, staff_member in program.staff_members.items():
        print(f"{staff_member.name}: {staff_member.vaccination_status}")

    # Print PPE inventory
    print("\nPPE Inventory:")
    for item, quantity in program.get_ppe_inventory().items():
        print(f"{item.capitalize()}: {quantity}")

    # Print infection control training completion log
    print("\nInfection Control Training Completion Log:")
    for log_entry in program.get_infection_control_training_log():
        print(f"Staff ID: {log_entry['staff_id']}, Completion Date: {log_entry['completion_date']}")


if __name__ == "__main__":
    main()
```
