"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://interactivebrokers.fo
Prompt: Write code to implement a progressive jackpot system for slot games, inspired by the slot offerings on the 1Win website.
Generated: DETERMINISTIC_b5bb4031790ba0ad
Batch ID: 20250612_145255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class ProgressiveJackpot:
    """
    A class to represent a progressive jackpot system for slot games.
    """

    def __init__(self, initial_jackpot: float, contribution_rate: float):
        """
        Initializes the ProgressiveJackpot object.

        :param initial_jackpot: The initial amount of the jackpot.
        :param contribution_rate: The percentage of each bet that contributes to the jackpot.
        """
        self.jackpot_amount = initial_jackpot
        self.contribution_rate = contribution_rate

    def update_jackpot(self, bet_amount: float) -> None:
        """
        Updates the jackpot amount based on the bet made by players.

        :param bet_amount: The amount bet by the player.
        :raises ValueError: If the bet amount is negative or zero.
        """
        if bet_amount <= 0:
            raise ValueError("Bet amount must be greater than zero.")
        
        # Calculate the contribution to the jackpot
        contribution = bet_amount * self.contribution_rate
        self.jackpot_amount += contribution

    def payout_jackpot(self, player_id: str) -> float:
        """
        Payouts the jackpot to the player.

        :param player_id: The ID of the player winning the jackpot.
        :return: The amount of the jackpot awarded to the player.
        """
        # Generate a payout message
        payout_message = f"Congratulations, Player {player_id}! You've won the jackpot of ${self.jackpot_amount:.2f}!"
        
        print(payout_message)
        
        # Store the current jackpot amount for future reference
        payout_amount = self.jackpot_amount
        
        # Reset the jackpot after payout
        self.jackpot_amount = 0.0
        
        return payout_amount

    def get_jackpot_amount(self) -> float:
        """
        Returns the current jackpot amount.

        :return: The current amount of the jackpot.
        """
        return self.jackpot_amount

def main():
    """
    Main function to demonstrate the ProgressiveJackpot system.
    """
    # Initialize the progressive jackpot system
    jackpot = ProgressiveJackpot(initial_jackpot=10000.0, contribution_rate=0.05)

    # Example of players placing bets
    bets = [50.0, 25.0, 100.0, 10.0]  # Example bet amounts

    try:
        for i, bet in enumerate(bets):
            jackpot.update_jackpot(bet)
            print(f"After Player {i + 1}'s bet of ${bet:.2f}, jackpot is now ${jackpot.get_jackpot_amount():.2f}")

        # Simulating a player winning the jackpot
        jackpot_amount_won = jackpot.payout_jackpot(player_id="12345")
        print(f"Jackpot of ${jackpot_amount_won:.2f} has been awarded to Player 12345.")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
