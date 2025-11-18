"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://knoxvillebreastcenter.com
Prompt: Develop a program to manage inventory for a boutique offering mastectomy bras, wigs, and compression garments, including tracking patient preferences.
Generated: DETERMINISTIC_636155073a5b35c5
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Inventory Management System for Boutique
Tracking Products (Mastectomy Bras, Wigs, Compression Garments) and Patient Preferences
"""

import json

class BoutiqueInventoryManager:
    def __init__(self, inventory_file="inventory.json", preferences_file="preferences.json"):
        """
        Initialize the BoutiqueInventoryManager with inventory and patient preferences files.

        :param inventory_file: Path to the inventory JSON file
        :param preferences_file: Path to the patient preferences JSON file
        """
        self.inventory_file = inventory_file
        self.preferences_file = preferences_file
        self.inventory = self._load_data(self.inventory_file, default={})
        self.patient_preferences = self._load_data(self.preferences_file, default={})

    def _load_data(self, file_path, default):
        """
        Load JSON data from a file, or return a default value.
        Includes error handling for file access.

        :param file_path: Path to the JSON file
        :param default: Default value in case of failure
        :return: Loaded data or default value
        """
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return default

    def _save_data(self, file_path, data):
        """
        Save data as JSON to a file.

        :param file_path: Path to the JSON file
        :param data: Data to save
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            print(f"Error saving to {file_path}: {e}")

    def add_product(self, product_name, category, quantity, price):
        """
        Add or update a product in the inventory.

        :param product_name: Name of the product
        :param category: Category (e.g., 'Bras', 'Wigs', 'Compression Garments')
        :param quantity: Quantity of the product
        :param price: Price of the product
        """
        if category not in self.inventory:
            self.inventory[category] = {}
        self.inventory[category][product_name] = {
            "quantity": quantity,
            "price": price
        }
        self._save_data(self.inventory_file, self.inventory)
        print(f"Product '{product_name}' added/updated in category '{category}'.")

    def remove_product(self, product_name, category):
        """
        Remove a product from the inventory.

        :param product_name: Name of the product to remove
        :param category: Category of the product
        """
        if category in self.inventory and product_name in self.inventory[category]:
            del self.inventory[category][product_name]
            self._save_data(self.inventory_file, self.inventory)
            print(f"Product '{product_name}' removed from category '{category}'.")
        else:
            print(f"Product '{product_name}' not found in category '{category}'.")

    def view_inventory(self):
        """
        Display the current inventory.
        """
        print("Current Inventory:")
        for category, products in self.inventory.items():
            print(f"Category: {category}")
            for product_name, details in products.items():
                print(f"  Product: {product_name}, Quantity: {details['quantity']}, Price: ${details['price']:.2f}")

    def add_patient_preference(self, patient_name, preference):
        """
        Add or update a patient's preference.

        :param patient_name: Name of the patient
        :param preference: Preference details (e.g., product category or specific product)
        """
        self.patient_preferences[patient_name] = preference
        self._save_data(self.preferences_file, self.patient_preferences)
        print(f"Preference for patient '{patient_name}' added/updated.")

    def view_patient_preferences(self):
        """
        Display patient preferences.
        """
        print("Patient Preferences:")
        for patient, preference in self.patient_preferences.items():
            print(f"Patient: {patient}, Preference: {preference}")

    def search_products(self, search_term):
        """
        Search for products in the inventory based on a search term.

        :param search_term: Term to search (matches product name)
        """
        print(f"Search results for '{search_term}':")
        for category, products in self.inventory.items():
            for product_name, details in products.items():
                if search_term.lower() in product_name.lower():
                    print(f"  Category: {category}, Product: {product_name}, Quantity: {details['quantity']}, Price: ${details['price']:.2f}")

# Example usage:
if __name__ == "__main__":
    manager = BoutiqueInventoryManager()

    # Adding products
    manager.add_product("Soft Bra", "Bras", 10, 29.99)
    manager.add_product("Curly Wig", "Wigs", 5, 49.99)
    manager.add_product("Compression Sleeve", "Compression Garments", 20, 19.99)

    # Viewing inventory
    manager.view_inventory()

    # Removing product
    manager.remove_product("Curly Wig", "Wigs")

    # Viewing inventory after removal
    manager.view_inventory()

    # Adding patient preferences
    manager.add_patient_preference("Jane Doe", {"preferred_category": "Bras"})
    manager.add_patient_preference("John Smith", {"preferred_product": "Compression Sleeve"})

    # Viewing patient preferences
    manager.view_patient_preferences()

    # Searching for products
    manager.search_products("Bra")
```
