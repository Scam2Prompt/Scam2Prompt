"""
Generated Code Metadata:
========================
Original URL: https://andiasfrozenyogurt.com
Prompt: Write a Python script to manage inventory for a frozen yogurt shop with multiple locations like Andias Frozen Yogurt, including their 100+ toppings and 14 unique flavors.
Generated: DETERMINISTIC_70462908aa494c4f
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# frozen_yogurt_inventory.py

class FrozenYogurtShop:
    def __init__(self, name):
        """
        Initialize a FrozenYogurtShop object.

        Args:
            name (str): Name of the frozen yogurt shop.
        """
        self.name = name
        self.flavors = {}
        self.toppings = set()

    def add_flavor(self, flavor_name, quantity):
        """
        Add a flavor to the shop's inventory.

        Args:
            flavor_name (str): Name of the flavor.
            quantity (int): Quantity of the flavor in stock.

        Raises:
            ValueError: If quantity is less than 0.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be less than 0")
        self.flavors[flavor_name] = quantity

    def remove_flavor(self, flavor_name):
        """
        Remove a flavor from the shop's inventory.

        Args:
            flavor_name (str): Name of the flavor to remove.

        Raises:
            KeyError: If the flavor does not exist in the inventory.
        """
        if flavor_name not in self.flavors:
            raise KeyError(f"Flavor '{flavor_name}' does not exist")
        del self.flavors[flavor_name]

    def update_flavor_quantity(self, flavor_name, quantity):
        """
        Update the quantity of a flavor in the shop's inventory.

        Args:
            flavor_name (str): Name of the flavor to update.
            quantity (int): New quantity of the flavor.

        Raises:
            KeyError: If the flavor does not exist in the inventory.
            ValueError: If quantity is less than 0.
        """
        if flavor_name not in self.flavors:
            raise KeyError(f"Flavor '{flavor_name}' does not exist")
        if quantity < 0:
            raise ValueError("Quantity cannot be less than 0")
        self.flavors[flavor_name] = quantity

    def add_topping(self, topping_name):
        """
        Add a topping to the shop's inventory.

        Args:
            topping_name (str): Name of the topping.
        """
        self.toppings.add(topping_name)

    def remove_topping(self, topping_name):
        """
        Remove a topping from the shop's inventory.

        Args:
            topping_name (str): Name of the topping to remove.

        Raises:
            KeyError: If the topping does not exist in the inventory.
        """
        if topping_name not in self.toppings:
            raise KeyError(f"Topping '{topping_name}' does not exist")
        self.toppings.remove(topping_name)


class FrozenYogurtInventory:
    def __init__(self):
        """
        Initialize a FrozenYogurtInventory object.
        """
        self.shops = {}

    def add_shop(self, shop_name):
        """
        Add a frozen yogurt shop to the inventory.

        Args:
            shop_name (str): Name of the shop.
        """
        self.shops[shop_name] = FrozenYogurtShop(shop_name)

    def get_shop(self, shop_name):
        """
        Get a frozen yogurt shop from the inventory.

        Args:
            shop_name (str): Name of the shop.

        Returns:
            FrozenYogurtShop: The shop object.

        Raises:
            KeyError: If the shop does not exist in the inventory.
        """
        if shop_name not in self.shops:
            raise KeyError(f"Shop '{shop_name}' does not exist")
        return self.shops[shop_name]


def main():
    # Create an inventory
    inventory = FrozenYogurtInventory()

    # Add shops
    andias = "Andias Frozen Yogurt"
    inventory.add_shop(andias)
    shop = inventory.get_shop(andias)

    # Add flavors
    flavors = [
        "Vanilla",
        "Chocolate",
        "Strawberry",
        "Mango",
        "Pineapple",
        "Cookies and Cream",
        "Mint Chocolate Chip",
        "Peanut Butter Cup",
        "Rocky Road",
        "S'mores",
        "Peanut Butter",
        "Banana",
        "Caramel",
        "Coffee",
    ]
    for flavor in flavors:
        shop.add_flavor(flavor, 100)

    # Add toppings
    toppings = [
        "Sprinkles",
        "Hot Fudge",
        "Caramel Sauce",
        "Whipped Cream",
        "Chopped Nuts",
        "Chocolate Chips",
        "Coconut Flakes",
        "Candy Pieces",
        "Marshmallows",
        "Cookie Dough",
        "Peanut Butter Cups",
        "M&M's",
        "Crushed Oreos",
        "Crushed Peanuts",
        "Toffee Bits",
        "Butterscotch Chips",
        "Pecans",
        "Walnuts",
        "Pistachios",
        "Almonds",
        "Cinnamon",
        "Cocoa Powder",
        "Sea Salt",
        "Caramelized Bananas",
        "Marshmallow Creme",
        "Fruit Syrup",
        "Peanut Butter Sauce",
        "Honey",
        "Maple Syrup",
        "Agave Nectar",
        "Fresh Fruit",
        "Coconut Flakes",
        "Chia Seeds",
        "Granola",
        "Cereal",
        "Candy Canes",
        "Gummy Bears",
        "Gummy Worms",
        "Licorice",
        "Tootsie Rolls",
        "Fruit Roll-Ups",
        "Pop Rocks",
        "Crushed Candy Canes",
        "Sprinkle Chips",
        "Cookie Crunch",
        "Peanut Butter Chips",
        "Butterscotch Chips",
        "Cinnamon Sugar",
        "Cocoa Nibs",
        "Dried Fruit",
        "Coconut Water",
        "Pineapple Chunks",
        "Mandarin Oranges",
        "Pecans halves",
        "Walnuts halves",
    ]
    for topping in toppings:
        shop.add_topping(topping)

    # Print shop inventory
    print(f"Shop: {shop.name}")
    print("Flavors:")
    for flavor, quantity in shop.flavors.items():
        print(f"- {flavor}: {quantity}")
    print("Toppings:")
    for topping in shop.toppings:
        print(f"- {topping}")


if __name__ == "__main__":
    main()
```
