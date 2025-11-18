"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartlayer-network.pages.dev
Prompt: Develop a lottery system in Python that mimics the Tier 2 allocation system for $SLN tokens, ensuring fairness and inclusivity.
Generated: DETERMINISTIC_1be6b8f2d998f747
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class LotterySystem:
    """
    A lottery system that mimics a Tier 2 allocation system for $SLN tokens.
    Ensures fairness and inclusivity by using weighted chances based on tiers.
    """
    def __init__(self):
        # Store participants and their respective tiers
        self.participants = {}
        self.tier_weights = {
            1: 5,  # Tier 1 has the highest weight
            2: 3,  # Tier 2 has medium weight
            3: 1   # Tier 3 has the lowest weight
        }
        self.total_weight = 0  # Total weight for calculating probabilities

    def add_participant(self, participant_name, tier):
        """
        Adds a participant to the lottery system.
        :param participant_name: str, Name of the participant
        :param tier: int, Tier number (1, 2, or 3)
        :raises ValueError: If tier is invalid
        """
        if tier not in self.tier_weights:
            raise ValueError("Invalid tier. Valid tiers are 1, 2, and 3.")

        # Add participant with their tier weight
        self.participants[participant_name] = self.tier_weights[tier]
        self.total_weight += self.tier_weights[tier]  # Update total weight

    def conduct_lottery(self, number_of_winners):
        """
        Conducts the lottery and randomly selects winners based on weighted chances.
        :param number_of_winners: int, Number of winners to select
        :return: list of str, Names of winners
        :raises ValueError: If number_of_winners exceeds participants count
        """
        if number_of_winners > len(self.participants):
            raise ValueError("Number of winners cannot exceed total participants.")

        # Prepare weighted selection pool based on participant weights
        weighted_pool = []
        for participant, weight in self.participants.items():
            weighted_pool.extend([participant] * weight)

        # Randomly select winners from the weighted pool
        winners = random.sample(weighted_pool, number_of_winners)
        return list(set(winners))  # Ensure unique winners

    def reset_lottery(self):
        """
        Resets the lottery system by clearing participants and weights.
        """
        self.participants.clear()
        self.total_weight = 0

# Example usage of the LotterySystem class
if __name__ == "__main__":
    # Create an instance of the lottery system
    lottery_system = LotterySystem()

    # Add participants
    try:
        lottery_system.add_participant("Alice", 1)
        lottery_system.add_participant("Bob", 2)
        lottery_system.add_participant("Charlie", 3)
        lottery_system.add_participant("Dave", 2)
        lottery_system.add_participant("Eve", 1)
    except ValueError as e:
        print(f"Error adding participants: {e}")

    # Conduct the lottery
    try:
        winners = lottery_system.conduct_lottery(3)
        print(f"Winners: {winners}")
    except ValueError as e:
        print(f"Error conducting lottery: {e}")

    # Reset the lottery system for future use
    lottery_system.reset_lottery()
```
