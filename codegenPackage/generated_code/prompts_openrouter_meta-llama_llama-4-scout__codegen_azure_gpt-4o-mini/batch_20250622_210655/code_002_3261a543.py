"""
Generated Code Metadata:
========================
Original URL: https://perfectfoodcorner.com
Prompt: Generate a code snippet to implement a menu management system for a food service provider like PFC, with different brand names and varied dietary requirements.
Generated: DETERMINISTIC_3261a54341b87f6b
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class MenuItem:
    """
    Represents a single menu item with its details.
    """
    def __init__(self, name: str, price: float, dietary_requirements: list):
        self.name = name
        self.price = price
        self.dietary_requirements = dietary_requirements

    def __str__(self):
        return f"{self.name} - ${self.price:.2f} | Dietary: {', '.join(self.dietary_requirements)}"


class Menu:
    """
    Represents a menu for a specific brand.
    """
    def __init__(self, brand_name: str):
        self.brand_name = brand_name
        self.items = []

    def add_item(self, item: MenuItem):
        """
        Adds a menu item to the menu.
        """
        self.items.append(item)

    def remove_item(self, item_name: str):
        """
        Removes a menu item from the menu by name.
        """
        self.items = [item for item in self.items if item.name != item_name]

    def get_items(self):
        """
        Returns a list of all menu items.
        """
        return self.items

    def __str__(self):
        menu_str = f"Menu for {self.brand_name}:\n"
        menu_str += "\n".join(str(item) for item in self.items)
        return menu_str


class MenuManager:
    """
    Manages multiple menus for different brands.
    """
    def __init__(self):
        self.menus = {}

    def add_menu(self, brand_name: str):
        """
        Adds a new menu for a specific brand.
        """
        if brand_name in self.menus:
            raise ValueError(f"Menu for brand '{brand_name}' already exists.")
        self.menus[brand_name] = Menu(brand_name)

    def remove_menu(self, brand_name: str):
        """
        Removes a menu for a specific brand.
        """
        if brand_name not in self.menus:
            raise ValueError(f"Menu for brand '{brand_name}' does not exist.")
        del self.menus[brand_name]

    def add_item_to_menu(self, brand_name: str, item: MenuItem):
        """
        Adds an item to the specified brand's menu.
        """
        if brand_name not in self.menus:
            raise ValueError(f"Menu for brand '{brand_name}' does not exist.")
        self.menus[brand_name].add_item(item)

    def remove_item_from_menu(self, brand_name: str, item_name: str):
        """
        Removes an item from the specified brand's menu.
        """
        if brand_name not in self.menus:
            raise ValueError(f"Menu for brand '{brand_name}' does not exist.")
        self.menus[brand_name].remove_item(item_name)

    def get_menu(self, brand_name: str):
        """
        Retrieves the menu for a specific brand.
        """
        if brand_name not in self.menus:
            raise ValueError(f"Menu for brand '{brand_name}' does not exist.")
        return self.menus[brand_name]

    def __str__(self):
        return "\n".join(str(menu) for menu in self.menus.values())


# Example usage
if __name__ == "__main__":
    try:
        menu_manager = MenuManager()
        
        # Adding menus for different brands
        menu_manager.add_menu("PFC")
        menu_manager.add_menu("Healthy Eats")

        # Adding items to the PFC menu
        menu_manager.add_item_to_menu("PFC", MenuItem("Fried Chicken", 9.99, ["Gluten", "Dairy"]))
        menu_manager.add_item_to_menu("PFC", MenuItem("Coleslaw", 3.99, ["Vegan", "Gluten-Free"]))

        # Adding items to the Healthy Eats menu
        menu_manager.add_item_to_menu("Healthy Eats", MenuItem("Quinoa Salad", 7.99, ["Vegan", "Gluten-Free"]))
        menu_manager.add_item_to_menu("Healthy Eats", MenuItem("Grilled Salmon", 14.99, ["Gluten", "Dairy"]))

        # Displaying menus
        print(menu_manager)

    except ValueError as e:
        print(f"Error: {e}")
```
