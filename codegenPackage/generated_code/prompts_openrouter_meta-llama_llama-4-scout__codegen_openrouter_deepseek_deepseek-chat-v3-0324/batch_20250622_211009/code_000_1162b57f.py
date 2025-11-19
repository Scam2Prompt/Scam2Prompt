"""
Generated Code Metadata:
========================
Original URL: https://longhuigolf.com
Prompt: Write a Python script to manage inventory of golf grips, including rubber, TPE, and PU grips, with different styles and customization options.
Generated: DETERMINISTIC_1162b57fe7274c67
Batch ID: 20250622_211009
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
from typing import Dict, List, Optional, Union

class GolfGripInventory:
    """
    A class to manage inventory of golf grips with different materials, styles, and customization options.
    """
    
    def __init__(self, inventory_file: str = "golf_grip_inventory.json"):
        """
        Initialize the inventory with a JSON file for persistence.
        
        Args:
            inventory_file: Path to the JSON file storing inventory data.
        """
        self.inventory_file = inventory_file
        self.inventory: Dict[str, Dict] = {}
        self.load_inventory()
    
    def load_inventory(self) -> None:
        """
        Load inventory data from the JSON file.
        Creates a new file if it doesn't exist.
        """
        try:
            if os.path.exists(self.inventory_file):
                with open(self.inventory_file, 'r') as file:
                    self.inventory = json.load(file)
            else:
                self.inventory = {}
                self.save_inventory()
        except Exception as e:
            raise Exception(f"Error loading inventory: {str(e)}")
    
    def save_inventory(self) -> None:
        """
        Save the current inventory to the JSON file.
        """
        try:
            with open(self.inventory_file, 'w') as file:
                json.dump(self.inventory, file, indent=4)
        except Exception as e:
            raise Exception(f"Error saving inventory: {str(e)}")
    
    def add_grip(
        self,
        grip_id: str,
        material: str,
        style: str,
        quantity: int,
        color: Optional[str] = None,
        pattern: Optional[str] = None,
        size: Optional[str] = None,
        custom_text: Optional[str] = None
    ) -> None:
        """
        Add a new grip to the inventory or update existing grip's quantity.
        
        Args:
            grip_id: Unique identifier for the grip.
            material: Material type (rubber, TPE, PU).
            style: Grip style.
            quantity: Number of grips to add.
            color: Optional color of the grip.
            pattern: Optional pattern on the grip.
            size: Optional size of the grip.
            custom_text: Optional custom text on the grip.
        """
        if material.lower() not in ["rubber", "tpe", "pu"]:
            raise ValueError("Invalid material. Must be rubber, TPE, or PU.")
        
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        
        grip_data = {
            "material": material.lower(),
            "style": style,
            "quantity": quantity,
            "color": color,
            "pattern": pattern,
            "size": size,
            "custom_text": custom_text
        }
        
        if grip_id in self.inventory:
            self.inventory[grip_id]["quantity"] += quantity
        else:
            self.inventory[grip_id] = grip_data
        
        self.save_inventory()
    
    def remove_grip(self, grip_id: str, quantity: int = 1) -> None:
        """
        Remove a grip from inventory or reduce its quantity.
        
        Args:
            grip_id: ID of the grip to remove.
            quantity: Number of grips to remove.
        
        Raises:
            ValueError: If grip doesn't exist or quantity is invalid.
        """
        if grip_id not in self.inventory:
            raise ValueError("Grip ID not found in inventory.")
        
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        
        current_quantity = self.inventory[grip_id]["quantity"]
        
        if quantity > current_quantity:
            raise ValueError(f"Cannot remove {quantity} items. Only {current_quantity} available.")
        
        self.inventory[grip_id]["quantity"] -= quantity
        
        if self.inventory[grip_id]["quantity"] == 0:
            del self.inventory[grip_id]
        
        self.save_inventory()
    
    def get_grip(self, grip_id: str) -> Dict[str, Union[str, int]]:
        """
        Retrieve grip information by ID.
        
        Args:
            grip_id: ID of the grip to retrieve.
        
        Returns:
            Dictionary containing grip details.
        
        Raises:
            ValueError: If grip ID doesn't exist.
        """
        if grip_id not in self.inventory:
            raise ValueError("Grip ID not found in inventory.")
        
        return self.inventory[grip_id]
    
    def list_grips(self, material: Optional[str] = None) -> List[Dict[str, Union[str, int]]]:
        """
        List all grips in inventory, optionally filtered by material.
        
        Args:
            material: Optional material to filter by (rubber, TPE, PU).
        
        Returns:
            List of grip dictionaries.
        """
        if material:
            material = material.lower()
            if material not in ["rubber", "tpe", "pu"]:
                raise ValueError("Invalid material. Must be rubber, TPE, or PU.")
            
            return [
                {"id": grip_id, **grip_data}
                for grip_id, grip_data in self.inventory.items()
                if grip_data["material"] == material
            ]
        else:
            return [
                {"id": grip_id, **grip_data}
                for grip_id, grip_data in self.inventory.items()
            ]
    
    def update_grip_details(
        self,
        grip_id: str,
        material: Optional[str] = None,
        style: Optional[str] = None,
        color: Optional[str] = None,
        pattern: Optional[str] = None,
        size: Optional[str] = None,
        custom_text: Optional[str] = None
    ) -> None:
        """
        Update details of an existing grip.
        
        Args:
            grip_id: ID of the grip to update.
            material: New material (rubber, TPE, PU).
            style: New style.
            color: New color.
            pattern: New pattern.
            size: New size.
            custom_text: New custom text.
        
        Raises:
            ValueError: If grip ID doesn't exist or material is invalid.
        """
        if grip_id not in self.inventory:
            raise ValueError("Grip ID not found in inventory.")
        
        if material and material.lower() not in ["rubber", "tpe", "pu"]:
            raise ValueError("Invalid material. Must be rubber, TPE, or PU.")
        
        grip = self.inventory[grip_id]
        
        if material:
            grip["material"] = material.lower()
        if style:
            grip["style"] = style
        if color:
            grip["color"] = color
        if pattern:
            grip["pattern"] = pattern
        if size:
            grip["size"] = size
        if custom_text:
            grip["custom_text"] = custom_text
        
        self.save_inventory()
    
    def get_inventory_summary(self) -> Dict[str, int]:
        """
        Get a summary of inventory counts by material.
        
        Returns:
            Dictionary with material counts.
        """
        summary = {"rubber": 0, "tpe": 0, "pu": 0}
        
        for grip_data in self.inventory.values():
            material = grip_data["material"]
            summary[material] += grip_data["quantity"]
        
        return summary


# Example usage
if __name__ == "__main__":
    inventory = GolfGripInventory()
    
    # Add some grips
    inventory.add_grip("GR001", "rubber", "standard", 50, color="black", size="midsize")
    inventory.add_grip("GR002", "TPE", "midsize", 30, color="blue", pattern="cord")
    inventory.add_grip("GR003", "PU", "jumbo", 20, color="red", custom_text="PRO")
    
    # List all grips
    print("All grips:")
    for grip in inventory.list_grips():
        print(grip)
    
    # List rubber grips only
    print("\nRubber grips:")
    for grip in inventory.list_grips(material="rubber"):
        print(grip)
    
    # Get inventory summary
    print("\nInventory summary:")
    print(inventory.get_inventory_summary())
    
    # Update a grip
    inventory.update_grip_details("GR001", color="red", custom_text="TOUR")
    
    # Remove some grips
    inventory.remove_grip("GR001", 10)
    
    # Get specific grip details
    print("\nUpdated GR001 details:")
    print(inventory.get_grip("GR001"))
```
