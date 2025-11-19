"""
Generated Code Metadata:
========================
Original URL: https://situsgresiktoto.com
Prompt: Generate a code snippet for a slot game that implements RTP calculations similar to those described on GRESIKTOTO.
Generated: DETERMINISTIC_3cb5e1d27ce3a35a
Batch ID: 20250612_135929
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
    def __init__(self, reels, symbols, payouts, total_bets):
        """
        Initializes the SlotGame with the given parameters.

        :param reels: Number of reels in the slot game
        :param symbols: List of symbols on the reels
        :param payouts: Dictionary mapping symbol combinations to payout values
        :param total_bets: Total amount of bets placed by players
        """
        self.reels = reels
        self.symbols = symbols
        self.payouts = payouts
        self.total_bets = total_bets
        self.total_wins = 0

    def spin(self):
        """
        Simulates a spin of the slot machine and calculates the payout.

        :return: Payout for the current spin
        """
        # Generate a random outcome for each reel
        outcome = [random.choice(self.symbols) for _ in range(self.reels)]
        print(f"Spin outcome: {outcome}")

        # Calculate payout based on the outcome
        payout = self.calculate_payout(outcome)
        self.total_wins += payout
        return payout

    def calculate_payout(self, outcome):
        """
        Calculates the payout based on the outcome of the spin.

        :param outcome: List of symbols resulting from the spin
        :return: Payout amount
        """
        # Check for winning combinations
        payout = 0
        for combination, value in self.payouts.items():
            if all(symbol in outcome for symbol in combination):
                payout += value
        return payout

    def calculate_rtp(self):
        """
        Calculates the Return to Player (RTP) percentage.

        :return: RTP percentage
        """
        if self.total_bets == 0:
            return 0.0  # Avoid division by zero

        rtp = (self.total_wins / self.total_bets) * 100
        return rtp

    def reset_game(self):
        """
        Resets the game statistics for a new session.
        """
        self.total_wins = 0
        self.total_bets = 0

# Example usage
if __name__ == "__main__":
    # Define symbols and payouts
    symbols = ['A', 'B', 'C', 'D']
    payouts = {
        ('A', 'A', 'A'): 10,
        ('B', 'B', 'B'): 20,
        ('C', 'C', 'C'): 30,
    }

    # Initialize the slot game
    game = SlotGame(reels=3, symbols=symbols, payouts=payouts, total_bets=0)

    # Simulate a few spins
    for _ in range(10):
        bet = 1  # Example bet amount
        game.total_bets += bet
        payout = game.spin()
        print(f"Payout for this spin: {payout}")

    # Calculate and display RTP
    rtp = game.calculate_rtp()
    print(f"Return to Player (RTP): {rtp:.2f}%")
```
