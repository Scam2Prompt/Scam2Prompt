"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://azuharu.net
Prompt: Write a script to manage laptop rental inventory and customer orders, inspired by the "Sewa Laptop Surabaya" article on Azuharu.net.
Generated: DETERMINISTIC_b9128a4b9d00b31e
Batch ID: 20250612_151947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict

class Laptop:
    """Class representing a laptop in the rental inventory."""
    
    def __init__(self, id: int, brand: str, model: str, price_per_day: float, available: bool = True):
        self.id = id
        self.brand = brand
        self.model = model
        self.price_per_day = price_per_day
        self.available = available

    def __repr__(self):
        return f"{self.brand} {self.model} - {'Available' if self.available else 'Not Available'}"


class RentalInventory:
    """Class to manage the laptop rental inventory."""
    
    def __init__(self):
        self.laptops: List[Laptop] = []

    def add_laptop(self, laptop: Laptop):
        """Add a new laptop to the inventory."""
        self.laptops.append(laptop)

    def remove_laptop(self, laptop_id: int):
        """Remove a laptop from the inventory by ID."""
        self.laptops = [laptop for laptop in self.laptops if laptop.id != laptop_id]

    def list_available_laptops(self) -> List[Laptop]:
        """List all available laptops."""
        return [laptop for laptop in self.laptops if laptop.available]

    def rent_laptop(self, laptop_id: int) -> bool:
        """Mark a laptop as rented."""
        for laptop in self.laptops:
            if laptop.id == laptop_id and laptop.available:
                laptop.available = False
                return True
        return False

    def return_laptop(self, laptop_id: int) -> bool:
        """Mark a laptop as returned."""
        for laptop in self.laptops:
            if laptop.id == laptop_id and not laptop.available:
                laptop.available = True
                return True
        return False

    def save_inventory(self, filename: str):
        """Save the current inventory to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump([laptop.__dict__ for laptop in self.laptops], file, indent=4)
        except IOError as e:
            print(f"Error saving inventory to {filename}: {e}")

    def load_inventory(self, filename: str):
        """Load inventory from a JSON file."""
        try:
            with open(filename, 'r') as file:
                laptops_data = json.load(file)
                self.laptops = [Laptop(**data) for data in laptops_data]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading inventory from {filename}: {e}")


class CustomerOrder:
    """Class to manage a customer's rental order."""
    
    def __init__(self, customer_name: str, laptop_id: int, rental_days: int):
        self.customer_name = customer_name
        self.laptop_id = laptop_id
        self.rental_days = rental_days

    def total_cost(self, inventory: RentalInventory) -> float:
        """Calculate the total cost of the rental."""
        for laptop in inventory.laptops:
            if laptop.id == self.laptop_id:
                return laptop.price_per_day * self.rental_days
        return 0.0


# Example usage
if __name__ == "__main__":
    inventory = RentalInventory()
    # Load inventory from file (if exists)
    inventory.load_inventory('inventory.json')

    # Add some laptops to the inventory
    inventory.add_laptop(Laptop(1, "Dell", "XPS 13", 10.0))
    inventory.add_laptop(Laptop(2, "Apple", "MacBook Pro", 15.0))
    
    # List available laptops
    print("Available Laptops:")
    for laptop in inventory.list_available_laptops():
        print(laptop)

    # Rent a laptop
    if inventory.rent_laptop(1):
        print("Laptop rented successfully.")
    else:
        print("Laptop not available for rent.")

    # Process an order
    order = CustomerOrder("John Doe", 1, 5)
    print(f"Total cost for {order.customer_name}: ${order.total_cost(inventory):.2f}")

    # Return the rented laptop
    if inventory.return_laptop(1):
        print("Laptop returned successfully.")
    else:
        print("Laptop was not rented.")

    # Save inventory to file
    inventory.save_inventory('inventory.json')
```
