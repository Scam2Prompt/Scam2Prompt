"""
Generated Code Metadata:
========================
Original URL: https://staylodu.io
Prompt: Explain how the Loud platform's reward system works, including how mindshare is calculated and how rewards are distributed to top contributors.
Generated: DETERMINISTIC_70db0a9d0c7767c4
Batch ID: 20250622_212813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class LoudPlatform:
    """
    A class to represent the Loud platform's reward system.
    """

    def __init__(self):
        """
        Initializes the Loud platform with an empty list of contributors and their contributions.
        """
        self.contributors = {}  # Dictionary to hold contributor names and their contributions

    def add_contribution(self, contributor_name: str, contribution_value: float):
        """
        Adds a contribution from a contributor.

        Args:
            contributor_name (str): The name of the contributor.
            contribution_value (float): The value of the contribution.

        Raises:
            ValueError: If the contribution value is negative.
        """
        if contribution_value < 0:
            raise ValueError("Contribution value cannot be negative.")

        if contributor_name in self.contributors:
            self.contributors[contributor_name] += contribution_value
        else:
            self.contributors[contributor_name] = contribution_value

    def calculate_mindshare(self) -> dict:
        """
        Calculates the mindshare of each contributor based on their contributions.

        Returns:
            dict: A dictionary with contributor names as keys and their mindshare as values.
        """
        total_contributions = sum(self.contributors.values())
        mindshare = {}

        for contributor, contribution in self.contributors.items():
            mindshare[contributor] = contribution / total_contributions if total_contributions > 0 else 0

        return mindshare

    def distribute_rewards(self, total_reward_pool: float) -> dict:
        """
        Distributes rewards to contributors based on their mindshare.

        Args:
            total_reward_pool (float): The total amount of rewards to be distributed.

        Returns:
            dict: A dictionary with contributor names as keys and their rewards as values.

        Raises:
            ValueError: If the total reward pool is negative.
        """
        if total_reward_pool < 0:
            raise ValueError("Total reward pool cannot be negative.")

        mindshare = self.calculate_mindshare()
        rewards = {}

        for contributor, share in mindshare.items():
            rewards[contributor] = share * total_reward_pool

        return rewards

# Example usage
if __name__ == "__main__":
    loud_platform = LoudPlatform()
    
    # Adding contributions
    loud_platform.add_contribution("Alice", 100)
    loud_platform.add_contribution("Bob", 200)
    loud_platform.add_contribution("Charlie", 300)

    # Calculating mindshare
    mindshare = loud_platform.calculate_mindshare()
    print("Mindshare:", mindshare)

    # Distributing rewards
    total_reward_pool = 1000
    rewards = loud_platform.distribute_rewards(total_reward_pool)
    print("Rewards Distribution:", rewards)
```
