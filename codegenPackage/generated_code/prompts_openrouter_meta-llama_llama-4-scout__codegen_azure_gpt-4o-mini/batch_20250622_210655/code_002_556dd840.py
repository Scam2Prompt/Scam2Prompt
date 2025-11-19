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
class MenuItem:
    """
    Class to represent a menu item in the restaurant.
    """

    def __init__(self, name: str, description: str, price: float):
        """
        Initializes a new menu item.

        :param name: The name of the menu item.
        :param description: A brief description of the menu item.
        :param price: The price of the menu item in Quetzales (Q).
        """
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        """
        Returns a string representation of the menu item.
        """
        return f"{self.name} - {self.description} (Q{self.price:.2f})"


class Menu:
    """
    Class to represent a restaurant menu.
    """

    def __init__(self):
        """
        Initializes a new menu with an empty list of items.
        """
        self.items = []

    def add_item(self, item: MenuItem):
        """
        Adds a new item to the menu.

        :param item: An instance of MenuItem to be added to the menu.
        """
        if not isinstance(item, MenuItem):
            raise ValueError("item must be an instance of MenuItem")
        self.items.append(item)

    def display_menu(self):
        """
        Displays the menu items in a formatted manner.
        """
        print("Gourmet Restaurant Menu\n" + "=" * 30)
        for item in self.items:
            print(item)
        print("=" * 30)


def main():
    """
    Main function to create and display the restaurant menu.
    """
    try:
        # Create a new menu
        restaurant_menu = Menu()

        # Add menu items
        restaurant_menu.add_item(MenuItem("HAMBURGUESA GOURMET DE LA CASA",
                                            "Delicious gourmet burger with special sauce and fresh ingredients.",
                                            85.00))
        restaurant_menu.add_item(MenuItem("PARRILLADA PARA 2 PERSONAS",
                                            "A mixed grill platter for two, featuring various meats and sides.",
                                            250.00))
        restaurant_menu.add_item(MenuItem("ENSALADA FRESCA",
                                            "A refreshing salad with seasonal vegetables and a light dressing.",
                                            45.00))
        restaurant_menu.add_item(MenuItem("POSTRE DEL DÍA",
                                            "Chef's special dessert of the day.",
                                            30.00))

        # Display the menu
        restaurant_menu.display_menu()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
