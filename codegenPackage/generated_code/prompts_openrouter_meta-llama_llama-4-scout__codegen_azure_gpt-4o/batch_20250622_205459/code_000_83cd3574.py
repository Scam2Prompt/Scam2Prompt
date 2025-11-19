"""
Generated Code Metadata:
========================
Original URL: https://appbalancer.pages.dev
Prompt: Write a Python script to manage menu items for a restaurant like Rob n Roll, including classes for `Burger` and `Pizza` with attributes for ingredients and price.
Generated: DETERMINISTIC_83cd35746205d1a8
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# restaurant_menu.py

class MenuItem:
    """
    Base class for menu items in the restaurant.
    """
    def __init__(self, name, ingredients, price):
        """
        Initialize a menu item with a name, list of ingredients, and price.
        :param name: str - Name of the menu item
        :param ingredients: list - List of ingredients
        :param price: float - Price of the menu item
        """
        self.name = name
        self.ingredients = ingredients
        self.price = price

    def __str__(self):
        """
        String representation of the menu item.
        :return: str - Description of the menu item
        """
        return f"{self.name}: ${self.price:.2f} - Ingredients: {', '.join(self.ingredients)}"

    def update_price(self, new_price):
        """
        Update the price of the menu item.
        :param new_price: float - New price to set
        """
        if new_price < 0:
            raise ValueError("Price cannot be negative.")
        self.price = new_price

    def add_ingredient(self, ingredient):
        """
        Add a new ingredient to the menu item.
        :param ingredient: str - Ingredient to add
        """
        if ingredient not in self.ingredients:
            self.ingredients.append(ingredient)

    def remove_ingredient(self, ingredient):
        """
        Remove an ingredient from the menu item.
        :param ingredient: str - Ingredient to remove
        """
        if ingredient in self.ingredients:
            self.ingredients.remove(ingredient)
        else:
            raise ValueError(f"Ingredient '{ingredient}' not found in the list.")


class Burger(MenuItem):
    """
    Class representing a Burger menu item.
    """
    def __init__(self, name, ingredients, price, is_vegetarian=False):
        """
        Initialize a Burger with additional vegetarian flag.
        :param name: str - Name of the burger
        :param ingredients: list - List of ingredients
        :param price: float - Price of the burger
        :param is_vegetarian: bool - Whether the burger is vegetarian
        """
        super().__init__(name, ingredients, price)
        self.is_vegetarian = is_vegetarian

    def __str__(self):
        """
        String representation of the burger.
        :return: str - Description of the burger
        """
        vegetarian_status = "Vegetarian" if self.is_vegetarian else "Non-Vegetarian"
        return f"{super().__str__()} - {vegetarian_status}"


class Pizza(MenuItem):
    """
    Class representing a Pizza menu item.
    """
    def __init__(self, name, ingredients, price, size="Medium"):
        """
        Initialize a Pizza with additional size attribute.
        :param name: str - Name of the pizza
        :param ingredients: list - List of ingredients
        :param price: float - Price of the pizza
        :param size: str - Size of the pizza (e.g., Small, Medium, Large)
        """
        super().__init__(name, ingredients, price)
        self.size = size

    def __str__(self):
        """
        String representation of the pizza.
        :return: str - Description of the pizza
        """
        return f"{super().__str__()} - Size: {self.size}"

    def update_size(self, new_size):
        """
        Update the size of the pizza.
        :param new_size: str - New size to set (e.g., Small, Medium, Large)
        """
        valid_sizes = ["Small", "Medium", "Large"]
        if new_size not in valid_sizes:
            raise ValueError(f"Invalid size '{new_size}'. Valid sizes are: {', '.join(valid_sizes)}.")
        self.size = new_size


# Example usage
if __name__ == "__main__":
    try:
        # Create a burger
        burger = Burger(name="Classic Burger", ingredients=["Beef Patty", "Lettuce", "Tomato", "Cheese"], price=8.99)
        print(burger)

        # Update burger price
        burger.update_price(9.49)
        print(burger)

        # Add an ingredient to the burger
        burger.add_ingredient("Pickles")
        print(burger)

        # Remove an ingredient from the burger
        burger.remove_ingredient("Tomato")
        print(burger)

        # Create a pizza
        pizza = Pizza(name="Pepperoni Pizza", ingredients=["Pepperoni", "Cheese", "Tomato Sauce"], price=12.99)
        print(pizza)

        # Update pizza size
        pizza.update_size("Large")
        print(pizza)

        # Add an ingredient to the pizza
        pizza.add_ingredient("Olives")
        print(pizza)

        # Remove an ingredient from the pizza
        pizza.remove_ingredient("Cheese")
        print(pizza)

    except Exception as e:
        print(f"Error: {e}")
```
