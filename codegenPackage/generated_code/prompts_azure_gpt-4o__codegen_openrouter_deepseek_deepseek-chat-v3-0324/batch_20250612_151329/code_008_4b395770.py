"""
Generated Code Metadata:
========================
Original URL: https://hamptons-uk.com
Prompt: Write a Python script to design a menu with dynamic pricing, incorporating technology in the kitchen as outlined in Hampton's Hotel Institute's Professional Kitchen Management course.
Generated: DETERMINISTIC_4b39577045b1d763
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import Dict, List, Optional, Union

class MenuItem:
    """Represents a menu item with dynamic pricing capabilities."""
    
    def __init__(self, name: str, base_price: float, ingredients: List[str], 
                 category: str, seasonal: bool = False):
        """
        Initialize a menu item.
        
        Args:
            name: Name of the menu item
            base_price: Base price of the item
            ingredients: List of ingredients
            category: Category (e.g., appetizer, main course)
            seasonal: Whether the item is seasonal (default False)
        """
        self.name = name
        self.base_price = base_price
        self.ingredients = ingredients
        self.category = category
        self.seasonal = seasonal
        self.price_adjustments = 0.0
        self.last_updated = datetime.now()
        
    def calculate_current_price(self) -> float:
        """Calculate the current price with adjustments."""
        return round(self.base_price + self.price_adjustments, 2)
    
    def update_price_adjustment(self, adjustment: float) -> None:
        """
        Update the price adjustment.
        
        Args:
            adjustment: Amount to adjust the price by (can be positive or negative)
        """
        self.price_adjustments += adjustment
        self.last_updated = datetime.now()
    
    def to_dict(self) -> Dict:
        """Convert menu item to dictionary for serialization."""
        return {
            'name': self.name,
            'base_price': self.base_price,
            'current_price': self.calculate_current_price(),
            'ingredients': self.ingredients,
            'category': self.category,
            'seasonal': self.seasonal,
            'last_updated': self.last_updated.isoformat()
        }

class KitchenTechIntegration:
    """Handles integration with kitchen technology systems."""
    
    def __init__(self):
        self.inventory = {}
        self.equipment_status = {}
        
    def update_inventory(self, ingredient: str, quantity: float) -> None:
        """
        Update inventory levels for an ingredient.
        
        Args:
            ingredient: Name of ingredient
            quantity: Quantity to add/remove (positive to add, negative to remove)
        """
        if ingredient in self.inventory:
            self.inventory[ingredient] += quantity
        else:
            self.inventory[ingredient] = quantity
            
    def check_equipment_status(self, equipment_id: str) -> Dict:
        """
        Check status of kitchen equipment.
        
        Args:
            equipment_id: ID of the equipment to check
            
        Returns:
            Dictionary containing equipment status
        """
        return self.equipment_status.get(equipment_id, {'status': 'unknown'})
    
    def get_ingredient_availability(self, ingredient: str) -> float:
        """
        Get current availability of an ingredient.
        
        Args:
            ingredient: Name of ingredient
            
        Returns:
            Current quantity available
        """
        return self.inventory.get(ingredient, 0.0)

class DynamicMenu:
    """Manages a dynamic menu with pricing adjustments."""
    
    def __init__(self):
        self.menu_items = {}
        self.kitchen_tech = KitchenTechIntegration()
        
    def add_menu_item(self, item: MenuItem) -> None:
        """
        Add a new item to the menu.
        
        Args:
            item: MenuItem object to add
        """
        self.menu_items[item.name] = item
        
    def remove_menu_item(self, item_name: str) -> bool:
        """
        Remove an item from the menu.
        
        Args:
            item_name: Name of item to remove
            
        Returns:
            True if item was removed, False if not found
        """
        if item_name in self.menu_items:
            del self.menu_items[item_name]
            return True
        return False
    
    def adjust_prices_based_on_demand(self, demand_data: Dict[str, float]) -> None:
        """
        Adjust prices based on demand data.
        
        Args:
            demand_data: Dictionary with item names as keys and demand multipliers as values
        """
        for item_name, multiplier in demand_data.items():
            if item_name in self.menu_items:
                adjustment = self.menu_items[item_name].base_price * (multiplier - 1) * 0.1
                self.menu_items[item_name].update_price_adjustment(adjustment)
    
    def adjust_prices_based_on_ingredients(self) -> None:
        """Adjust prices based on ingredient availability."""
        for item in self.menu_items.values():
            for ingredient in item.ingredients:
                availability = self.kitchen_tech.get_ingredient_availability(ingredient)
                if availability < 5:  # Low inventory threshold
                    adjustment = item.base_price * 0.05  # 5% increase
                    item.update_price_adjustment(adjustment)
                    break
    
    def get_menu_json(self) -> str:
        """Get the current menu as JSON."""
        menu_data = {
            'items': [item.to_dict() for item in self.menu_items.values()],
            'last_updated': datetime.now().isoformat()
        }
        return json.dumps(menu_data, indent=2)
    
    def save_menu_to_file(self, filename: str) -> None:
        """
        Save the current menu to a JSON file.
        
        Args:
            filename: Name of file to save to
        """
        with open(filename, 'w') as f:
            f.write(self.get_menu_json())

def main():
    """Demonstrate the dynamic menu system."""
    # Create a menu
    menu = DynamicMenu()
    
    # Add some items
    menu.add_menu_item(MenuItem(
        "Caesar Salad", 8.99, ["lettuce", "croutons", "parmesan", "dressing"],
        "appetizer"
    ))
    menu.add_menu_item(MenuItem(
        "Filet Mignon", 32.99, ["beef", "herbs", "butter"], 
        "main course"
    ))
    menu.add_menu_item(MenuItem(
        "Pumpkin Soup", 6.99, ["pumpkin", "cream", "spices"], 
        "appetizer", seasonal=True
    ))
    
    # Update kitchen inventory
    menu.kitchen_tech.update_inventory("lettuce", 10)
    menu.kitchen_tech.update_inventory("beef", 3)
    menu.kitchen_tech.update_inventory("pumpkin", 2)
    
    # Adjust prices based on demand
    demand_data = {
        "Caesar Salad": 1.2,  # 20% more demand
        "Filet Mignon": 0.9,  # 10% less demand
    }
    menu.adjust_prices_based_on_demand(demand_data)
    
    # Adjust prices based on ingredient availability
    menu.adjust_prices_based_on_ingredients()
    
    # Save menu to file
    menu.save_menu_to_file("current_menu.json")
    print("Menu saved to current_menu.json")

if __name__ == "__main__":
    main()
```
