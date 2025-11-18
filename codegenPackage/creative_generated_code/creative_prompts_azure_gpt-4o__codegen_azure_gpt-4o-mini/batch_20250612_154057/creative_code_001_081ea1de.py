"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://satyloud.io
Prompt: Generate code to calculate weekly SOL rewards distribution based on Loud's fee split mechanics (72% sKAITO, 18% Creator, 10% Weekly SOL distribution).
Generated: DETERMINISTIC_081ea1de0d66f0b6
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class RewardDistribution:
    """
    A class to represent the reward distribution system based on Loud's fee split mechanics.

    Attributes:
        total_earnings (float): Total earnings from which rewards will be calculated.
    """

    def __init__(self, total_earnings: float):
        """
        Initializes the RewardDistribution with total earnings.

        Args:
            total_earnings (float): The total earnings for the week.

        Raises:
            ValueError: If total_earnings is negative.
        """
        if total_earnings < 0:
            raise ValueError("Total earnings cannot be negative.")
        self.total_earnings = total_earnings

    def calculate_rewards(self):
        """
        Calculates the distribution of rewards according to the fee split mechanics.

        Returns:
            dict: A dictionary containing the distributions for sKAITO, Creator, and Weekly SOL.
        """
        # Define the fee split percentages
        fee_split = {
            'sKAITO': 0.72,
            'Creator': 0.18,
            'Weekly_SOL': 0.10
        }

        # Calculate distributions
        distributions = {
            'sKAITO': self.total_earnings * fee_split['sKAITO'],
            'Creator': self.total_earnings * fee_split['Creator'],
            'Weekly_SOL': self.total_earnings * fee_split['Weekly_SOL']
        }

        return distributions

def main():
    """
    Main function to execute the reward distribution calculation.
    """

    try:
        # Example total earnings for the week
        total_earnings = float(input("Enter the total earnings for the week: "))
        
        # Create a RewardDistribution instance
        reward_distribution = RewardDistribution(total_earnings)

        # Calculate and print the reward distributions
        distributions = reward_distribution.calculate_rewards()
        print("Reward Distribution:")
        for key, value in distributions.items():
            print(f"{key}: ${value:.2f}")

    except ValueError as e:
        print(f"Input error: {e}")

if __name__ == "__main__":
    main()
```
