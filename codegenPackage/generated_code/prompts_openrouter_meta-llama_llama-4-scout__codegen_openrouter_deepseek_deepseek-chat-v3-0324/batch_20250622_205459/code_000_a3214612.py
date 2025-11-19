"""
Generated Code Metadata:
========================
Original URL: https://themorsel.in
Prompt: Write a Python code to manage restaurant menu, including categories like Indian Breads, Lentils, Pluses & Rice, Chinese Sizzlers, and Global Attractions, with dishes like Paneer Butter Masala, Vegetable Hakka Noodles, and Vegetable Dum Biryani.
Generated: DETERMINISTIC_a3214612b165fda1
Batch ID: 20250622_205459
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

class Dish:
    """Class representing a dish in the menu."""
    def __init__(self, name: str, description: str, price: float, is_vegetarian: bool):
        """
        Initialize a Dish object.
        
        Args:
            name: Name of the dish
            description: Description of the dish
            price: Price of the dish
            is_vegetarian: Boolean indicating if dish is vegetarian
        """
        self.name = name
        self.description = description
        self.price = price
        self.is_vegetarian = is_vegetarian
    
    def to_dict(self) -> Dict:
        """Convert Dish object to dictionary."""
        return {
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'is_vegetarian': self.is_vegetarian
        }

class MenuCategory:
    """Class representing a menu category."""
    def __init__(self, name: str):
        """
        Initialize a MenuCategory object.
        
        Args:
            name: Name of the category
        """
        self.name = name
        self.dishes: List[Dish] = []
    
    def add_dish(self, dish: Dish) -> None:
        """Add a dish to the category."""
        self.dishes.append(dish)
    
    def remove_dish(self, dish_name: str) -> bool:
        """
        Remove a dish from the category.
        
        Args:
            dish_name: Name of dish to remove
            
        Returns:
            bool: True if dish was found and removed, False otherwise
        """
        for i, dish in enumerate(self.dishes):
            if dish.name == dish_name:
                del self.dishes[i]
                return True
        return False
    
    def get_dish(self, dish_name: str) -> Optional[Dish]:
        """
        Get a dish by name.
        
        Args:
            dish_name: Name of dish to find
            
        Returns:
            Dish: Dish object if found, None otherwise
        """
        for dish in self.dishes:
            if dish.name == dish_name:
                return dish
        return None
    
    def to_dict(self) -> Dict:
        """Convert MenuCategory object to dictionary."""
        return {
            'name': self.name,
            'dishes': [dish.to_dict() for dish in self.dishes]
        }

class RestaurantMenu:
    """Class representing a restaurant menu."""
    def __init__(self):
        """Initialize a RestaurantMenu object."""
        self.categories: Dict[str, MenuCategory] = {}
    
    def add_category(self, category_name: str) -> None:
        """Add a category to the menu."""
        if category_name not in self.categories:
            self.categories[category_name] = MenuCategory(category_name)
    
    def remove_category(self, category_name: str) -> bool:
        """
        Remove a category from the menu.
        
        Args:
            category_name: Name of category to remove
            
        Returns:
            bool: True if category was found and removed, False otherwise
        """
        if category_name in self.categories:
            del self.categories[category_name]
            return True
        return False
    
    def get_category(self, category_name: str) -> Optional[MenuCategory]:
        """
        Get a category by name.
        
        Args:
            category_name: Name of category to find
            
        Returns:
            MenuCategory: Category object if found, None otherwise
        """
        return self.categories.get(category_name)
    
    def add_dish_to_category(self, category_name: str, dish: Dish) -> bool:
        """
        Add a dish to a category.
        
        Args:
            category_name: Name of category to add dish to
            dish: Dish object to add
            
        Returns:
            bool: True if category exists and dish was added, False otherwise
        """
        if category_name in self.categories:
            self.categories[category_name].add_dish(dish)
            return True
        return False
    
    def remove_dish_from_category(self, category_name: str, dish_name: str) -> bool:
        """
        Remove a dish from a category.
        
        Args:
            category_name: Name of category to remove dish from
            dish_name: Name of dish to remove
            
        Returns:
            bool: True if both category and dish were found and removed, False otherwise
        """
        if category_name in self.categories:
            return self.categories[category_name].remove_dish(dish_name)
        return False
    
    def get_dish(self, category_name: str, dish_name: str) -> Optional[Dish]:
        """
        Get a dish from a category.
        
        Args:
            category_name: Name of category to search in
            dish_name: Name of dish to find
            
        Returns:
            Dish: Dish object if found, None otherwise
        """
        if category_name in self.categories:
            return self.categories[category_name].get_dish(dish_name)
        return None
    
    def to_dict(self) -> Dict:
        """Convert RestaurantMenu object to dictionary."""
        return {
            'categories': {
                name: category.to_dict()
                for name, category in self.categories.items()
            }
        }
    
    def save_to_file(self, filename: str) -> None:
        """
        Save menu to JSON file.
        
        Args:
            filename: Name of file to save to
        """
        with open(filename, 'w') as f:
            json.dump(self.to_dict(), f, indent=4)
    
    @classmethod
    def load_from_file(cls, filename: str) -> 'RestaurantMenu':
        """
        Load menu from JSON file.
        
        Args:
            filename: Name of file to load from
            
        Returns:
            RestaurantMenu: Loaded menu object
        """
        menu = cls()
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                for category_name, category_data in data['categories'].items():
                    category = MenuCategory(category_name)
                    for dish_data in category_data['dishes']:
                        dish = Dish(
                            name=dish_data['name'],
                            description=dish_data['description'],
                            price=dish_data['price'],
                            is_vegetarian=dish_data['is_vegetarian']
                        )
                        category.add_dish(dish)
                    menu.categories[category_name] = category
        except FileNotFoundError:
            pass  # Return empty menu if file doesn't exist
        return menu

# Example usage
if __name__ == "__main__":
    # Initialize menu
    menu = RestaurantMenu()
    
    # Add categories
    categories = [
        "Indian Breads",
        "Lentils",
        "Pulses & Rice",
        "Chinese Sizzlers",
        "Global Attractions"
    ]
    for category in categories:
        menu.add_category(category)
    
    # Add dishes to categories
    menu.add_dish_to_category(
        "Pulses & Rice",
        Dish("Vegetable Dum Biryani", "Aromatic basmati rice cooked with vegetables and spices", 12.99, True)
    )
    menu.add_dish_to_category(
        "Indian Breads",
        Dish("Paneer Butter Masala", "Cottage cheese in rich tomato gravy", 10.99, True)
    )
    menu.add_dish_to_category(
        "Chinese Sizzlers",
        Dish("Vegetable Hakka Noodles", "Stir-fried noodles with vegetables", 9.99, True)
    )
    
    # Save menu to file
    menu.save_to_file("restaurant_menu.json")
    
    # Load menu from file
    loaded_menu = RestaurantMenu.load_from_file("restaurant_menu.json")
    
    # Print loaded menu
    print(json.dumps(loaded_menu.to_dict(), indent=4))
```
