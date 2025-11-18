"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dashboard-inqubeta.pages.dev
Prompt: Write a function to calculate the burn rate of $QUBE tokens based on the platform's tokenomics (e.g., 1% for buy tax and 2% for sell tax).
Generated: DETERMINISTIC_da70d55392ded9ea
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Tokenomics:
    """
    A class to represent the tokenomics of the QUBE token.
    Contains methods to calculate the burn rate based on buy and sell tax rates.
    """

    def __init__(self, buy_tax_rate: float, sell_tax_rate: float):
        """
        Initializes the Tokenomics class with specified buy and sell tax rates.

        Parameters:
        buy_tax_rate (float): The tax rate applied on buying tokens in percentage.
        sell_tax_rate (float): The tax rate applied on selling tokens in percentage.
        """
        if not (0 <= buy_tax_rate <= 100) or not (0 <= sell_tax_rate <= 100):
            raise ValueError("Tax rates must be between 0 and 100.")

        self.buy_tax_rate = buy_tax_rate / 100  # Convert percentage to decimal
        self.sell_tax_rate = sell_tax_rate / 100  # Convert percentage to decimal

    def calculate_burn_rate(self, transaction_amount: float, transaction_type: str) -> float:
        """
        Calculates the burn rate for a given transaction amount based on the transaction type.

        Parameters:
        transaction_amount (float): The amount of tokens being bought or sold.
        transaction_type (str): The type of transaction, either "buy" or "sell".

        Returns:
        float: The burn amount that will be deducted from the transaction.

        Raises:
        ValueError: If an invalid transaction type is provided.
        """
        if transaction_amount < 0:
            raise ValueError("Transaction amount must be non-negative.")
        
        if transaction_type not in ['buy', 'sell']:
            raise ValueError("Transaction type must be either 'buy' or 'sell'.")

        if transaction_type == 'buy':
            burn_amount = transaction_amount * self.buy_tax_rate
        else:  # transaction_type == 'sell'
            burn_amount = transaction_amount * self.sell_tax_rate

        return burn_amount


# Example usage:
if __name__ == "__main__":
    try:
        # Create an instance of Tokenomics with specified tax rates
        tokenomics = Tokenomics(buy_tax_rate=1.0, sell_tax_rate=2.0)

        # Calculate burn rate for a buy transaction
        buy_transaction_amount = 1000.0  # Amount of tokens being bought
        buy_burn_rate = tokenomics.calculate_burn_rate(buy_transaction_amount, "buy")
        print(f"Burn rate for buying {buy_transaction_amount} QUBE tokens: {buy_burn_rate}")

        # Calculate burn rate for a sell transaction
        sell_transaction_amount = 500.0  # Amount of tokens being sold
        sell_burn_rate = tokenomics.calculate_burn_rate(sell_transaction_amount, "sell")
        print(f"Burn rate for selling {sell_transaction_amount} QUBE tokens: {sell_burn_rate}")

    except ValueError as e:
        print(f"Error: {e}")
```
