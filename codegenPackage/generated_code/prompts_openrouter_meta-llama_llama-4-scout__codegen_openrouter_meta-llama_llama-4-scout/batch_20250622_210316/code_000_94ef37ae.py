"""
Generated Code Metadata:
========================
Original URL: https://mollinari.com.pl
Prompt: Write a Python script to create a restaurant menu like Mollinari's, including pizza and cocktail options, with prices and daily operating hours.
Generated: DETERMINISTIC_94ef37ae2ad452e6
Batch ID: 20250622_210316
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
    """Base class for menu items."""

    def __init__(self, name, price):
        """
        Initialize a menu item.

        Args:
            name (str): Name of the menu item.
            price (float): Price of the menu item.
        """
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"


class Pizza(MenuItem):
    """Class for pizza menu items."""

    def __init__(self, name, price, toppings):
        """
        Initialize a pizza menu item.

        Args:
            name (str): Name of the pizza.
            price (float): Price of the pizza.
            toppings (list): List of toppings.
        """
        super().__init__(name, price)
        self.toppings = toppings

    def __str__(self):
        toppings_str = ", ".join(self.toppings)
        return f"{self.name} Pizza: ${self.price:.2f} - Toppings: {toppings_str}"


class Cocktail(MenuItem):
    """Class for cocktail menu items."""

    def __init__(self, name, price, ingredients):
        """
        Initialize a cocktail menu item.

        Args:
            name (str): Name of the cocktail.
            price (float): Price of the cocktail.
            ingredients (list): List of ingredients.
        """
        super().__init__(name, price)
        self.ingredients = ingredients

    def __str__(self):
        ingredients_str = ", ".join(self.ingredients)
        return f"{self.name}: ${self.price:.2f} - Ingredients: {ingredients_str}"


class Restaurant:
    """Class for restaurant."""

    def __init__(self, name, operating_hours):
        """
        Initialize a restaurant.

        Args:
            name (str): Name of the restaurant.
            operating_hours (str): Daily operating hours.
        """
        self.name = name
        self.operating_hours = operating_hours
        self.menu = {"pizzas": [], "cocktails": []}

    def add_pizza(self, pizza):
        """Add a pizza to the menu."""
        self.menu["pizzas"].append(pizza)

    def add_cocktail(self, cocktail):
        """Add a cocktail to the menu."""
        self.menu["cocktails"].append(cocktail)

    def display_menu(self):
        """Display the restaurant menu."""
        print(f"**{self.name} Menu**")
        print(f"Operating Hours: {self.operating_hours}")
        print("\n**Pizzas**")
        for pizza in self.menu["pizzas"]:
            print(pizza)
        print("\n**Cocktails**")
        for cocktail in self.menu["cocktails"]:
            print(cocktail)


def main():
    try:
        # Create restaurant
        restaurant = Restaurant("Mollinari's", "11am - 10pm")

        # Create pizzas
        margherita = Pizza("Margherita", 14.99, ["Fresh Tomatoes", "Mozzarella", "Basil"])
        pepperoni = Pizza("Pepperoni", 16.99, ["Pepperoni", "Mozzarella", "Tomato Sauce"])
        vegetarian = Pizza("Vegetarian", 15.99, ["Mushrooms", "Onions", "Bell Peppers", "Mozzarella"])

        # Create cocktails
        old_fashioned = Cocktail("Old Fashioned", 12.99, ["Bourbon", "Sugar", "Bitters"])
        margarita = Cocktail("Margarita", 10.99, ["Tequila", "Lime Juice", "Triple Sec"])
        cosmopolitan = Cocktail("Cosmopolitan", 11.99, ["Vodka", "Lime Juice", "Triple Sec", "Cranberry Juice"])

        # Add pizzas and cocktails to menu
        restaurant.add_pizza(margherita)
        restaurant.add_pizza(pepperoni)
        restaurant.add_pizza(vegetarian)
        restaurant.add_cocktail(old_fashioned)
        restaurant.add_cocktail(margarita)
        restaurant.add_cocktail(cosmopolitan)

        # Display menu
        restaurant.display_menu()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
