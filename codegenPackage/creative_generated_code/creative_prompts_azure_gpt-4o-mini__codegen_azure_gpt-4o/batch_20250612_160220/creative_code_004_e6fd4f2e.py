"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://storyi.foundation
Prompt: Illustrate how to implement a checkout system that supports local currency payments for domain purchases, inspired by the features of storyi.foundation.
Generated: DETERMINISTIC_e6fd4f2ea871d925
Batch ID: 20250612_160220
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from decimal import Decimal


class CheckoutSystem:
    """
    A checkout system for domain purchases that supports local currency payments.
    """

    def __init__(self, supported_currencies):
        """
        Initialize the checkout system with supported currencies.

        :param supported_currencies: Dictionary of supported currencies and their conversion rates.
                                     Example: {'USD': 1.0, 'EUR': 0.92, 'GBP': 0.81}
        """
        self.supported_currencies = supported_currencies
        self.domains = {}  # Store domain and its price in USD

    def add_domain(self, domain_name, price_usd):
        """
        Add a domain to the system.

        :param domain_name: Name of the domain (string).
        :param price_usd: Price of the domain in USD (decimal).
        """
        if price_usd <= 0:
            raise ValueError("Price must be greater than zero.")
        self.domains[domain_name] = Decimal(price_usd)

    def list_domains(self):
        """
        List available domains for purchase.

        :return: Dictionary of domains and their prices in USD.
        """
        return self.domains

    def calculate_price(self, domain_name, currency):
        """
        Calculate the price of a domain in a specified currency.

        :param domain_name: Name of the domain.
        :param currency: Target currency (string).
        :return: Price in the specified currency.
        """
        if domain_name not in self.domains:
            raise ValueError("Domain not found.")

        if currency not in self.supported_currencies:
            raise ValueError("Currency not supported.")

        price_usd = self.domains[domain_name]
        conversion_rate = Decimal(self.supported_currencies[currency])
        return price_usd * conversion_rate

    def checkout(self, domain_name, currency):
        """
        Checkout a domain using the specified currency.

        :param domain_name: Name of the domain.
        :param currency: Currency for payment (string).
        :return: Transaction summary.
        """
        try:
            price_in_currency = self.calculate_price(domain_name, currency)
            transaction = {
                "domain": domain_name,
                "price": str(price_in_currency),
                "currency": currency
            }
            # Simulate a successful transaction
            return json.dumps(transaction, indent=4)
        except ValueError as e:
            return f"Error: {str(e)}"
        except Exception as e:
            return f"Unexpected error occurred: {str(e)}"


# Example Usage:
if __name__ == "__main__":
    try:
        # Supported currencies and their conversion rates
        currencies = {
            "USD": 1.0,
            "EUR": 0.92,
            "GBP": 0.81,
            "JPY": 110.0
        }

        # Initialize the checkout system
        checkout_system = CheckoutSystem(currencies)

        # Add domains to the system
        checkout_system.add_domain("example.com", 10.0)
        checkout_system.add_domain("storyi.foundation", 20.0)

        # List available domains
        print("Available Domains:")
        print(json.dumps(checkout_system.list_domains(), indent=4))

        # Calculate price in GBP for "example.com"
        print("\nPrice of 'example.com' in GBP:")
        print(checkout_system.calculate_price("example.com", "GBP"))

        # Checkout "storyi.foundation" in EUR
        print("\nCheckout 'storyi.foundation' in EUR:")
        print(checkout_system.checkout("storyi.foundation", "EUR"))

    except Exception as e:
        print(f"Error initializing checkout system: {str(e)}")
```
