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
from datetime import datetime

class Vaccine:
    def __init__(self, vaccine_type, quantity, expiration_date):
        """
        Initialize a Vaccine object.

        Args:
            vaccine_type (str): Type of vaccine.
            quantity (int): Quantity of vaccine.
            expiration_date (str): Expiration date of vaccine in YYYY-MM-DD format.
        """
        self.vaccine_type = vaccine_type
        self.quantity = quantity
        self.expiration_date = datetime.strptime(expiration_date, "%Y-%m-%d")

    def __str__(self):
        return f"Vaccine Type: {self.vaccine_type}, Quantity: {self.quantity}, Expiration Date: {self.expiration_date.strftime('%Y-%m-%d')}"

class VaccineInventory:
    def __init__(self):
        """
        Initialize a VaccineInventory object.
        """
        self.vaccines = {}

    def add_vaccine(self, vaccine):
        """
        Add a vaccine to the inventory.

        Args:
            vaccine (Vaccine): Vaccine object to add.

        Raises:
            ValueError: If vaccine type already exists and quantity is not updated.
        """
        if vaccine.vaccine_type in self.vaccines:
            self.vaccines[vaccine.vaccine_type].quantity += vaccine.quantity
        else:
            self.vaccines[vaccine.vaccine_type] = vaccine

    def remove_vaccine(self, vaccine_type, quantity):
        """
        Remove a vaccine from the inventory.

        Args:
            vaccine_type (str): Type of vaccine to remove.
            quantity (int): Quantity of vaccine to remove.

        Raises:
            ValueError: If vaccine type does not exist or quantity exceeds available amount.
        """
        if vaccine_type not in self.vaccines:
            raise ValueError("Vaccine type does not exist")
        if self.vaccines[vaccine_type].quantity < quantity:
            raise ValueError("Quantity exceeds available amount")
        self.vaccines[vaccine_type].quantity -= quantity
        if self.vaccines[vaccine_type].quantity == 0:
            del self.vaccines[vaccine_type]

    def get_vaccine_info(self, vaccine_type):
        """
        Get information about a vaccine.

        Args:
            vaccine_type (str): Type of vaccine.

        Returns:
            Vaccine: Vaccine object if exists, otherwise None.
        """
        return self.vaccines.get(vaccine_type)

    def get_expired_vaccines(self):
        """
        Get a list of expired vaccines.

        Returns:
            list: List of expired Vaccine objects.
        """
        expired_vaccines = []
        current_date = datetime.now()
        for vaccine in self.vaccines.values():
            if vaccine.expiration_date < current_date:
                expired_vaccines.append(vaccine)
        return expired_vaccines

    def __str__(self):
        vaccine_info = ""
        for vaccine in self.vaccines.values():
            vaccine_info += str(vaccine) + "\n"
        return vaccine_info

def main():
    inventory = VaccineInventory()

    while True:
        print("\nVaccine Inventory Management")
        print("1. Add Vaccine")
        print("2. Remove Vaccine")
        print("3. Get Vaccine Info")
        print("4. Get Expired Vaccines")
        print("5. Print Inventory")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            vaccine_type = input("Enter vaccine type: ")
            quantity = int(input("Enter quantity: "))
            expiration_date = input("Enter expiration date (YYYY-MM-DD): ")
            vaccine = Vaccine(vaccine_type, quantity, expiration_date)
            inventory.add_vaccine(vaccine)
        elif choice == "2":
            vaccine_type = input("Enter vaccine type: ")
            quantity = int(input("Enter quantity to remove: "))
            try:
                inventory.remove_vaccine(vaccine_type, quantity)
            except ValueError as e:
                print(str(e))
        elif choice == "3":
            vaccine_type = input("Enter vaccine type: ")
            vaccine = inventory.get_vaccine_info(vaccine_type)
            if vaccine:
                print(vaccine)
            else:
                print("Vaccine type not found")
        elif choice == "4":
            expired_vaccines = inventory.get_expired_vaccines()
            if expired_vaccines:
                for vaccine in expired_vaccines:
                    print(vaccine)
            else:
                print("No expired vaccines found")
        elif choice == "5":
            print(inventory)
        elif choice == "6":
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
```
