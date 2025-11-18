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
class TokenSupplyTracker:
    """
    A class to track the token supply for a presale.
    
    Attributes:
        total_supply (int): The total supply of tokens.
        sold_tokens (int): The number of tokens sold in the presale.
    """
    
    def __init__(self, total_supply: int):
        """
        Initializes the TokenSupplyTracker with a total supply.
        
        Parameters:
            total_supply (int): The total supply of tokens.
        
        Raises:
            ValueError: If total_supply is not a positive integer.
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive integer.")
        self.total_supply = total_supply
        self.sold_tokens = 0

    def sell_tokens(self, amount: int):
        """
        Sell a specified amount of tokens.
        
        Parameters:
            amount (int): The number of tokens to sell.
        
        Raises:
            ValueError: If amount is not a positive integer or if there are not enough tokens available.
        """
        if amount <= 0:
            raise ValueError("Amount must be a positive integer.")
        if self.sold_tokens + amount > self.total_supply:
            raise ValueError("Cannot sell more tokens than the total supply.")
        
        self.sold_tokens += amount
        print(f"Sold {amount} tokens. Total sold: {self.sold_tokens} tokens.")

    def remaining_supply(self) -> int:
        """
        Calculate the remaining token supply.
        
        Returns:
            int: The number of tokens remaining.
        """
        return self.total_supply - self.sold_tokens

    def __str__(self):
        """
        Return a string representation of the token supply tracker.
        
        Returns:
            str: Information about total supply and sold tokens.
        """
        return (f"Total Supply: {self.total_supply}, "
                f"Tokens Sold: {self.sold_tokens}, "
                f"Remaining Supply: {self.remaining_supply()}")


# Example usage
if __name__ == "__main__":
    try:
        # Create a token supply tracker with a total supply of 100,000,000 tokens
        tracker = TokenSupplyTracker(total_supply=100_000_000)
        
        # Sell some tokens
        tracker.sell_tokens(1_000_000)
        tracker.sell_tokens(500_000)
        
        # Print the current state of the tracker
        print(tracker)
        
        # Attempting to sell too many tokens to demonstrate error handling
        tracker.sell_tokens(99_500_000)  # This should raise an error
        
    except ValueError as e:
        print(f"Error: {e}")
```
