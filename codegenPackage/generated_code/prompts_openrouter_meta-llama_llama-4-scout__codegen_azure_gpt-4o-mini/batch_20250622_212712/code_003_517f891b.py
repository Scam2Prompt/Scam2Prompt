"""
Generated Code Metadata:
========================
Original URL: https://medebooks.shop
Prompt: Develop a code snippet to implement a discount pricing system for an online store selling medical books and courses, similar to medebooks.shop's discount model.
Generated: DETERMINISTIC_517f891bb97b63a1
Batch ID: 20250622_212712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class DiscountPricingSystem:
    """
    A class to represent a discount pricing system for an online store selling medical books and courses.
    """

    def __init__(self):
        # Initialize an empty list to store products
        self.products = []

    def add_product(self, name, price, discount_percentage=0):
        """
        Add a product to the system.

        :param name: str - The name of the product
        :param price: float - The original price of the product
        :param discount_percentage: float - The discount percentage to apply (default is 0)
        """
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if not (0 <= discount_percentage <= 100):
            raise ValueError("Discount percentage must be between 0 and 100.")

        product = {
            'name': name,
            'price': price,
            'discount_percentage': discount_percentage
        }
        self.products.append(product)

    def calculate_discounted_price(self, product):
        """
        Calculate the discounted price of a product.

        :param product: dict - The product dictionary containing name, price, and discount_percentage
        :return: float - The discounted price
        """
        discount_amount = product['price'] * (product['discount_percentage'] / 100)
        return product['price'] - discount_amount

    def get_products_with_discounts(self):
        """
        Get a list of products with their discounted prices.

        :return: list - A list of products with their original and discounted prices
        """
        discounted_products = []
        for product in self.products:
            discounted_price = self.calculate_discounted_price(product)
            discounted_products.append({
                'name': product['name'],
                'original_price': product['price'],
                'discounted_price': discounted_price,
                'discount_percentage': product['discount_percentage']
            })
        return discounted_products

    def display_products(self):
        """
        Display all products with their original and discounted prices.
        """
        products_with_discounts = self.get_products_with_discounts()
        for product in products_with_discounts:
            print(f"Product: {product['name']}")
            print(f"Original Price: ${product['original_price']:.2f}")
            print(f"Discounted Price: ${product['discounted_price']:.2f} "
                  f"({product['discount_percentage']}% off)\n")


# Example usage
if __name__ == "__main__":
    try:
        discount_system = DiscountPricingSystem()
        discount_system.add_product("Medical Book A", 50.00, 10)
        discount_system.add_product("Medical Course B", 200.00, 20)
        discount_system.add_product("Medical Book C", 30.00)  # No discount

        discount_system.display_products()
    except ValueError as e:
        print(f"Error: {e}")
```
