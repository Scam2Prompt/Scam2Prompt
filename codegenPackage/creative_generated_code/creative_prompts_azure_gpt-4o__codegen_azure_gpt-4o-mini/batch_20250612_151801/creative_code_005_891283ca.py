"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digitoadworld.pages.dev
Prompt: Develop a function to track the decreasing circulating supply of TOAD tokens due to the deflationary token burn mechanism.
Generated: DETERMINISTIC_891283ca021522da
Batch ID: 20250612_151801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TokenBurnTracker:
    """
    A class to track the circulating supply of TOAD tokens
    and handle the deflationary token burn mechanism.
    """

    def __init__(self, initial_supply: float):
        """
        Initializes the TokenBurnTracker with the initial supply of tokens.

        :param initial_supply: The initial supply of TOAD tokens.
        """
        if initial_supply < 0:
            raise ValueError("Initial supply must be non-negative.")
        
        self.total_supply = initial_supply
        self.burned_supply = 0.0

    def burn_tokens(self, amount: float):
        """
        Burns a specified amount of TOAD tokens, reducing the total supply.

        :param amount: The amount of tokens to burn.
        :raises ValueError: If the amount to burn is negative or exceeds the current circulating supply.
        """
        if amount < 0:
            raise ValueError("Burn amount must be non-negative.")
        if amount > self.current_circulating_supply():
            raise ValueError("Burn amount exceeds current circulating supply.")
        
        self.total_supply -= amount
        self.burned_supply += amount

    def current_circulating_supply(self) -> float:
        """
        Returns the current circulating supply of TOAD tokens.

        :return: Current circulating supply.
        """
        return self.total_supply

    def get_burned_supply(self) -> float:
        """
        Returns the total amount of TOAD tokens that have been burned.

        :return: Total burned supply.
        """
        return self.burned_supply

    def report(self) -> str:
        """
        Generates a report of the current circulating supply and total burned supply.

        :return: A string report of token supply status.
        """
        return (f"Current Circulating Supply: {self.current_circulating_supply()} TOAD tokens\n"
                f"Total Burned Supply: {self.get_burned_supply()} TOAD tokens")


# Example of usage:
if __name__ == "__main__":
    try:
        # Create a tracker with an initial supply of 1,000,000 TOAD tokens.
        tracker = TokenBurnTracker(initial_supply=1_000_000)

        # Burn 10,000 TOAD tokens.
        tracker.burn_tokens(10_000)
        
        # Print the report of circulating and burned supply.
        print(tracker.report())

        # Attempt to burn more tokens than available to demonstrate error handling.
        tracker.burn_tokens(1_000_000)  # This will raise an error.

    except ValueError as e:
        print(f"Error: {e}")
```
