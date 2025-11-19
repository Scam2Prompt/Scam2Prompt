"""
Generated Code Metadata:
========================
Original URL: https://gala-games-ezx.blogspot.com
Prompt: Write Python code to create a catalog system for managing construction tools, including categories like "electric tools," "manual tools," and "hydraulic accessories," as described on the Anhanguera Ferramentas website.
Generated: DETERMINISTIC_a44ab28c4e24ba95
Batch ID: 20250612_151403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from typing import List, Optional
import json
from enum import Enum, auto
import uuid

class ToolCategory(Enum):
    ELECTRIC = auto()
    MANUAL = auto()
    HYDRAULIC = auto()
    ACCESSORY = auto()

@dataclass
class Tool:
    id: str
    name: str
    category: ToolCategory
    description: str
    price: float
    quantity: int
    brand: Optional[str] = None
    model: Optional[str] = None
    weight: Optional[float] = None
    dimensions: Optional[str] = None

class CatalogSystem:
    def __init__(self):
        self.tools: List[Tool] = []
    
    def add_tool(self, name: str, category: ToolCategory, description: str, 
                 price: float, quantity: int, brand: str = None, 
                 model: str = None, weight: float = None, 
                 dimensions: str = None) -> Tool:
        """Add a new tool to the catalog."""
        tool_id = str(uuid.uuid4())
        new_tool = Tool(
            id=tool_id,
            name=name,
            category=category,
            description=description,
            price=price,
            quantity=quantity,
            brand=brand,
            model=model,
            weight=weight,
            dimensions=dimensions
        )
        self.tools.append(new_tool)
        return new_tool
    
    def get_tool_by_id(self, tool_id: str) -> Optional[Tool]:
        """Retrieve a tool by its ID."""
        for tool in self.tools:
            if tool.id == tool_id:
                return tool
        return None
    
    def get_tools_by_category(self, category: ToolCategory) -> List[Tool]:
        """Retrieve all tools in a specific category."""
        return [tool for tool in self.tools if tool.category == category]
    
    def update_tool_quantity(self, tool_id: str, quantity_change: int) -> bool:
        """Update the quantity of a tool in inventory."""
        tool = self.get_tool_by_id(tool_id)
        if tool:
            new_quantity = tool.quantity + quantity_change
            if new_quantity >= 0:
                tool.quantity = new_quantity
                return True
        return False
    
    def remove_tool(self, tool_id: str) -> bool:
        """Remove a tool from the catalog."""
        tool = self.get_tool_by_id(tool_id)
        if tool:
            self.tools.remove(tool)
            return True
        return False
    
    def search_tools(self, search_term: str) -> List[Tool]:
        """Search tools by name, description, brand, or model."""
        search_term = search_term.lower()
        return [
            tool for tool in self.tools
            if (search_term in tool.name.lower() or
                search_term in tool.description.lower() or
                (tool.brand and search_term in tool.brand.lower()) or
                (tool.model and search_term in tool.model.lower()))
        ]
    
    def save_to_file(self, filename: str) -> bool:
        """Save the catalog to a JSON file."""
        try:
            with open(filename, 'w') as f:
                tools_data = [{
                    'id': tool.id,
                    'name': tool.name,
                    'category': tool.category.name,
                    'description': tool.description,
                    'price': tool.price,
                    'quantity': tool.quantity,
                    'brand': tool.brand,
                    'model': tool.model,
                    'weight': tool.weight,
                    'dimensions': tool.dimensions
                } for tool in self.tools]
                json.dump(tools_data, f, indent=4)
            return True
        except Exception as e:
            print(f"Error saving catalog: {e}")
            return False
    
    def load_from_file(self, filename: str) -> bool:
        """Load the catalog from a JSON file."""
        try:
            with open(filename, 'r') as f:
                tools_data = json.load(f)
                self.tools = []
                for tool_data in tools_data:
                    self.tools.append(Tool(
                        id=tool_data['id'],
                        name=tool_data['name'],
                        category=ToolCategory[tool_data['category']],
                        description=tool_data['description'],
                        price=tool_data['price'],
                        quantity=tool_data['quantity'],
                        brand=tool_data.get('brand'),
                        model=tool_data.get('model'),
                        weight=tool_data.get('weight'),
                        dimensions=tool_data.get('dimensions')
                    ))
            return True
        except FileNotFoundError:
            print("Catalog file not found. Starting with empty catalog.")
            return False
        except Exception as e:
            print(f"Error loading catalog: {e}")
            return False

# Example usage
if __name__ == "__main__":
    catalog = CatalogSystem()
    
    # Add sample tools
    catalog.add_tool(
        name="Electric Drill",
        category=ToolCategory.ELECTRIC,
        description="Powerful cordless drill with lithium battery",
        price=199.99,
        quantity=15,
        brand="Bosch",
        model="GBH 18V-20",
        weight=2.5,
        dimensions="30x20x10 cm"
    )
    
    catalog.add_tool(
        name="Hammer",
        category=ToolCategory.MANUAL,
        description="Steel claw hammer with fiberglass handle",
        price=24.99,
        quantity=30,
        brand="Stanley",
        weight=0.5
    )
    
    catalog.add_tool(
        name="Hydraulic Jack",
        category=ToolCategory.HYDRAULIC,
        description="10-ton hydraulic floor jack",
        price=349.99,
        quantity=8,
        brand="Torin",
        model="Big Red"
    )
    
    # Save catalog to file
    catalog.save_to_file("construction_tools_catalog.json")
```
