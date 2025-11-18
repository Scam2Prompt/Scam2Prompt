"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://earthmeta-aijko.pages.dev
Prompt: Write a Python script to calculate the market cap of $EMT tokens based on the presale price, listing price, and total token supply.
Generated: DETERMINISTIC_97cfae8aa4ab89e1
Batch ID: 20250612_154322
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TokenMarketCapCalculator:
    """
    A class to calculate the market capitalization of a cryptocurrency token.
    """

    def __init__(self, presale_price, listing_price, total_supply):
        """
        Initializes the calculator with presale price, listing price, and total supply.
        
        :param presale_price: The price of the token during the presale (float).
        :param listing_price: The price of the token during the listing (float).
        :param total_supply: The total supply of the token (int).
        """
        self.presale_price = presale_price
        self.listing_price = listing_price
        self.total_supply = total_supply

    def calculate_market_cap(self):
        """
        Calculate the market capitalization based on the listing price and total supply.
        
        :return: Market cap (float).
        :raises ValueError: If the total supply is less than zero or prices are negative.
        """
        if self.total_supply < 0:
            raise ValueError("Total supply must be a non-negative integer.")
        if self.presale_price < 0 or self.listing_price < 0:
            raise ValueError("Presale price and listing price must be non-negative.")

        # Calculate market cap using the listing price
        market_cap = self.listing_price * self.total_supply
        return market_cap

def main():
    """
    Main function to execute the market cap calculation.
    """
    try:
        # Example values for presale price, listing price, and total supply
        presale_price = float(input("Enter the presale price of $EMT token: "))
        listing_price = float(input("Enter the listing price of $EMT token: "))
        total_supply = int(input("Enter the total supply of $EMT token: "))
        
        # Create a calculator instance
        calculator = TokenMarketCapCalculator(presale_price, listing_price, total_supply)
        
        # Calculate and display the market cap
        market_cap = calculator.calculate_market_cap()
        print(f"The market capitalization of $EMT token is: ${market_cap:,.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
