"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nc8301x1.pages.dev
Prompt: Create a function to calculate the total Notcoin rewards distributed based on the given statistics from the Notcoin airdrop.
Generated: DETERMINISTIC_6d3500f07c6a0ad4
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class NotcoinAirdrop:
    def __init__(self, total_rewards: float, total_participants: int):
        """
        Initialize the NotcoinAirdrop instance.

        :param total_rewards: Total amount of Notcoin rewards distributed.
        :param total_participants: Total number of participants in the airdrop.
        """
        if total_rewards < 0:
            raise ValueError("Total rewards must be a non-negative value.")
        if total_participants < 0:
            raise ValueError("Total participants must be a non-negative integer.")
        
        self.total_rewards = total_rewards
        self.total_participants = total_participants

    def calculate_average_reward(self) -> float:
        """
        Calculate the average reward per participant.

        :return: Average Notcoin rewards per participant.
        """
        if self.total_participants == 0:
            return 0.0  # Avoid division by zero
        
        average_reward = self.total_rewards / self.total_participants
        return average_reward

    def total_notcoin_distributed(self) -> float:
        """
        Get the total Notcoin rewards distributed.

        :return: Total Notcoin rewards distributed.
        """
        return self.total_rewards

# Example usage
if __name__ == "__main__":
    try:
        airdrop = NotcoinAirdrop(total_rewards=1000.0, total_participants=50)
        average = airdrop.calculate_average_reward()
        total_distributed = airdrop.total_notcoin_distributed()
        
        print(f"Average Notcoin reward per participant: {average:.2f}")
        print(f"Total Notcoin rewards distributed: {total_distributed:.2f}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
