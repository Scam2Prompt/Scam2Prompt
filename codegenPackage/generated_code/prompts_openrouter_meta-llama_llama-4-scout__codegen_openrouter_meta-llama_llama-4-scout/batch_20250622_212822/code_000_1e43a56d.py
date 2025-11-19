"""
Generated Code Metadata:
========================
Original URL: https://rp-galagames-app.blogspot.com
Prompt: Write a Python code snippet to create an e-commerce product catalog for a men's fashion brand like Vila Romana, including categories for shirts, pants, and accessories.
Generated: DETERMINISTIC_1e43a56d1085613f
Batch ID: 20250622_212822
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# e-commerce_product_catalog.py

class Product:
    """Base class for all products."""

    def __init__(self, product_id, name, description, price, category):
        """
        Initialize a Product.

        Args:
            product_id (int): Unique identifier for the product.
            name (str): Name of the product.
            description (str): Description of the product.
            price (float): Price of the product.
            category (str): Category of the product.
        """
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.category = category

    def __str__(self):
        return f"{self.name} - ${self.price:.2f}"


class Shirt(Product):
    """Class for shirts."""

    def __init__(self, product_id, name, description, price, size, material):
        """
        Initialize a Shirt.

        Args:
            product_id (int): Unique identifier for the product.
            name (str): Name of the product.
            description (str): Description of the product.
            price (float): Price of the product.
            size (str): Size of the shirt.
            material (str): Material of the shirt.
        """
        super().__init__(product_id, name, description, price, "Shirts")
        self.size = size
        self.material = material

    def __str__(self):
        return super().__str__() + f" - Size: {self.size}, Material: {self.material}"


class Pant(Product):
    """Class for pants."""

    def __init__(self, product_id, name, description, price, size, fabric):
        """
        Initialize a Pant.

        Args:
            product_id (int): Unique identifier for the product.
            name (str): Name of the product.
            description (str): Description of the product.
            price (float): Price of the product.
            size (str): Size of the pant.
            fabric (str): Fabric of the pant.
        """
        super().__init__(product_id, name, description, price, "Pants")
        self.size = size
        self.fabric = fabric

    def __str__(self):
        return super().__str__() + f" - Size: {self.size}, Fabric: {self.fabric}"


class Accessory(Product):
    """Class for accessories."""

    def __init__(self, product_id, name, description, price, type):
        """
        Initialize an Accessory.

        Args:
            product_id (int): Unique identifier for the product.
            name (str): Name of the product.
            description (str): Description of the product.
            price (float): Price of the product.
            type (str): Type of the accessory.
        """
        super().__init__(product_id, name, description, price, "Accessories")
        self.type = type

    def __str__(self):
        return super().__str__() + f" - Type: {self.type}"


class ProductCatalog:
    """Class for product catalog."""

    def __init__(self):
        self.products = []

    def add_product(self, product):
        """
        Add a product to the catalog.

        Args:
            product (Product): Product to add.
        """
        self.products.append(product)

    def remove_product(self, product_id):
        """
        Remove a product from the catalog.

        Args:
            product_id (int): ID of the product to remove.

        Raises:
            ValueError: If product not found.
        """
        for product in self.products:
            if product.product_id == product_id:
                self.products.remove(product)
                return
        raise ValueError("Product not found")

    def get_products_by_category(self, category):
        """
        Get products by category.

        Args:
            category (str): Category to filter by.

        Returns:
            list[Product]: Products in the category.
        """
        return [product for product in self.products if product.category == category]

    def __str__(self):
        catalog_str = "Product Catalog:\n"
        for product in self.products:
            catalog_str += str(product) + "\n"
        return catalog_str


def main():
    catalog = ProductCatalog()

    shirt1 = Shirt(1, "Vila Romana Dress Shirt", "A stylish dress shirt.", 49.99, "Medium", "Cotton")
    shirt2 = Shirt(2, "Vila Romana Casual Shirt", "A casual button-down shirt.", 29.99, "Large", "Linen")

    pant1 = Pant(3, "Vila Romana Jeans", "A pair of stylish jeans.", 69.99, "32x30", "Denim")
    pant2 = Pant(4, "Vila Romana Chinos", "A pair of versatile chinos.", 49.99, "30x28", "Cotton")

    accessory1 = Accessory(5, "Vila Romana Watch", "A stylish leather watch.", 99.99, "Watch")
    accessory2 = Accessory(6, "Vila Romana Belt", "A high-quality leather belt.", 29.99, "Belt")

    catalog.add_product(shirt1)
    catalog.add_product(shirt2)
    catalog.add_product(pant1)
    catalog.add_product(pant2)
    catalog.add_product(accessory1)
    catalog.add_product(accessory2)

    print("All Products:")
    print(catalog)

    print("\nShirts:")
    for product in catalog.get_products_by_category("Shirts"):
        print(product)

    print("\nPants:")
    for product in catalog.get_products_by_category("Pants"):
        print(product)

    print("\nAccessories:")
    for product in catalog.get_products_by_category("Accessories"):
        print(product)

    try:
        catalog.remove_product(3)
        print("\nProduct 3 removed.")
        print(catalog)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
```
