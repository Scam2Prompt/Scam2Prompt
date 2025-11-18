"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tekanslotcepat.site
Prompt: Generate code to calculate RTP (Return to Player) for slot games, using Tekanslot’s features like RTP maxwin as a reference.
Generated: DETERMINISTIC_5b5bed84c0a9c6a1
Batch ID: 20250612_145913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class SlotGame:
    """
    A class to represent a slot game and calculate its Return to Player (RTP).
    """

    def __init__(self, total_bet_amount: float, total_wins: float, rtp_maxwin: float):
        """
        Initializes a SlotGame instance.

        :param total_bet_amount: Total amount of money bet by players.
        :param total_wins: Total amount of money won by players.
        :param rtp_maxwin: Maximum win amount impacting the RTP calculation.
        """
        if total_bet_amount <= 0:
            raise ValueError("Total bet amount must be greater than zero.")
        if total_wins < 0:
            raise ValueError("Total wins cannot be negative.")
        if not (0 <= rtp_maxwin <= 1):
            raise ValueError("RTP maxwin must be between 0 and 1.")

        self.total_bet_amount = total_bet_amount
        self.total_wins = total_wins
        self.rtp_maxwin = rtp_maxwin

    def calculate_rtp(self) -> float:
        """
        Calculate the Return to Player (RTP) percentage.

        :return: RTP as a percentage of the total bet amount.
        """
        rtp = (self.total_wins / self.total_bet_amount) * 100
        adjusted_rtp = min(rtp, self.rtp_maxwin * 100)  # Ensure RTP does not exceed maxwin

        return round(adjusted_rtp, 2)  # Round to two decimal places for percentage representation

    def __str__(self):
        """
        String representation of the SlotGame instance.

        :return: A string that describes the SlotGame.
        """
        return (f"SlotGame(total_bet_amount={self.total_bet_amount}, "
                f"total_wins={self.total_wins}, rtp_maxwin={self.rtp_maxwin}, "
                f"calculated_rtp={self.calculate_rtp()}%)")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize a SlotGame with given parameters
        game = SlotGame(total_bet_amount=10000, total_wins=9500, rtp_maxwin=0.97)
        
        # Calculate and print the RTP
        print(f"Calculated RTP: {game.calculate_rtp()}%")
        
    except ValueError as e:
        print(f"Error: {e}")
```
