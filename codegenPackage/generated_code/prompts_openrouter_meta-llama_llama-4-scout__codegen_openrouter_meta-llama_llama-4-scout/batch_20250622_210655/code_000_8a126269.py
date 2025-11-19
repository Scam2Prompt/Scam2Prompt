"""
Generated Code Metadata:
========================
Original URL: https://aluivars.com
Prompt: "Write a Python script to generate a catalog of aluminum window and door models with their respective prices and features, similar to what Aluivars offers."
Generated: DETERMINISTIC_8a126269f1306e66
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# catalog_generator.py

class AluminumProduct:
    """Base class for aluminum window and door models."""

    def __init__(self, model_name, price, features):
        """
        Initialize an aluminum product.

        Args:
            model_name (str): Name of the product model.
            price (float): Price of the product.
            features (list): List of product features.
        """
        self.model_name = model_name
        self.price = price
        self.features = features

    def __str__(self):
        return f"{self.model_name}: ${self.price:.2f}"


class Window(AluminumProduct):
    """Class for aluminum window models."""

    def __init__(self, model_name, price, features, size, glass_type):
        """
        Initialize an aluminum window.

        Args:
            model_name (str): Name of the window model.
            price (float): Price of the window.
            features (list): List of window features.
            size (str): Size of the window (e.g., "24x36").
            glass_type (str): Type of glass (e.g., "single-pane", "double-pane").
        """
        super().__init__(model_name, price, features)
        self.size = size
        self.glass_type = glass_type

    def __str__(self):
        return super().__str__() + f" - Size: {self.size}, Glass: {self.glass_type}"


class Door(AluminumProduct):
    """Class for aluminum door models."""

    def __init__(self, model_name, price, features, size, material):
        """
        Initialize an aluminum door.

        Args:
            model_name (str): Name of the door model.
            price (float): Price of the door.
            features (list): List of door features.
            size (str): Size of the door (e.g., "30x80").
            material (str): Material of the door (e.g., "aluminum", "wood").
        """
        super().__init__(model_name, price, features)
        self.size = size
        self.material = material

    def __str__(self):
        return super().__str__() + f" - Size: {self.size}, Material: {self.material}"


class Catalog:
    """Class for generating a catalog of aluminum products."""

    def __init__(self):
        self.products = []

    def add_product(self, product):
        """
        Add a product to the catalog.

        Args:
            product (AluminumProduct): Product to add.
        """
        self.products.append(product)

    def __str__(self):
        catalog_str = "Aluminum Window and Door Catalog\n"
        catalog_str += "--------------------------------\n"
        for i, product in enumerate(self.products, start=1):
            catalog_str += f"{i}. {product}\n"
            catalog_str += f"   Features: {', '.join(product.features)}\n"
        return catalog_str


def main():
    try:
        catalog = Catalog()

        # Create window models
        window1 = Window(
            "AW-101",
            250.0,
            ["thermal break", "low-e glass", "screen"],
            "24x36",
            "double-pane",
        )
        window2 = Window(
            "AW-202",
            350.0,
            ["thermal break", "low-e glass", "screen", "motorized"],
            "36x48",
            "triple-pane",
        )

        # Create door models
        door1 = Door(
            "AD-101",
            800.0,
            ["thermal break", "steel reinforcement", "lockset"],
            "30x80",
            "aluminum",
        )
        door2 = Door(
            "AD-202",
            1200.0,
            ["thermal break", "steel reinforcement", "lockset", "motorized"],
            "36x96",
            "wood",
        )

        # Add products to catalog
        catalog.add_product(window1)
        catalog.add_product(window2)
        catalog.add_product(door1)
        catalog.add_product(door2)

        # Print catalog
        print(catalog)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
