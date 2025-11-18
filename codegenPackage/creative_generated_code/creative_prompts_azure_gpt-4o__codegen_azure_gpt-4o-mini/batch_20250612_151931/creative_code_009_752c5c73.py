"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://noymi.in
Prompt: Write a program to track warranty registrations for products sold by Noymi, such as smartwatches and grooming accessories.
Generated: DETERMINISTIC_752c5c7395a36305
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
from datetime import datetime, timedelta

class WarrantyRegistration:
    """
    A class to manage warranty registrations for Noymi products.
    """

    def __init__(self, product_name, purchase_date, warranty_period_months):
        """
        Initialize a new warranty registration instance.

        :param product_name: Name of the product
        :param purchase_date: Date of purchase in 'YYYY-MM-DD' format
        :param warranty_period_months: Warranty period in months
        """
        self.product_name = product_name
        self.purchase_date = datetime.strptime(purchase_date, '%Y-%m-%d')
        self.warranty_period = timedelta(days=warranty_period_months * 30)  # Approximate month to days
        self.registration_date = datetime.now()

    def is_warranty_valid(self):
        """
        Check if the warranty is still valid.

        :return: True if warranty is valid, False otherwise
        """
        return datetime.now() < (self.purchase_date + self.warranty_period)

    def to_dict(self):
        """
        Convert the warranty registration to a dictionary for easy serialization.

        :return: A dictionary representation of the warranty registration
        """
        return {
            'product_name': self.product_name,
            'purchase_date': self.purchase_date.strftime('%Y-%m-%d'),
            'registration_date': self.registration_date.strftime('%Y-%m-%d'),
            'warranty_period_months': self.warranty_period.days // 30,
            'is_valid': self.is_warranty_valid()
        }


class WarrantyManager:
    """
    A class to manage a collection of warranty registrations.
    """

    def __init__(self, storage_file='warranty_registrations.json'):
        """
        Initialize the WarrantyManager with a specified storage file.

        :param storage_file: Path to the JSON file for storing registrations
        """
        self.storage_file = storage_file
        self.registrations = self.load_registrations()

    def load_registrations(self):
        """
        Load existing warranty registrations from the storage file.

        :return: List of WarrantyRegistration instances
        """
        if os.path.exists(self.storage_file):
            with open(self.storage_file, 'r') as file:
                try:
                    data = json.load(file)
                    return [self.create_registration_from_dict(item) for item in data]
                except json.JSONDecodeError:
                    print("Error decoding JSON, starting with an empty list.")
                    return []
        return []

    def create_registration_from_dict(self, data):
        """
        Create a WarrantyRegistration instance from a dictionary.

        :param data: Dictionary representation of a warranty registration
        :return: A WarrantyRegistration instance
        """
        return WarrantyRegistration(data['product_name'], data['purchase_date'], data['warranty_period_months'])

    def save_registrations(self):
        """
        Save the current warranty registrations to the storage file.
        """
        with open(self.storage_file, 'w') as file:
            json.dump([registration.to_dict() for registration in self.registrations], file, indent=4)

    def register_product(self, product_name, purchase_date, warranty_period_months):
        """
        Register a new product warranty.

        :param product_name: Name of the product
        :param purchase_date: Date of purchase in 'YYYY-MM-DD' format
        :param warranty_period_months: Warranty period in months
        """
        new_registration = WarrantyRegistration(product_name, purchase_date, warranty_period_months)
        self.registrations.append(new_registration)
        self.save_registrations()

    def list_warranties(self):
        """
        List all registered warranties along with their validity status.
        """
        for registration in self.registrations:
            print(f"Product: {registration.product_name}, "
                  f"Purchase Date: {registration.purchase_date.strftime('%Y-%m-%d')}, "
                  f"Warranty Valid: {'Yes' if registration.is_warranty_valid() else 'No'}")


if __name__ == "__main__":
    # Example usage of the WarrantyManager
    manager = WarrantyManager()

    # Register a new product
    try:
        manager.register_product("Smartwatch", "2023-01-15", 24)  # 2-year warranty
        manager.register_product("Grooming Kit", "2023-03-01", 12)  # 1-year warranty
    except Exception as e:
        print(f"An error occurred while registering products: {e}")

    # List all warranties
    manager.list_warranties()
```
