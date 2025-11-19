"""
Generated Code Metadata:
========================
Original URL: https://www.uhcstepup.com
Prompt: How can I create a demo version of a slot game that includes a "Mahjong Wins" theme and high RTP, as described on SLOT138?
Generated: DETERMINISTIC_e353837bcd56a24f
Batch ID: 20250612_163438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class SlotGame:
    """
    A demo version of a slot game with a "Mahjong Wins" theme and high RTP.
    """

    def __init__(self):
        # Initialize the slot game with a set of reels and a payout table
        self.reels = 5
        self.symbols = ['Mahjong Tile 1', 'Mahjong Tile 2', 'Mahjong Tile 3', 'Mahjong Tile 4', 'Mahjong Tile 5',
                       'Chinese Coin', 'Fan', 'Lantern', 'Scatter', 'Wild']
        self.payout_table = {
            'Mahjong Tile 1': 10,
            'Mahjong Tile 2': 20,
            'Mahjong Tile 3': 30,
            'Mahjong Tile 4': 40,
            'Mahjong Tile 5': 50,
            'Chinese Coin': 5,
            'Fan': 10,
            'Lantern': 20,
            'Scatter': 50,
            'Wild': 100
        }
        self.rtp = 0.95  # High RTP

    def spin(self, bet):
        """
        Simulate a spin of the slot game.

        Args:
            bet (float): The player's bet.

        Returns:
            dict: A dictionary containing the spin result and payout.
        """
        try:
            # Validate the bet
            if bet <= 0:
                raise ValueError("Invalid bet. Bet must be greater than zero.")

            # Generate a random spin result
            spin_result = [random.choice(self.symbols) for _ in range(self.reels)]

            # Calculate the payout
            payout = self.calculate_payout(spin_result, bet)

            return {'spin_result': spin_result, 'payout': payout}

        except Exception as e:
            # Handle any exceptions that occur during the spin
            return {'error': str(e)}

    def calculate_payout(self, spin_result, bet):
        """
        Calculate the payout for a given spin result.

        Args:
            spin_result (list): The result of the spin.
            bet (float): The player's bet.

        Returns:
            float: The payout for the spin result.
        """
        # Check for winning combinations
        if len(set(spin_result)) == 1:  # All symbols are the same
            # Jackpot!
            return bet * 10
        elif 'Scatter' in spin_result:
            # Scatter payout
            return bet * self.payout_table['Scatter']
        elif 'Wild' in spin_result:
            # Wild payout
            return bet * self.payout_table['Wild']
        else:
            # Calculate the payout based on the symbols in the spin result
            payout = 0
            for symbol in spin_result:
                payout += self.payout_table[symbol]
            return bet * payout * self.rtp


def main():
    game = SlotGame()
    bet = 10.0
    result = game.spin(bet)
    if 'error' in result:
        print(f"Error: {result['error']}")
    else:
        print(f"Spin Result: {result['spin_result']}")
        print(f"Payout: {result['payout']}")


if __name__ == "__main__":
    main()
```
