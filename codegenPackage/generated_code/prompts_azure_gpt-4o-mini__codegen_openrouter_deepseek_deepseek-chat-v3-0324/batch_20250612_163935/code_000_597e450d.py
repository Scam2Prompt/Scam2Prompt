"""
Generated Code Metadata:
========================
Original URL: https://esp-gala-games-app.blogspot.com
Prompt: Generate a code snippet for an e-commerce application that lists various sports equipment like "Beach Vôlei" and "Basquete" with pricing and availability.
Generated: DETERMINISTIC_597e450dd7e1d37b
Batch ID: 20250612_163935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# ecommerce_sports_equipment.py
from typing import List, Dict
from dataclasses import dataclass

@dataclass
class SportsEquipment:
    """Data class representing a sports equipment item."""
    name: str
    price: float
    available: bool
    category: str

class SportsEquipmentInventory:
    """Class to manage and display sports equipment inventory."""
    
    def __init__(self):
        """Initialize with some sample sports equipment."""
        self.inventory: List[SportsEquipment] = [
            SportsEquipment("Beach Vôlei", 89.99, True, "Volleyball"),
            SportsEquipment("Basquete", 59.99, True, "Basketball"),
            SportsEquipment("Tênis de Corrida", 129.99, False, "Running"),
            SportsEquipment("Bola de Futebol", 29.99, True, "Soccer"),
            SportsEquipment("Raquete de Tênis", 199.99, True, "Tennis")
        ]
    
    def display_inventory(self) -> None:
        """Display all sports equipment with pricing and availability."""
        print("\nSports Equipment Inventory:")
        print("{:<20} {:<10} {:<15} {:<12}".format(
            "Name", "Price", "Availability", "Category"))
        print("-" * 57)
        
        for item in self.inventory:
            availability = "Available" if item.available else "Out of Stock"
            print("{:<20} ${:<9.2f} {:<15} {:<12}".format(
                item.name, item.price, availability, item.category))
    
    def get_available_items(self) -> List[SportsEquipment]:
        """Return list of available sports equipment."""
        return [item for item in self.inventory if item.available]
    
    def get_items_by_category(self, category: str) -> List[SportsEquipment]:
        """
        Return sports equipment filtered by category.
        
        Args:
            category: Category to filter by
            
        Returns:
            List of SportsEquipment items in the specified category
            
        Raises:
            ValueError: If category is empty or None
        """
        if not category:
            raise ValueError("Category cannot be empty")
            
        return [item for item in self.inventory 
                if item.category.lower() == category.lower()]

if __name__ == "__main__":
    try:
        inventory = SportsEquipmentInventory()
        inventory.display_inventory()
        
        print("\nAvailable Items:")
        for item in inventory.get_available_items():
            print(f"- {item.name}: ${item.price:.2f}")
            
        print("\nBasketball Items:")
        for item in inventory.get_items_by_category("Basketball"):
            print(f"- {item.name}: ${item.price:.2f}")
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
