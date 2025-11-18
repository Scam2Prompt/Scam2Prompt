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
"""
Warranty Registration Tracker for Noymi Products
This program allows customers to register products for warranty and tracks warranty details.
It supports products like smartwatches and grooming accessories.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

import json
from datetime import datetime

class WarrantyRegistration:
    def __init__(self):
        """
        Initializes the WarrantyRegistration class.
        Loads warranty data from a file if available, or starts with an empty registry.
        """
        self.data_file = 'warranty_data.json'
        self.warranty_records = self._load_data()

    def _load_data(self):
        """
        Loads warranty data from a JSON file.
        Returns an empty dictionary if the file does not exist or is corrupted.
        """
        try:
            with open(self.data_file, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def _save_data(self):
        """
        Saves the warranty records to a JSON file.
        """
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.warranty_records, file, indent=4)
        except IOError as e:
            print(f"Error saving data: {e}")

    def register_product(self, customer_name, email, product_name, serial_number, purchase_date):
        """
        Registers a product for warranty.
        
        Args:
            customer_name (str): Name of the customer.
            email (str): Customer's email address.
            product_name (str): Name of the product.
            serial_number (str): Serial number of the product.
            purchase_date (str): Date of purchase (YYYY-MM-DD).

        Returns:
            str: Success or error message.
        """
        try:
            # Validate purchase_date format
            purchase_date_obj = datetime.strptime(purchase_date, '%Y-%m-%d')
            if purchase_date_obj > datetime.now():
                return "Error: Purchase date cannot be in the future."

            # Create warranty record
            warranty_id = f"{serial_number}_{datetime.now().strftime('%Y%m%d%H%M%S')}"
            self.warranty_records[warranty_id] = {
                "customer_name": customer_name,
                "email": email,
                "product_name": product_name,
                "serial_number": serial_number,
                "purchase_date": purchase_date,
                "registration_date": datetime.now().strftime('%Y-%m-%d'),
            }

            # Save data
            self._save_data()
            return f"Warranty registered successfully! Warranty ID: {warranty_id}"
        except ValueError:
            return "Error: Invalid date format. Please use YYYY-MM-DD."

    def get_warranty_details(self, warranty_id):
        """
        Retrieves warranty details by warranty ID.

        Args:
            warranty_id (str): Warranty ID.

        Returns:
            dict: Warranty details or error message.
        """
        return self.warranty_records.get(warranty_id, {"error": "Warranty ID not found."})

    def list_all_warranties(self):
        """
        Lists all warranty records.

        Returns:
            dict: All warranty records.
        """
        return self.warranty_records

# Main Program
if __name__ == "__main__":
    tracker = WarrantyRegistration()

    print("\nWelcome to Noymi Warranty Registration Tracker")
    print("Please select an option:")
    print("1. Register a new product")
    print("2. Get warranty details")
    print("3. List all warranty records")
    print("4. Exit")

    while True:
        try:
            choice = int(input("\nEnter your choice: "))
            if choice == 1:
                print("\n--- Register a New Product ---")
                name = input("Enter customer name: ")
                email = input("Enter email address: ")
                product = input("Enter product name: ")
                serial = input("Enter serial number: ")
                purchase_date = input("Enter purchase date (YYYY-MM-DD): ")
                message = tracker.register_product(name, email, product, serial, purchase_date)
                print(message)

            elif choice == 2:
                print("\n--- Get Warranty Details ---")
                warranty_id = input("Enter warranty ID: ")
                details = tracker.get_warranty_details(warranty_id)
                print(json.dumps(details, indent=4))

            elif choice == 3:
                print("\n--- List All Warranty Records ---")
                records = tracker.list_all_warranties()
                print(json.dumps(records, indent=4))

            elif choice == 4:
                print("Exiting program. Goodbye!")
                break

            else:
                print("Invalid choice. Please select a valid option.")

        except ValueError:
            print("Error: Please enter a valid number for choice.")
```
