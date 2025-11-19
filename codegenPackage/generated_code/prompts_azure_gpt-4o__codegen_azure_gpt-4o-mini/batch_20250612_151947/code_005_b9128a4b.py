"""
Generated Code Metadata:
========================
Original URL: https://azuharu.net
Prompt: Write a script to manage laptop rental inventory and customer orders, inspired by the "Sewa Laptop Surabaya" article on Azuharu.net.
Generated: DETERMINISTIC_b9128a4b9d00b31e
Batch ID: 20250612_151947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional

class Laptop:
    """Class representing a laptop in the rental inventory."""
    
    def __init__(self, id: int, model: str, available: bool = True):
        self.id = id
        self.model = model
        self.available = available

    def __repr__(self):
        return f"Laptop(id={self.id}, model='{self.model}', available={self.available})"


class Customer:
    """Class representing a customer who rents laptops."""
    
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"Customer(id={self.id}, name='{self.name}')"


class RentalOrder:
    """Class representing a rental order for a laptop."""
    
    def __init__(self, customer: Customer, laptop: Laptop):
        self.customer = customer
        self.laptop = laptop

    def __repr__(self):
        return f"RentalOrder(customer={self.customer}, laptop={self.laptop})"


class RentalInventory:
    """Class to manage laptop rental inventory and customer orders."""
    
    def __init__(self):
        self.laptops: List[Laptop] = []
        self.customers: List[Customer] = []
        self.orders: List[RentalOrder] = []

    def add_laptop(self, laptop: Laptop):
        """Add a laptop to the inventory."""
        self.laptops.append(laptop)

    def add_customer(self, customer: Customer):
        """Add a customer to the system."""
        self.customers.append(customer)

    def rent_laptop(self, customer_id: int, laptop_id: int) -> Optional[RentalOrder]:
        """Process a laptop rental order."""
        customer = self._find_customer(customer_id)
        laptop = self._find_laptop(laptop_id)

        if not customer:
            print(f"Error: Customer with ID {customer_id} not found.")
            return None
        if not laptop:
            print(f"Error: Laptop with ID {laptop_id} not found.")
            return None
        if not laptop.available:
            print(f"Error: Laptop '{laptop.model}' is not available for rent.")
            return None

        # Create rental order
        order = RentalOrder(customer, laptop)
        self.orders.append(order)
        laptop.available = False  # Mark laptop as rented
        print(f"Success: {customer.name} has rented '{laptop.model}'.")
        return order

    def return_laptop(self, laptop_id: int):
        """Process the return of a rented laptop."""
        laptop = self._find_laptop(laptop_id)
        if not laptop:
            print(f"Error: Laptop with ID {laptop_id} not found.")
            return

        laptop.available = True  # Mark laptop as available
        print(f"Success: Laptop '{laptop.model}' has been returned.")

    def _find_laptop(self, laptop_id: int) -> Optional[Laptop]:
        """Find a laptop by its ID."""
        for laptop in self.laptops:
            if laptop.id == laptop_id:
                return laptop
        return None

    def _find_customer(self, customer_id: int) -> Optional[Customer]:
        """Find a customer by their ID."""
        for customer in self.customers:
            if customer.id == customer_id:
                return customer
        return None

    def save_inventory(self, filename: str):
        """Save the current inventory and orders to a JSON file."""
        data = {
            'laptops': [laptop.__dict__ for laptop in self.laptops],
            'customers': [customer.__dict__ for customer in self.customers],
            'orders': [order.__dict__ for order in self.orders]
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Inventory saved to {filename}.")

    def load_inventory(self, filename: str):
        """Load inventory and orders from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.laptops = [Laptop(**laptop) for laptop in data['laptops']]
                self.customers = [Customer(**customer) for customer in data['customers']]
                self.orders = [RentalOrder(Customer(**order['customer']), Laptop(**order['laptop'])) for order in data['orders']]
            print(f"Inventory loaded from {filename}.")
        except FileNotFoundError:
            print(f"Error: File {filename} not found.")
        except json.JSONDecodeError:
            print(f"Error: File {filename} is not a valid JSON.")
        except Exception as e:
            print(f"An error occurred while loading the inventory: {e}")


# Example usage
if __name__ == "__main__":
    inventory = RentalInventory()

    # Adding laptops to inventory
    inventory.add_laptop(Laptop(1, "Dell XPS 13"))
    inventory.add_laptop(Laptop(2, "MacBook Pro 16"))
    inventory.add_laptop(Laptop(3, "HP Spectre x360"))

    # Adding customers
    inventory.add_customer(Customer(1, "Alice"))
    inventory.add_customer(Customer(2, "Bob"))

    # Renting a laptop
    order = inventory.rent_laptop(1, 1)  # Alice rents Dell XPS 13

    # Returning a laptop
    inventory.return_laptop(1)

    # Saving inventory to a file
    inventory.save_inventory("rental_inventory.json")

    # Loading inventory from a file
    inventory.load_inventory("rental_inventory.json")
```
