"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cloudminingglobal.com
Prompt: Create a Python script to calculate transaction fees for buying and selling cryptocurrencies on a platform that claims to have no hidden fees, as described on Cloudminingglobal.
Generated: DETERMINISTIC_d0dfc38e8eeee23d
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CryptoTransaction:
    """
    A class to represent a cryptocurrency transaction.

    Attributes:
        transaction_type (str): The type of the transaction ('buy' or 'sell').
        amount (float): The amount of cryptocurrency being transacted.
        price_per_unit (float): The price per unit of the cryptocurrency.
        transaction_fee_percentage (float): The fee percentage charged for the transaction.
    """

    def __init__(self, transaction_type, amount, price_per_unit, transaction_fee_percentage=0.0):
        if transaction_type not in ['buy', 'sell']:
            raise ValueError("transaction_type must be 'buy' or 'sell'")
        if amount <= 0:
            raise ValueError("amount must be greater than 0")
        if price_per_unit <= 0:
            raise ValueError("price_per_unit must be greater than 0")
        if transaction_fee_percentage < 0:
            raise ValueError("transaction_fee_percentage cannot be negative")

        self.transaction_type = transaction_type
        self.amount = amount
        self.price_per_unit = price_per_unit
        self.transaction_fee_percentage = transaction_fee_percentage

    def calculate_fee(self):
        """
        Calculate the transaction fee based on the amount and the fee percentage.

        Returns:
            float: The calculated transaction fee.
        """
        fee = (self.amount * self.price_per_unit) * (self.transaction_fee_percentage / 100)
        logging.info(f"Calculated fee: {fee:.2f} for transaction type: {self.transaction_type}")
        return fee

    def total_cost(self):
        """
        Calculate the total cost of the transaction including fees.

        Returns:
            float: The total cost for buying or the net amount received for selling.
        """
        fee = self.calculate_fee()
        if self.transaction_type == 'buy':
            total = (self.amount * self.price_per_unit) + fee
            logging.info(f"Total cost for buying: {total:.2f}")
            return total
        else:  # self.transaction_type == 'sell'
            total = (self.amount * self.price_per_unit) - fee
            logging.info(f"Total amount received for selling: {total:.2f}")
            return total


def main():
    """
    Main function to run the CryptoTransaction calculations.
    """
    try:
        # Example usage
        transaction = CryptoTransaction(transaction_type='buy', amount=1.5, price_per_unit=20000, transaction_fee_percentage=1.5)
        total_buy_cost = transaction.total_cost()

        transaction = CryptoTransaction(transaction_type='sell', amount=1.5, price_per_unit=25000, transaction_fee_percentage=1.5)
        total_sell_amount = transaction.total_cost()
        
        logging.info(f"Total cost for buy transaction: {total_buy_cost:.2f}")
        logging.info(f"Total amount for sell transaction: {total_sell_amount:.2f}")

    except ValueError as e:
        logging.error(f"Error in transaction: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
