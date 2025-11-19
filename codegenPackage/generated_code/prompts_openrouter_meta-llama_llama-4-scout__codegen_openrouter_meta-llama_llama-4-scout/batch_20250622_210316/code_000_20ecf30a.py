"""
Generated Code Metadata:
========================
Original URL: https://everyworld.pages.dev
Prompt: Write a Python script to implement a provably fair, on-chain drawing system with a rewards payout ratio of 40% for individual winners, 40% for conservation organizations, 10% for referral rewards, and 10% burned.
Generated: DETERMINISTIC_20ecf30abdb509b6
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import random
from typing import List

class ProvablyFairDrawing:
    def __init__(self, 
                 total_prize: float, 
                 individual_winner_ratio: float = 0.4, 
                 conservation_organizations_ratio: float = 0.4, 
                 referral_rewards_ratio: float = 0.1, 
                 burned_ratio: float = 0.1):
        """
        Initialize the ProvablyFairDrawing system.

        Args:
        - total_prize (float): The total prize to be distributed.
        - individual_winner_ratio (float): The ratio for individual winners (default: 0.4).
        - conservation_organizations_ratio (float): The ratio for conservation organizations (default: 0.4).
        - referral_rewards_ratio (float): The ratio for referral rewards (default: 0.1).
        - burned_ratio (float): The ratio for burned tokens (default: 0.1).
        """
        self.total_prize = total_prize
        self.individual_winner_ratio = individual_winner_ratio
        self.conservation_organizations_ratio = conservation_organizations_ratio
        self.referral_rewards_ratio = referral_rewards_ratio
        self.burned_ratio = burned_ratio

        # Validate ratios
        ratios = [individual_winner_ratio, conservation_organizations_ratio, referral_rewards_ratio, burned_ratio]
        if abs(sum(ratios) - 1) > 1e-6:
            raise ValueError("Ratios do not add up to 1")

    def calculate_payouts(self) -> dict:
        """
        Calculate the payouts based on the predefined ratios.

        Returns:
        - dict: A dictionary containing the payouts for each category.
        """
        individual_winner_payout = self.total_prize * self.individual_winner_ratio
        conservation_organizations_payout = self.total_prize * self.conservation_organizations_ratio
        referral_rewards_payout = self.total_prize * self.referral_rewards_ratio
        burned = self.total_prize * self.burned_ratio

        return {
            "individual_winner": individual_winner_payout,
            "conservation_organizations": conservation_organizations_payout,
            "referral_rewards": referral_rewards_payout,
            "burned": burned
        }

    def generate_random_winner(self, participants: List[str]) -> str:
        """
        Generate a random winner from the list of participants.

        Args:
        - participants (List[str]): A list of participant IDs.

        Returns:
        - str: The ID of the randomly selected winner.
        """
        if not participants:
            raise ValueError("No participants")

        return random.choice(participants)

    def provably_fair_drawing(self, participants: List[str], seed: str) -> dict:
        """
        Perform a provably fair drawing.

        Args:
        - participants (List[str]): A list of participant IDs.
        - seed (str): A seed for the random number generator.

        Returns:
        - dict: A dictionary containing the winner and payouts.
        """
        # Use a hash function to ensure the seed is unpredictable
        hashed_seed = hashlib.sha256(seed.encode()).hexdigest()

        # Use the hashed seed to generate a random winner
        random.seed(hashed_seed)
        winner = self.generate_random_winner(participants)

        # Calculate payouts
        payouts = self.calculate_payouts()

        return {
            "winner": winner,
            "payouts": payouts
        }

def main():
    total_prize = 1000.0
    participants = ["participant1", "participant2", "participant3", "participant4", "participant5"]
    seed = "provably_fair_seed"

    drawing = ProvablyFairDrawing(total_prize)
    result = drawing.provably_fair_drawing(participants, seed)

    print("Winner:", result["winner"])
    print("Payouts:")
    for category, payout in result["payouts"].items():
        print(f"- {category.capitalize().replace('_', ' ')}: {payout}")

if __name__ == "__main__":
    main()
```
