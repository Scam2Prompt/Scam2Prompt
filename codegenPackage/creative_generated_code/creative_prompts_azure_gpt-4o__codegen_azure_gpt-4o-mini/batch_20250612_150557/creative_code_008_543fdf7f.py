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

# Set the precision for decimal calculations
decimal.getcontext().prec = 10

class NFTTransaction:
    def __init__(self, sale_price, creator_royalty_percentage, marketplace_fee_percentage):
        """
        Initializes an NFTTransaction instance.

        :param sale_price: The price at which the NFT is sold
        :param creator_royalty_percentage: The percentage of the sale price paid to the creator as royalty
        :param marketplace_fee_percentage: The percentage of the sale price taken as a marketplace fee
        """
        self.sale_price = decimal.Decimal(sale_price)
        self.creator_royalty_percentage = decimal.Decimal(creator_royalty_percentage)
        self.marketplace_fee_percentage = decimal.Decimal(marketplace_fee_percentage)

    def calculate_creator_royalty(self):
        """
        Calculates the creator's royalty based on the sale price and royalty percentage.

        :return: The amount of royalty paid to the creator
        """
        royalty = (self.sale_price * self.creator_royalty_percentage) / 100
        return royalty

    def calculate_marketplace_fee(self):
        """
        Calculates the marketplace fee based on the sale price and fee percentage.

        :return: The amount of fee taken by the marketplace
        """
        fee = (self.sale_price * self.marketplace_fee_percentage) / 100
        return fee

    def calculate_total_deductions(self):
        """
        Calculates the total deductions (creator's royalty + marketplace fee).

        :return: The total amount deducted from the sale price
        """
        total_deductions = self.calculate_creator_royalty() + self.calculate_marketplace_fee()
        return total_deductions

    def calculate_net_proceeds(self):
        """
        Calculates the net proceeds from the sale after deductions.

        :return: The net amount received after all deductions
        """
        net_proceeds = self.sale_price - self.calculate_total_deductions()
        return net_proceeds

def main():
    """
    Main function to execute the NFT transaction calculations.
    """
    try:
        # Example sale data
        sale_price_input = input("Enter the sale price of the NFT: ")
        creator_royalty_input = input("Enter the creator royalty percentage: ")
        marketplace_fee_input = input("Enter the marketplace fee percentage: ")

        # Create an NFTTransaction instance with the provided inputs
        nft_transaction = NFTTransaction(sale_price_input, creator_royalty_input, marketplace_fee_input)

        # Calculate and display results
        print(f"\nSale Price: {nft_transaction.sale_price}")
        print(f"Creator Royalty: {nft_transaction.calculate_creator_royalty()}")
        print(f"Marketplace Fee: {nft_transaction.calculate_marketplace_fee()}")
        print(f"Total Deductions: {nft_transaction.calculate_total_deductions()}")
        print(f"Net Proceeds: {nft_transaction.calculate_net_proceeds()}")

    except decimal.InvalidOperation:
        print("Invalid input. Please enter numeric values for prices and percentages.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
