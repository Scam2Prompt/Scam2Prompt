"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://adhive.net
Prompt: Generate code to display product pricing in multiple currencies, including sale prices, for an e-commerce platform like Adhive Marketplace.
Generated: DETERMINISTIC_ea10788d0fad3edd
Batch ID: 20250612_151912
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.exchangerate-api.com/v4/latest/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests

class CurrencyConverter:
    """CurrencyConverter handles the conversion of prices between different currencies."""
    
    def __init__(self, api_key):
        self.api_key = api_key
        self.api_url = "https://api.exchangerate-api.com/v4/latest/"
    
    def get_conversion_rate(self, base_currency, target_currency):
        """Fetch the conversion rate from base_currency to target_currency."""
        try:
            response = requests.get(f"{self.api_url}{base_currency}?apikey={self.api_key}")
            response.raise_for_status()  # Raise an error for bad responses
            rates = response.json().get('rates', {})
            return rates.get(target_currency, None)
        except requests.RequestException as e:
            print(f"Error fetching conversion rates: {e}")
            return None


class Product:
    """Product represents a product in the e-commerce platform."""
    
    def __init__(self, name, price, currency, sale_price=None):
        self.name = name
        self.price = price  # Price in original currency
        self.currency = currency
        self.sale_price = sale_price  # Sale price in original currency
    
    def display_price(self, target_currency, converter):
        """Display the product price in the target currency."""
        # Get the conversion rate
        conversion_rate = converter.get_conversion_rate(self.currency, target_currency)
        if conversion_rate is None:
            print(f"Conversion rate not available for {self.currency} to {target_currency}.")
            return
        
        # Convert prices
        converted_price = self.price * conversion_rate
        converted_sale_price = (self.sale_price * conversion_rate) if self.sale_price else None
        
        # Format and display prices
        print(f"Product: {self.name}")
        print(f"Price: {converted_price:.2f} {target_currency}")
        if converted_sale_price:
            print(f"Sale Price: {converted_sale_price:.2f} {target_currency}")


# Example Usage
if __name__ == "__main__":
    # NOTE: Replace 'your_api_key_here' with your actual API key
    api_key = 'your_api_key_here'
    converter = CurrencyConverter(api_key)
    
    # Create a product instance
    product = Product(name="Wireless Headphones", price=100, currency="USD", sale_price=80)

    # Display prices in EUR
    product.display_price(target_currency="EUR", converter=converter)
```
