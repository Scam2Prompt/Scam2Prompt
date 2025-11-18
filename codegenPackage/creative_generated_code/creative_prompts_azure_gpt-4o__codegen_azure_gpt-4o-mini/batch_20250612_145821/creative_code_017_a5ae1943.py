"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shibariumdao.io
Prompt: Write a function to calculate payouts for various betting types in a casino game, such as Baccarat or Roulette, inspired by S666's live casino offerings.
Generated: DETERMINISTIC_a5ae19430d60fe65
Batch ID: 20250612_145821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CasinoGame:
    """
    A class to calculate payouts for various betting types in a casino game.
    Supported games include Baccarat and Roulette.
    """

    def __init__(self):
        # Initialize payout multipliers for different betting types
        self.payouts = {
            'baccarat': {
                'player': 1.0,      # Player wins: 1:1 payout
                'banker': 0.95,     # Banker wins: 0.95:1 payout (5% commission)
                'tie': 8.0          # Tie: 8:1 payout
            },
            'roulette': {
                'single_number': 35.0,    # Single number win: 35:1 payout
                'color': 1.0,              # Color win (red/black): 1:1 payout
                'even_odd': 1.0,           # Even/Odd win: 1:1 payout
                'dozen': 2.0,              # Dozen win: 2:1 payout
                'column': 2.0              # Column win: 2:1 payout
            }
        }

    def calculate_payout(self, game_type, bet_type, bet_amount):
        """
        Calculate the payout based on the game type, bet type, and bet amount.

        :param game_type: Type of the game ('baccarat' or 'roulette')
        :param bet_type: Type of bet (depends on the game type)
        :param bet_amount: Amount of the bet placed
        :return: The total payout amount including the original bet or an error message
        """
        try:
            if game_type not in self.payouts:
                raise ValueError("Invalid game type. Supported types: 'baccarat', 'roulette'.")

            if bet_type not in self.payouts[game_type]:
                raise ValueError(f"Invalid bet type for {game_type}. Supported types: {list(self.payouts[game_type].keys())}.")

            # Calculate payout
            payout_multiplier = self.payouts[game_type][bet_type]
            total_payout = bet_amount * (1 + payout_multiplier)

            return total_payout

        except ValueError as ve:
            return str(ve)
        except Exception as e:
            return f"An error occurred: {str(e)}"

# Example usage
if __name__ == "__main__":
    game = CasinoGame()
    
    # Test bankrolls and bet types
    print(game.calculate_payout('baccarat', 'player', 100))  # Should return 200.0
    print(game.calculate_payout('roulette', 'single_number', 10))  # Should return 360.0
    print(game.calculate_payout('baccarat', 'tie', 50))  # Should return 400.0
    print(game.calculate_payout('roulette', 'color', 20))  # Should return 40.0

    # Test error handling
    print(game.calculate_payout('baccarat', 'invalid_bet', 100))  # Invalid bet type
    print(game.calculate_payout('invalid_game', 'player', 100))  # Invalid game type
```
