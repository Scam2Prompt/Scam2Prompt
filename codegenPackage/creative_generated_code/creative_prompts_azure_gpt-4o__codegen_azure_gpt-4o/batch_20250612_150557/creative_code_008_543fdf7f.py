"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dao-magi-alpha.web.app
Prompt: Generate a program that dynamically calculates the trading fees and royalties for an NFT transaction using the Open Creator Protocol features described on the webpage.
Generated: DETERMINISTIC_543fdf7fcf47e298
Batch ID: 20250612_150557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import decimal

# Constants
DECIMAL_PRECISION = decimal.Decimal('0.00000001')  # Precision for calculations

class NFTTransaction:
    """
    A class to represent an NFT transaction and calculate fees and royalties
    based on the Open Creator Protocol.
    """

    def __init__(self, sale_price, trading_fee_rate, royalty_rate):
        """
        Initialize the transaction with sale price, trading fee rate,
        and royalty rate.

        :param sale_price: The price at which the NFT is sold (Decimal).
        :param trading_fee_rate: The trading fee rate as a percentage (Decimal).
        :param royalty_rate: The royalty rate as a percentage (Decimal).
        """
        if sale_price <= 0:
            raise ValueError("Sale price must be greater than zero.")
        if not (0 <= trading_fee_rate <= 100):
            raise ValueError("Trading fee rate must be between 0 and 100 (inclusive).")
        if not (0 <= royalty_rate <= 100):
            raise ValueError("Royalty rate must be between 0 and 100 (inclusive).")

        self.sale_price = decimal.Decimal(sale_price).quantize(DECIMAL_PRECISION)
        self.trading_fee_rate = decimal.Decimal(trading_fee_rate).quantize(DECIMAL_PRECISION)
        self.royalty_rate = decimal.Decimal(royalty_rate).quantize(DECIMAL_PRECISION)

    def calculate_trading_fee(self):
        """
        Calculate the trading fee based on the sale price and trading fee rate.

        :return: Trading fee (Decimal).
        """
        return (self.sale_price * self.trading_fee_rate / 100).quantize(DECIMAL_PRECISION)

    def calculate_royalty(self):
        """
        Calculate the royalty based on the sale price and royalty rate.

        :return: Royalty amount (Decimal).
        """
        return (self.sale_price * self.royalty_rate / 100).quantize(DECIMAL_PRECISION)

    def calculate_net_amount(self):
        """
        Calculate the net amount received by the seller after deducting
        trading fees and royalties.

        :return: Net amount (Decimal).
        """
        trading_fee = self.calculate_trading_fee()
        royalty = self.calculate_royalty()
        return (self.sale_price - trading_fee - royalty).quantize(DECIMAL_PRECISION)

def main():
    """
    Main function to demonstrate the NFTTransaction class functionality.
    Users can input sale price, trading fee rate, and royalty rate to calculate
    the trading fees, royalties, and net amount.
    """
    try:
        print("Welcome to NFT Transaction Fee Calculator (Open Creator Protocol).")

        # Input values
        sale_price = decimal.Decimal(input("Enter the sale price of the NFT: "))
        trading_fee_rate = decimal.Decimal(input("Enter the trading fee rate (e.g., 2.5 for 2.5%): "))
        royalty_rate = decimal.Decimal(input("Enter the royalty rate (e.g., 10 for 10%): "))

        # Create an NFTTransaction instance
        transaction = NFTTransaction(sale_price, trading_fee_rate, royalty_rate)

        # Perform calculations
        trading_fee = transaction.calculate_trading_fee()
        royalty = transaction.calculate_royalty()
        net_amount = transaction.calculate_net_amount()

        # Output results
        print("\nTransaction Summary:")
        print(f"Sale Price: {sale_price}")
        print(f"Trading Fee ({trading_fee_rate}%): {trading_fee}")
        print(f"Royalty ({royalty_rate}%): {royalty}")
        print(f"Net Amount: {net_amount}")

    except decimal.InvalidOperation:
        print("Error: Please enter valid decimal numbers.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
```
