"""
Generated Code Metadata:
========================
Original URL: https://antalyasehiricinakliye.com
Prompt: Write a Python script to manage moving services for a company like Antalya Şehir İçi Nakliye, including customer information and moving details.
Generated: DETERMINISTIC_7d1e5f2f5352083c
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import uuid
from datetime import datetime

class MovingService:
    """Class to manage moving services for a moving company."""

    def __init__(self):
        """Initialize the moving service with an empty customer list."""
        self.customers = []

    def add_customer(self, name, address, phone):
        """Add a new customer to the service.

        Args:
            name (str): The name of the customer.
            address (str): The address of the customer.
            phone (str): The phone number of the customer.

        Returns:
            dict: The added customer information.
        """
        customer_id = str(uuid.uuid4())
        customer = {
            'id': customer_id,
            'name': name,
            'address': address,
            'phone': phone,
            'moving_details': []
        }
        self.customers.append(customer)
        return customer

    def schedule_move(self, customer_id, date, details):
        """Schedule a moving service for a customer.

        Args:
            customer_id (str): The ID of the customer.
            date (str): The date of the move in YYYY-MM-DD format.
            details (str): Additional details about the move.

        Returns:
            dict: The scheduled moving details or an error message.
        """
        customer = self.find_customer(customer_id)
        if not customer:
            return {"error": "Customer not found."}

        move_id = str(uuid.uuid4())
        move = {
            'id': move_id,
            'date': date,
            'details': details,
            'status': 'Scheduled'
        }
        customer['moving_details'].append(move)
        return move

    def find_customer(self, customer_id):
        """Find a customer by their ID.

        Args:
            customer_id (str): The ID of the customer.

        Returns:
            dict or None: The customer information or None if not found.
        """
        for customer in self.customers:
            if customer['id'] == customer_id:
                return customer
        return None

    def save_data(self, filename):
        """Save customer data to a JSON file.

        Args:
            filename (str): The name of the file to save the data.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.customers, file, indent=4)
        except IOError as e:
            print(f"Error saving data to {filename}: {e}")

    def load_data(self, filename):
        """Load customer data from a JSON file.

        Args:
            filename (str): The name of the file to load the data from.
        """
        try:
            with open(filename, 'r') as file:
                self.customers = json.load(file)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading data from {filename}: {e}")

if __name__ == "__main__":
    service = MovingService()
    
    # Load existing customer data if available
    service.load_data('customers.json')

    # Example usage
    customer = service.add_customer("John Doe", "123 Main St", "555-1234")
    print(f"Added customer: {customer}")

    move = service.schedule_move(customer['id'], "2023-10-15", "Moving from Main St to 456 Elm St")
    print(f"Scheduled move: {move}")

    # Save updated customer data
    service.save_data('customers.json')
```
