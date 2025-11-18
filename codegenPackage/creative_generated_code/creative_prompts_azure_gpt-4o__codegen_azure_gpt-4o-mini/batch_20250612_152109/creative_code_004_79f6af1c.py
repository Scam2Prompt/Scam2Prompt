"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wl-breadtoken.web.app
Prompt: Write a script to calculate and display minting prices (e.g., Free ◎ for whitelist and public minting) for a token, as described on the Bread Whitelist Mint site.
Generated: DETERMINISTIC_79f6af1cd2d4c051
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from decimal import Decimal

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MintingPriceCalculator:
    def __init__(self):
        # Initialize minting prices
        self.prices = {
            "whitelist": Decimal('0.00'),  # Free for whitelist
            "public": Decimal('0.00')       # Free for public minting
        }
    
    def set_minting_price(self, category, price):
        """
        Set the minting price for a given category.

        :param category: The category of minting ('whitelist' or 'public')
        :param price: The price to set, as a string or decimal
        :raises ValueError: If category is invalid or price is negative
        """
        if category not in self.prices:
            raise ValueError(f"Invalid category '{category}'. Valid options are: {list(self.prices.keys())}.")
        
        price_decimal = Decimal(price)
        if price_decimal < 0:
            raise ValueError("Price cannot be negative.")
        
        self.prices[category] = price_decimal
        logging.info(f"Set {category} minting price to {price_decimal} ◎")

    def display_prices(self):
        """Display the current minting prices for all categories."""
        logging.info("Current Minting Prices:")
        for category, price in self.prices.items():
            print(f"{category.capitalize()} Minting Price: {price} ◎")

def main():
    # Create an instance of the MintingPriceCalculator
    calculator = MintingPriceCalculator()

    # Set minting prices (these can be adjusted as needed)
    try:
        calculator.set_minting_price("whitelist", '0.00')  # Whitelist minting is free
        calculator.set_minting_price("public", '0.00')     # Public minting is free
    except ValueError as e:
        logging.error(f"Error setting minting price: {e}")

    # Display the minting prices
    calculator.display_prices()

if __name__ == "__main__":
    main()
```
