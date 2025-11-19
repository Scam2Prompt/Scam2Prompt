"""
Generated Code Metadata:
========================
Original URL: https://www.lky.com.tw
Prompt: Write a Python script to generate a menu for 老廣粵台南花雕雞專門店, including dishes such as 廣粵花雕雞, 澳門豬骨煲, and 麻辣廣粵花雕雞.
Generated: DETERMINISTIC_aed543c3197efde7
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Menu Generator for 老廣粵台南花雕雞專門店
This script generates a menu with dishes and their details.
"""

import json
from typing import List, Dict

class MenuItem:
    """Class representing a single menu item."""
    
    def __init__(self, name: str, description: str, price: float, spicy: bool = False):
        """
        Initialize a menu item.
        
        Args:
            name: Name of the dish
            description: Description of the dish
            price: Price in local currency
            spicy: Whether the dish is spicy (default: False)
        """
        self.name = name
        self.description = description
        self.price = price
        self.spicy = spicy
    
    def to_dict(self) -> Dict:
        """Convert menu item to dictionary for serialization."""
        return {
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'spicy': self.spicy
        }

class MenuGenerator:
    """Class to generate and manage the restaurant menu."""
    
    def __init__(self):
        """Initialize menu with default items."""
        self.menu_items: List[MenuItem] = []
        self._initialize_menu()
    
    def _initialize_menu(self):
        """Add default menu items."""
        self.add_item(
            "廣粵花雕雞",
            "傳統廣東風味花雕雞，酒香濃郁，肉質鮮嫩",
            128.00
        )
        self.add_item(
            "澳門豬骨煲",
            "澳門特色豬骨煲，湯底濃郁，配料豐富",
            98.00
        )
        self.add_item(
            "麻辣廣粵花雕雞",
            "廣粵花雕雞加入四川麻辣風味，香辣過癮",
            138.00,
            spicy=True
        )
    
    def add_item(self, name: str, description: str, price: float, spicy: bool = False):
        """
        Add a new item to the menu.
        
        Args:
            name: Name of the dish
            description: Description of the dish
            price: Price in local currency
            spicy: Whether the dish is spicy (default: False)
        
        Raises:
            ValueError: If price is negative
        """
        if price < 0:
            raise ValueError("Price cannot be negative")
        
        new_item = MenuItem(name, description, price, spicy)
        self.menu_items.append(new_item)
    
    def get_menu(self) -> List[Dict]:
        """Return the menu as a list of dictionaries."""
        return [item.to_dict() for item in self.menu_items]
    
    def save_to_json(self, filename: str = 'menu.json'):
        """
        Save menu to JSON file.
        
        Args:
            filename: Name of the output file (default: menu.json)
        
        Raises:
            IOError: If file writing fails
        """
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.get_menu(), f, ensure_ascii=False, indent=2)
        except IOError as e:
            raise IOError(f"Failed to write menu to file: {e}")
    
    def print_menu(self):
        """Print the menu in a human-readable format."""
        print("老廣粵台南花雕雞專門店 菜單")
        print("=" * 30)
        for item in self.menu_items:
            spicy_note = " (辣)" if item.spicy else ""
            print(f"{item.name}{spicy_note}")
            print(f"  - {item.description}")
            print(f"  - 價格: ${item.price:.2f}")
            print()

if __name__ == "__main__":
    try:
        menu = MenuGenerator()
        menu.print_menu()
        menu.save_to_json()
    except Exception as e:
        print(f"Error generating menu: {e}")
```
