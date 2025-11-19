"""
Generated Code Metadata:
========================
Original URL: https://meatmaster.pe
Prompt: Create a program to filter Meat Master products based on user preferences for material (e.g., acero inoxidable or galvanizado), size, and price range.
Generated: DETERMINISTIC_d50af39e8a057fcf
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# meat_master_filter.py

class MeatMasterProduct:
    """Represents a Meat Master product."""

    def __init__(self, name, material, size, price):
        """
        Initializes a Meat Master product.

        Args:
            name (str): Product name.
            material (str): Product material.
            size (str): Product size.
            price (float): Product price.
        """
        self.name = name
        self.material = material
        self.size = size
        self.price = price

    def __repr__(self):
        return f"MeatMasterProduct(name='{self.name}', material='{self.material}', size='{self.size}', price={self.price})"


class MeatMasterFilter:
    """Filters Meat Master products based on user preferences."""

    def __init__(self, products):
        """
        Initializes a Meat Master filter.

        Args:
            products (list[MeatMasterProduct]): List of Meat Master products.
        """
        self.products = products

    def filter_by_material(self, material):
        """
        Filters products by material.

        Args:
            material (str): Material to filter by.

        Returns:
            list[MeatMasterProduct]: Filtered products.
        """
        return [product for product in self.products if product.material.lower() == material.lower()]

    def filter_by_size(self, size):
        """
        Filters products by size.

        Args:
            size (str): Size to filter by.

        Returns:
            list[MeatMasterProduct]: Filtered products.
        """
        return [product for product in self.products if product.size.lower() == size.lower()]

    def filter_by_price_range(self, min_price, max_price):
        """
        Filters products by price range.

        Args:
            min_price (float): Minimum price.
            max_price (float): Maximum price.

        Returns:
            list[MeatMasterProduct]: Filtered products.
        """
        if min_price > max_price:
            raise ValueError("Invalid price range")

        return [product for product in self.products if min_price <= product.price <= max_price]

    def filter_products(self, material=None, size=None, min_price=None, max_price=None):
        """
        Filters products based on user preferences.

        Args:
            material (str, optional): Material to filter by. Defaults to None.
            size (str, optional): Size to filter by. Defaults to None.
            min_price (float, optional): Minimum price. Defaults to None.
            max_price (float, optional): Maximum price. Defaults to None.

        Returns:
            list[MeatMasterProduct]: Filtered products.
        """
        filtered_products = self.products

        if material:
            filtered_products = self.filter_by_material(material)
        if size:
            filtered_products = self.filter_by_size(size)
        if min_price is not None and max_price is not None:
            filtered_products = self.filter_by_price_range(min_price, max_price)

        return filtered_products


def main():
    # Example usage
    products = [
        MeatMasterProduct("Product 1", "Acero Inoxidable", "10x10", 100.0),
        MeatMasterProduct("Product 2", "Galvanizado", "20x20", 200.0),
        MeatMasterProduct("Product 3", "Acero Inoxidable", "30x30", 300.0),
        MeatMasterProduct("Product 4", "Galvanizado", "40x40", 400.0),
    ]

    filter = MeatMasterFilter(products)

    material = input("Enter material (e.g., acero inoxidable or galvanizado): ")
    size = input("Enter size (e.g., 10x10): ")
    min_price = float(input("Enter minimum price: "))
    max_price = float(input("Enter maximum price: "))

    try:
        filtered_products = filter.filter_products(material, size, min_price, max_price)
        print("Filtered products:")
        for product in filtered_products:
            print(product)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
