"""
Generated Code Metadata:
========================
Original URL: https://metamark.lt
Prompt: What are the essential features to include in an e-commerce platform to ensure a smooth shopping experience, as suggested by Metamark's services?
Generated: DETERMINISTIC_d786cc9226f14032
Batch ID: 20250612_135046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# e_commerce_platform.py

class ECommercePlatform:
    """
    A class to represent an e-commerce platform with essential features
    to ensure a smooth shopping experience.
    """

    def __init__(self):
        """
        Initializes the e-commerce platform with essential features.
        """
        self.products = []  # List to store products
        self.cart = []      # List to store items in the shopping cart
        self.orders = []    # List to store completed orders

    def add_product(self, product):
        """
        Adds a product to the platform.

        Args:
            product (dict): A dictionary containing product details.
        """
        if not isinstance(product, dict):
            raise ValueError("Product must be a dictionary.")
        self.products.append(product)

    def view_products(self):
        """
        Returns a list of available products.
        
        Returns:
            list: A list of products.
        """
        return self.products

    def add_to_cart(self, product_id):
        """
        Adds a product to the shopping cart.

        Args:
            product_id (int): The ID of the product to add to the cart.

        Raises:
            ValueError: If the product ID is not found.
        """
        product = self.get_product_by_id(product_id)
        if product:
            self.cart.append(product)
        else:
            raise ValueError("Product ID not found.")

    def get_product_by_id(self, product_id):
        """
        Retrieves a product by its ID.

        Args:
            product_id (int): The ID of the product.

        Returns:
            dict: The product details if found, else None.
        """
        for product in self.products:
            if product.get('id') == product_id:
                return product
        return None

    def view_cart(self):
        """
        Returns the current shopping cart contents.

        Returns:
            list: A list of items in the cart.
        """
        return self.cart

    def checkout(self):
        """
        Processes the checkout and completes the order.

        Returns:
            dict: The order details.
        """
        if not self.cart:
            raise ValueError("Cart is empty. Add items to the cart before checkout.")
        
        order = {
            'items': self.cart,
            'total': self.calculate_total(),
            'status': 'completed'
        }
        self.orders.append(order)
        self.cart.clear()  # Clear the cart after checkout
        return order

    def calculate_total(self):
        """
        Calculates the total price of items in the cart.

        Returns:
            float: The total price.
        """
        total = sum(item.get('price', 0) for item in self.cart)
        return total

    def view_orders(self):
        """
        Returns a list of completed orders.

        Returns:
            list: A list of orders.
        """
        return self.orders


# Example usage
if __name__ == "__main__":
    platform = ECommercePlatform()

    # Adding products
    platform.add_product({'id': 1, 'name': 'Laptop', 'price': 999.99})
    platform.add_product({'id': 2, 'name': 'Smartphone', 'price': 499.99})

    # Viewing products
    print("Available Products:", platform.view_products())

    # Adding to cart
    platform.add_to_cart(1)  # Adding Laptop
    platform.add_to_cart(2)  # Adding Smartphone

    # Viewing cart
    print("Shopping Cart:", platform.view_cart())

    # Checkout
    order = platform.checkout()
    print("Order Details:", order)

    # Viewing orders
    print("Completed Orders:", platform.view_orders())
```
