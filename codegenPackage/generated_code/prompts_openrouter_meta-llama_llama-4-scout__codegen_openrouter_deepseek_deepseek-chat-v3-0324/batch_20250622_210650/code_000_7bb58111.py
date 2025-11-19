"""
Generated Code Metadata:
========================
Original URL: https://tdkco.ir
Prompt: "Write a Python code to manage inventory of car bearings for different vehicle models, including SEDAN, HATCHBACK, COMBI, and SUV."
Generated: DETERMINISTIC_7bb581114e0210ee
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from enum import Enum
from typing import Dict, List, Optional
import json
import os

class VehicleType(Enum):
    """Enumeration for vehicle types."""
    SEDAN = "SEDAN"
    HATCHBACK = "HATCHBACK"
    COMBI = "COMBI"
    SUV = "SUV"

class Bearing:
    """Class representing a car bearing."""
    def __init__(self, part_number: str, description: str, quantity: int, price: float):
        """
        Initialize a bearing instance.
        
        Args:
            part_number: Unique identifier for the bearing
            description: Description of the bearing
            quantity: Current stock quantity
            price: Unit price of the bearing
        """
        self.part_number = part_number
        self.description = description
        self.quantity = quantity
        self.price = price

    def to_dict(self) -> Dict:
        """Convert bearing object to dictionary."""
        return {
            "part_number": self.part_number,
            "description": self.description,
            "quantity": self.quantity,
            "price": self.price
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Bearing':
        """Create bearing object from dictionary."""
        return cls(
            part_number=data["part_number"],
            description=data["description"],
            quantity=data["quantity"],
            price=data["price"]
        )

class InventoryManager:
    """Class to manage inventory of car bearings."""
    def __init__(self, file_path: str = "inventory.json"):
        """
        Initialize inventory manager.
        
        Args:
            file_path: Path to JSON file for storing inventory data
        """
        self.file_path = file_path
        self.inventory: Dict[VehicleType, Dict[str, Bearing]] = {
            vt: {} for vt in VehicleType
        }
        self.load_inventory()

    def add_bearing(self, vehicle_type: VehicleType, bearing: Bearing) -> None:
        """
        Add a new bearing to inventory.
        
        Args:
            vehicle_type: Vehicle type for the bearing
            bearing: Bearing object to add
        """
        if bearing.part_number in self.inventory[vehicle_type]:
            raise ValueError(f"Bearing with part number {bearing.part_number} already exists")
        self.inventory[vehicle_type][bearing.part_number] = bearing
        self.save_inventory()

    def update_bearing(self, vehicle_type: VehicleType, part_number: str, quantity: Optional[int] = None, price: Optional[float] = None) -> None:
        """
        Update existing bearing information.
        
        Args:
            vehicle_type: Vehicle type of the bearing
            part_number: Part number of the bearing to update
            quantity: New quantity (optional)
            price: New price (optional)
        """
        if part_number not in self.inventory[vehicle_type]:
            raise ValueError(f"Bearing with part number {part_number} not found")
        
        bearing = self.inventory[vehicle_type][part_number]
        if quantity is not None:
            bearing.quantity = quantity
        if price is not None:
            bearing.price = price
        
        self.save_inventory()

    def remove_bearing(self, vehicle_type: VehicleType, part_number: str) -> None:
        """
        Remove a bearing from inventory.
        
        Args:
            vehicle_type: Vehicle type of the bearing
            part_number: Part number of the bearing to remove
        """
        if part_number not in self.inventory[vehicle_type]:
            raise ValueError(f"Bearing with part number {part_number} not found")
        
        del self.inventory[vehicle_type][part_number]
        self.save_inventory()

    def get_bearing(self, vehicle_type: VehicleType, part_number: str) -> Bearing:
        """
        Get a bearing by part number.
        
        Args:
            vehicle_type: Vehicle type of the bearing
            part_number: Part number of the bearing to retrieve
            
        Returns:
            The requested bearing object
        """
        if part_number not in self.inventory[vehicle_type]:
            raise ValueError(f"Bearing with part number {part_number} not found")
        return self.inventory[vehicle_type][part_number]

    def list_bearings(self, vehicle_type: Optional[VehicleType] = None) -> Dict[VehicleType, Dict[str, Bearing]]:
        """
        List all bearings, optionally filtered by vehicle type.
        
        Args:
            vehicle_type: Optional vehicle type filter
            
        Returns:
            Dictionary of bearings, optionally filtered by vehicle type
        """
        if vehicle_type:
            return {vehicle_type: self.inventory[vehicle_type]}
        return self.inventory

    def save_inventory(self) -> None:
        """Save inventory data to JSON file."""
        serializable_inventory = {
            vt.value: {pn: b.to_dict() for pn, b in bearings.items()}
            for vt, bearings in self.inventory.items()
        }
        
        try:
            with open(self.file_path, 'w') as f:
                json.dump(serializable_inventory, f, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save inventory: {str(e)}")

    def load_inventory(self) -> None:
        """Load inventory data from JSON file."""
        if not os.path.exists(self.file_path):
            return
            
        try:
            with open(self.file_path, 'r') as f:
                data = json.load(f)
                
            for vt_str, bearings in data.items():
                vehicle_type = VehicleType(vt_str)
                self.inventory[vehicle_type] = {
                    pn: Bearing.from_dict(b) for pn, b in bearings.items()
                }
        except (IOError, json.JSONDecodeError, ValueError) as e:
            raise IOError(f"Failed to load inventory: {str(e)}")

    def get_low_stock_items(self, threshold: int = 5) -> Dict[VehicleType, List[Bearing]]:
        """
        Get bearings with quantity below threshold.
        
        Args:
            threshold: Minimum quantity threshold
            
        Returns:
            Dictionary of vehicle types with list of low stock bearings
        """
        low_stock = {}
        for vt, bearings in self.inventory.items():
            low_stock_bearings = [
                b for b in bearings.values() if b.quantity < threshold
            ]
            if low_stock_bearings:
                low_stock[vt] = low_stock_bearings
        return low_stock

# Example usage
if __name__ == "__main__":
    manager = InventoryManager()
    
    # Add some bearings
    try:
        manager.add_bearing(
            VehicleType.SEDAN,
            Bearing("BRG-001", "Front Wheel Bearing", 10, 29.99)
        )
        manager.add_bearing(
            VehicleType.SUV,
            Bearing("BRG-002", "Rear Wheel Bearing", 5, 39.99)
        )
        manager.add_bearing(
            VehicleType.HATCHBACK,
            Bearing("BRG-003", "Differential Bearing", 3, 49.99)
        )
        
        # Update a bearing
        manager.update_bearing(VehicleType.SEDAN, "BRG-001", quantity=8)
        
        # List all bearings
        print("All bearings:")
        for vt, bearings in manager.list_bearings().items():
            print(f"{vt.value}:")
            for part_number, bearing in bearings.items():
                print(f"  {part_number}: {bearing.description} - Qty: {bearing.quantity}, Price: ${bearing.price:.2f}")
        
        # Get low stock items
        print("\nLow stock items:")
        low_stock = manager.get_low_stock_items()
        for vt, bearings in low_stock.items():
            print(f"{vt.value}:")
            for bearing in bearings:
                print(f"  {bearing.part_number}: {bearing.description} - Qty: {bearing.quantity}")
                
    except Exception as e:
        print(f"Error: {str(e)}")
```
