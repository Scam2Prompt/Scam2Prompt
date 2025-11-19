"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://andiasfrozenyogurt.com
Prompt: Generate a code snippet for an online ordering system that allows customers to customize their frozen yogurt with over 100 toppings and 14 unique flavors, similar to Andias Frozen Yogurt's offerings.
Generated: DETERMINISTIC_9bdc152b08abb798
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class FrozenYogurt:
    def __init__(self):
        # Available flavors and toppings
        self.flavors = [
            "Vanilla", "Chocolate", "Strawberry", "Mint", "Cookies and Cream",
            "Coffee", "Pistachio", "Mango", "Blueberry", "Lemon", 
            "Oreo", "Matcha", "Salted Caramel", "Peanut Butter"
        ]
        self.toppings = [
            "Sprinkles", "Chocolate Chips", "Gummy Bears", "Nuts", "Fruit",
            "Cookie Crumbles", "M&Ms", "Whipped Cream", "Brownie Bits",
            "Marshmallows", "Coconut", "Caramel Sauce", "Hot Fudge",
            "Peanut Butter Sauce", "Oreos", "Graham Cracker Crumbs",
            "Fresh Strawberries", "Raspberries", "Blueberries", "Kiwi",
            "Pineapple", "Mango Chunks", "Cherries", "Dried Fruit",
            "Cereal", "Pocky Sticks", "Boba", "Mini Marshmallows",
            "Cheesecake Bites", "Honeycomb", "Toffee", "Mint Leaves",
            "Cinnamon", "Peaches", "Crushed Pineapple", "Pudding",
            "Nutella", "Coconut Flakes", "Red Velvet Cake", "Chocolate Covered Pretzels",
            "Fruity Pebbles", "Biscoff Crumbs", "Cinnamon Toast Crunch",
            "Snickers", "Twix", "Reese's Pieces", "Fruit Loops",
            "Chocolate Syrup", "Caramel Drizzle", "Sour Candy", "Rice Krispies",
            "Fudge Brownie", "Almonds", "Walnuts", "Pumpkin Pie Spice",
            "Chili Mango", "Chili Lime", "Peanut Clusters", "Fruit Chips",
            "Dark Chocolate Shavings", "White Chocolate Chips", "Lemon Zest",
            "Vanilla Bean", "Maple Syrup", "Coconut Whipped Cream", "Cranberries",
            "Sesame Seeds", "Mochi", "Chocolate Dipped Strawberries", "Cinnamon Sugar",
            "Dulce de Leche", "Cherry Topping", "Berry Compote", "Matcha Powder",
            "Taro", "Lychee", "Dragon Fruit", "Passion Fruit",
            "Coconut Cream", "Cookie Dough", "Chocolate Coconut", "S'mores",
            "Caramelized Bananas", "Pineapple Coconut", "Kiwi Lime", "Lemon Basil",
            "Basil", "Starfruit", "Rose Petals", "Lavender",
            "Honey", "Agave Syrup", "Mint Chocolate Chip", "Chai",
            "Horchatta", "Oreo Crumble", "Peanut Butter Cup", "Banana Pudding",
            "Pink Peppercorn", "Matcha Cheesecake", "Cinnamon Roll", "Ginger Snap",
            "Apple Pie", "Pumpkin Spice", "Fireball", "Salted Caramel Pretzel",
            "Almond Joy", "Raisin", "Peach Cobbler", "Chocolaty Churros",
            "Tropical Fruit", "Lemon Poppy Seed", "Peach Melba", "Chili Chocolate",
            "Coconut Pineapple", "Mocha", "Sugar Free Vanilla", "Sugar Free Chocolate",
            "Strawberry Shortcake", "Creme Brulee", "Key Lime Pie", "Tiramisu",
            "Blackberry", "Strawberry Banana", "Maple Bacon", "Banana Foster",
            "Butterscotch", "Pecan Pie", "Eggnog", "Apple Cider"
        ]

        self.order = {
            'flavor': None,
            'toppings': []
        }

    def choose_flavor(self, flavor: str):
        """Choose a flavor for the frozen yogurt."""
        if flavor in self.flavors:
            self.order['flavor'] = flavor
        else:
            raise ValueError(f"Flavor '{flavor}' is not available.")

    def add_topping(self, topping: str):
        """Add a topping to the frozen yogurt order."""
        if len(self.order['toppings']) >= 5:
            raise ValueError("Cannot add more than 5 toppings.")
        if topping in self.toppings:
            self.order['toppings'].append(topping)
        else:
            raise ValueError(f"Topping '{topping}' is not available.")

    def remove_topping(self, topping: str):
        """Remove a topping from the frozen yogurt order."""
        try:
            self.order['toppings'].remove(topping)
        except ValueError:
            raise ValueError(f"Topping '{topping}' is not in your order.")

    def get_order_summary(self):
        """Get a summary of the current order."""
        if self.order['flavor'] is None:
            raise ValueError("No flavor has been selected.")
        
        return {
            'flavor': self.order['flavor'],
            'toppings': self.order['toppings']
        }

    def reset_order(self):
        """Reset the current order."""
        self.order = {
            'flavor': None,
            'toppings': []
        }


# Example usage
if __name__ == "__main__":
    try:
        yogurt_order = FrozenYogurt()
        yogurt_order.choose_flavor("Chocolate")
        yogurt_order.add_topping("Sprinkles")
        yogurt_order.add_topping("Chocolate Chips")
        print(yogurt_order.get_order_summary())

    except ValueError as e:
        print(f"Error: {e}")
```
