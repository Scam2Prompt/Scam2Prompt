"""
Generated Code Metadata:
========================
Original URL: https://andiasfrozenyogurt.com
Prompt: Generate a sample menu for a frozen yogurt shop inspired by Andias Frozen Yogurt, including unique flavors and over 100 toppings, using Markdown formatting.
Generated: DETERMINISTIC_631a2d32fb5fdb09
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# frozen_yogurt_menu.py

class FrozenYogurtFlavor:
    """Represents a frozen yogurt flavor."""

    def __init__(self, name, description):
        """
        Initializes a FrozenYogurtFlavor.

        Args:
            name (str): The name of the flavor.
            description (str): A brief description of the flavor.
        """
        self.name = name
        self.description = description

class Topping:
    """Represents a topping."""

    def __init__(self, name, category):
        """
        Initializes a Topping.

        Args:
            name (str): The name of the topping.
            category (str): The category of the topping (e.g., fruit, nuts, etc.).
        """
        self.name = name
        self.category = category

class FrozenYogurtShop:
    """Represents a frozen yogurt shop."""

    def __init__(self, name):
        """
        Initializes a FrozenYogurtShop.

        Args:
            name (str): The name of the shop.
        """
        self.name = name
        self.flavors = []
        self.toppings = []

    def add_flavor(self, flavor):
        """Adds a flavor to the shop's menu."""
        self.flavors.append(flavor)

    def add_topping(self, topping):
        """Adds a topping to the shop's menu."""
        self.toppings.append(topping)

    def generate_menu(self):
        """Generates the shop's menu in Markdown formatting."""
        menu = f"# {self.name} Menu\n\n"

        ## Flavors
        menu += "## Flavors\n\n"
        for i, flavor in enumerate(self.flavors, start=1):
            menu += f"{i}. **{flavor.name}**: {flavor.description}\n"

        ## Toppings
        menu += "\n## Toppings\n\n"
        for category in set(topping.category for topping in self.toppings):
            menu += f"### {category.capitalize()}\n"
            for topping in [t for t in self.toppings if t.category == category]:
                menu += f"* {topping.name}\n"
            menu += "\n"

        return menu

def main():
    try:
        shop = FrozenYogurtShop("Andias Frozen Yogurt")

        # Add flavors
        flavors = [
            FrozenYogurtFlavor("Tropical Temptation", "A sweet and tangy blend of pineapple, mango, and coconut."),
            FrozenYogurtFlavor("Strawberry Cheesecake", "A creamy strawberry flavor with a hint of cheesecake."),
            FrozenYogurtFlavor("Mint to Be", "A refreshing peppermint flavor with dark chocolate chips."),
            FrozenYogurtFlavor("Peanut Butter Cup", "A rich peanut butter flavor with chunks of peanut butter cups."),
            FrozenYogurtFlavor("S'mores Please", "A classic campfire treat in a cup, with chocolate, marshmallows, and graham crackers."),
        ]
        for flavor in flavors:
            shop.add_flavor(flavor)

        # Add toppings
        toppings = [
            Topping("Fresh Strawberries", "fruit"),
            Topping("Blueberries", "fruit"),
            Topping("Raspberries", "fruit"),
            Topping("Blackberries", "fruit"),
            Topping("Banana Slices", "fruit"),
            Topping("Peanuts", "nuts"),
            Topping("Almonds", "nuts"),
            Topping("Walnuts", "nuts"),
            Topping("Pecans", "nuts"),
            Topping("Sprinkles", "candy"),
            Topping("Chocolate Chips", "candy"),
            Topping("Caramel Sauce", "sauces"),
            Topping("Hot Fudge", "sauces"),
            Topping("Whipped Cream", "toppings"),
            Topping("Marshmallow Creme", "toppings"),
            Topping("Cookie Dough", "toppings"),
            Topping("Candy Pieces", "toppings"),
            Topping("Coconut Flakes", "toppings"),
            Topping("Cocoa Puffs", "toppings"),
            Topping("Crushed Oreos", "toppings"),
            Topping("Crushed Peanut Butter Cookies", "toppings"),
            Topping("M&M's", "toppings"),
            Topping("Peanut Butter Cups", "toppings"),
            Topping("Banana Chips", "toppings"),
            Topping("Diced Pineapple", "toppings"),
            Topping("Diced Mango", "toppings"),
            Topping("Diced Kiwi", "toppings"),
            Topping("Cereal Pieces", "toppings"),
            Topping("Candy Cane Pieces", "toppings"),
            Topping("Pretzels", "toppings"),
            Topping("Crackers", "toppings"),
            Topping("Toffee Bits", "toppings"),
            Topping("Butterscotch Chips", "toppings"),
            Topping("Dulce de Leche", "toppings"),
            Topping("Creamy Caramel", "toppings"),
            Topping("Sea Salt", "toppings"),
            Topping("Cookie Crunch", "toppings"),
            Topping("Fruit Loops", "toppings"),
            Topping("Cinnamon Sugar", "toppings"),
            Topping("Churro Pieces", "toppings"),
            Topping("Pecan Praline", "toppings"),
            Topping("Maple Walnuts", "toppings"),
            Topping("Pistachios", "toppings"),
            Topping("Hazelnuts", "toppings"),
            Topping("Diced Apples", "toppings"),
            Topping("Diced Pears", "toppings"),
            Topping("Cranberries", "toppings"),
            Topping("Cherries", "toppings"),
            Topping("Apricots", "toppings"),
            Topping("Pineapple Upside-Down Cake", "toppings"),
            Topping("Cheesecake Pieces", "toppings"),
            Topping("Brownies", "toppings"),
            Topping("Brownie Bits", "toppings"),
            Topping("Cookie Butter", "toppings"),
            Topping("Dulce de Leche Sauce", "toppings"),
            Topping("Caramel Apple Empanada", "toppings"),
            Topping("Cinnamon Sugar Donut Holes", "toppings"),
            Topping("Fruit Roll-Ups", "toppings"),
            Topping("Granola", "toppings"),
            Topping("Oatmeal Raisin", "toppings"),
            Topping("Peanut Butter Filled Pretzels", "toppings"),
            Topping("Candy Bars", "toppings"),
            Topping("Creamy Coconut", "toppings"),
            Topping("Toasted Coconut Flakes", "toppings"),
            Topping("Cinnamon Toast Crunch", "toppings"),
            Topping("Fruity Pebbles", "toppings"),
            Topping("Golden Grahams", "toppings"),
            Topping("Candy Canes", "toppings"),
            Topping("Marshmallow Peeps", "toppings"),
            Topping("Diced Peaches", "toppings"),
            Topping("Pistachio Crunch", "toppings"),
            Topping("Cranberry Orange", "toppings"),
            Topping("Maple Bacon", "toppings"),
            Topping("S'mores Toppings", "toppings"),
            Topping("Cookie Cake Pieces", "toppings"),
            Topping("Cream Cheese Frosting", "toppings"),
            Topping("Cinnamon Sugar Pretzel Rods", "toppings"),
            Topping("Churro Bites", "toppings"),
            Topping("Pecan Pie Pieces", "toppings"),
            Topping("Coconut Haystacks", "toppings"),
            Topping("Candy Pieces Surprise", "toppings"),
            Topping("Cereal Killer", "toppings"),
            Topping("Fruit and Nut Mix", "toppings"),
            Topping("Caramel Turtle", "toppings"),
            Topping("Pistachio Cardamom", "toppings"),
            Topping("Cinnamon Apple", "toppings"),
            Topping("Cranberry White Chocolate", "toppings"),
            Topping("Chocolate Dipped Strawberries", "toppings"),
            Topping("Pretzel Crust", "toppings"),
            Topping("Cinnamon Sugar Donuts", "toppings"),
            Topping("Cereal Treats", "toppings"),
            Topping("Coconut Cream Pie", "toppings"),
            Topping("Cinnamon Roll", "toppings"),
            Topping("Cranberry Crunch", "toppings"),
            Topping("Pistachio Rosewater", "toppings"),
            Topping("Chocolate Mousse", "toppings"),
            Topping("Cinnamon Swirl Buns", "toppings"),
            Topping("Cereal Bars", "toppings"),
            Topping("Coconut Macaroons", "toppings"),
            Topping("Cinnamon Sugar Cookies", "toppings"),
            Topping("Cranberry Oatmeal", "toppings"),
            Topping("Pistachio Pudding", "toppings"),
            Topping("Chocolate Fudge", "toppings"),
            Topping("Cinnamon Sugar Cake", "toppings"),
            Topping("Coconut Cream", "
