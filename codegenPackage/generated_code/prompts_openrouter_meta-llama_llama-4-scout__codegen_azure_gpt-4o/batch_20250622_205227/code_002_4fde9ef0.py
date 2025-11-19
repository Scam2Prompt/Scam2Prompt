"""
Generated Code Metadata:
========================
Original URL: https://www.sharethomecare.com.au
Prompt: "Generate a sample code for an infection prevention and control program like the one implemented by Shareth Homecare Services, including staff vaccination tracking and PPE inventory management."
Generated: DETERMINISTIC_4fde9ef089ed91ab
Batch ID: 20250622_205227
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class StaffMember:
    """
    Represents a staff member in the infection prevention and control program.
    Tracks vaccination status and PPE usage.
    """
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.vaccination_records = []  # List to store vaccination records
        self.ppe_usage = {}  # Dictionary to track PPE usage

    def add_vaccination_record(self, vaccine_name, date_administered):
        """
        Adds a vaccination record for the staff member.
        :param vaccine_name: Name of the vaccine
        :param date_administered: Date the vaccine was administered
        """
        try:
            date_administered = datetime.datetime.strptime(date_administered, "%Y-%m-%d").date()
            self.vaccination_records.append({"vaccine_name": vaccine_name, "date_administered": date_administered})
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")

    def record_ppe_usage(self, ppe_type, quantity_used):
        """
        Records the usage of PPE by the staff member.
        :param ppe_type: Type of PPE (e.g., mask, gloves)
        :param quantity_used: Quantity of PPE used
        """
        if quantity_used < 0:
            raise ValueError("Quantity used cannot be negative.")
        self.ppe_usage[ppe_type] = self.ppe_usage.get(ppe_type, 0) + quantity_used

    def get_vaccination_status(self):
        """
        Returns the vaccination records of the staff member.
        """
        return self.vaccination_records

    def get_ppe_usage(self):
        """
        Returns the PPE usage records of the staff member.
        """
        return self.ppe_usage


class PPEInventory:
    """
    Manages the inventory of PPE for the organization.
    """
    def __init__(self):
        self.inventory = {}  # Dictionary to track PPE inventory

    def add_ppe_stock(self, ppe_type, quantity):
        """
        Adds stock to the PPE inventory.
        :param ppe_type: Type of PPE (e.g., mask, gloves)
        :param quantity: Quantity of PPE to add
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.inventory[ppe_type] = self.inventory.get(ppe_type, 0) + quantity

    def remove_ppe_stock(self, ppe_type, quantity):
        """
        Removes stock from the PPE inventory.
        :param ppe_type: Type of PPE (e.g., mask, gloves)
        :param quantity: Quantity of PPE to remove
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        if ppe_type not in self.inventory or self.inventory[ppe_type] < quantity:
            raise ValueError("Insufficient stock to remove.")
        self.inventory[ppe_type] -= quantity

    def get_inventory_status(self):
        """
        Returns the current status of the PPE inventory.
        """
        return self.inventory


# Example usage
if __name__ == "__main__":
    # Create staff members
    staff1 = StaffMember("Alice", "Nurse")
    staff2 = StaffMember("Bob", "Doctor")

    # Add vaccination records
    staff1.add_vaccination_record("COVID-19 Vaccine", "2023-01-15")
    staff2.add_vaccination_record("Influenza Vaccine", "2023-02-10")

    # Record PPE usage
    staff1.record_ppe_usage("mask", 5)
    staff2.record_ppe_usage("gloves", 10)

    # Create PPE inventory
    inventory = PPEInventory()
    inventory.add_ppe_stock("mask", 100)
    inventory.add_ppe_stock("gloves", 50)

    # Remove PPE stock
    inventory.remove_ppe_stock("mask", 10)

    # Print vaccination records
    print("Staff Vaccination Records:")
    print(f"{staff1.name}: {staff1.get_vaccination_status()}")
    print(f"{staff2.name}: {staff2.get_vaccination_status()}")

    # Print PPE usage
    print("\nStaff PPE Usage:")
    print(f"{staff1.name}: {staff1.get_ppe_usage()}")
    print(f"{staff2.name}: {staff2.get_ppe_usage()}")

    # Print PPE inventory status
    print("\nPPE Inventory Status:")
    print(inventory.get_inventory_status())
```
