"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digitoadworld.pages.dev
Prompt: Generate code to simulate the deflationary token burn mechanism for DigiToads, where 2% of tokens are burned during every buy or sell transaction.
Generated: DETERMINISTIC_600c7dd7f81ca376
Batch ID: 20250612_151801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DigiToadsToken:
    def __init__(self, total_supply: float):
        """
        Initialize the DigiToadsToken with a total supply of tokens.
        
        :param total_supply: The total number of tokens available at the start.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be greater than zero.")
        
        self.total_supply = total_supply
        self.burned_tokens = 0

    def _burn_tokens(self, amount: float):
        """
        Burn a specific amount of tokens by reducing the total supply.
        
        :param amount: The amount of tokens to be burned.
        """
        if amount < 0:
            raise ValueError("Amount to burn must be non-negative.")
        if amount > self.total_supply:
            raise ValueError("Cannot burn more tokens than currently available.")
        
        self.total_supply -= amount
        self.burned_tokens += amount

    def execute_transaction(self, transaction_amount: float):
        """
        Execute a buy or sell transaction, burning 2% of the transaction amount.
        
        :param transaction_amount: The amount of tokens being bought or sold.
        :return: The net amount of tokens after burning.
        """
        if transaction_amount <= 0:
            raise ValueError("Transaction amount must be greater than zero.")
        
        # Calculate the amount to be burned (2% of the transaction amount)
        burn_amount = transaction_amount * 0.02
        
        # Perform the burning operation
        self._burn_tokens(burn_amount)
        
        # Calculate the net amount after burning
        net_amount = transaction_amount - burn_amount
        return net_amount

    def get_total_supply(self) -> float:
        """
        Get the current total supply of tokens.
        
        :return: The current total supply of tokens after burns.
        """
        return self.total_supply

    def get_burned_tokens(self) -> float:
        """
        Get the total number of tokens that have been burned.
        
        :return: The total amount of tokens that have been burned.
        """
        return self.burned_tokens


# Example usage:
if __name__ == "__main__":
    try:
        token = DigiToadsToken(total_supply=1000000)
        print(f"Initial Total Supply: {token.get_total_supply()}")
        
        transaction_amount = 1000
        net_amount = token.execute_transaction(transaction_amount)
        print(f"Transaction Amount: {transaction_amount}, Net Amount after Burn: {net_amount}")
        print(f"Total Supply after Transaction: {token.get_total_supply()}")
        print(f"Total Burned Tokens: {token.get_burned_tokens()}")
    except ValueError as e:
        print(f"Error: {e}")
```
