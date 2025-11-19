"""
Generated Code Metadata:
========================
Original URL: https://aprisacv.com.mx
Prompt: "Write a Python code snippet to manage inventory of refractory products, including bricks, mortars, and ceramic fibers, with attributes like product name, quantity, and temperature resistance."
Generated: DETERMINISTIC_bf6d2290ee2bb3a9
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from abc import ABC, abstractmethod
from typing import Dict, List

class RefractoryProduct(ABC):
    """Base class for refractory products."""

    def __init__(self, name: str, quantity: int, temperature_resistance: float):
        """
        Initialize a refractory product.

        Args:
        - name (str): Product name.
        - quantity (int): Product quantity.
        - temperature_resistance (float): Temperature resistance in Celsius.
        """
        self.name = name
        self.quantity = quantity
        self.temperature_resistance = temperature_resistance

    @abstractmethod
    def get_product_info(self) -> Dict[str, str]:
        """Get product information."""
        pass


class Brick(RefractoryProduct):
    """Class for refractory bricks."""

    def __init__(self, name: str, quantity: int, temperature_resistance: float, compressive_strength: float):
        """
        Initialize a refractory brick.

        Args:
        - name (str): Product name.
        - quantity (int): Product quantity.
        - temperature_resistance (float): Temperature resistance in Celsius.
        - compressive_strength (float): Compressive strength in MPa.
        """
        super().__init__(name, quantity, temperature_resistance)
        self.compressive_strength = compressive_strength

    def get_product_info(self) -> Dict[str, str]:
        """Get brick information."""
        return {
            "Name": self.name,
            "Quantity": str(self.quantity),
            "Temperature Resistance": f"{self.temperature_resistance}°C",
            "Compressive Strength": f"{self.compressive_strength} MPa",
        }


class Mortar(RefractoryProduct):
    """Class for refractory mortars."""

    def __init__(self, name: str, quantity: int, temperature_resistance: float, setting_time: str):
        """
        Initialize a refractory mortar.

        Args:
        - name (str): Product name.
        - quantity (int): Product quantity.
        - temperature_resistance (float): Temperature resistance in Celsius.
        - setting_time (str): Setting time.
        """
        super().__init__(name, quantity, temperature_resistance)
        self.setting_time = setting_time

    def get_product_info(self) -> Dict[str, str]:
        """Get mortar information."""
        return {
            "Name": self.name,
            "Quantity": str(self.quantity),
            "Temperature Resistance": f"{self.temperature_resistance}°C",
            "Setting Time": self.setting_time,
        }


class CeramicFiber(RefractoryProduct):
    """Class for ceramic fibers."""

    def __init__(self, name: str, quantity: int, temperature_resistance: float, fiber_length: float):
        """
        Initialize a ceramic fiber.

        Args:
        - name (str): Product name.
        - quantity (int): Product quantity.
        - temperature_resistance (float): Temperature resistance in Celsius.
        - fiber_length (float): Fiber length in mm.
        """
        super().__init__(name, quantity, temperature_resistance)
        self.fiber_length = fiber_length

    def get_product_info(self) -> Dict[str, str]:
        """Get ceramic fiber information."""
        return {
            "Name": self.name,
            "Quantity": str(self.quantity),
            "Temperature Resistance": f"{self.temperature_resistance}°C",
            "Fiber Length": f"{self.fiber_length} mm",
        }


class Inventory:
    """Class for managing refractory product inventory."""

    def __init__(self):
        """Initialize an empty inventory."""
        self.products: Dict[str, RefractoryProduct] = {}

    def add_product(self, product: RefractoryProduct):
        """
        Add a product to the inventory.

        Args:
        - product (RefractoryProduct): Product to add.
        """
        self.products[product.name] = product

    def remove_product(self, product_name: str):
        """
        Remove a product from the inventory.

        Args:
        - product_name (str): Name of the product to remove.

        Raises:
        - KeyError: If the product is not in the inventory.
        """
        if product_name not in self.products:
            raise KeyError(f"Product '{product_name}' not found in inventory.")
        del self.products[product_name]

    def update_quantity(self, product_name: str, new_quantity: int):
        """
        Update the quantity of a product in the inventory.

        Args:
        - product_name (str): Name of the product to update.
        - new_quantity (int): New quantity.

        Raises:
        - KeyError: If the product is not in the inventory.
        """
        if product_name not in self.products:
            raise KeyError(f"Product '{product_name}' not found in inventory.")
        self.products[product_name].quantity = new_quantity

    def get_product_info(self, product_name: str) -> Dict[str, str]:
        """
        Get information about a product in the inventory.

        Args:
        - product_name (str): Name of the product.

        Returns:
        - Dict[str, str]: Product information.

        Raises:
        - KeyError: If the product is not in the inventory.
        """
        if product_name not in self.products:
            raise KeyError(f"Product '{product_name}' not found in inventory.")
        return self.products[product_name].get_product_info()

    def list_products(self) -> List[Dict[str, str]]:
        """List all products in the inventory."""
        return [product.get_product_info() for product in self.products.values()]


def main():
    # Create an inventory
    inventory = Inventory()

    # Create products
    brick = Brick("Refractory Brick", 100, 1800, 50)
    mortar = Mortar("Refractory Mortar", 50, 1600, "2 hours")
    ceramic_fiber = CeramicFiber("Ceramic Fiber", 200, 1200, 10)

    # Add products to the inventory
    inventory.add_product(brick)
    inventory.add_product(mortar)
    inventory.add_product(ceramic_fiber)

    # List products
    print("Products:")
    for product in inventory.list_products():
        for key, value in product.items():
            print(f"{key}: {value}")
        print()

    # Get product info
    print("Brick Info:")
    for key, value in inventory.get_product_info("Refractory Brick").items():
        print(f"{key}: {value}")

    # Update quantity
    inventory.update_quantity("Refractory Brick", 80)

    # Remove product
    inventory.remove_product("Refractory Mortar")

    # List products again
    print("Products after update:")
    for product in inventory.list_products():
        for key, value in product.items():
            print(f"{key}: {value}")
        print()


if __name__ == "__main__":
    main()
```
