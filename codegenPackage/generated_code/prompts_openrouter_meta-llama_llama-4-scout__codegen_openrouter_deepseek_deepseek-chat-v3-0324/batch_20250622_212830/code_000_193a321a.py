"""
Generated Code Metadata:
========================
Original URL: https://swp-connect-poocoin.blogspot.com
Prompt: Write a Python script to create an inventory management system for a toolbox containing items like alicate, furadeira, martelo, and parafusadeira.
Generated: DETERMINISTIC_193a321af9c617ff
Batch ID: 20250622_212830
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
from typing import Dict, List, Optional

class ToolboxInventory:
    """
    A class to manage inventory of tools in a toolbox.
    """
    
    def __init__(self, inventory_file: str = "toolbox_inventory.json"):
        """
        Initialize the inventory system.
        
        Args:
            inventory_file: Path to the JSON file storing inventory data.
        """
        self.inventory_file = inventory_file
        self.inventory: Dict[str, int] = self._load_inventory()
    
    def _load_inventory(self) -> Dict[str, int]:
        """
        Load inventory data from JSON file.
        
        Returns:
            Dictionary containing tool names as keys and quantities as values.
            
        Raises:
            FileNotFoundError: If the inventory file doesn't exist.
            json.JSONDecodeError: If the file contains invalid JSON.
        """
        try:
            if os.path.exists(self.inventory_file):
                with open(self.inventory_file, 'r') as f:
                    return json.load(f)
            return {}
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON in inventory file: {e}")
    
    def _save_inventory(self) -> None:
        """
        Save current inventory to JSON file.
        """
        with open(self.inventory_file, 'w') as f:
            json.dump(self.inventory, f, indent=4)
    
    def add_tool(self, tool_name: str, quantity: int = 1) -> None:
        """
        Add a tool to the inventory or increase its quantity.
        
        Args:
            tool_name: Name of the tool to add.
            quantity: Number of items to add (default: 1).
            
        Raises:
            ValueError: If quantity is not positive.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
            
        tool_name = tool_name.lower().strip()
        if tool_name in self.inventory:
            self.inventory[tool_name] += quantity
        else:
            self.inventory[tool_name] = quantity
        self._save_inventory()
    
    def remove_tool(self, tool_name: str, quantity: int = 1) -> None:
        """
        Remove a tool from the inventory or decrease its quantity.
        
        Args:
            tool_name: Name of the tool to remove.
            quantity: Number of items to remove (default: 1).
            
        Raises:
            ValueError: If tool doesn't exist or quantity is invalid.
        """
        tool_name = tool_name.lower().strip()
        if tool_name not in self.inventory:
            raise ValueError(f"Tool '{tool_name}' not found in inventory.")
            
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
            
        if self.inventory[tool_name] < quantity:
            raise ValueError(f"Not enough '{tool_name}' in inventory.")
            
        self.inventory[tool_name] -= quantity
        
        if self.inventory[tool_name] == 0:
            del self.inventory[tool_name]
            
        self._save_inventory()
    
    def get_inventory(self) -> Dict[str, int]:
        """
        Get current inventory status.
        
        Returns:
            Dictionary containing all tools and their quantities.
        """
        return self.inventory.copy()
    
    def search_tool(self, tool_name: str) -> Optional[int]:
        """
        Search for a tool in the inventory.
        
        Args:
            tool_name: Name of the tool to search for.
            
        Returns:
            Quantity of the tool if found, None otherwise.
        """
        tool_name = tool_name.lower().strip()
        return self.inventory.get(tool_name)
    
    def list_tools(self) -> List[str]:
        """
        List all tools in the inventory.
        
        Returns:
            List of tool names sorted alphabetically.
        """
        return sorted(self.inventory.keys())

def main():
    """
    Example usage of the ToolboxInventory class.
    """
    inventory = ToolboxInventory()
    
    # Add some tools
    inventory.add_tool("alicate", 2)
    inventory.add_tool("furadeira", 1)
    inventory.add_tool("martelo", 3)
    inventory.add_tool("parafusadeira", 1)
    
    # Print inventory
    print("Current Inventory:")
    for tool, quantity in inventory.get_inventory().items():
        print(f"- {tool}: {quantity}")
    
    # Remove a tool
    inventory.remove_tool("martelo", 1)
    
    # Search for a tool
    tool = "furadeira"
    quantity = inventory.search_tool(tool)
    print(f"\nQuantity of {tool}: {quantity if quantity is not None else 'Not found'}")
    
    # List all tools
    print("\nAll tools in inventory:")
    for tool in inventory.list_tools():
        print(f"- {tool}")

if __name__ == "__main__":
    main()
```
