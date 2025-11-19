"""
Generated Code Metadata:
========================
Original URL: https://maradonacoinz.vercel.app
Prompt: Design a tokenomics structure for a new cryptocurrency, including parameters such as total supply, decimals, and taxes, inspired by Hand of Pepe's $HOPE token.
Generated: DETERMINISTIC_d12505297a8da253
Batch ID: 20250622_210803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from decimal import Decimal

class Tokenomics:
    """
    A class to represent the tokenomics structure of a cryptocurrency.
    
    Attributes:
        total_supply (Decimal): The total supply of the token.
        decimals (int): The number of decimal places for the token.
        tax_rate (Decimal): The tax rate applied to transactions.
        burn_rate (Decimal): The rate at which tokens are burned.
        liquidity_rate (Decimal): The rate at which tokens are allocated to liquidity.
    """

    def __init__(self, total_supply: int, decimals: int, tax_rate: float, burn_rate: float, liquidity_rate: float):
        """
        Initializes the Tokenomics structure with the given parameters.
        
        Args:
            total_supply (int): The total supply of the token.
            decimals (int): The number of decimal places for the token.
            tax_rate (float): The tax rate applied to transactions (as a percentage).
            burn_rate (float): The rate at which tokens are burned (as a percentage).
            liquidity_rate (float): The rate at which tokens are allocated to liquidity (as a percentage).
        
        Raises:
            ValueError: If any of the rates are negative or if total_supply is non-positive.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive integer.")
        if not (0 <= tax_rate <= 100):
            raise ValueError("Tax rate must be between 0 and 100.")
        if not (0 <= burn_rate <= 100):
            raise ValueError("Burn rate must be between 0 and 100.")
        if not (0 <= liquidity_rate <= 100):
            raise ValueError("Liquidity rate must be between 0 and 100.")

        self.total_supply = Decimal(total_supply)
        self.decimals = decimals
        self.tax_rate = Decimal(tax_rate) / Decimal(100)
        self.burn_rate = Decimal(burn_rate) / Decimal(100)
        self.liquidity_rate = Decimal(liquidity_rate) / Decimal(100)

    def calculate_tax(self, amount: Decimal) -> Decimal:
        """
        Calculates the tax for a given transaction amount.
        
        Args:
            amount (Decimal): The transaction amount.
        
        Returns:
            Decimal: The calculated tax amount.
        """
        return amount * self.tax_rate

    def calculate_burn(self, amount: Decimal) -> Decimal:
        """
        Calculates the amount to be burned from a given transaction amount.
        
        Args:
            amount (Decimal): The transaction amount.
        
        Returns:
            Decimal: The calculated burn amount.
        """
        return amount * self.burn_rate

    def calculate_liquidity(self, amount: Decimal) -> Decimal:
        """
        Calculates the amount to be allocated to liquidity from a given transaction amount.
        
        Args:
            amount (Decimal): The transaction amount.
        
        Returns:
            Decimal: The calculated liquidity amount.
        """
        return amount * self.liquidity_rate

    def __str__(self):
        """
        Returns a string representation of the Tokenomics structure.
        
        Returns:
            str: A string summarizing the tokenomics parameters.
        """
        return (f"Tokenomics(total_supply={self.total_supply}, decimals={self.decimals}, "
                f"tax_rate={self.tax_rate * 100}%, burn_rate={self.burn_rate * 100}%, "
                f"liquidity_rate={self.liquidity_rate * 100}%)")

# Example usage
if __name__ == "__main__":
    try:
        # Create a Tokenomics instance for the $HOPE token
        hope_token = Tokenomics(total_supply=1000000, decimals=18, tax_rate=5.0, burn_rate=2.0, liquidity_rate=3.0)
        
        # Print the tokenomics structure
        print(hope_token)

        # Example transaction amount
        transaction_amount = Decimal('100.00')

        # Calculate and print tax, burn, and liquidity amounts
        tax = hope_token.calculate_tax(transaction_amount)
        burn = hope_token.calculate_burn(transaction_amount)
        liquidity = hope_token.calculate_liquidity(transaction_amount)

        print(f"Transaction Amount: {transaction_amount}")
        print(f"Tax Amount: {tax}")
        print(f"Burn Amount: {burn}")
        print(f"Liquidity Amount: {liquidity}")

    except ValueError as e:
        print(f"Error: {e}")
```
