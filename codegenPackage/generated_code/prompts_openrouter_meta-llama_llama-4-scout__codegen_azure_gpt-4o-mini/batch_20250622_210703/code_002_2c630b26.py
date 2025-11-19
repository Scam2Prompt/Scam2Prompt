"""
Generated Code Metadata:
========================
Original URL: https://citygardenmexico.com.mx
Prompt: "Create a Python script to manage a plant inventory for a gardening store in Mexico, including pricing and customer information."
Generated: DETERMINISTIC_2c630b269da40370
Batch ID: 20250622_210703
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

class Plant:
    """Class to represent a plant in the inventory."""
    
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def to_dict(self):
        """Convert the plant object to a dictionary."""
        return {
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity
        }

class Inventory:
    """Class to manage the plant inventory."""
    
    def __init__(self, filename='inventory.json'):
        self.filename = filename
        self.plants = self.load_inventory()

    def load_inventory(self):
        """Load inventory from a JSON file."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return [Plant(**data) for data in json.load(file)]
        return []

    def save_inventory(self):
        """Save the current inventory to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump([plant.to_dict() for plant in self.plants], file, indent=4)

    def add_plant(self, name, price, quantity):
        """Add a new plant to the inventory."""
        self.plants.append(Plant(name, price, quantity))
        self.save_inventory()

    def update_plant(self, name, price=None, quantity=None):
        """Update the details of an existing plant."""
        for plant in self.plants:
            if plant.name == name:
                if price is not None:
                    plant.price = price
                if quantity is not None:
                    plant.quantity = quantity
                self.save_inventory()
                return
        raise ValueError(f"Plant '{name}' not found in inventory.")

    def remove_plant(self, name):
        """Remove a plant from the inventory."""
        self.plants = [plant for plant in self.plants if plant.name != name]
        self.save_inventory()

    def list_plants(self):
        """List all plants in the inventory."""
        return [plant.to_dict() for plant in self.plants]

class Customer:
    """Class to represent a customer."""
    
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def to_dict(self):
        """Convert the customer object to a dictionary."""
        return {
            'name': self.name,
            'email': self.email
        }

class CustomerManager:
    """Class to manage customer information."""
    
    def __init__(self, filename='customers.json'):
        self.filename = filename
        self.customers = self.load_customers()

    def load_customers(self):
        """Load customers from a JSON file."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return [Customer(**data) for data in json.load(file)]
        return []

    def save_customers(self):
        """Save the current customers to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump([customer.to_dict() for customer in self.customers], file, indent=4)

    def add_customer(self, name, email):
        """Add a new customer."""
        self.customers.append(Customer(name, email))
        self.save_customers()

    def list_customers(self):
        """List all customers."""
        return [customer.to_dict() for customer in self.customers]

def main():
    """Main function to demonstrate the inventory and customer management."""
    inventory = Inventory()
    customer_manager = CustomerManager()

    # Example usage
    try:
        # Add plants to inventory
        inventory.add_plant('Cactus', 50.0, 10)
        inventory.add_plant('Fern', 30.0, 5)

        # List plants
        print("Current Inventory:")
        for plant in inventory.list_plants():
            print(plant)

        # Update a plant
        inventory.update_plant('Cactus', quantity=8)

        # Remove a plant
        inventory.remove_plant('Fern')

        # Add a customer
        customer_manager.add_customer('Juan Perez', 'juan.perez@example.com')

        # List customers
        print("\nCustomer List:")
        for customer in customer_manager.list_customers():
            print(customer)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
