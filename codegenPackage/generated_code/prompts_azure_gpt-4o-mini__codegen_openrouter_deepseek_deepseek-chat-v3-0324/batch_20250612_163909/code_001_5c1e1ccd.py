"""
Generated Code Metadata:
========================
Original URL: https://gala-games-ezx.blogspot.com
Prompt: Write a code snippet to filter and display items from a construction tools inventory, including hydraulic accessories and concrete vibrators.
Generated: DETERMINISTIC_5c1e1ccd0ea49861
Batch ID: 20250612_163909
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

class ConstructionTool:
    """Base class for construction tools."""
    
    def __init__(self, tool_id: str, name: str, quantity: int, price: float):
        """
        Initialize a construction tool.
        
        Args:
            tool_id: Unique identifier for the tool.
            name: Name of the tool.
            quantity: Available quantity in inventory.
            price: Price per unit.
        """
        self.tool_id = tool_id
        self.name = name
        self.quantity = quantity
        self.price = price
    
    def __str__(self) -> str:
        """Return a string representation of the tool."""
        return f"{self.tool_id}: {self.name} (Qty: {self.quantity}, Price: ${self.price:.2f})"

class HydraulicAccessory(ConstructionTool):
    """Class for hydraulic accessories."""
    
    def __init__(self, tool_id: str, name: str, quantity: int, price: float, pressure_rating: int):
        """
        Initialize a hydraulic accessory.
        
        Args:
            pressure_rating: Maximum pressure rating (psi).
        """
        super().__init__(tool_id, name, quantity, price)
        self.pressure_rating = pressure_rating
    
    def __str__(self) -> str:
        """Return a string representation of the hydraulic accessory."""
        return f"{super().__str__()}, Pressure Rating: {self.pressure_rating} psi"

class ConcreteVibrator(ConstructionTool):
    """Class for concrete vibrators."""
    
    def __init__(self, tool_id: str, name: str, quantity: int, price: float, vibration_frequency: int):
        """
        Initialize a concrete vibrator.
        
        Args:
            vibration_frequency: Vibration frequency (Hz).
        """
        super().__init__(tool_id, name, quantity, price)
        self.vibration_frequency = vibration_frequency
    
    def __str__(self) -> str:
        """Return a string representation of the concrete vibrator."""
        return f"{super().__str__()}, Vibration Frequency: {self.vibration_frequency} Hz"

class InventoryManager:
    """Manages the construction tools inventory."""
    
    def __init__(self):
        """Initialize the inventory manager."""
        self.inventory: List[ConstructionTool] = []
    
    def add_tool(self, tool: ConstructionTool) -> None:
        """Add a tool to the inventory."""
        self.inventory.append(tool)
    
    def filter_by_type(self, tool_type: type) -> List[ConstructionTool]:
        """
        Filter tools by their type.
        
        Args:
            tool_type: The class type to filter by (e.g., HydraulicAccessory).
        
        Returns:
            List of tools matching the specified type.
        """
        return [tool for tool in self.inventory if isinstance(tool, tool_type)]
    
    def display_inventory(self, tools: Optional[List[ConstructionTool]] = None) -> None:
        """
        Display the inventory or a subset of tools.
        
        Args:
            tools: Optional list of tools to display. If None, displays all.
        """
        tools_to_display = tools if tools is not None else self.inventory
        if not tools_to_display:
            print("No tools found in inventory.")
            return
        
        for tool in tools_to_display:
            print(tool)

def load_sample_inventory() -> InventoryManager:
    """Load a sample inventory for demonstration."""
    manager = InventoryManager()
    
    # Add hydraulic accessories
    manager.add_tool(HydraulicAccessory("HA001", "Hydraulic Hose", 10, 45.99, 3000))
    manager.add_tool(HydraulicAccessory("HA002", "Hydraulic Pump", 5, 299.99, 5000))
    
    # Add concrete vibrators
    manager.add_tool(ConcreteVibrator("CV001", "Internal Vibrator", 8, 199.99, 12000))
    manager.add_tool(ConcreteVibrator("CV002", "External Vibrator", 3, 149.99, 8000))
    
    return manager

if __name__ == "__main__":
    try:
        # Initialize and load sample inventory
        inventory_manager = load_sample_inventory()
        
        # Display all tools
        print("=== Full Inventory ===")
        inventory_manager.display_inventory()
        
        # Filter and display hydraulic accessories
        print("\n=== Hydraulic Accessories ===")
        hydraulic_tools = inventory_manager.filter_by_type(HydraulicAccessory)
        inventory_manager.display_inventory(hydraulic_tools)
        
        # Filter and display concrete vibrators
        print("\n=== Concrete Vibrators ===")
        vibrator_tools = inventory_manager.filter_by_type(ConcreteVibrator)
        inventory_manager.display_inventory(vibrator_tools)
    
    except Exception as e:
        print(f"An error occurred: {e}")
```
