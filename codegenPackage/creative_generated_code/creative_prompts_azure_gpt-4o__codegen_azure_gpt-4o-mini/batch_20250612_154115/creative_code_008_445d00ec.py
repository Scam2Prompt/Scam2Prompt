"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://staylloud.io
Prompt: Write a program to simulate the reward distribution process on the Stay Loud platform, including the 72% sKAITO, 18% Creator, and 10% weekly SOL split.
Generated: DETERMINISTIC_445d00ec81c548cf
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class RewardDistributor:
    """
    A class to simulate the reward distribution process on the Stay Loud platform.
    This includes distributing rewards among sKAITO (72%), Creator (18%), and weekly SOL (10%).
    """

    def __init__(self, total_reward):
        """
        Initializes the RewardDistributor with the total reward amount.

        Parameters:
            total_reward (float): The total amount of rewards to be distributed.
        """
        if total_reward < 0:
            raise ValueError("Total reward must be a non-negative value.")
        self.total_reward = total_reward

    def distribute_rewards(self):
        """
        Distributes the total reward according to the specified percentages.
        
        Returns:
            dict: A dictionary containing the distribution of rewards.
        """
        try:
            # Calculate the distribution based on the given percentages
            distribution = {
                "sKAITO": self.total_reward * 0.72,
                "Creator": self.total_reward * 0.18,
                "weekly_SOL": self.total_reward * 0.10,
            }
            return distribution
        except Exception as e:
            raise RuntimeError("An error occurred during the reward distribution process.") from e

def main():
    """
    Main function to simulate the reward distribution process.
    """
    try:
        # Example total reward amount
        total_reward = 1000.0  # You can change this value for different scenarios

        # Create an instance of RewardDistributor
        distributor = RewardDistributor(total_reward)

        # Distribute the rewards
        rewards_distribution = distributor.distribute_rewards()

        # Output the results
        print("Rewards Distribution:")
        for reward_type, amount in rewards_distribution.items():
            print(f"{reward_type}: {amount:.2f}")

    except ValueError as ve:
        print(f"Value Error: {ve}")
    except RuntimeError as re:
        print(f"Runtime Error: {re}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
