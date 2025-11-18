"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sctoll.io
Prompt: Create a program to manage inventory for modular wheel configurations, including Carbon Fiber, Forged, and Titanium options from Brixton Forged™.
Generated: DETERMINISTIC_79550f331055ad19
Batch ID: 20250612_151057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Wheel:
    """
    A class to represent a wheel configuration.
    
    Attributes:
        material (str): The material of the wheel (e.g., Carbon Fiber, Forged, Titanium).
        diameter (float): The diameter of the wheel in inches.
        quantity (int): The quantity of wheels in the inventory.
    """

    def __init__(self, material, diameter, quantity):
        """
        Initializes a new Wheel instance.
        
        Parameters:
            material (str): The material of the wheel.
            diameter (float): The diameter of the wheel in inches.
            quantity (int): The quantity of wheels available.
        """
        self.material = material
        self.diameter = diameter
        self.quantity = quantity

    def __str__(self):
        """ Returns a string representation of the wheel. """
        return f"{self.material} Wheel - Diameter: {self.diameter} inches, Quantity: {self.quantity}"

    def update_quantity(self, amount):
        """
        Updates the quantity of wheels.
        
        Parameters:
            amount (int): The amount to add or subtract from the inventory.
        """
        if self.quantity + amount < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity += amount

    
class Inventory:
    """
    A class to manage a collection of wheel configurations.

    Attributes:
        wheels (dict): A dictionary holding wheel configurations with a unique key.
    """

    def __init__(self):
        """ Initializes the inventory with an empty dictionary of wheels. """
        self.wheels = {}

    def add_wheel(self, key, wheel):
        """
        Adds a new wheel to the inventory.
        
        Parameters:
            key (str): The unique key for the wheel.
            wheel (Wheel): An instance of the Wheel class.
        """
        if key in self.wheels:
            raise KeyError(f"Wheel with key '{key}' already exists.")
        self.wheels[key] = wheel

    def remove_wheel(self, key):
        """
        Removes a wheel from the inventory by its unique key.
        
        Parameters:
            key (str): The unique key for the wheel to be removed.
        """
        if key not in self.wheels:
            raise KeyError(f"Wheel with key '{key}' does not exist.")
        del self.wheels[key]

    def update_wheel_quantity(self, key, amount):
        """
        Updates the quantity of a specified wheel in the inventory.
        
        Parameters:
            key (str): The unique key for the wheel to be updated.
            amount (int): The amount to add or subtract from the quantity.
        """
        if key not in self.wheels:
            raise KeyError(f"Wheel with key '{key}' does not exist.")
        self.wheels[key].update_quantity(amount)

    def display_inventory(self):
        """ Displays all wheels in the inventory. """
        if not self.wheels:
            print("Inventory is empty.")
            return
        for key, wheel in self.wheels.items():
            print(f"{key}: {wheel}")


# Example usage
if __name__ == "__main__":
    try:
        inventory = Inventory()
        
        # Adding wheels to inventory
        inventory.add_wheel("CF_19", Wheel("Carbon Fiber", 19, 10))
        inventory.add_wheel("F_20", Wheel("Forged", 20, 5))
        inventory.add_wheel("T_21", Wheel("Titanium", 21, 3))

        # Displaying the inventory
        print("Current Inventory:")
        inventory.display_inventory()

        # Updating quantities
        inventory.update_wheel_quantity("CF_19", -2)
        print("\nUpdated Inventory after removing 2 Carbon Fiber wheels:")
        inventory.display_inventory()

        # Removing a wheel
        inventory.remove_wheel("T_21")
        print("\nInventory after removing Titanium wheels:")
        inventory.display_inventory()

    except Exception as e:
        print(f"An error occurred: {e}")
```
