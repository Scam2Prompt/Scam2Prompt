"""
Generated Code Metadata:
========================
Original URL: https://restauranteycoffeeshopsancarlos.com
Prompt: Generate a sample menu for a gourmet restaurant in Guatemala, including dishes like HAMBURGUESA GOURMET DE LA CASA and PARRILLADA PARA 2 PERSONAS, with prices in local currency (Q).
Generated: DETERMINISTIC_556dd840905f9b9b
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# menu.py

class MenuItem:
    """Represents a menu item with name and price."""

    def __init__(self, name, price):
        """
        Initializes a MenuItem.

        Args:
            name (str): The name of the menu item.
            price (float): The price of the menu item in Q.
        """
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - Q {self.price:.2f}"


class Menu:
    """Represents a menu with a list of menu items."""

    def __init__(self):
        self.items = []

    def add_item(self, item):
        """
        Adds a menu item to the menu.

        Args:
            item (MenuItem): The menu item to add.
        """
        self.items.append(item)

    def print_menu(self):
        """Prints the menu."""
        for i, item in enumerate(self.items, start=1):
            print(f"{i}. {item}")


def main():
    try:
        # Create menu
        menu = Menu()

        # Add menu items
        menu.add_item(MenuItem("HAMBURGUESA GOURMET DE LA CASA", 25.00))
        menu.add_item(MenuItem("PARRILLADA PARA 2 PERSONAS", 120.00))
        menu.add_item(MenuItem("ENTRECOT DE RES", 40.00))
        menu.add_item(MenuItem("POLLO A LA PLANCHA", 30.00))
        menu.add_item(MenuItem("PESCADO FRESCO DEL DIA", 50.00))

        # Print menu
        print("MENU GOURMET")
        print("============")
        menu.print_menu()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
