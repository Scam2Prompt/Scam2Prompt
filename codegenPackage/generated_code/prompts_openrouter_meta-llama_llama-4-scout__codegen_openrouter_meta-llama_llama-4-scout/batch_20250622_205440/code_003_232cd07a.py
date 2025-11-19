"""
Generated Code Metadata:
========================
Original URL: https://poocoinmod.blogspot.com
Prompt: Create a description for an online store selling sapatos sociais and sandalias coloridas for men and women.
Generated: DETERMINISTIC_232cd07a14084036
Batch ID: 20250622_205440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# online_store.py

class Product:
    """Represents a product in the online store."""

    def __init__(self, id, name, description, price, category, gender):
        """
        Initializes a Product object.

        Args:
            id (int): Unique product ID.
            name (str): Product name.
            description (str): Product description.
            price (float): Product price.
            category (str): Product category (e.g., sapatos sociais, sandalias coloridas).
            gender (str): Product gender (e.g., men, women).
        """
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.gender = gender

    def __str__(self):
        return f"{self.name} - {self.description} ({self.price:.2f})"


class OnlineStore:
    """Represents an online store selling sapatos sociais and sandalias coloridas."""

    def __init__(self):
        """Initializes an empty online store."""
        self.products = []

    def add_product(self, product):
        """
        Adds a product to the online store.

        Args:
            product (Product): Product to add.

        Raises:
            ValueError: If the product ID already exists.
        """
        if any(p.id == product.id for p in self.products):
            raise ValueError("Product ID already exists")
        self.products.append(product)

    def get_products(self, category=None, gender=None):
        """
        Retrieves products from the online store.

        Args:
            category (str, optional): Product category filter. Defaults to None.
            gender (str, optional): Product gender filter. Defaults to None.

        Returns:
            list[Product]: List of products matching the filters.
        """
        products = self.products
        if category:
            products = [p for p in products if p.category == category]
        if gender:
            products = [p for p in products if p.gender == gender]
        return products

    def __str__(self):
        store_description = "Online Store - Sapatos Sociais and Sandalias Coloridas\n"
        store_description += "-----------------------------------------------\n"
        for product in self.products:
            store_description += f"- {product}\n"
        return store_description


def main():
    store = OnlineStore()

    # Add products
    store.add_product(Product(1, "Sapatos Sociais", "Formal shoes for men", 99.99, "sapatos sociais", "men"))
    store.add_product(Product(2, "Sandalias Coloridas", "Colorful sandals for women", 49.99, "sandalias coloridas", "women"))
    store.add_product(Product(3, "Sapatos Sociais", "Formal shoes for women", 89.99, "sapatos sociais", "women"))
    store.add_product(Product(4, "Sandalias Coloridas", "Colorful sandals for men", 59.99, "sandalias coloridas", "men"))

    # Print store description
    print(store)

    # Get products by category and gender
    print("\nSapatos Sociais for Men:")
    for product in store.get_products(category="sapatos sociais", gender="men"):
        print(product)

    print("\nSandalias Coloridas for Women:")
    for product in store.get_products(category="sandalias coloridas", gender="women"):
        print(product)


if __name__ == "__main__":
    main()
```
