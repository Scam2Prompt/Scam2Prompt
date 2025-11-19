"""
Generated Code Metadata:
========================
Original URL: https://kingoficecream.com
Prompt: Create a code snippet that generates a menu for a snow cone truck, including unique flavors and pricing.
Generated: DETERMINISTIC_65bc84db6354f800
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class SnowConeTruckMenu:
    def __init__(self):
        """Initialize the menu with unique flavors and their prices."""
        self.menu = {
            "Classic Cherry": 3.00,
            "Blue Raspberry": 3.50,
            "Lime": 2.75,
            "Mango Madness": 4.00,
            "Pineapple Paradise": 3.25,
            "Cotton Candy": 3.75,
            "Watermelon Wave": 3.00,
            "Strawberry Shortcake": 4.50,
            "Tropical Punch": 3.50,
            "Root Beer Float": 4.00
        }

    def display_menu(self):
        """Display the snow cone menu with flavors and prices."""
        print("Welcome to the Snow Cone Truck!")
        print("Here is our menu:")
        print("-" * 30)
        for flavor, price in self.menu.items():
            print(f"{flavor}: ${price:.2f}")
        print("-" * 30)

    def get_price(self, flavor):
        """Get the price of a specific flavor.

        Args:
            flavor (str): The name of the flavor.

        Returns:
            float: The price of the flavor if it exists, else None.
        """
        return self.menu.get(flavor, None)

    def add_flavor(self, flavor, price):
        """Add a new flavor to the menu.

        Args:
            flavor (str): The name of the new flavor.
            price (float): The price of the new flavor.

        Raises:
            ValueError: If the flavor already exists or if the price is negative.
        """
        if flavor in self.menu:
            raise ValueError(f"Flavor '{flavor}' already exists in the menu.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.menu[flavor] = price
        print(f"Added '{flavor}' to the menu at ${price:.2f}.")

    def remove_flavor(self, flavor):
        """Remove a flavor from the menu.

        Args:
            flavor (str): The name of the flavor to remove.

        Raises:
            KeyError: If the flavor does not exist in the menu.
        """
        if flavor not in self.menu:
            raise KeyError(f"Flavor '{flavor}' does not exist in the menu.")
        del self.menu[flavor]
        print(f"Removed '{flavor}' from the menu.")

# Example usage
if __name__ == "__main__":
    try:
        menu = SnowConeTruckMenu()
        menu.display_menu()
        
        # Adding a new flavor
        menu.add_flavor("Peach Delight", 3.50)
        menu.display_menu()
        
        # Removing a flavor
        menu.remove_flavor("Lime")
        menu.display_menu()
        
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
