"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://staylodu.io
Prompt: Write a script to calculate the weekly SOL rewards distribution for Loud contributors based on the fee split percentages (72% sKAITO, 18% Creator, 10% Weekly SOL distribution).
Generated: DETERMINISTIC_24aa118c0c6ed1e2
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# weekly_rewards_distribution.py

class RewardsDistribution:
    """
    A class to calculate weekly rewards distribution for Loud contributors.
    """

    def __init__(self, total_fees: float):
        """
        Initializes the RewardsDistribution with total fees collected.

        :param total_fees: The total fees collected for the week.
        """
        if total_fees < 0:
            raise ValueError("Total fees must be a non-negative number.")
        self.total_fees = total_fees
        self.skaito_percentage = 0.72
        self.creator_percentage = 0.18
        self.weekly_sol_percentage = 0.10

    def calculate_distribution(self):
        """
        Calculates the distribution of fees according to predefined percentages.

        :return: A dictionary containing the distribution amounts for sKAITO, Creator, and Weekly SOL.
        """
        try:
            skaito_reward = self.total_fees * self.skaito_percentage
            creator_reward = self.total_fees * self.creator_percentage
            weekly_sol_reward = self.total_fees * self.weekly_sol_percentage
            
            distribution = {
                "sKAITO": skaito_reward,
                "Creator": creator_reward,
                "Weekly SOL": weekly_sol_reward
            }
            return distribution
        except Exception as e:
            raise RuntimeError("Error calculating rewards distribution: " + str(e))

def main():
    """
    Main function to execute the rewards distribution calculation.
    """
    try:
        # Example total fees collected for the week
        total_fees = float(input("Enter the total fees collected this week: "))
        
        # Create an instance of RewardsDistribution
        rewards_distribution = RewardsDistribution(total_fees)
        
        # Calculate the distribution
        distribution = rewards_distribution.calculate_distribution()
        
        # Print the results
        print("Weekly Rewards Distribution:")
        for key, value in distribution.items():
            print(f"{key}: {value:.2f}")
    
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
