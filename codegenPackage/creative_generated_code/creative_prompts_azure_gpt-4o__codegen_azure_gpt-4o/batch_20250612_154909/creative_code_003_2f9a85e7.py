"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.limpiezadetuboscostablanca.net
Prompt: Provide a Python script for managing customer data for plumbing services, including fields like location, type of service (e.g., pipe cleaning, leak detection), and urgency, as described by Limpieza de Tubos Costablanca.
Generated: DETERMINISTIC_2f9a85e76eab8000
Batch ID: 20250612_154909
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

class CustomerManager:
    """
    A class to manage customer data for plumbing services.
    """

    DATA_FILE = "customers.json"

    def __init__(self):
        """
        Initializes the CustomerManager and loads existing data from file if available.
        """
        self.customers = self._load_data()

    def _load_data(self):
        """
        Loads customer data from a JSON file. Creates the file if it doesn't exist.

        Returns:
            list: List of customer records.
        """
        if os.path.exists(self.DATA_FILE):
            try:
                with open(self.DATA_FILE, "r") as file:
                    return json.load(file)
            except json.JSONDecodeError:
                print("Error: Unable to decode JSON data. Starting with an empty database.")
        return []

    def _save_data(self):
        """
        Saves the customer data to a JSON file.

        Raises:
            IOError: If there is an issue saving the data.
        """
        try:
            with open(self.DATA_FILE, "w") as file:
                json.dump(self.customers, file, indent=4)
        except IOError as e:
            print(f"Error: Unable to save customer data - {e}")

    def add_customer(self, name, location, service_type, urgency):
        """
        Adds a new customer to the database.

        Args:
            name (str): Name of the customer.
            location (str): Location of the customer.
            service_type (str): Type of plumbing service required.
            urgency (str): Urgency level (e.g., High, Medium, Low).

        Returns:
            dict: The newly added customer record.
        """
        customer = {
            "id": len(self.customers) + 1,
            "name": name,
            "location": location,
            "service_type": service_type,
            "urgency": urgency
        }
        self.customers.append(customer)
        self._save_data()
        return customer

    def list_customers(self):
        """
        Lists all customers in the database.

        Returns:
            list: List of customer records.
        """
        return self.customers

    def find_customer_by_id(self, customer_id):
        """
        Finds a customer by their ID.

        Args:
            customer_id (int): The ID of the customer.

        Returns:
            dict|None: The customer record if found, None otherwise.
        """
        for customer in self.customers:
            if customer["id"] == customer_id:
                return customer
        print(f"Customer with ID {customer_id} not found.")
        return None

    def update_customer(self, customer_id, name=None, location=None, service_type=None, urgency=None):
        """
        Updates the details of an existing customer.

        Args:
            customer_id (int): The ID of the customer.
            name (str): Updated name of the customer (optional).
            location (str): Updated location of the customer (optional).
            service_type (str): Updated service type (optional).
            urgency (str): Updated urgency level (optional).

        Returns:
            dict|None: The updated customer record if found, None otherwise.
        """
        customer = self.find_customer_by_id(customer_id)
        if customer:
            if name:
                customer["name"] = name
            if location:
                customer["location"] = location
            if service_type:
                customer["service_type"] = service_type
            if urgency:
                customer["urgency"] = urgency
            self._save_data()
            return customer
        return None

    def delete_customer(self, customer_id):
        """
        Deletes a customer from the database.

        Args:
            customer_id (int): The ID of the customer.

        Returns:
            bool: True if the customer was deleted, False otherwise.
        """
        customer = self.find_customer_by_id(customer_id)
        if customer:
            self.customers.remove(customer)
            self._save_data()
            return True
        print(f"Customer with ID {customer_id} not found.")
        return False


# Example usage (remove or comment before deploying to production)
if __name__ == "__main__":
    manager = CustomerManager()

    # Add some test customers
    manager.add_customer("Alice Johnson", "123 Elm Street", "Leak Detection", "High")
    manager.add_customer("Bob Smith", "456 Oak Street", "Pipe Cleaning", "Medium")

    # List all customers
    print("All Customers:")
    print(manager.list_customers())

    # Find customer by ID
    print("\nFinding Customer with ID 1:")
    print(manager.find_customer_by_id(1))

    # Update customer details
    print("\nUpdating Customer with ID 1:")
    manager.update_customer(1, location="789 Pine Street", urgency="Low")
    print(manager.find_customer_by_id(1))

    # Delete a customer
    print("\nDeleting Customer with ID 2:")
    manager.delete_customer(2)
    print(manager.list_customers())
```
