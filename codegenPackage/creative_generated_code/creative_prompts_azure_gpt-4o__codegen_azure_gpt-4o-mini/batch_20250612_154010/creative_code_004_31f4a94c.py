"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://batteryaustralia.com.au
Prompt: Write code to track battery inventory and sales for a store selling products like those on Battery Australia's website, including features for managing returns and refunds.
Generated: DETERMINISTIC_31f4a94c297808b9
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict, Optional

class Battery:
    """Represents a battery product with a name, quantity, and price."""
    
    def __init__(self, name: str, quantity: int, price: float):
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"{self.name} - Quantity: {self.quantity}, Price: ${self.price:.2f}"

class Inventory:
    """Manages battery inventory, sales, returns, and refunds."""
    
    def __init__(self):
        self.batteries: List[Battery] = []

    def add_battery(self, battery: Battery) -> None:
        """Adds a new battery to the inventory."""
        self.batteries.append(battery)
        print(f"Added {battery}")

    def sell_battery(self, battery_name: str, quantity: int) -> Optional[str]:
        """Processes a sale for a battery by name and quantity."""
        battery = self.find_battery(battery_name)
        if battery and battery.quantity >= quantity:
            battery.quantity -= quantity
            print(f"Sold {quantity} of {battery_name}")
            return f"Sale successful: {quantity} x {battery_name} sold."
        if battery is None:
            return f"Error: Battery '{battery_name}' not found."
        return f"Error: Insufficient quantity for '{battery_name}'. Available: {battery.quantity}"

    def return_battery(self, battery_name: str, quantity: int) -> Optional[str]:
        """Processes a return for a battery by name and quantity."""
        battery = self.find_battery(battery_name)
        if battery:
            battery.quantity += quantity
            print(f"Returned {quantity} of {battery_name}")
            return f"Return successful: {quantity} x {battery_name} returned."
        return f"Error: Battery '{battery_name}' not found."

    def find_battery(self, battery_name: str) -> Optional[Battery]:
        """Finds a battery in the inventory by name."""
        for battery in self.batteries:
            if battery.name == battery_name:
                return battery
        return None

    def get_inventory(self) -> Dict[str, Dict[str, float]]:
        """Returns a summary of the current inventory."""
        inventory_summary = {}
        for battery in self.batteries:
            inventory_summary[battery.name] = {
                "quantity": battery.quantity,
                "price": battery.price
            }
        return inventory_summary


# Example usage
if __name__ == "__main__":
    # Initialize inventory
    store_inventory = Inventory()

    # Add batteries to inventory
    store_inventory.add_battery(Battery("AA Lithium", 100, 1.99))
    store_inventory.add_battery(Battery("AAA Alkaline", 50, 0.99))
    store_inventory.add_battery(Battery("9V Rechargeable", 30, 5.49))

    # Sell batteries
    print(store_inventory.sell_battery("AA Lithium", 10))
    print(store_inventory.sell_battery("AAA Alkaline", 5))

    # Return batteries
    print(store_inventory.return_battery("AA Lithium", 5))

    # Print inventory status
    print("Current Inventory:")
    for name, details in store_inventory.get_inventory().items():
        print(f"{name}: {details['quantity']} in stock, Price: ${details['price']:.2f}")
```
