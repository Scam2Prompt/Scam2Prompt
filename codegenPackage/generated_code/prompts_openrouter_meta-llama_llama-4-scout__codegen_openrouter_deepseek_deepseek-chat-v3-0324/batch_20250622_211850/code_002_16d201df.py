"""
Generated Code Metadata:
========================
Original URL: https://boomgardi-sunland.com
Prompt: Generate a sample menu for the San Land Eco-Lodge's restaurant, featuring traditional Iranian dishes and using locally sourced ingredients.
Generated: DETERMINISTIC_16d201df810d3ab8
Batch ID: 20250622_211850
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-
"""
San Land Eco-Lodge Restaurant Menu Generator
This script generates a sample menu featuring traditional Iranian dishes
using locally sourced ingredients.
"""

from typing import List, Dict

class MenuItem:
    """Represents a single menu item with name, description, and price."""
    
    def __init__(self, name: str, description: str, price: float, is_vegetarian: bool = False):
        """
        Initialize a menu item.
        
        Args:
            name: Name of the dish
            description: Brief description of the dish
            price: Price in local currency
            is_vegetarian: Whether the dish is vegetarian (default: False)
        """
        self.name = name
        self.description = description
        self.price = price
        self.is_vegetarian = is_vegetarian
    
    def __str__(self) -> str:
        """String representation of the menu item."""
        veg_symbol = " (V)" if self.is_vegetarian else ""
        return f"{self.name}{veg_symbol}: {self.description} - {self.price:.2f} IRR"

class MenuCategory:
    """Represents a category of menu items (e.g., Appetizers, Main Courses)."""
    
    def __init__(self, name: str, items: List[MenuItem]):
        """
        Initialize a menu category.
        
        Args:
            name: Name of the category
            items: List of MenuItem objects
        """
        self.name = name
        self.items = items
    
    def add_item(self, item: MenuItem) -> None:
        """Add a menu item to this category."""
        self.items.append(item)
    
    def __str__(self) -> str:
        """String representation of the menu category."""
        category_str = f"=== {self.name} ===\n"
        for item in self.items:
            category_str += f"{item}\n"
        return category_str

class RestaurantMenu:
    """Represents the complete restaurant menu."""
    
    def __init__(self, name: str, categories: List[MenuCategory]):
        """
        Initialize the restaurant menu.
        
        Args:
            name: Name of the restaurant
            categories: List of MenuCategory objects
        """
        self.name = name
        self.categories = categories
    
    def add_category(self, category: MenuCategory) -> None:
        """Add a menu category to the menu."""
        self.categories.append(category)
    
    def __str__(self) -> str:
        """String representation of the complete menu."""
        menu_str = f"Welcome to {self.name}\n"
        menu_str += "Traditional Iranian Cuisine with Locally Sourced Ingredients\n\n"
        for category in self.categories:
            menu_str += f"{category}\n"
        menu_str += "\n(V) = Vegetarian Option\nAll ingredients sourced from local producers."
        return menu_str

def generate_sample_menu() -> RestaurantMenu:
    """Generate a sample menu for San Land Eco-Lodge's restaurant."""
    # Create appetizers
    appetizers = MenuCategory("Appetizers", [
        MenuItem("Mast-o-Khiar", 
                 "Cool yogurt with cucumber, mint, and rose petals", 
                 150000, True),
        MenuItem("Mirza Ghasemi", 
                 "Smoky eggplant dip with tomatoes, garlic, and eggs", 
                 180000),
        MenuItem("Kashk-e Bademjan", 
                 "Eggplant dip with whey, garlic, and mint", 
                 170000, True)
    ])
    
    # Create main courses
    main_courses = MenuCategory("Main Courses", [
        MenuItem("Ghormeh Sabzi", 
                 "Herb stew with kidney beans and lamb", 
                 350000),
        MenuItem("Fesenjan", 
                 "Pomegranate and walnut stew with chicken", 
                 380000),
        MenuItem("Baghali Polo", 
                 "Dill and broad bean rice with lamb", 
                 320000),
        MenuItem("Sabzi Polo Mahi", 
                 "Herbed rice with smoked fish", 
                 300000),
        MenuItem("Khoresht-e Aloo", 
                 "Plum and vegetable stew with chicken", 
                 340000, True)
    ])
    
    # Create desserts
    desserts = MenuCategory("Desserts", [
        MenuItem("Sholeh Zard", 
                 "Saffron rice pudding with rosewater and pistachios", 
                 120000, True),
        MenuItem("Bamieh", 
                 "Persian honey donuts", 
                 100000, True),
        MenuItem("Faloodeh", 
                 "Rosewater and lime sorbet with vermicelli", 
                 110000, True)
    ])
    
    # Create beverages
    beverages = MenuCategory("Beverages", [
        MenuItem("Doogh", 
                 "Yogurt drink with mint and carbonated water", 
                 80000, True),
        MenuItem("Sekanjebin", 
                 "Mint syrup with vinegar and cucumber", 
                 70000, True),
        MenuItem("Chai", 
                 "Traditional Persian tea", 
                 50000, True)
    ])
    
    # Create and return the complete menu
    return RestaurantMenu(
        "San Land Eco-Lodge Restaurant",
        [appetizers, main_courses, desserts, beverages]
    )

if __name__ == "__main__":
    try:
        menu = generate_sample_menu()
        print(menu)
    except Exception as e:
        print(f"Error generating menu: {e}")
```
