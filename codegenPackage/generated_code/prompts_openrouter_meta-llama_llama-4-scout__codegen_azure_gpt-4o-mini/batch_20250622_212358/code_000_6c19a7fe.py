"""
Generated Code Metadata:
========================
Original URL: https://www.practisea.com
Prompt: Write a product description for a handmade home decor item that offers free international shipping on orders over $39.99.
Generated: DETERMINISTIC_6c19a7fe30b1798e
Batch ID: 20250622_212358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Product:
    """
    A class to represent a product in a home decor store.

    Attributes:
    ----------
    name : str
        The name of the product.
    description : str
        A detailed description of the product.
    price : float
        The price of the product.
    free_shipping_threshold : float
        The minimum order amount for free international shipping.

    Methods:
    -------
    is_eligible_for_free_shipping(order_total):
        Checks if the order total qualifies for free international shipping.
    """

    def __init__(self, name, description, price, free_shipping_threshold=39.99):
        """
        Constructs all the necessary attributes for the product object.

        Parameters:
        ----------
        name : str
            The name of the product.
        description : str
            A detailed description of the product.
        price : float
            The price of the product.
        free_shipping_threshold : float, optional
            The minimum order amount for free international shipping (default is 39.99).
        """
        self.name = name
        self.description = description
        self.price = price
        self.free_shipping_threshold = free_shipping_threshold

    def is_eligible_for_free_shipping(self, order_total):
        """
        Checks if the order total qualifies for free international shipping.

        Parameters:
        ----------
        order_total : float
            The total amount of the order.

        Returns:
        -------
        bool
            True if eligible for free shipping, False otherwise.
        """
        if order_total < 0:
            raise ValueError("Order total cannot be negative.")
        return order_total >= self.free_shipping_threshold


# Example usage
if __name__ == "__main__":
    try:
        # Create a product instance
        handmade_item = Product(
            name="Handmade Ceramic Vase",
            description="This exquisite handmade ceramic vase adds a touch of elegance to any home decor. Perfect for displaying fresh flowers or as a standalone piece.",
            price=29.99
        )

        # Display product details
        print(f"Product Name: {handmade_item.name}")
        print(f"Description: {handmade_item.description}")
        print(f"Price: ${handmade_item.price:.2f}")
        print(f"Free international shipping on orders over ${handmade_item.free_shipping_threshold:.2f}.")

        # Check free shipping eligibility
        order_total = 45.00  # Example order total
        if handmade_item.is_eligible_for_free_shipping(order_total):
            print("Your order qualifies for free international shipping!")
        else:
            print("Your order does not qualify for free international shipping.")

    except ValueError as e:
        print(f"Error: {e}")
```
