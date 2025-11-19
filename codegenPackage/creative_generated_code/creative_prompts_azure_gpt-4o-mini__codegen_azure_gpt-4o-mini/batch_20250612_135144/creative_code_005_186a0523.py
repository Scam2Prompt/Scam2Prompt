"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linea.be
Prompt: Suggest a library for managing product displays for cleaning tools similar to those offered by PDC Brush.
Generated: DETERMINISTIC_186a0523bbd87fdb
Batch ID: 20250612_135144
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
ProductDisplayManager - A class to manage product displays for cleaning tools.
This implementation allows adding, removing, and displaying products in a simple format.
"""

class Product:
    """Class to represent a cleaning tool product."""
    
    def __init__(self, name: str, price: float, description: str):
        """
        Initialize a new product.

        :param name: Name of the product.
        :param price: Price of the product.
        :param description: Description of the product.
        """
        self.name = name
        self.price = price
        self.description = description

    def __repr__(self):
        """Return a string representation of the product."""
        return f"{self.name}: ${self.price:.2f} - {self.description}"


class ProductDisplayManager:
    """Class to manage a collection of cleaning tool products."""
    
    def __init__(self):
        """Initialize the ProductDisplayManager with an empty product list."""
        self.products = []

    def add_product(self, product: Product):
        """
        Add a new product to the display.

        :param product: An instance of Product to add.
        """
        if not isinstance(product, Product):
            raise ValueError("Invalid product type. Must be an instance of Product.")
        self.products.append(product)

    def remove_product(self, product_name: str):
        """
        Remove a product from the display by its name.

        :param product_name: The name of the product to remove.
        :raises ValueError: If the product is not found.
        """
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                return
        raise ValueError("Product not found: {}".format(product_name))

    def display_products(self):
        """Display all products in the product list."""
        if not self.products:
            print("No products available.")
            return
        print("Available Products:")
        for product in self.products:
            print(product)


# Example usage
if __name__ == "__main__":
    manager = ProductDisplayManager()
    
    # Create some products
    product1 = Product("PDC Brush Pro", 19.99, "High-performance cleaning brush.")
    product2 = Product("PDC Mop Deluxe", 29.99, "Heavy-duty mop for tough cleaning.")
    
    # Add products to the manager
    manager.add_product(product1)
    manager.add_product(product2)
    
    # Display all products
    manager.display_products()
    
    # Remove a product
    try:
        manager.remove_product("PDC Brush Pro")
    except ValueError as e:
        print(e)
    
    # Display products after removal
    manager.display_products()
```
