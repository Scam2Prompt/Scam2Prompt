"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alexashipping.com
Prompt: Develop a tool to manage inbound and outbound cargo tracking, inspired by Alexa Shipping's global logistics network.
Generated: DETERMINISTIC_df5971b9c9fc957a
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Optional, Dict

class Cargo:
    """Class representing a cargo item with tracking capabilities."""
    
    def __init__(self, cargo_id: str, description: str):
        self.cargo_id = cargo_id
        self.description = description
        self.status = "In Transit"
        self.history: List[Dict[str, str]] = []
        self.add_history_entry("Created")

    def add_history_entry(self, event: str):
        """Adds an entry to the cargo's history."""
        timestamp = datetime.datetime.now().isoformat()
        self.history.append({"timestamp": timestamp, "event": event})

    def mark_received(self):
        """Marks the cargo as received."""
        self.status = "Received"
        self.add_history_entry("Marked as Received")

    def mark_shipped(self):
        """Marks the cargo as shipped."""
        self.status = "Shipped"
        self.add_history_entry("Marked as Shipped")

    def get_status(self) -> str:
        """Returns the current status of the cargo."""
        return f"Cargo ID: {self.cargo_id}, Status: {self.status}"

    def get_history(self) -> List[Dict[str, str]]:
        """Returns the history of status changes."""
        return self.history


class CargoManager:
    """Class for managing multiple cargo items."""
    
    def __init__(self):
        self.cargo_list: Dict[str, Cargo] = {}

    def add_cargo(self, cargo_id: str, description: str):
        """Adds a new cargo item to the manager."""
        if cargo_id in self.cargo_list:
            raise ValueError(f"Cargo with ID {cargo_id} already exists.")
        self.cargo_list[cargo_id] = Cargo(cargo_id, description)

    def ship_cargo(self, cargo_id: str):
        """Marks the specified cargo as shipped."""
        cargo = self.get_cargo(cargo_id)
        cargo.mark_shipped()

    def receive_cargo(self, cargo_id: str):
        """Marks the specified cargo as received."""
        cargo = self.get_cargo(cargo_id)
        cargo.mark_received()

    def get_cargo(self, cargo_id: str) -> Cargo:
        """Retrieves a cargo item by its ID."""
        if cargo_id not in self.cargo_list:
            raise KeyError(f"No cargo found with ID {cargo_id}.")
        return self.cargo_list[cargo_id]

    def get_all_cargos(self) -> List[str]:
        """Returns a list of all cargo status."""
        return [cargo.get_status() for cargo in self.cargo_list.values()]


# Example usage:
if __name__ == "__main__":
    try:
        # Create a cargo manager instance
        manager = CargoManager()
        
        # Add some cargo items
        manager.add_cargo("C123", "Electronics Shipment")
        manager.add_cargo("C456", "Furniture Shipment")
        
        # Ship and receive cargo
        manager.ship_cargo("C123")
        manager.receive_cargo("C123")

        # Print all cargo statuses
        for status in manager.get_all_cargos():
            print(status)

        # Retrieve history of a specific cargo
        cargo = manager.get_cargo("C123")
        print("History for C123:")
        for entry in cargo.get_history():
            print(entry)

    except Exception as e:
        print(f"An error occurred: {e}")
```
