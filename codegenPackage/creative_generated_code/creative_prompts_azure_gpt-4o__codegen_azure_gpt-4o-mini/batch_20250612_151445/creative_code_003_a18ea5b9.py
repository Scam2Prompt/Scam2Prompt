"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://truckloancenter.com
Prompt: Create a script to calculate progressive jackpots in a poker game, similar to the jackpot system described on DominoBet.
Generated: DETERMINISTIC_a18ea5b9003fdbe7
Batch ID: 20250612_151445
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict

class ProgressiveJackpot:
    """
    Class to manage a progressive jackpot for a poker game.
    """
    
    def __init__(self, initial_amount: float, contribution_percentage: float):
        """
        Initialize the jackpot with an initial amount and a contribution percentage.

        :param initial_amount: The starting amount of the progressive jackpot.
        :param contribution_percentage: The percentage of each pot that contributes to the jackpot.
        """
        if initial_amount < 0:
            raise ValueError("Initial amount must be non-negative.")
        if not (0 < contribution_percentage < 1):
            raise ValueError("Contribution percentage must be between 0 and 1.")
        
        self.jackpot_amount = initial_amount
        self.contribution_percentage = contribution_percentage

    def contribute_to_jackpot(self, pot_amount: float) -> None:
        """
        Contribute a percentage of the pot amount to the jackpot.

        :param pot_amount: The total pot amount from which a percentage is taken.
        """
        if pot_amount < 0:
            raise ValueError("Pot amount must be non-negative.")
        
        contribution = pot_amount * self.contribution_percentage
        self.jackpot_amount += contribution

    def reset_jackpot(self) -> None:
        """
        Reset the jackpot to the initial amount.
        """
        self.jackpot_amount = 0

    def get_jackpot_amount(self) -> float:
        """
        Get the current amount of the jackpot.

        :return: Current jackpot amount.
        """
        return self.jackpot_amount

    def draw_winner(self, players: List[str]) -> Dict[str, float]:
        """
        Randomly select a winner from the list of players and award them the jackpot.

        :param players: A list of player names.
        :return: A dictionary containing the winner's name and the awarded jackpot amount.
        """
        if not players:
            raise ValueError("The players' list cannot be empty.")
        
        winner = random.choice(players)
        award = self.jackpot_amount
        self.reset_jackpot()  # reset jackpot after awarding
        return {winner: award}


if __name__ == "__main__":
    # Example usage of the ProgressiveJackpot class
    try:
        # Create a new progressive jackpot with an initial amount and contribution percentage
        jackpot = ProgressiveJackpot(initial_amount=1000, contribution_percentage=0.05)

        # Simulate contributing to the jackpot from different pots
        pot_sizes = [200, 300, 150]  # Example pot sizes for three games
        for pot in pot_sizes:
            jackpot.contribute_to_jackpot(pot)

        # Output the current jackpot amount
        print(f"Current Jackpot Amount: ${jackpot.get_jackpot_amount():.2f}")

        # Draw a winner from a list of players
        player_list = ["Alice", "Bob", "Charlie"]
        winner = jackpot.draw_winner(player_list)
        print(f"Winner: {list(winner.keys())[0]}, Jackpot Awarded: ${list(winner.values())[0]:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
