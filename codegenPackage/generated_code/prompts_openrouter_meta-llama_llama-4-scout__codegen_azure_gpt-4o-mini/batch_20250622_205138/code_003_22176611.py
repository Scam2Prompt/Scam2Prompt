"""
Generated Code Metadata:
========================
Original URL: https://bibbydivs.com
Prompt: Develop a simple algorithm to calculate the dividend earnings based on the amount of $BIBBY tokens invested and the total dividends distributed.
Generated: DETERMINISTIC_2217661135e9cdc0
Batch ID: 20250622_205138
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class DividendCalculator:
    """
    A class to calculate dividend earnings based on the amount of BIBBY tokens invested
    and the total dividends distributed.
    """

    def __init__(self, total_dividends: float):
        """
        Initializes the DividendCalculator with the total dividends distributed.

        :param total_dividends: Total amount of dividends to be distributed.
        """
        if total_dividends < 0:
            raise ValueError("Total dividends must be a non-negative value.")
        self.total_dividends = total_dividends

    def calculate_earnings(self, tokens_invested: float, total_tokens: float) -> float:
        """
        Calculates the dividend earnings based on the amount of BIBBY tokens invested.

        :param tokens_invested: Amount of BIBBY tokens the user has invested.
        :param total_tokens: Total amount of BIBBY tokens in circulation.
        :return: The dividend earnings for the invested tokens.
        """
        if tokens_invested < 0:
            raise ValueError("Tokens invested must be a non-negative value.")
        if total_tokens <= 0:
            raise ValueError("Total tokens must be a positive value.")
        
        # Calculate the user's share of the total tokens
        share_of_tokens = tokens_invested / total_tokens
        
        # Calculate the earnings based on the user's share of the total dividends
        earnings = share_of_tokens * self.total_dividends
        
        return earnings


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the calculator with total dividends
        total_dividends = 10000.0  # Example total dividends
        calculator = DividendCalculator(total_dividends)

        # User's investment details
        tokens_invested = 500.0  # Example tokens invested by the user
        total_tokens = 10000.0    # Example total tokens in circulation

        # Calculate earnings
        earnings = calculator.calculate_earnings(tokens_invested, total_tokens)
        print(f"Dividend earnings: ${earnings:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
