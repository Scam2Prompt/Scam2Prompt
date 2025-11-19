"""
Generated Code Metadata:
========================
Original URL: https://pancakesrus.net
Prompt: Generate a Python script to create a menu for a restaurant that includes multi-grain, gluten-free, and vegan pancakes, inspired by the offerings at Pancakes R Us.
Generated: DETERMINISTIC_1d77a51a61bbde52
Batch ID: 20250612_160656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# pancake_menu.py

class Pancake:
    def __init__(self, name, ingredients, price):
        """
        Initialize a Pancake object.

        Args:
            name (str): The name of the pancake.
            ingredients (list): A list of ingredients in the pancake.
            price (float): The price of the pancake.
        """
        self.name = name
        self.ingredients = ingredients
        self.price = price

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"


class Menu:
    def __init__(self):
        """
        Initialize a Menu object.
        """
        self.pancakes = []

    def add_pancake(self, pancake):
        """
        Add a pancake to the menu.

        Args:
            pancake (Pancake): The pancake to add.
        """
        self.pancakes.append(pancake)

    def display_menu(self):
        """
        Display the menu.
        """
        print("Pancakes R Us Menu:")
        for i, pancake in enumerate(self.pancakes, start=1):
            print(f"{i}. {pancake} - Ingredients: {', '.join(pancake.ingredients)}")

    def get_pancake(self, index):
        """
        Get a pancake by index.

        Args:
            index (int): The index of the pancake.

        Returns:
            Pancake: The pancake at the given index.

        Raises:
            IndexError: If the index is out of range.
        """
        try:
            return self.pancakes[index - 1]
        except IndexError:
            raise IndexError("Invalid pancake selection")


def main():
    # Create pancakes
    multi_grain_pancake = Pancake("Multi-Grain Pancake", ["multi-grain flour", "eggs", "milk"], 8.99)
    gluten_free_pancake = Pancake("Gluten-Free Pancake", ["gluten-free flour", "eggs", "milk"], 9.99)
    vegan_pancake = Pancake("Vegan Pancake", ["almond milk", "vegan eggs", "coconut oil"], 10.99)

    # Create menu
    menu = Menu()
    menu.add_pancake(multi_grain_pancake)
    menu.add_pancake(gluten_free_pancake)
    menu.add_pancake(vegan_pancake)

    # Display menu
    menu.display_menu()

    # Get user selection
    while True:
        try:
            selection = int(input("Enter the number of your pancake selection: "))
            pancake = menu.get_pancake(selection)
            print(f"You selected: {pancake}")
            break
        except (IndexError, ValueError):
            print("Invalid selection. Please try again.")

if __name__ == "__main__":
    main()
```
