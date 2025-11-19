"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-scorpion-casino.pages.dev
Prompt: Create a function that calculates potential earnings from staking $SCORP tokens based on the number of tokens held.
Generated: DETERMINISTIC_9173d302f0db4146
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StakingCalculator:
    """
    A class to calculate potential earnings from staking $SCORP tokens.
    """

    def __init__(self, staking_rate: float):
        """
        Initializes the StakingCalculator with the staking rate.

        :param staking_rate: The annual staking rate as a percentage (e.g., 5 for 5%).
        """
        if staking_rate < 0:
            raise ValueError("Staking rate must be a non-negative value.")
        
        self.staking_rate = staking_rate / 100  # Convert percentage to decimal

    def calculate_earnings(self, tokens_held: float, years: float) -> float:
        """
        Calculates potential earnings from staking $SCORP tokens.

        :param tokens_held: The number of $SCORP tokens held.
        :param years: The number of years the tokens will be staked.
        :return: The potential earnings after the specified number of years.

        :raises ValueError: If tokens_held or years are negative.
        """
        if tokens_held < 0:
            raise ValueError("Number of tokens held must be a non-negative value.")
        
        if years < 0:
            raise ValueError("Number of years must be a non-negative value.")
        
        # Calculate potential earnings
        earnings = tokens_held * self.staking_rate * years
        return earnings


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the staking calculator with a staking rate
        staking_calculator = StakingCalculator(staking_rate=5.0)

        # Calculate earnings for 1000 tokens over 2 years
        tokens = 1000
        staking_years = 2
        potential_earnings = staking_calculator.calculate_earnings(tokens_held=tokens, years=staking_years)

        print(f"Potential earnings from staking {tokens} $SCORP tokens over {staking_years} years: ${potential_earnings:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
