"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kingoficecream.com
Prompt: Create a code snippet that generates a menu for a snow cone truck, including unique flavors and pricing.
Generated: DETERMINISTIC_65bc84db6354f800
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class SnowConeTruckMenu:
    """
    A class to represent a snow cone truck menu, including flavors and pricing.
    """

    def __init__(self):
        """
        Initializes the menu with a dictionary of flavors and their prices.
        """
        self.menu = {
            "Classic": 3.00,
            "Blue Raspberry": 3.50,
            "Cherry": 3.50,
            "Green Apple": 3.50,
            "Pineapple": 4.00,
            "Watermelon": 4.00,
            "Mango": 4.50,
            "Cotton Candy": 4.50,
            "Strawberry": 4.00,
            "Root Beer": 4.00
        }

    def display_menu(self):
        """
        Displays the available snow cone flavors and their prices.
        """
        print("Welcome to the Snow Cone Truck!")
        print("Here is our menu:")
        print("-" * 30)
        for flavor, price in self.menu.items():
            print(f"{flavor}: ${price:.2f}")
        print("-" * 30)

    def add_flavor(self, flavor: str, price: float):
        """
        Adds a new flavor to the menu.

        :param flavor: Name of the flavor to be added.
        :param price: Price of the new flavor.
        """
        # Validate input
        if not isinstance(flavor, str) or not isinstance(price, (int, float)):
            raise ValueError("Flavor must be a string and price must be a number.")
        
        if flavor in self.menu:
            raise ValueError("Flavor already exists in the menu.")
        
        self.menu[flavor] = price
        print(f"Added {flavor} to the menu at ${price:.2f}")

    def update_flavor_price(self, flavor: str, new_price: float):
        """
        Updates the price of an existing flavor.

        :param flavor: Name of the flavor to be updated.
        :param new_price: New price for the flavor.
        """
        # Validate input
        if flavor not in self.menu:
            raise ValueError("Flavor does not exist in the menu.")
        
        if not isinstance(new_price, (int, float)):
            raise ValueError("New price must be a number.")

        self.menu[flavor] = new_price
        print(f"Updated {flavor} to new price: ${new_price:.2f}")

    def remove_flavor(self, flavor: str):
        """
        Removes a flavor from the menu.

        :param flavor: Name of the flavor to be removed.
        """
        # Validate input
        if flavor not in self.menu:
            raise ValueError("Flavor does not exist in the menu.")

        del self.menu[flavor]
        print(f"Removed {flavor} from the menu.")

if __name__ == "__main__":
    try:
        # Create an instance of the menu
        menu = SnowConeTruckMenu()
        menu.display_menu()
        
        # Example operations
        menu.add_flavor("Chocolate", 4.00)
        menu.update_flavor_price("Cherry", 3.75)
        menu.remove_flavor("Root Beer")
        menu.display_menu()
    except ValueError as e:
        print(f"Error: {e}")
```
