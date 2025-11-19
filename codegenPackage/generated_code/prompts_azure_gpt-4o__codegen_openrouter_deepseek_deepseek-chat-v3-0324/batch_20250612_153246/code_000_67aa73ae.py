"""
Generated Code Metadata:
========================
Original URL: https://sanurisupplies.com
Prompt: Write Python code to generate a checklist for office supplies, including items like computers, printers, planners, and document scanners, as described on Sanuri Supplies' website.
Generated: DETERMINISTIC_67aa73ae5b33765b
Batch ID: 20250612_153246
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

class OfficeSuppliesChecklist:
    """
    A class to generate and manage an office supplies checklist.
    """
    
    def __init__(self):
        """
        Initialize the checklist with default items from Sanuri Supplies.
        """
        self.checklist = [
            {"name": "Computers", "quantity": 0, "checked": False},
            {"name": "Printers", "quantity": 0, "checked": False},
            {"name": "Planners", "quantity": 0, "checked": False},
            {"name": "Document Scanners", "quantity": 0, "checked": False}
        ]
    
    def add_item(self, name: str, quantity: int = 0) -> None:
        """
        Add a new item to the checklist.
        
        Args:
            name: Name of the item to add.
            quantity: Initial quantity (default 0).
        """
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Item name must be a non-empty string.")
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")
            
        self.checklist.append({
            "name": name.strip(),
            "quantity": quantity,
            "checked": False
        })
    
    def remove_item(self, name: str) -> None:
        """
        Remove an item from the checklist.
        
        Args:
            name: Name of the item to remove.
        """
        if not isinstance(name, str):
            raise ValueError("Item name must be a string.")
            
        name = name.strip()
        self.checklist = [item for item in self.checklist if item["name"] != name]
    
    def update_quantity(self, name: str, quantity: int) -> None:
        """
        Update the quantity of an item.
        
        Args:
            name: Name of the item to update.
            quantity: New quantity.
        """
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Item name must be a non-empty string.")
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")
            
        name = name.strip()
        for item in self.checklist:
            if item["name"] == name:
                item["quantity"] = quantity
                return
        raise ValueError(f"Item '{name}' not found in checklist.")
    
    def toggle_check(self, name: str) -> None:
        """
        Toggle the checked status of an item.
        
        Args:
            name: Name of the item to toggle.
        """
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Item name must be a non-empty string.")
            
        name = name.strip()
        for item in self.checklist:
            if item["name"] == name:
                item["checked"] = not item["checked"]
                return
        raise ValueError(f"Item '{name}' not found in checklist.")
    
    def get_checklist(self) -> List[Dict[str, object]]:
        """
        Get the current checklist.
        
        Returns:
            A list of dictionary items representing the checklist.
        """
        return self.checklist
    
    def save_to_file(self, filename: str) -> None:
        """
        Save the checklist to a JSON file.
        
        Args:
            filename: Name of the file to save to.
        """
        if not isinstance(filename, str) or not filename.strip():
            raise ValueError("Filename must be a non-empty string.")
            
        with open(filename.strip(), 'w') as f:
            json.dump(self.checklist, f, indent=4)
    
    def load_from_file(self, filename: str) -> None:
        """
        Load a checklist from a JSON file.
        
        Args:
            filename: Name of the file to load from.
        """
        if not isinstance(filename, str) or not filename.strip():
            raise ValueError("Filename must be a non-empty string.")
            
        try:
            with open(filename.strip(), 'r') as f:
                self.checklist = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"File '{filename}' not found.")
        except json.JSONDecodeError:
            raise ValueError(f"File '{filename}' contains invalid JSON.")

# Example usage
if __name__ == "__main__":
    try:
        checklist = OfficeSuppliesChecklist()
        
        # Add some items
        checklist.add_item("Staplers", 2)
        checklist.add_item("Paper Clips", 100)
        
        # Update quantities
        checklist.update_quantity("Computers", 5)
        checklist.update_quantity("Printers", 2)
        
        # Toggle some items
        checklist.toggle_check("Computers")
        checklist.toggle_check("Planners")
        
        # Save to file
        checklist.save_to_file("office_supplies_checklist.json")
        
        # Print current checklist
        print("Current Checklist:")
        for item in checklist.get_checklist():
            print(f"{'[X]' if item['checked'] else '[ ]'} {item['name']} - Qty: {item['quantity']}")
            
    except Exception as e:
        print(f"An error occurred: {e}")
```
