"""
Generated Code Metadata:
========================
Original URL: https://connectnetwork.lojavirtualnuvem.com.br
Prompt: Write code to implement a "frete grátis" (free shipping) promotion for specific products, as seen in the Connect Network site's product listings.
Generated: DETERMINISTIC_0bf651741a8db47c
Batch ID: 20250612_152306
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
    A class to represent a product in the store.

    Attributes:
    ----------
    name : str
        The name of the product.
    price : float
        The price of the product.
    eligible_for_free_shipping : bool
        Indicates if the product is eligible for free shipping.
    """

    def __init__(self, name: str, price: float, eligible_for_free_shipping: bool = False):
        """
        Initializes a new product instance.

        Parameters:
        ----------
        name : str
            The name of the product.
        price : float
            The price of the product.
        eligible_for_free_shipping : bool
            Indicates if the product is eligible for free shipping (default is False).
        """
        self.name = name
        self.price = price
        self.eligible_for_free_shipping = eligible_for_free_shipping

    def __str__(self):
        """Returns a string representation of the product."""
        return f"{self.name} - ${self.price:.2f} - Free Shipping: {'Yes' if self.eligible_for_free_shipping else 'No'}"


class ShoppingCart:
    """
    A class to represent a shopping cart.

    Attributes:
    ----------
    products : list
        A list of products in the shopping cart.
    """

    def __init__(self):
        """Initializes an empty shopping cart."""
        self.products = []

    def add_product(self, product: Product):
        """
        Adds a product to the shopping cart.

        Parameters:
        ----------
        product : Product
            The product to be added to the cart.
        """
        self.products.append(product)

    def calculate_total(self) -> float:
        """
        Calculates the total price of the products in the cart.

        Returns:
        -------
        float
            The total price of the products, including shipping if applicable.
        """
        total = sum(product.price for product in self.products)
        if not self.is_eligible_for_free_shipping():
            total += self.calculate_shipping_cost()
        return total

    def is_eligible_for_free_shipping(self) -> bool:
        """
        Checks if the cart is eligible for free shipping.

        Returns:
        -------
        bool
            True if any product in the cart is eligible for free shipping, False otherwise.
        """
        return any(product.eligible_for_free_shipping for product in self.products)

    def calculate_shipping_cost(self) -> float:
        """
        Calculates the shipping cost for the cart.

        Returns:
        -------
        float
            The shipping cost, which is a fixed rate of $5.00.
        """
        return 5.00

    def __str__(self):
        """Returns a string representation of the shopping cart."""
        product_list = "\n".join(str(product) for product in self.products)
        total = self.calculate_total()
        return f"Shopping Cart:\n{product_list}\nTotal: ${total:.2f}"


# Example usage
if __name__ == "__main__":
    # Create some products
    product1 = Product("Laptop", 999.99, eligible_for_free_shipping=True)
    product2 = Product("Headphones", 199.99)
    product3 = Product("Mouse", 49.99, eligible_for_free_shipping=True)

    # Create a shopping cart and add products
    cart = ShoppingCart()
    cart.add_product(product1)
    cart.add_product(product2)
    cart.add_product(product3)

    # Print the shopping cart details
    print(cart)
```
