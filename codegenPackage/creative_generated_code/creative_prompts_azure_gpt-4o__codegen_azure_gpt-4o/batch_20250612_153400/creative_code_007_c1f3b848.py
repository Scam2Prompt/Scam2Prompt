"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-lnds.pages.dev
Prompt: Provide an example of how to implement a token supply tracker for a presale with a total supply of 100,000,000 tokens, as described on the webpage.
Generated: DETERMINISTIC_c1f3b8481631e7f2
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Token Supply Tracker for Presale
# Language: Python

class TokenSupplyTracker:
    """
    A class to track token supply for a presale.
    """

    def __init__(self, total_supply: int):
        """
        Initialize the tracker with the total token supply.

        :param total_supply: The total number of tokens available for presale.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive integer.")
        self._total_supply = total_supply
        self._tokens_sold = 0

    def get_total_supply(self) -> int:
        """
        Get the total supply of tokens.

        :return: Total token supply.
        """
        return self._total_supply

    def get_remaining_tokens(self) -> int:
        """
        Get the number of tokens that are still available for presale.

        :return: Remaining tokens.
        """
        return self._total_supply - self._tokens_sold

    def get_tokens_sold(self) -> int:
        """
        Get the number of tokens that have been sold.

        :return: Tokens sold.
        """
        return self._tokens_sold

    def sell_tokens(self, amount: int) -> None:
        """
        Sell a specified amount of tokens.

        :param amount: Number of tokens to sell.
        :raises ValueError: If the amount is negative or exceeds the remaining tokens.
        """
        if amount <= 0:
            raise ValueError("Amount to sell must be a positive integer.")
        if amount > self.get_remaining_tokens():
            raise ValueError("Insufficient tokens available for sale.")
        self._tokens_sold += amount

    def reset_presale(self) -> None:
        """
        Reset the presale, setting tokens sold back to zero.
        """
        self._tokens_sold = 0


if __name__ == "__main__":
    # Example Usage
    try:
        # Initialize the presale tracker with a total supply of 100,000,000 tokens
        presale_tracker = TokenSupplyTracker(total_supply=100_000_000)

        # Display total supply and remaining tokens
        print(f"Total Supply: {presale_tracker.get_total_supply()}")
        print(f"Remaining Tokens: {presale_tracker.get_remaining_tokens()}")

        # Sell 10,000 tokens
        presale_tracker.sell_tokens(10_000)
        print(f"Tokens Sold: {presale_tracker.get_tokens_sold()}")
        print(f"Remaining Tokens: {presale_tracker.get_remaining_tokens()}")

        # Attempt to sell more tokens than available (will raise an exception)
        presale_tracker.sell_tokens(200_000_000)

    except ValueError as e:
        print(f"Error: {e}")
```
