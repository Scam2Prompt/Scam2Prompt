"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shubaswap.com
Prompt: Create an algorithm to calculate RTP (Return to Player) for slot games, as highlighted in MESIN128's content.
Generated: DETERMINISTIC_df96af97854407a8
Batch ID: 20250612_152527
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

    def __init__(self, total_bets: float, total_wins: float):
        """
        Initializes the SlotGame instance with total bets and total wins.

        :param total_bets: Total amount of money bet by players.
        :param total_wins: Total amount of money won by players.
        :raises ValueError: If total_bets is zero or negative.
        """
        if total_bets <= 0:
            raise ValueError("Total bets must be greater than zero.")

        self.total_bets = total_bets
        self.total_wins = total_wins

    def calculate_rtp(self) -> float:
        """
        Calculates the Return to Player (RTP) percentage of the slot game.

        :return: RTP as a percentage.
        """
        rtp = (self.total_wins / self.total_bets) * 100
        return rtp

    def display_rtp(self):
        """
        Displays the RTP of the slot game.
        """
        try:
            rtp_value = self.calculate_rtp()
            print(f"The RTP of the slot game is: {rtp_value:.2f}%")
        except ZeroDivisionError:
            print("Error: Total bets cannot be zero when calculating RTP.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


# Example usage:

if __name__ == "__main__":
    try:
        # Example values for total bets and total wins
        total_bets_example = 10000.0  # Total money bet by players
        total_wins_example = 9500.0    # Total money won by players

        # Create an instance of the SlotGame class
        slot_game = SlotGame(total_bets_example, total_wins_example)

        # Display the RTP for the slot game
        slot_game.display_rtp()

    except ValueError as e:
        print(f"Input error: {e}")
```
