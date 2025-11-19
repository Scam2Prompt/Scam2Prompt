"""
Generated Code Metadata:
========================
Original URL: https://labelmystuff.com
Prompt: Write code to manage an inventory of label designs for small businesses, including options for crafts and sports teams, referencing the use cases from Labelmystuff.com.
Generated: DETERMINISTIC_1c6c6e5f5d08cbd2
Batch ID: 20250612_145615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Label Design Inventory Management System

This module provides functionality to manage an inventory of label designs
for small businesses, including crafts and sports teams.
"""

from dataclasses import dataclass
from enum import Enum
import json
from typing import List, Dict, Optional
import os
from datetime import datetime
import uuid


class DesignCategory(Enum):
    """Enum representing different categories of label designs."""
    CRAFTS = "Crafts"
    SPORTS_TEAMS = "Sports Teams"
    BUSINESS = "Business"
    OTHER = "Other"


@dataclass
class LabelDesign:
    """Data class representing a label design."""
    design_id: str
    name: str
    category: DesignCategory
    description: str
    dimensions: str
    colors: List[str]
    price: float
    stock_quantity: int
    created_at: str
    updated_at: str
    image_path: Optional[str] = None


class LabelInventoryManager:
    """Class to manage label design inventory operations."""
    
    def __init__(self, data_file: str = "label_designs.json"):
        """Initialize the inventory manager with a data file."""
        self.data_file = data_file
        self.designs: Dict[str, LabelDesign] = {}
        self._load_data()
    
    def _load_data(self) -> None:
        """Load design data from the JSON file."""
        try:
            if os.path.exists(self.data_file):
                with open(self.data_file, 'r') as file:
                    data = json.load(file)
                    for design_id, design_data in data.items():
                        design_data['category'] = DesignCategory(design_data['category'])
                        self.designs[design_id] = LabelDesign(**design_data)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading data: {e}")
            self.designs = {}
    
    def _save_data(self) -> None:
        """Save design data to the JSON file."""
        try:
            with open(self.data_file, 'w') as file:
                serializable_data = {
                    design_id: {
                        **design.__dict__,
                        'category': design.category.value
                    }
                    for design_id, design in self.designs.items()
                }
                json.dump(serializable_data, file, indent=2)
        except IOError as e:
            print(f"Error saving data: {e}")
    
    def add_design(
        self,
        name: str,
        category: DesignCategory,
        description: str,
        dimensions: str,
        colors: List[str],
        price: float,
        stock_quantity: int,
        image_path: Optional[str] = None
    ) -> LabelDesign:
        """Add a new label design to the inventory."""
        design_id = str(uuid.uuid4())
        now = datetime.now().isoformat()
        
        new_design = LabelDesign(
            design_id=design_id,
            name=name,
            category=category,
            description=description,
            dimensions=dimensions,
            colors=colors,
            price=price,
            stock_quantity=stock_quantity,
            created_at=now,
            updated_at=now,
            image_path=image_path
        )
        
        self.designs[design_id] = new_design
        self._save_data()
        return new_design
    
    def update_design(
        self,
        design_id: str,
        name: Optional[str] = None,
        category: Optional[DesignCategory] = None,
        description: Optional[str] = None,
        dimensions: Optional[str] = None,
        colors: Optional[List[str]] = None,
        price: Optional[float] = None,
        stock_quantity: Optional[int] = None,
        image_path: Optional[str] = None
    ) -> Optional[LabelDesign]:
        """Update an existing label design."""
        if design_id not in self.designs:
            return None
        
        design = self.designs[design_id]
        
        if name is not None:
            design.name = name
        if category is not None:
            design.category = category
        if description is not None:
            design.description = description
        if dimensions is not None:
            design.dimensions = dimensions
        if colors is not None:
            design.colors = colors
        if price is not None:
            design.price = price
        if stock_quantity is not None:
            design.stock_quantity = stock_quantity
        if image_path is not None:
            design.image_path = image_path
        
        design.updated_at = datetime.now().isoformat()
        self._save_data()
        return design
    
    def get_design(self, design_id: str) -> Optional[LabelDesign]:
        """Retrieve a design by its ID."""
        return self.designs.get(design_id)
    
    def get_all_designs(self) -> List[LabelDesign]:
        """Retrieve all designs in the inventory."""
        return list(self.designs.values())
    
    def get_designs_by_category(self, category: DesignCategory) -> List[LabelDesign]:
        """Retrieve designs filtered by category."""
        return [design for design in self.designs.values() if design.category == category]
    
    def delete_design(self, design_id: str) -> bool:
        """Delete a design from the inventory."""
        if design_id in self.designs:
            del self.designs[design_id]
            self._save_data()
            return True
        return False
    
    def update_stock(self, design_id: str, quantity_change: int) -> Optional[LabelDesign]:
        """Update the stock quantity of a design."""
        if design_id not in self.designs:
            return None
        
        design = self.designs[design_id]
        new_quantity = design.stock_quantity + quantity_change
        
        if new_quantity < 0:
            raise ValueError("Stock quantity cannot be negative")
        
        design.stock_quantity = new_quantity
        design.updated_at = datetime.now().isoformat()
        self._save_data()
        return design


# Example usage
if __name__ == "__main__":
    manager = LabelInventoryManager()
    
    # Add a new design
    craft_design = manager.add_design(
        name="Floral Craft Labels",
        category=DesignCategory.CRAFTS,
        description="Beautiful floral labels for craft projects",
        dimensions="2x3 inches",
        colors=["pink", "green", "yellow"],
        price=12.99,
        stock_quantity=50,
        image_path="images/floral_labels.jpg"
    )
    
    # Update the design
    manager.update_design(
        design_id=craft_design.design_id,
        price=14.99,
        stock_quantity=45
    )
    
    # Get all designs
    all_designs = manager.get_all_designs()
    print(f"Total designs: {len(all_designs)}")
    
    # Get designs by category
    craft_designs = manager.get_designs_by_category(DesignCategory.CRAFTS)
    print(f"Craft designs: {len(craft_designs)}")
```
