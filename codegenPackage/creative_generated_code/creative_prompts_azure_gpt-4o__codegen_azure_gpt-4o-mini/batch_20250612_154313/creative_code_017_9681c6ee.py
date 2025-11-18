"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lidofi.us.com
Prompt: Generate code in Python to calculate the odds for WW88's "Kèo Châu Âu" bets, using the site's explanation of 1x2 betting.
Generated: DETERMINISTIC_9681c6eeeddc6ecb
Batch ID: 20250612_154313
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class EuropeanOddsCalculator:
    """
    A class to calculate the potential winnings based on European odds (1x2 betting).
    
    Attributes:
        odds (dict): A dictionary containing the odds for home win, draw, and away win.
    """

    def __init__(self, home_odds: float, draw_odds: float, away_odds: float):
        """
        Initializes the EuropeanOddsCalculator with the given odds.

        Args:
            home_odds (float): The odds for the home team to win.
            draw_odds (float): The odds for the match to end in a draw.
            away_odds (float): The odds for the away team to win.

        Raises:
            ValueError: If any of the odds are less than or equal to zero.
        """
        if home_odds <= 0 or draw_odds <= 0 or away_odds <= 0:
            raise ValueError("Odds must be greater than zero.")

        self.odds = {
            'home': home_odds,
            'draw': draw_odds,
            'away': away_odds
        }

    def calculate_potential_winnings(self, stake: float, bet_type: str) -> float:
        """
        Calculates the potential winnings based on the stake and bet type.

        Args:
            stake (float): The amount of money placed on the bet.
            bet_type (str): The type of bet ('home', 'draw', or 'away').

        Returns:
            float: The potential winnings if the bet is successful.

        Raises:
            ValueError: If the bet type is invalid.
        """
        if stake <= 0:
            raise ValueError("Stake must be greater than zero.")

        bet_type = bet_type.lower()

        if bet_type not in self.odds:
            raise ValueError("Invalid bet type. Choose 'home', 'draw', or 'away'.")

        # Calculate potential winnings
        potential_winnings = stake * self.odds[bet_type]
        return potential_winnings

    def __str__(self):
        """Returns a string representation of the odds."""
        return f"Odds: Home - {self.odds['home']}, Draw - {self.odds['draw']}, Away - {self.odds['away']}"

# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the calculator with example odds
        calculator = EuropeanOddsCalculator(home_odds=2.5, draw_odds=3.2, away_odds=2.8)

        # Display the odds
        print(calculator)

        # Calculate potential winnings for a home win bet
        stake = 100  # example stake
        bet_type = 'home'
        winnings = calculator.calculate_potential_winnings(stake, bet_type)
        print(f"Potential winnings for a {bet_type} bet with stake {stake}: {winnings:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
