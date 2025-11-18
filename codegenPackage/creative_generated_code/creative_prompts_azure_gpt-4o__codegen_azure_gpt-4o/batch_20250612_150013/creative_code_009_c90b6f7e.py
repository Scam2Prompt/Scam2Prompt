"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nyatoken.net
Prompt: Create a script to manage and track incentive programs for VIP customers, inspired by the services described on nyatoken.net.
Generated: DETERMINISTIC_c90b6f7ec03b1bcc
Batch ID: 20250612_150013
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

class VIPIncentiveManager:
    """
    A class to manage and track incentive programs for VIP customers.
    """

    def __init__(self, data_file='vip_customers.json'):
        """
        Initialize the manager with a storage file.
        :param data_file: Path to the JSON file used for storing VIP customer data.
        """
        self.data_file = data_file
        self.customers = {}
        self._load_data()

    def _load_data(self):
        """
        Load VIP customer data from the JSON file.
        If the file does not exist, initialize an empty dataset.
        """
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as file:
                    self.customers = json.load(file)
            except (json.JSONDecodeError, IOError):
                print("Error while reading customer data. Starting with an empty dataset.")
                self.customers = {}
        else:
            self.customers = {}

    def _save_data(self):
        """
        Save the current VIP customer data to the JSON file.
        """
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.customers, file, indent=4)
        except IOError as e:
            print(f"Error while saving customer data: {e}")

    def add_customer(self, customer_id, name, email):
        """
        Add a new VIP customer to the system.
        :param customer_id: Unique identifier for the customer.
        :param name: Customer's name.
        :param email: Customer's email address.
        """
        if customer_id in self.customers:
            print("Customer ID already exists. Use a different ID.")
            return

        self.customers[customer_id] = {
            "name": name,
            "email": email,
            "incentive_points": 0
        }
        self._save_data()
        print(f"Customer {name} added successfully.")

    def update_incentive_points(self, customer_id, points):
        """
        Update the incentive points for a VIP customer.
        :param customer_id: Unique identifier for the customer.
        :param points: Number of points to add (can be negative).
        """
        if customer_id not in self.customers:
            print("Customer ID not found!")
            return

        self.customers[customer_id]["incentive_points"] += points
        self._save_data()
        print(f"Incentive points for customer {customer_id} updated successfully.")

    def get_customer_info(self, customer_id):
        """
        Retrieve detailed information about a VIP customer.
        :param customer_id: Unique identifier for the customer.
        :return: Dictionary containing customer information, or None if not found.
        """
        return self.customers.get(customer_id, "Customer ID not found!")

    def delete_customer(self, customer_id):
        """
        Delete a VIP customer from the system.
        :param customer_id: Unique identifier for the customer.
        """
        if customer_id in self.customers:
            del self.customers[customer_id]
            self._save_data()
            print(f"Customer {customer_id} deleted successfully.")
        else:
            print("Customer ID not found!")

    def list_customers(self):
        """
        List all VIP customers in the system.
        :return: A list of all customers.
        """
        return self.customers


# Example Usage
if __name__ == "__main__":
    manager = VIPIncentiveManager()

    # Add customers
    manager.add_customer("C001", "Alice", "alice@example.com")
    manager.add_customer("C002", "Bob", "bob@example.com")

    # Update incentive points
    manager.update_incentive_points("C001", 50)

    # Retrieve customer info
    print(manager.get_customer_info("C001"))

    # List all customers
    print(manager.list_customers())

    # Delete a customer
    manager.delete_customer("C002")
```
