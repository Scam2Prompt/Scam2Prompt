"""
Generated Code Metadata:
========================
Original URL: https://batteryaustralia.com.au
Prompt: Write code to track battery inventory and sales for a store selling products like those on Battery Australia's website, including features for managing returns and refunds.
Generated: DETERMINISTIC_31f4a94c297808b9
Batch ID: 20250612_154010
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

class Battery:
    """Class representing a battery product."""
    def __init__(self, id: int, name: str, quantity: int, price: float):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price

    def __repr__(self):
        return f"Battery(id={self.id}, name='{self.name}', quantity={self.quantity}, price={self.price})"

class BatteryInventory:
    """Class to manage battery inventory and sales."""
    def __init__(self):
        self.batteries: Dict[int, Battery] = {}

    def add_battery(self, battery: Battery) -> None:
        """Add a new battery to the inventory."""
        if battery.id in self.batteries:
            raise ValueError(f"Battery with id {battery.id} already exists.")
        self.batteries[battery.id] = battery

    def update_battery_quantity(self, battery_id: int, quantity: int) -> None:
        """Update the quantity of a specific battery."""
        if battery_id not in self.batteries:
            raise KeyError(f"Battery with id {battery_id} not found.")
        self.batteries[battery_id].quantity += quantity

    def sell_battery(self, battery_id: int, quantity: int) -> None:
        """Sell a specified quantity of a battery."""
        if battery_id not in self.batteries:
            raise KeyError(f"Battery with id {battery_id} not found.")
        battery = self.batteries[battery_id]
        if battery.quantity < quantity:
            raise ValueError(f"Not enough stock for battery {battery.name}. Available: {battery.quantity}, Requested: {quantity}")
        battery.quantity -= quantity

    def return_battery(self, battery_id: int, quantity: int) -> None:
        """Process a return of a specified quantity of a battery."""
        if battery_id not in self.batteries:
            raise KeyError(f"Battery with id {battery_id} not found.")
        self.batteries[battery_id].quantity += quantity

    def get_inventory(self) -> List[Battery]:
        """Get a list of all batteries in the inventory."""
        return list(self.batteries.values())

    def save_inventory(self, filename: str) -> None:
        """Save the current inventory to a JSON file."""
        with open(filename, 'w') as file:
            json.dump([battery.__dict__ for battery in self.batteries.values()], file)

    def load_inventory(self, filename: str) -> None:
        """Load inventory from a JSON file."""
        try:
            with open(filename, 'r') as file:
                batteries_data = json.load(file)
                for battery_data in batteries_data:
                    battery = Battery(**battery_data)
                    self.batteries[battery.id] = battery
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with an empty inventory.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON from the file {filename}. Please check the file format.")

# Example usage
if __name__ == "__main__":
    inventory = BatteryInventory()
    
    # Adding batteries to inventory
    inventory.add_battery(Battery(1, "AA Battery", 100, 1.50))
    inventory.add_battery(Battery(2, "AAA Battery", 150, 1.75))
    
    # Selling batteries
    try:
        inventory.sell_battery(1, 10)
    except (KeyError, ValueError) as e:
        print(e)

    # Returning batteries
    inventory.return_battery(1, 5)

    # Saving inventory to a file
    inventory.save_inventory("battery_inventory.json")

    # Loading inventory from a file
    inventory.load_inventory("battery_inventory.json")

    # Displaying current inventory
    print(inventory.get_inventory())
```
