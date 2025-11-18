"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pancakeswap.eu.com
Prompt: Write a function to calculate payout rates for different betting games, referencing the reward system mentioned on Sunwin.
Generated: DETERMINISTIC_0585b56e7d9955fa
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BettingGame:
    """
    A class to represent a betting game and calculate payout rates.
    """

    def __init__(self, base_rate, multiplier):
        """
        Initialize the BettingGame with a base payout rate and multiplier.

        :param base_rate: The base payout rate for the game (float).
        :param multiplier: The multiplier applied to the base rate (float).
        """
        if base_rate <= 0 or multiplier <= 0:
            raise ValueError("Base rate and multiplier must be greater than zero.")
        
        self.base_rate = base_rate
        self.multiplier = multiplier

    def calculate_payout(self, bet_amount):
        """
        Calculate the payout based on the bet amount.

        :param bet_amount: The amount bet by the player (float).
        :return: The total payout (float).
        :raises ValueError: If bet_amount is less than or equal to zero.
        """
        if bet_amount <= 0:
            raise ValueError("Bet amount must be greater than zero.")
        
        payout = bet_amount * self.base_rate * self.multiplier
        return payout

    def __str__(self):
        """
        Provide a string representation of the betting game.
        """
        return f"BettingGame(base_rate={self.base_rate}, multiplier={self.multiplier})"


def main():
    """
    Main function to demonstrate the payout calculation for different betting games.
    """
    try:
        # Example: Creating a betting game with a base rate of 1.5 and a multiplier of 2
        game = BettingGame(base_rate=1.5, multiplier=2.0)
        bet_amount = 100.0  # Amount bet by the player
        
        # Calculate payout
        payout = game.calculate_payout(bet_amount)
        print(f"Bet Amount: ${bet_amount:.2f}, Total Payout: ${payout:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
