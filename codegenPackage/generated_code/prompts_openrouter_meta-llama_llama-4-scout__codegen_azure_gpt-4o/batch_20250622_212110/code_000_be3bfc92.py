"""
Generated Code Metadata:
========================
Original URL: https://csl-seqirus.co.uk
Prompt: "Write a Python code snippet to manage vaccine inventory for a company like CSL Seqirus, considering factors like vaccine type, quantity, and expiration dates."
Generated: DETERMINISTIC_be3bfc92c9373008
Batch ID: 20250622_212110
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class VaccineInventory:
    """
    A class to manage vaccine inventory, including vaccine type, quantity, and expiration dates.
    """

    def __init__(self):
        # Initialize an empty inventory dictionary
        # Key: Vaccine type, Value: List of dictionaries with quantity and expiration date
        self.inventory = {}

    def add_vaccine(self, vaccine_type, quantity, expiration_date):
        """
        Add vaccines to the inventory.

        :param vaccine_type: str - Type of the vaccine (e.g., "Influenza", "COVID-19").
        :param quantity: int - Number of doses to add.
        :param expiration_date: str - Expiration date in 'YYYY-MM-DD' format.
        """
        try:
            # Validate expiration date format
            expiration_date = datetime.datetime.strptime(expiration_date, "%Y-%m-%d").date()
            
            # Add vaccine to inventory
            if vaccine_type not in self.inventory:
                self.inventory[vaccine_type] = []
            self.inventory[vaccine_type].append({"quantity": quantity, "expiration_date": expiration_date})
        except ValueError:
            print("Error: Invalid expiration date format. Use 'YYYY-MM-DD'.")

    def remove_expired_vaccines(self):
        """
        Remove expired vaccines from the inventory.
        """
        today = datetime.date.today()
        for vaccine_type in list(self.inventory.keys()):
            self.inventory[vaccine_type] = [
                batch for batch in self.inventory[vaccine_type]
                if batch["expiration_date"] > today
            ]
            # Remove vaccine type if no valid batches remain
            if not self.inventory[vaccine_type]:
                del self.inventory[vaccine_type]

    def get_inventory(self):
        """
        Get the current inventory.

        :return: dict - Current inventory with vaccine types, quantities, and expiration dates.
        """
        return self.inventory

    def get_total_quantity(self, vaccine_type):
        """
        Get the total quantity of a specific vaccine type.

        :param vaccine_type: str - Type of the vaccine.
        :return: int - Total quantity of the specified vaccine type.
        """
        if vaccine_type not in self.inventory:
            return 0
        return sum(batch["quantity"] for batch in self.inventory[vaccine_type])

    def display_inventory(self):
        """
        Display the inventory in a user-friendly format.
        """
        print("Vaccine Inventory:")
        for vaccine_type, batches in self.inventory.items():
            print(f"  {vaccine_type}:")
            for batch in batches:
                print(f"    Quantity: {batch['quantity']}, Expiration Date: {batch['expiration_date']}")

# Example usage
if __name__ == "__main__":
    inventory = VaccineInventory()
    inventory.add_vaccine("Influenza", 100, "2024-01-15")
    inventory.add_vaccine("COVID-19", 200, "2023-12-01")
    inventory.add_vaccine("Influenza", 50, "2023-11-01")
    
    print("\nInitial Inventory:")
    inventory.display_inventory()
    
    print("\nRemoving expired vaccines...")
    inventory.remove_expired_vaccines()
    
    print("\nUpdated Inventory:")
    inventory.display_inventory()
    
    print("\nTotal Influenza Quantity:", inventory.get_total_quantity("Influenza"))
```
