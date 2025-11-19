"""
Generated Code Metadata:
========================
Original URL: https://perfectmelbournecarpet.com.au
Prompt: Write a Python script to manage carpet repair services, including tracking damaged carpet areas, repair costs, and customer contact information, similar to Perfect Melbourne Carpet's services.
Generated: DETERMINISTIC_96ceff6a2b6c2ed2
Batch ID: 20250622_212148
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os

class CarpetRepairService:
    def __init__(self, data_file="carpet_repair_data.json"):
        """
        Initialize the CarpetRepairService with a data file to store customer and repair information.
        """
        self.data_file = data_file
        self.data = self._load_data()

    def _load_data(self):
        """
        Load data from the JSON file. If the file doesn't exist, initialize an empty data structure.
        """
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as file:
                    return json.load(file)
            except json.JSONDecodeError:
                print("Error: Data file is corrupted. Initializing empty data.")
                return {}
        return {}

    def _save_data(self):
        """
        Save the current data to the JSON file.
        """
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.data, file, indent=4)
        except IOError as e:
            print(f"Error: Unable to save data to file. {e}")

    def add_customer(self, customer_id, name, contact):
        """
        Add a new customer to the system.
        :param customer_id: Unique identifier for the customer
        :param name: Name of the customer
        :param contact: Contact information (e.g., phone or email)
        """
        if customer_id in self.data:
            print("Error: Customer ID already exists.")
            return

        self.data[customer_id] = {
            "name": name,
            "contact": contact,
            "repairs": []
        }
        self._save_data()
        print(f"Customer {name} added successfully.")

    def add_repair(self, customer_id, area, cost, description):
        """
        Add a repair record for a specific customer.
        :param customer_id: Unique identifier for the customer
        :param area: Damaged carpet area (e.g., "Living Room")
        :param cost: Cost of the repair
        :param description: Description of the repair
        """
        if customer_id not in self.data:
            print("Error: Customer ID not found.")
            return

        repair_record = {
            "area": area,
            "cost": cost,
            "description": description
        }
        self.data[customer_id]["repairs"].append(repair_record)
        self._save_data()
        print(f"Repair record added for customer ID {customer_id}.")

    def view_customer(self, customer_id):
        """
        View details of a specific customer, including their repair history.
        :param customer_id: Unique identifier for the customer
        """
        if customer_id not in self.data:
            print("Error: Customer ID not found.")
            return

        customer_data = self.data[customer_id]
        print(f"Customer ID: {customer_id}")
        print(f"Name: {customer_data['name']}")
        print(f"Contact: {customer_data['contact']}")
        print("Repairs:")
        for repair in customer_data["repairs"]:
            print(f"  - Area: {repair['area']}, Cost: ${repair['cost']:.2f}, Description: {repair['description']}")

    def delete_customer(self, customer_id):
        """
        Delete a customer and their repair records from the system.
        :param customer_id: Unique identifier for the customer
        """
        if customer_id not in self.data:
            print("Error: Customer ID not found.")
            return

        del self.data[customer_id]
        self._save_data()
        print(f"Customer ID {customer_id} deleted successfully.")

    def list_customers(self):
        """
        List all customers in the system.
        """
        if not self.data:
            print("No customers found.")
            return

        print("Customers:")
        for customer_id, customer_data in self.data.items():
            print(f"  - ID: {customer_id}, Name: {customer_data['name']}, Contact: {customer_data['contact']}")


# Example usage
if __name__ == "__main__":
    service = CarpetRepairService()

    # Add customers
    service.add_customer("C001", "John Doe", "john.doe@example.com")
    service.add_customer("C002", "Jane Smith", "jane.smith@example.com")

    # Add repairs
    service.add_repair("C001", "Living Room", 150.00, "Replaced torn carpet")
    service.add_repair("C001", "Bedroom", 200.00, "Fixed burn marks")
    service.add_repair("C002", "Hallway", 100.00, "Repaired frayed edges")

    # View customer details
    service.view_customer("C001")

    # List all customers
    service.list_customers()

    # Delete a customer
    service.delete_customer("C002")

    # List all customers after deletion
    service.list_customers()
```
