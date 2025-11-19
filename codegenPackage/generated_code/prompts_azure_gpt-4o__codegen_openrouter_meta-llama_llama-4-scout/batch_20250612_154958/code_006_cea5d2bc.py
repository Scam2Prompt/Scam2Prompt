"""
Generated Code Metadata:
========================
Original URL: https://simbatools.com
Prompt: Write code to generate an online quotation system for 심바공구, allowing users to select products like "백두장사 유압도끼" and "허스크바나 엔진톱" and receive a detailed price breakdown.
Generated: DETERMINISTIC_cea5d2bc77c144e5
Batch ID: 20250612_154958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# quotation_system.py

class Product:
    """Represents a product with a name and price."""

    def __init__(self, name, price):
        """
        Initializes a Product instance.

        Args:
            name (str): The product name.
            price (float): The product price.
        """
        self.name = name
        self.price = price

class QuotationSystem:
    """Manages products and generates quotations."""

    def __init__(self):
        """Initializes a QuotationSystem instance with an empty product catalog."""
        self.products = {}

    def add_product(self, product):
        """
        Adds a product to the catalog.

        Args:
            product (Product): The product to add.
        """
        self.products[product.name] = product

    def get_product(self, name):
        """
        Retrieves a product by name.

        Args:
            name (str): The product name.

        Returns:
            Product: The product instance, or None if not found.
        """
        return self.products.get(name)

    def generate_quotation(self, product_names, quantities):
        """
        Generates a detailed quotation for the specified products and quantities.

        Args:
            product_names (list[str]): The names of the products to quote.
            quantities (list[int]): The quantities of each product.

        Returns:
            dict: A dictionary containing the quotation details.

        Raises:
            ValueError: If the product names and quantities lists have different lengths.
        """
        if len(product_names) != len(quantities):
            raise ValueError("Product names and quantities lists must have the same length")

        quotation = {}
        subtotal = 0

        for name, quantity in zip(product_names, quantities):
            product = self.get_product(name)
            if product is None:
                raise ValueError(f"Product '{name}' not found in catalog")

            product_total = product.price * quantity
            quotation[name] = {
                "price": product.price,
                "quantity": quantity,
                "total": product_total
            }
            subtotal += product_total

        quotation["subtotal"] = subtotal
        quotation["tax"] = subtotal * 0.1  # 10% tax
        quotation["total"] = subtotal + quotation["tax"]

        return quotation

def main():
    # Create a quotation system and add products
    system = QuotationSystem()
    system.add_product(Product("백두장사 유압도끼", 10000))
    system.add_product(Product("허스크바나 엔진톱", 50000))

    # Get user input
    product_names = input("Enter product names (comma-separated): ").split(",")
    product_names = [name.strip() for name in product_names]
    quantities = [int(x) for x in input("Enter quantities (comma-separated): ").split(",")]

    try:
        # Generate quotation
        quotation = system.generate_quotation(product_names, quantities)

        # Print quotation
        print("Quotation:")
        for name, details in quotation.items():
            if name not in ["subtotal", "tax", "total"]:
                print(f"{name}: {details['quantity']} x {details['price']} = {details['total']}")
            else:
                print(f"{name.capitalize()}: {details}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
