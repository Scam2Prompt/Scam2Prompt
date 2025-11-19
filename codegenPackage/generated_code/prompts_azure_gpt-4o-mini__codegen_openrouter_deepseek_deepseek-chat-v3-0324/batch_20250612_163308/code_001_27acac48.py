"""
Generated Code Metadata:
========================
Original URL: https://swp-connect-poocoin.blogspot.com
Prompt: Write a Python function that integrates with a library to manage a toolbox inventory, specifically for tools mentioned in Jeilson Ferramentas JA, such as "martelo" and "fios."
Generated: DETERMINISTIC_27acac48b854757d
Batch ID: 20250612_163308
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

class ToolboxInventory:
    """
    A class to manage the inventory of tools from Jeilson Ferramentas JA.
    Supports adding, removing, searching, and listing tools in the inventory.
    """

    def __init__(self, inventory_file: str = "toolbox_inventory.json"):
        """
        Initialize the ToolboxInventory with a JSON file for storage.
        
        Args:
            inventory_file (str): Path to the JSON file storing the inventory data.
        """
        self.inventory_file = inventory_file
        self.inventory: Dict[str, int] = self._load_inventory()

    def _load_inventory(self) -> Dict[str, int]:
        """
        Load the inventory data from the JSON file.
        
        Returns:
            Dict[str, int]: Dictionary mapping tool names to their quantities.
            
        Raises:
            FileNotFoundError: If the inventory file does not exist.
            json.JSONDecodeError: If the file contains invalid JSON.
        """
        try:
            with open(self.inventory_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}  # Return empty inventory if file doesn't exist
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(f"Invalid JSON in {self.inventory_file}", e.doc, e.pos)

    def _save_inventory(self):
        """
        Save the current inventory to the JSON file.
        
        Raises:
            IOError: If the file cannot be written.
        """
        try:
            with open(self.inventory_file, 'w') as f:
                json.dump(self.inventory, f, indent=4)
        except IOError as e:
            raise IOError(f"Failed to save inventory: {e}")

    def add_tool(self, tool_name: str, quantity: int = 1) -> None:
        """
        Add a tool or increase its quantity in the inventory.
        
        Args:
            tool_name (str): Name of the tool (e.g., "martelo", "fios").
            quantity (int): Quantity to add. Must be positive.
            
        Raises:
            ValueError: If quantity is not positive.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        
        if tool_name in self.inventory:
            self.inventory[tool_name] += quantity
        else:
            self.inventory[tool_name] = quantity
        self._save_inventory()

    def remove_tool(self, tool_name: str, quantity: int = 1) -> None:
        """
        Remove a tool or decrease its quantity in the inventory.
        
        Args:
            tool_name (str): Name of the tool (e.g., "martelo", "fios").
            quantity (int): Quantity to remove. Must be positive.
            
        Raises:
            ValueError: If quantity is not positive or exceeds available quantity.
            KeyError: If the tool is not in the inventory.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        
        if tool_name not in self.inventory:
            raise KeyError(f"Tool '{tool_name}' not found in inventory.")
        
        if self.inventory[tool_name] < quantity:
            raise ValueError(f"Cannot remove {quantity} '{tool_name}'. Only {self.inventory[tool_name]} available.")
        
        self.inventory[tool_name] -= quantity
        if self.inventory[tool_name] == 0:
            del self.inventory[tool_name]
        self._save_inventory()

    def get_tool_quantity(self, tool_name: str) -> int:
        """
        Get the quantity of a specific tool in the inventory.
        
        Args:
            tool_name (str): Name of the tool (e.g., "martelo", "fios").
            
        Returns:
            int: Quantity of the tool in inventory.
            
        Raises:
            KeyError: If the tool is not in the inventory.
        """
        if tool_name not in self.inventory:
            raise KeyError(f"Tool '{tool_name}' not found in inventory.")
        return self.inventory[tool_name]

    def list_tools(self) -> List[str]:
        """
        List all tools in the inventory.
        
        Returns:
            List[str]: List of all tool names in the inventory.
        """
        return list(self.inventory.keys())

    def search_tools(self, keyword: str) -> List[str]:
        """
        Search for tools by a keyword.
        
        Args:
            keyword (str): Keyword to search in tool names.
            
        Returns:
            List[str]: List of matching tool names.
        """
        return [tool for tool in self.inventory.keys() if keyword.lower() in tool.lower()]
```
