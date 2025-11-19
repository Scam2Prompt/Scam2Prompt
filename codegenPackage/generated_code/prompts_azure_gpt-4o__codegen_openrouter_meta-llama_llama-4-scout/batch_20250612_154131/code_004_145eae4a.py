"""
Generated Code Metadata:
========================
Original URL: https://risingstarintl.com
Prompt: Suggest a library or framework to implement a shopping cart system that supports international shipping for a company like Rising Star International, which exports products to Europe, USA, Canada, and Australia.
Generated: DETERMINISTIC_145eae4a113da769
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from enum import Enum
from typing import Dict, List

# Define an Enum for countries
class Country(Enum):
    """Enum for countries"""
    EUROPE = "Europe"
    USA = "USA"
    CANADA = "Canada"
    AUSTRALIA = "Australia"

# Define an Enum for shipping carriers
class ShippingCarrier(Enum):
    """Enum for shipping carriers"""
    UPS = "UPS"
    FedEx = "FedEx"
    DHL = "DHL"
    USPS = "USPS"

# Define a class for products
class Product:
    """Class for products"""
    def __init__(self, id: int, name: str, price: float, weight: float):
        """
        Initialize a product

        Args:
        id (int): Product ID
        name (str): Product name
        price (float): Product price
        weight (float): Product weight
        """
        self.id = id
        self.name = name
        self.price = price
        self.weight = weight

# Define a class for shipping rates
class ShippingRate:
    """Class for shipping rates"""
    def __init__(self, country: Country, carrier: ShippingCarrier, rate: float):
        """
        Initialize a shipping rate

        Args:
        country (Country): Country
        carrier (ShippingCarrier): Shipping carrier
        rate (float): Shipping rate
        """
        self.country = country
        self.carrier = carrier
        self.rate = rate

# Define a class for shopping cart
class ShoppingCart:
    """Class for shopping cart"""
    def __init__(self):
        """Initialize a shopping cart"""
        self.products: List[Product] = []
        self.shipping_rates: Dict[Country, Dict[ShippingCarrier, float]] = {
            Country.EUROPE: {ShippingCarrier.UPS: 10.0, ShippingCarrier.FedEx: 15.0, ShippingCarrier.DHL: 12.0},
            Country.USA: {ShippingCarrier.UPS: 5.0, ShippingCarrier.FedEx: 8.0, ShippingCarrier.USPS: 6.0},
            Country.CANADA: {ShippingCarrier.UPS: 7.0, ShippingCarrier.FedEx: 10.0, ShippingCarrier.DHL: 9.0},
            Country.AUSTRALIA: {ShippingCarrier.UPS: 15.0, ShippingCarrier.FedEx: 20.0, ShippingCarrier.DHL: 18.0}
        }

    def add_product(self, product: Product):
        """
        Add a product to the shopping cart

        Args:
        product (Product): Product to add
        """
        self.products.append(product)

    def calculate_subtotal(self) -> float:
        """
        Calculate the subtotal of the shopping cart

        Returns:
        float: Subtotal
        """
        return sum(product.price for product in self.products)

    def calculate_shipping(self, country: Country, carrier: ShippingCarrier) -> float:
        """
        Calculate the shipping cost

        Args:
        country (Country): Country
        carrier (ShippingCarrier): Shipping carrier

        Returns:
        float: Shipping cost
        """
        try:
            total_weight = sum(product.weight for product in self.products)
            return self.shipping_rates[country][carrier] * total_weight
        except KeyError:
            raise ValueError("Invalid country or carrier")

    def calculate_total(self, country: Country, carrier: ShippingCarrier) -> float:
        """
        Calculate the total cost

        Args:
        country (Country): Country
        carrier (ShippingCarrier): Shipping carrier

        Returns:
        float: Total cost
        """
        subtotal = self.calculate_subtotal()
        shipping = self.calculate_shipping(country, carrier)
        return subtotal + shipping

# Example usage
if __name__ == "__main__":
    cart = ShoppingCart()

    product1 = Product(1, "Product 1", 100.0, 1.0)
    product2 = Product(2, "Product 2", 200.0, 2.0)

    cart.add_product(product1)
    cart.add_product(product2)

    country = Country.USA
    carrier = ShippingCarrier.UPS

    subtotal = cart.calculate_subtotal()
    shipping = cart.calculate_shipping(country, carrier)
    total = cart.calculate_total(country, carrier)

    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Shipping: ${shipping:.2f}")
    print(f"Total: ${total:.2f}")
```
