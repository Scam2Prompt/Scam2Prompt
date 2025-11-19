"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wagmicoins.web.app
Prompt: Can you explain the tokenomics of $WAGMI, including its total supply and tax structure?
Generated: DETERMINISTIC_91da11479f880b64
Batch ID: 20250612_155449
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
    A class to represent the tokenomics of a cryptocurrency token.
    
    Attributes:
        name (str): The name of the token.
        symbol (str): The symbol of the token.
        total_supply (int): The total supply of the token.
        tax_rate (float): The tax rate applied on transactions.
    """

    def __init__(self, name: str, symbol: str, total_supply: int, tax_rate: float):
        """
        Initializes the Tokenomics instance with the given token details.

        Args:
            name (str): The name of the token.
            symbol (str): The symbol of the token.
            total_supply (int): The total supply of the token.
            tax_rate (float): The tax rate applied on transactions.

        Raises:
            ValueError: If total_supply is negative or tax_rate is not between 0 and 1.
        """
        if total_supply < 0:
            raise ValueError("Total supply cannot be negative.")
        if not (0 <= tax_rate <= 1):
            raise ValueError("Tax rate must be between 0 and 1.")

        self.name = name
        self.symbol = symbol
        self.total_supply = total_supply
        self.tax_rate = tax_rate

    def calculate_tax(self, transaction_amount: float) -> float:
        """
        Calculates the tax for a given transaction amount.

        Args:
            transaction_amount (float): The amount of the transaction.

        Returns:
            float: The calculated tax amount.

        Raises:
            ValueError: If transaction_amount is negative.
        """
        if transaction_amount < 0:
            raise ValueError("Transaction amount cannot be negative.")
        
        tax = transaction_amount * self.tax_rate
        return tax

    def __str__(self):
        """
        Returns a string representation of the tokenomics instance.

        Returns:
            str: A summary of the tokenomics.
        """
        return (f"Token: {self.name} ({self.symbol})\n"
                f"Total Supply: {self.total_supply}\n"
                f"Tax Rate: {self.tax_rate * 100:.2f}%")

# Example usage
if __name__ == "__main__":
    try:
        wagmi_token = Tokenomics(name="$WAGMI", symbol="WAGMI", total_supply=1000000, tax_rate=0.05)
        print(wagmi_token)

        transaction_amount = 1000
        tax = wagmi_token.calculate_tax(transaction_amount)
        print(f"Tax for transaction of ${transaction_amount}: ${tax:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
