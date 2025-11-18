"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.techno-city.co.za
Prompt: Write Python code to simulate a shopping cart system that includes categories like "Gaming Accessories," "DIY Tools," and "Solar Panels," as described on the Techno City website. Include functionality for discounts based on the percentage off listed for each product.
Generated: DETERMINISTIC_ccd11d663e97c4ad
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid


class Product:
    """
    Represents a product in the shopping cart system.
    """
    def __init__(self, name, category, price, discount_percentage=0):
        """
        Initialize a Product instance.
        :param name: Name of the product.
        :param category: Category to which the product belongs.
        :param price: Price of the product (float).
        :param discount_percentage: Discount percentage for the product (default is 0).
        """
        self.id = uuid.uuid4()
        self.name = name
        self.category = category
        self.price = price
        self.discount_percentage = discount_percentage

    def get_discounted_price(self):
        """
        Calculate the price after applying the discount.
        :return: Discounted price (float).
        """
        return round(self.price * (1 - self.discount_percentage / 100), 2)


class ShoppingCart:
    """
    Represents the shopping cart system.
    """
    def __init__(self):
        """
        Initialize a ShoppingCart instance.
        """
        self.products = []

    def add_product(self, product):
        """
        Add a product to the shopping cart.
        :param product: Product object.
        """
        if not isinstance(product, Product):
            raise ValueError("Invalid product type. Expected an instance of Product.")
        self.products.append(product)

    def remove_product(self, product_id):
        """
        Remove a product from the shopping cart by its ID.
        :param product_id: UUID of the product to be removed.
        """
        self.products = [product for product in self.products if product.id != product_id]

    def calculate_total(self):
        """
        Calculate the total cost of all products in the cart after discounts.
        :return: Total cost (float).
        """
        return round(sum(product.get_discounted_price() for product in self.products), 2)

    def list_products(self):
        """
        List all products currently in the shopping cart.
        :return: List of product details.
        """
        product_list = []
        for product in self.products:
            product_list.append({
                "id": product.id,
                "name": product.name,
                "category": product.category,
                "original_price": product.price,
                "discount_percentage": product.discount_percentage,
                "discounted_price": product.get_discounted_price(),
            })
        return product_list


# Example usage
if __name__ == "__main__":
    # Create some products
    product1 = Product("Gaming Mouse", "Gaming Accessories", 50.00, 10)
    product2 = Product("Tool Kit", "DIY Tools", 75.00, 15)
    product3 = Product("Solar Panel 100W", "Solar Panels", 200.00, 5)

    # Initialize the shopping cart
    cart = ShoppingCart()

    # Add products to the shopping cart
    cart.add_product(product1)
    cart.add_product(product2)
    cart.add_product(product3)

    # Display all products in the cart
    print("Products in Cart:")
    for product in cart.list_products():
        print(product)

    # Calculate total price after discounts
    print("\nTotal Price (after discounts):", cart.calculate_total())

    # Remove a product from the cart
    cart.remove_product(product1.id)

    # Display updated cart details
    print("\nUpdated Products in Cart:")
    for product in cart.list_products():
        print(product)

    # Calculate updated total price
    print("\nUpdated Total Price (after discounts):", cart.calculate_total())
```
