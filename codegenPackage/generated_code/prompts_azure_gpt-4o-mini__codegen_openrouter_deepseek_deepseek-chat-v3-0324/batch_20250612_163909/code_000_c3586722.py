"""
Generated Code Metadata:
========================
Original URL: https://gala-games-ezx.blogspot.com
Prompt: Generate a Python script that interacts with a catalog of construction tools, specifically focusing on electric and battery-operated tools.
Generated: DETERMINISTIC_c3586722a34cc7fb
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
    """
    A class to represent a construction tool in the catalog.
    """
    
    def __init__(self, tool_id: str, name: str, category: str, power_source: str, 
                 voltage: Optional[float] = None, battery_type: Optional[str] = None):
        """
        Initialize a construction tool.
        
        Args:
            tool_id (str): Unique identifier for the tool.
            name (str): Name of the tool.
            category (str): Category of the tool (e.g., "Drill", "Saw").
            power_source (str): Power source ("Electric" or "Battery").
            voltage (float, optional): Voltage for electric tools. Defaults to None.
            battery_type (str, optional): Battery type for battery-operated tools. Defaults to None.
        
        Raises:
            ValueError: If power_source is invalid or required fields are missing.
        """
        if power_source not in ["Electric", "Battery"]:
            raise ValueError("Power source must be 'Electric' or 'Battery'")
        
        if power_source == "Electric" and voltage is None:
            raise ValueError("Voltage is required for electric tools")
        
        if power_source == "Battery" and battery_type is None:
            raise ValueError("Battery type is required for battery-operated tools")
        
        self.tool_id = tool_id
        self.name = name
        self.category = category
        self.power_source = power_source
        self.voltage = voltage
        self.battery_type = battery_type
    
    def to_dict(self) -> Dict:
        """Convert the tool object to a dictionary."""
        return {
            "tool_id": self.tool_id,
            "name": self.name,
            "category": self.category,
            "power_source": self.power_source,
            "voltage": self.voltage,
            "battery_type": self.battery_type
        }
    
    def __repr__(self) -> str:
        return f"ConstructionTool(tool_id={self.tool_id}, name={self.name}, category={self.category}, power_source={self.power_source})"


class ToolCatalog:
    """
    A class to manage a catalog of construction tools.
    """
    
    def __init__(self, file_path: Optional[str] = None):
        """
        Initialize the tool catalog.
        
        Args:
            file_path (str, optional): Path to a JSON file to load tools from. Defaults to None.
        """
        self.tools: Dict[str, ConstructionTool] = {}
        
        if file_path:
            self.load_from_file(file_path)
    
    def add_tool(self, tool: ConstructionTool) -> None:
        """
        Add a tool to the catalog.
        
        Args:
            tool (ConstructionTool): The tool to add.
        
        Raises:
            ValueError: If a tool with the same ID already exists.
        """
        if tool.tool_id in self.tools:
            raise ValueError(f"Tool with ID {tool.tool_id} already exists")
        self.tools[tool.tool_id] = tool
    
    def remove_tool(self, tool_id: str) -> None:
        """
        Remove a tool from the catalog.
        
        Args:
            tool_id (str): ID of the tool to remove.
        
        Raises:
            KeyError: If the tool ID does not exist.
        """
        if tool_id not in self.tools:
            raise KeyError(f"Tool with ID {tool_id} not found")
        del self.tools[tool_id]
    
    def get_tool(self, tool_id: str) -> ConstructionTool:
        """
        Get a tool by ID.
        
        Args:
            tool_id (str): ID of the tool to retrieve.
        
        Returns:
            ConstructionTool: The requested tool.
        
        Raises:
            KeyError: If the tool ID does not exist.
        """
        if tool_id not in self.tools:
            raise KeyError(f"Tool with ID {tool_id} not found")
        return self.tools[tool_id]
    
    def get_tools_by_power_source(self, power_source: str) -> List[ConstructionTool]:
        """
        Get all tools with a specific power source.
        
        Args:
            power_source (str): Power source to filter by ("Electric" or "Battery").
        
        Returns:
            List[ConstructionTool]: List of matching tools.
        
        Raises:
            ValueError: If power_source is invalid.
        """
        if power_source not in ["Electric", "Battery"]:
            raise ValueError("Power source must be 'Electric' or 'Battery'")
        
        return [tool for tool in self.tools.values() if tool.power_source == power_source]
    
    def save_to_file(self, file_path: str) -> None:
        """
        Save the catalog to a JSON file.
        
        Args:
            file_path (str): Path to the file to save.
        
        Raises:
            IOError: If there is an issue writing to the file.
        """
        try:
            with open(file_path, 'w') as f:
                json.dump([tool.to_dict() for tool in self.tools.values()], f, indent=4)
        except Exception as e:
            raise IOError(f"Failed to save catalog to file: {e}")
    
    def load_from_file(self, file_path: str) -> None:
        """
        Load tools from a JSON file.
        
        Args:
            file_path (str): Path to the file to load.
        
        Raises:
            IOError: If there is an issue reading the file.
            ValueError: If the file contains invalid data.
        """
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
            
            for item in data:
                tool = ConstructionTool(
                    tool_id=item["tool_id"],
                    name=item["name"],
                    category=item["category"],
                    power_source=item["power_source"],
                    voltage=item.get("voltage"),
                    battery_type=item.get("battery_type")
                )
                self.add_tool(tool)
        except Exception as e:
            raise IOError(f"Failed to load catalog from file: {e}")


# Example usage
if __name__ == "__main__":
    try:
        # Create a catalog
        catalog = ToolCatalog()
        
        # Add some tools
        catalog.add_tool(ConstructionTool(
            tool_id="T001",
            name="Heavy-Duty Drill",
            category="Drill",
            power_source="Electric",
            voltage=120.0
        ))
        
        catalog.add_tool(ConstructionTool(
            tool_id="T002",
            name="Cordless Screwdriver",
            category="Screwdriver",
            power_source="Battery",
            battery_type="Li-Ion"
        ))
        
        # Save to file
        catalog.save_to_file("tools_catalog.json")
        
        # Load from file
        new_catalog = ToolCatalog("tools_catalog.json")
        
        # Print all battery-operated tools
        print("Battery-operated tools:")
        for tool in new_catalog.get_tools_by_power_source("Battery"):
            print(tool)
    
    except Exception as e:
        print(f"An error occurred: {e}")
```
