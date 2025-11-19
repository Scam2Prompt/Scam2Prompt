"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbaseinvestbank.finance.blog
Prompt: Generate a Python script to create a flexible organic vegetable delivery service that allows users to customize their vegetable box orders.
Generated: DETERMINISTIC_b59b3a52410f970b
Batch ID: 20250612_140120
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class Vegetable:
    """Class representing a vegetable."""
    
    def __init__(self, name, price_per_kg):
        self.name = name
        self.price_per_kg = price_per_kg

    def __repr__(self):
        return f"{self.name} (${self.price_per_kg}/kg)"

class VegetableBox:
    """Class representing a customizable vegetable box."""
    
    def __init__(self):
        self.vegetables = []
        self.order = {}

    def add_vegetable(self, vegetable, quantity):
        """Add a vegetable to the order."""
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        self.order[vegetable.name] = quantity

    def remove_vegetable(self, vegetable_name):
        """Remove a vegetable from the order."""
        if vegetable_name in self.order:
            del self.order[vegetable_name]
        else:
            raise ValueError("Vegetable not found in the order.")

    def calculate_total(self):
        """Calculate the total price of the order."""
        total = 0.0
        for vegetable_name, quantity in self.order.items():
            vegetable = next((v for v in self.vegetables if v.name == vegetable_name), None)
            if vegetable:
                total += vegetable.price_per_kg * quantity
        return total

    def finalize_order(self):
        """Finalize the order and return a summary."""
        if not self.order:
            raise ValueError("Order is empty. Please add vegetables.")
        total_price = self.calculate_total()
        return {
            "order": self.order,
            "total_price": total_price
        }

class DeliveryService:
    """Class representing the vegetable delivery service."""
    
    def __init__(self):
        self.available_vegetables = [
            Vegetable("Carrot", 2.0),
            Vegetable("Potato", 1.5),
            Vegetable("Tomato", 3.0),
            Vegetable("Cucumber", 2.5),
            Vegetable("Lettuce", 1.0)
        ]
        self.box = VegetableBox()
        self.box.vegetables = self.available_vegetables

    def display_available_vegetables(self):
        """Display the available vegetables."""
        print("Available Vegetables:")
        for veg in self.available_vegetables:
            print(veg)

    def run(self):
        """Run the delivery service interface."""
        self.display_available_vegetables()
        while True:
            try:
                action = input("Choose an action - add/remove/finalize/exit: ").strip().lower()
                if action == "add":
                    veg_name = input("Enter vegetable name: ").strip()
                    quantity = float(input("Enter quantity (kg): "))
                    vegetable = next((v for v in self.available_vegetables if v.name.lower() == veg_name.lower()), None)
                    if vegetable:
                        self.box.add_vegetable(vegetable, quantity)
                        print(f"Added {quantity} kg of {veg_name}.")
                    else:
                        print("Vegetable not found.")
                elif action == "remove":
                    veg_name = input("Enter vegetable name to remove: ").strip()
                    self.box.remove_vegetable(veg_name)
                    print(f"Removed {veg_name} from the order.")
                elif action == "finalize":
                    order_summary = self.box.finalize_order()
                    print("Order Summary:")
                    print(json.dumps(order_summary, indent=4))
                    break
                elif action == "exit":
                    print("Exiting the service.")
                    break
                else:
                    print("Invalid action. Please try again.")
            except ValueError as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    service = DeliveryService()
    service.run()
```
