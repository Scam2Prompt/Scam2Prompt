"""
Generated Code Metadata:
========================
Original URL: https://sigmacirebon.com
Prompt: Write a Python script to create a catalog for outdoor advertising products like billboards, videotrons, and neon boxes, including their prices and sizes.
Generated: DETERMINISTIC_1b4d5d760ec81dfb
Batch ID: 20250622_204554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# outdoor_advertising_catalog.py

class AdvertisingProduct:
    """Base class for outdoor advertising products."""

    def __init__(self, name, price, size):
        """
        Initialize an advertising product.

        Args:
            name (str): Product name.
            price (float): Product price.
            size (str): Product size.
        """
        self.name = name
        self.price = price
        self.size = size

    def __str__(self):
        return f"{self.name} - ${self.price:.2f} ({self.size})"


class Billboard(AdvertisingProduct):
    """Class for billboards."""

    def __init__(self, price, size, location):
        """
        Initialize a billboard.

        Args:
            price (float): Billboard price.
            size (str): Billboard size.
            location (str): Billboard location.
        """
        super().__init__("Billboard", price, size)
        self.location = location

    def __str__(self):
        return super().__str__() + f" at {self.location}"


class Videotron(AdvertisingProduct):
    """Class for videotrons."""

    def __init__(self, price, size, resolution):
        """
        Initialize a videotron.

        Args:
            price (float): Videotron price.
            size (str): Videotron size.
            resolution (str): Videotron resolution.
        """
        super().__init__("Videotron", price, size)
        self.resolution = resolution

    def __str__(self):
        return super().__str__() + f" with {self.resolution} resolution"


class NeonBox(AdvertisingProduct):
    """Class for neon boxes."""

    def __init__(self, price, size, color):
        """
        Initialize a neon box.

        Args:
            price (float): Neon box price.
            size (str): Neon box size.
            color (str): Neon box color.
        """
        super().__init__("Neon Box", price, size)
        self.color = color

    def __str__(self):
        return super().__str__() + f" in {self.color} color"


class Catalog:
    """Class for outdoor advertising product catalog."""

    def __init__(self):
        self.products = []

    def add_product(self, product):
        """
        Add a product to the catalog.

        Args:
            product (AdvertisingProduct): Product to add.
        """
        self.products.append(product)

    def remove_product(self, product_name):
        """
        Remove a product from the catalog.

        Args:
            product_name (str): Name of the product to remove.

        Raises:
            ValueError: If product not found.
        """
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                return
        raise ValueError("Product not found")

    def display_catalog(self):
        """Display all products in the catalog."""
        for product in self.products:
            print(product)


def main():
    catalog = Catalog()

    try:
        billboard = Billboard(1000.0, "10x5 meters", "City Center")
        videotron = Videotron(500.0, "5x3 meters", "Full HD")
        neon_box = NeonBox(200.0, "2x1 meters", "Red")

        catalog.add_product(billboard)
        catalog.add_product(videotron)
        catalog.add_product(neon_box)

        print("Outdoor Advertising Product Catalog:")
        catalog.display_catalog()

        catalog.remove_product("Videotron")

        print("\nUpdated Catalog:")
        catalog.display_catalog()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
