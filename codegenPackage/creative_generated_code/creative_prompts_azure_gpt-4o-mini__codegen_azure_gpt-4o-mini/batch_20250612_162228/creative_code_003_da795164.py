"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://whitelist-runecoin.pages.dev
Prompt: Generate a function that calculates the limit per buy and sell for tokens in a swap pool like OpenRunes.
Generated: DETERMINISTIC_da795164c1f0fbbf
Batch ID: 20250612_162228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class SwapPool:
    """
    Class to represent a token swap pool.
    """

    def __init__(self, token_a_balance: float, token_b_balance: float):
        """
        Initialize the swap pool with token balances.

        :param token_a_balance: Initial balance of token A in the pool.
        :param token_b_balance: Initial balance of token B in the pool.
        """
        if token_a_balance < 0 or token_b_balance < 0:
            raise ValueError("Token balances must be non-negative.")
        
        self.token_a_balance = token_a_balance
        self.token_b_balance = token_b_balance

    def calculate_limit_per_buy(self, amount_in: float) -> float:
        """
        Calculate the limit of token B that can be bought with a given amount
        of token A, based on the current pool balances.

        :param amount_in: Amount of token A to swap.
        :return: Limit of token B that can be received.
        """
        if amount_in <= 0:
            raise ValueError("Amount in must be greater than zero.")
        
        # Calculate the limit based on the current balances
        limit = (amount_in * self.token_b_balance) / (self.token_a_balance + amount_in)
        return limit

    def calculate_limit_per_sell(self, amount_out: float) -> float:
        """
        Calculate the limit of token A that can be sold for a given amount
        of token B, based on the current pool balances.

        :param amount_out: Amount of token B to swap.
        :return: Limit of token A that can be provided.
        """
        if amount_out <= 0:
            raise ValueError("Amount out must be greater than zero.")
        
        # Calculate the limit based on the current balances
        limit = (amount_out * self.token_a_balance) / (self.token_b_balance - amount_out)
        return limit

# Example usage:
if __name__ == "__main__":
    try:
        # Create a swap pool with initial balances
        pool = SwapPool(token_a_balance=1000.0, token_b_balance=500.0)

        # Calculate limits for buying and selling
        buy_limit = pool.calculate_limit_per_buy(amount_in=50.0)
        print(f"Limit of token B that can be bought: {buy_limit}")

        sell_limit = pool.calculate_limit_per_sell(amount_out=30.0)
        print(f"Limit of token A that can be sold: {sell_limit}")

    except ValueError as e:
        print(f"Error: {e}")
```
