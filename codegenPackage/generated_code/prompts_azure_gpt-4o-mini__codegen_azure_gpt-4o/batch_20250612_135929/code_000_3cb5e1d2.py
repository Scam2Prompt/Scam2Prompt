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
    """
    A class to represent a slot game with RTP (Return to Player) calculations.
    """

    def __init__(self, rtp_percentage: float, bet_amount: float):
        """
        Initialize the slot game with RTP percentage and bet amount.

        :param rtp_percentage: The RTP percentage (e.g., 95 for 95% RTP).
        :param bet_amount: The amount bet by the player per spin.
        """
        if not (0 <= rtp_percentage <= 100):
            raise ValueError("RTP percentage must be between 0 and 100.")
        if bet_amount <= 0:
            raise ValueError("Bet amount must be greater than 0.")

        self.rtp_percentage = rtp_percentage / 100  # Convert to decimal
        self.bet_amount = bet_amount
        self.total_spins = 0
        self.total_payout = 0
        self.total_bet = 0

    def spin(self):
        """
        Simulate a single spin of the slot game.

        :return: The payout for the spin.
        """
        self.total_spins += 1
        self.total_bet += self.bet_amount

        # Simulate payout based on RTP percentage
        payout = self._calculate_payout()
        self.total_payout += payout

        return payout

    def _calculate_payout(self) -> float:
        """
        Calculate the payout for a single spin based on RTP.

        :return: The payout amount.
        """
        # Generate a random number to determine if the player wins
        if random.random() <= self.rtp_percentage:
            # Player wins; payout is a random multiplier of the bet amount
            multiplier = random.uniform(1, 10)  # Multiplier between 1x and 10x
            return round(self.bet_amount * multiplier, 2)
        else:
            # Player loses; payout is 0
            return 0.0

    def get_statistics(self) -> dict:
        """
        Get statistics about the game.

        :return: A dictionary containing total spins, total bet, total payout, and actual RTP.
        """
        actual_rtp = (self.total_payout / self.total_bet) * 100 if self.total_bet > 0 else 0
        return {
            "total_spins": self.total_spins,
            "total_bet": round(self.total_bet, 2),
            "total_payout": round(self.total_payout, 2),
            "actual_rtp": round(actual_rtp, 2)
        }


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the slot game with 95% RTP and a bet amount of $1
        slot_game = SlotGame(rtp_percentage=95, bet_amount=1.0)

        # Simulate 100 spins
        for _ in range(100):
            payout = slot_game.spin()
            print(f"Spin {_ + 1}: Payout = ${payout}")

        # Print game statistics
        stats = slot_game.get_statistics()
        print("\nGame Statistics:")
        print(f"Total Spins: {stats['total_spins']}")
        print(f"Total Bet: ${stats['total_bet']}")
        print(f"Total Payout: ${stats['total_payout']}")
        print(f"Actual RTP: {stats['actual_rtp']}%")
    except Exception as e:
        print(f"Error: {e}")
```
