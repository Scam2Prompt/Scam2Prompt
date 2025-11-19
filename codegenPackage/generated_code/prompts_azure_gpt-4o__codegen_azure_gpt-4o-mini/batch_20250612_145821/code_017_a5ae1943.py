"""
Generated Code Metadata:
========================
Original URL: https://shibariumdao.io
Prompt: Write a function to calculate payouts for various betting types in a casino game, such as Baccarat or Roulette, inspired by S666's live casino offerings.
Generated: DETERMINISTIC_a5ae19430d60fe65
Batch ID: 20250612_145821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CasinoBetting:
    """
    A class to calculate payouts for various betting types in a casino game.
    Supported games: Baccarat, Roulette.
    """

    def __init__(self):
        # Define payout multipliers for different betting types
        self.payouts = {
            'baccarat': {
                'player': 1.0,
                'banker': 0.95,
                'tie': 8.0
            },
            'roulette': {
                'straight': 35.0,
                'split': 17.0,
                'street': 11.0,
                'corner': 8.0,
                'line': 5.0,
                'dozen': 2.0,
                'column': 2.0,
                'even_odd': 1.0,
                'red_black': 1.0
            }
        }

    def calculate_payout(self, game_type, bet_type, bet_amount):
        """
        Calculate the payout for a given bet in a specified game.

        :param game_type: str - The type of game ('baccarat' or 'roulette')
        :param bet_type: str - The type of bet (e.g., 'player', 'banker' for baccarat; 'straight', 'split' for roulette)
        :param bet_amount: float - The amount of the bet
        :return: float - The total payout amount, including the original bet
        :raises ValueError: If the game type or bet type is invalid
        :raises TypeError: If bet_amount is not a number
        """
        # Validate input types
        if not isinstance(bet_amount, (int, float)) or bet_amount < 0:
            raise TypeError("bet_amount must be a non-negative number.")

        # Validate game type
        if game_type not in self.payouts:
            raise ValueError(f"Invalid game type: {game_type}. Supported types: {list(self.payouts.keys())}")

        # Validate bet type
        if bet_type not in self.payouts[game_type]:
            raise ValueError(f"Invalid bet type: {bet_type}. Supported types: {list(self.payouts[game_type].keys())}")

        # Calculate payout
        payout_multiplier = self.payouts[game_type][bet_type]
        total_payout = bet_amount * payout_multiplier + bet_amount  # Include original bet

        return total_payout

# Example usage
if __name__ == "__main__":
    betting = CasinoBetting()
    try:
        # Calculate payout for a player bet in baccarat
        payout = betting.calculate_payout('baccarat', 'player', 100)
        print(f"Baccarat Player Bet Payout: ${payout:.2f}")

        # Calculate payout for a straight bet in roulette
        payout = betting.calculate_payout('roulette', 'straight', 10)
        print(f"Roulette Straight Bet Payout: ${payout:.2f}")

    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
```
