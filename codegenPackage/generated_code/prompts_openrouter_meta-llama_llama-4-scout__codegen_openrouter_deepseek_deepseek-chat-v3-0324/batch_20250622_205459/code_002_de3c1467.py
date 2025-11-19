"""
Generated Code Metadata:
========================
Original URL: https://pancakesvvap.sentinelresponse.com
Prompt: Generate a sample menu for a restaurant like Brownstone Pancake Factory, including sections for pancakes, breakfast, brunch, lunch, salads, and desserts.
Generated: DETERMINISTIC_de3c146722deb109
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class MenuItem:
    """Class to represent a menu item with name, description, and price."""
    
    def __init__(self, name: str, description: str, price: float):
        """
        Initialize a menu item.
        
        Args:
            name: Name of the item
            description: Description of the item
            price: Price in USD
        """
        self.name = name
        self.description = description
        self.price = price
    
    def __str__(self) -> str:
        """Return formatted string representation of menu item."""
        return f"{self.name} - ${self.price:.2f}\n   {self.description}"

class MenuCategory:
    """Class to represent a menu category containing multiple items."""
    
    def __init__(self, name: str):
        """Initialize a menu category with a name."""
        self.name = name
        self.items = []
    
    def add_item(self, item: MenuItem) -> None:
        """Add a menu item to this category."""
        self.items.append(item)
    
    def __str__(self) -> str:
        """Return formatted string representation of menu category."""
        category_str = f"=== {self.name.upper()} ===\n"
        for item in self.items:
            category_str += f"{item}\n"
        return category_str

class RestaurantMenu:
    """Class to represent a complete restaurant menu."""
    
    def __init__(self, restaurant_name: str):
        """Initialize a restaurant menu with name and empty categories."""
        self.restaurant_name = restaurant_name
        self.categories = {}
    
    def add_category(self, category_name: str) -> None:
        """Add a new category to the menu."""
        if category_name not in self.categories:
            self.categories[category_name] = MenuCategory(category_name)
    
    def add_item_to_category(self, category_name: str, item: MenuItem) -> None:
        """Add an item to a specific category."""
        if category_name not in self.categories:
            self.add_category(category_name)
        self.categories[category_name].add_item(item)
    
    def __str__(self) -> str:
        """Return formatted string representation of the entire menu."""
        menu_str = f"===== {self.restaurant_name.upper()} MENU =====\n\n"
        for category in self.categories.values():
            menu_str += f"{category}\n"
        return menu_str

def create_sample_menu() -> RestaurantMenu:
    """Create and return a sample menu for a pancake restaurant."""
    menu = RestaurantMenu("Brownstone Pancake Factory")
    
    # Pancakes Category
    menu.add_item_to_category("Pancakes", 
        MenuItem("Classic Buttermilk", "Fluffy buttermilk pancakes served with butter and maple syrup", 8.99))
    menu.add_item_to_category("Pancakes", 
        MenuItem("Blueberry Bliss", "Buttermilk pancakes stuffed with fresh blueberries", 10.99))
    menu.add_item_to_category("Pancakes", 
        MenuItem("Chocolate Chip Delight", "Pancakes loaded with chocolate chips", 11.49))
    menu.add_item_to_category("Pancakes", 
        MenuItem("Red Velvet", "Rich red velvet pancakes with cream cheese drizzle", 12.99))
    
    # Breakfast Category
    menu.add_item_to_category("Breakfast", 
        MenuItem("Two Eggs Any Style", "Two eggs cooked to order with toast and home fries", 9.99))
    menu.add_item_to_category("Breakfast", 
        MenuItem("Eggs Benedict", "English muffin topped with Canadian bacon, poached eggs, and hollandaise", 13.99))
    menu.add_item_to_category("Breakfast", 
        MenuItem("Breakfast Burrito", "Scrambled eggs, cheese, potatoes, and choice of meat wrapped in a tortilla", 11.99))
    menu.add_item_to_category("Breakfast", 
        MenuItem("Avocado Toast", "Sourdough toast with smashed avocado, cherry tomatoes, and feta", 10.49))
    
    # Brunch Category
    menu.add_item_to_category("Brunch", 
        MenuItem("Chicken & Waffles", "Crispy fried chicken served atop Belgian waffles", 15.99))
    menu.add_item_to_category("Brunch", 
        MenuItem("Steak & Eggs", "8oz sirloin steak with two eggs any style and breakfast potatoes", 18.99))
    menu.add_item_to_category("Brunch", 
        MenuItem("Smoked Salmon Platter", "Smoked salmon with bagel, cream cheese, capers, and onions", 16.49))
    menu.add_item_to_category("Brunch", 
        MenuItem("Vegetable Frittata", "Fluffy egg frittata with seasonal vegetables and goat cheese", 12.99))
    
    # Lunch Category
    menu.add_item_to_category("Lunch", 
        MenuItem("Classic Burger", "1/2 lb beef patty with lettuce, tomato, onion, and pickles", 12.99))
    menu.add_item_to_category("Lunch", 
        MenuItem("Grilled Chicken Sandwich", "Marinated chicken breast with avocado and chipotle mayo", 13.49))
    menu.add_item_to_category("Lunch", 
        MenuItem("Turkey Club", "Triple-decker sandwich with turkey, bacon, lettuce, and tomato", 11.99))
    menu.add_item_to_category("Lunch", 
        MenuItem("Grilled Cheese & Tomato Soup", "Classic comfort food combo", 9.99))
    
    # Salads Category
    menu.add_item_to_category("Salads", 
        MenuItem("Caesar Salad", "Romaine lettuce, croutons, parmesan, and Caesar dressing", 10.99))
    menu.add_item_to_category("Salads", 
        MenuItem("Cobb Salad", "Mixed greens with chicken, bacon, egg, avocado, and blue cheese", 14.99))
    menu.add_item_to_category("Salads", 
        MenuItem("Quinoa Bowl", "Quinoa with roasted vegetables, chickpeas, and tahini dressing", 12.49))
    menu.add_item_to_category("Salads", 
        MenuItem("Strawberry Spinach", "Fresh spinach with strawberries, almonds, and balsamic vinaigrette", 11.49))
    
    # Desserts Category
    menu.add_item_to_category("Desserts", 
        MenuItem("Chocolate Lava Cake", "Warm chocolate cake with a molten center and vanilla ice cream", 8.99))
    menu.add_item_to_category("Desserts", 
        MenuItem("New York Cheesecake", "Classic cheesecake with strawberry topping", 7.99))
    menu.add_item_to_category("Desserts", 
        MenuItem("Apple Pie", "Homemade apple pie with cinnamon and a flaky crust", 6.99))
    menu.add_item_to_category("Desserts", 
        MenuItem("Ice Cream Sundae", "Vanilla ice cream with hot fudge, whipped cream, and a cherry", 6.49))
    
    return menu

if __name__ == "__main__":
    sample_menu = create_sample_menu()
    print(sample_menu)
```
