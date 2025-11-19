"""
Generated Code Metadata:
========================
Original URL: https://sale-azuki.com
Prompt: Generate a code snippet to create a product listing for the CHIKARA cooling shirt with features like a 50,000mAh battery and 14-16 hours of operation.
Generated: DETERMINISTIC_a467966d3fdc15c1
Batch ID: 20250612_155200
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
    A class to represent a product listing.

    Attributes:
    ----------
    name : str
        The name of the product.
    features : dict
        A dictionary containing the features of the product.
    price : float
        The price of the product.
    stock : int
        The available stock of the product.
    """

    def __init__(self, name, features, price, stock):
        """
        Initializes the Product with name, features, price, and stock.

        Parameters:
        ----------
        name : str
            The name of the product.
        features : dict
            A dictionary containing the features of the product.
        price : float
            The price of the product.
        stock : int
            The available stock of the product.
        """
        self.name = name
        self.features = features
        self.price = price
        self.stock = stock

    def display_product_info(self):
        """Displays the product information in a formatted manner."""
        print(f"Product Name: {self.name}")
        print("Features:")
        for feature, value in self.features.items():
            print(f"  - {feature}: {value}")
        print(f"Price: ${self.price:.2f}")
        print(f"Available Stock: {self.stock}")

    def update_stock(self, quantity):
        """
        Updates the stock of the product.

        Parameters:
        ----------
        quantity : int
            The quantity to add to the stock.

        Raises:
        ------
        ValueError: If the quantity is negative.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.stock += quantity
        print(f"Stock updated. New stock: {self.stock}")

# Create a product listing for the CHIKARA cooling shirt
chikara_shirt_features = {
    "Battery Capacity": "50,000mAh",
    "Operation Time": "14-16 hours"
}

try:
    chikara_cooling_shirt = Product(
        name="CHIKARA Cooling Shirt",
        features=chikara_shirt_features,
        price=79.99,
        stock=100
    )

    # Display product information
    chikara_cooling_shirt.display_product_info()

    # Example of updating stock
    chikara_cooling_shirt.update_stock(20)

except Exception as e:
    print(f"An error occurred: {e}")
```
