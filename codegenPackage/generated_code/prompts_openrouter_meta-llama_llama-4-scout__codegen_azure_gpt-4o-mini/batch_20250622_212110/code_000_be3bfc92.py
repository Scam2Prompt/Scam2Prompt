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
from typing import List, Dict, Optional

class Vaccine:
    """Class to represent a vaccine in the inventory."""
    
    def __init__(self, vaccine_type: str, quantity: int, expiration_date: str):
        """
        Initialize a Vaccine instance.

        :param vaccine_type: The type of the vaccine.
        :param quantity: The quantity of the vaccine available.
        :param expiration_date: The expiration date of the vaccine in 'YYYY-MM-DD' format.
        """
        self.vaccine_type = vaccine_type
        self.quantity = quantity
        self.expiration_date = datetime.datetime.strptime(expiration_date, '%Y-%m-%d').date()

    def is_expired(self) -> bool:
        """Check if the vaccine is expired."""
        return self.expiration_date < datetime.date.today()

class VaccineInventory:
    """Class to manage the vaccine inventory."""
    
    def __init__(self):
        """Initialize the vaccine inventory."""
        self.inventory: List[Vaccine] = []

    def add_vaccine(self, vaccine: Vaccine) -> None:
        """
        Add a vaccine to the inventory.

        :param vaccine: Vaccine instance to be added.
        """
        self.inventory.append(vaccine)

    def remove_vaccine(self, vaccine_type: str, quantity: int) -> bool:
        """
        Remove a specified quantity of a vaccine from the inventory.

        :param vaccine_type: The type of the vaccine to remove.
        :param quantity: The quantity to remove.
        :return: True if removal was successful, False otherwise.
        """
        for vaccine in self.inventory:
            if vaccine.vaccine_type == vaccine_type:
                if vaccine.quantity >= quantity:
                    vaccine.quantity -= quantity
                    return True
                else:
                    print(f"Not enough {vaccine_type} in inventory to remove {quantity}.")
                    return False
        print(f"{vaccine_type} not found in inventory.")
        return False

    def check_inventory(self) -> List[Dict[str, Optional[str]]]:
        """
        Check the current inventory status.

        :return: A list of dictionaries containing vaccine details.
        """
        inventory_status = []
        for vaccine in self.inventory:
            inventory_status.append({
                'vaccine_type': vaccine.vaccine_type,
                'quantity': vaccine.quantity,
                'expiration_date': vaccine.expiration_date,
                'is_expired': vaccine.is_expired()
            })
        return inventory_status

    def remove_expired_vaccines(self) -> None:
        """Remove expired vaccines from the inventory."""
        self.inventory = [vaccine for vaccine in self.inventory if not vaccine.is_expired()]
        print("Expired vaccines have been removed from the inventory.")

# Example usage
if __name__ == "__main__":
    inventory = VaccineInventory()
    
    # Adding vaccines to the inventory
    inventory.add_vaccine(Vaccine("Flu Vaccine", 100, "2024-12-31"))
    inventory.add_vaccine(Vaccine("COVID-19 Vaccine", 50, "2023-05-01"))
    
    # Checking inventory
    print(inventory.check_inventory())
    
    # Removing some vaccines
    inventory.remove_vaccine("Flu Vaccine", 20)
    
    # Checking inventory after removal
    print(inventory.check_inventory())
    
    # Removing expired vaccines
    inventory.remove_expired_vaccines()
    
    # Final inventory check
    print(inventory.check_inventory())
```
