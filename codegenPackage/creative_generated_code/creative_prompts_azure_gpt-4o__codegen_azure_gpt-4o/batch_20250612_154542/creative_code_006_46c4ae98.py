"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://landing-jackpotcow.pages.dev
Prompt: Generate code to create a raffle jackpot system that distributes prizes among top contributors, as described in the Epic Drop Jackpots feature on Jackpot Cow Casino.
Generated: DETERMINISTIC_46c4ae98ac6ccdb4
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from collections import defaultdict


class RaffleJackpot:
    """
    A class to manage a raffle jackpot system that distributes prizes among top contributors.
    """

    def __init__(self):
        """
        Initializes the jackpot system.
        """
        self.contributors = defaultdict(float)  # Stores user contributions {user_id: contribution_amount}
        self.total_contributions = 0  # Tracks total amount contributed to the jackpot
        self.prize_pool = 0  # Prize pool amount

    def add_contribution(self, user_id: str, amount: float):
        """
        Adds a contribution to the jackpot from a user.

        :param user_id: Identifier for the user contributing.
        :param amount: Amount of the contribution.
        :raises ValueError: If the contribution amount is invalid.
        """
        if amount <= 0:
            raise ValueError("Contribution amount must be greater than zero.")
        
        self.contributors[user_id] += amount
        self.total_contributions += amount
        self.prize_pool += amount  # Assume contribution directly increases prize pool

    def distribute_prizes(self, num_winners: int):
        """
        Distributes prizes among top contributors based on their contribution.

        :param num_winners: Number of top contributors to distribute prizes to.
        :return: A dictionary of winners and their prize amounts.
        :raises ValueError: If num_winners is invalid or there's no prize pool to distribute.
        """
        if num_winners <= 0:
            raise ValueError("Number of winners must be greater than zero.")
        if self.total_contributions == 0:
            raise ValueError("No contributions have been made; cannot distribute prizes.")

        # Sort contributors by contribution amount in descending order
        sorted_contributors = sorted(self.contributors.items(), key=lambda item: item[1], reverse=True)
        top_contributors = sorted_contributors[:num_winners]

        # Calculate prize distribution (e.g., proportional to contributions)
        prizes = {}
        for user_id, contribution in top_contributors:
            prize_amount = (contribution / self.total_contributions) * self.prize_pool
            prizes[user_id] = prize_amount

        return prizes

    def reset_jackpot(self):
        """
        Resets the jackpot system for a new round.
        """
        self.contributors.clear()
        self.total_contributions = 0
        self.prize_pool = 0


# Example usage:
if __name__ == "__main__":
    # Create an instance of the RaffleJackpot
    jackpot = RaffleJackpot()

    # Add contributions
    try:
        jackpot.add_contribution("user1", 100)
        jackpot.add_contribution("user2", 200)
        jackpot.add_contribution("user3", 50)
    except ValueError as e:
        print(f"Error: {e}")

    # Distribute prizes
    try:
        winners = jackpot.distribute_prizes(num_winners=2)
        print("Winners and their prizes:", winners)
    except ValueError as e:
        print(f"Error: {e}")

    # Reset jackpot for a new round
    jackpot.reset_jackpot()
```
