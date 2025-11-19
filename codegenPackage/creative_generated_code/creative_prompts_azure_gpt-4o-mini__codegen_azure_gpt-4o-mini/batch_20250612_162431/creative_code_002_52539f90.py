"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airkombat.com
Prompt: Explain the unique community-based reward system for $WING token holders and how it ties to social media milestones.
Generated: DETERMINISTIC_52539f90d9429a1b
Batch ID: 20250612_162431
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class WingTokenRewardSystem:
    """
    A class to represent the unique community-based reward system for $WING token holders.
    
    Attributes:
        total_tokens (int): Total number of tokens held by the community.
        milestones (dict): A dictionary to store social media milestones and rewards.
        holders (dict): A dictionary to store token holders and their respective rewards.
    """

    def __init__(self):
        self.total_tokens = 0
        self.milestones = {}
        self.holders = {}

    def add_milestone(self, milestone_name: str, reward: int):
        """
        Adds a social media milestone with a corresponding reward.

        Args:
            milestone_name (str): The name of the social media milestone.
            reward (int): The reward amount for reaching the milestone.
        """
        if milestone_name in self.milestones:
            raise ValueError(f"Milestone '{milestone_name}' already exists.")
        self.milestones[milestone_name] = reward

    def add_holder(self, holder_address: str, tokens: int):
        """
        Adds a token holder and the amount of tokens they hold.

        Args:
            holder_address (str): The address of the token holder.
            tokens (int): The number of tokens held by the holder.
        """
        if tokens <= 0:
            raise ValueError("Number of tokens must be greater than zero.")
        self.holders[holder_address] = self.holders.get(holder_address, 0) + tokens
        self.total_tokens += tokens

    def distribute_rewards(self, milestone_name: str):
        """
        Distributes rewards to all token holders based on a specific milestone.

        Args:
            milestone_name (str): The name of the milestone that has been reached.

        Raises:
            ValueError: If the milestone does not exist.
        """
        if milestone_name not in self.milestones:
            raise ValueError(f"Milestone '{milestone_name}' does not exist.")

        reward_per_token = self.milestones[milestone_name]
        
        for holder, tokens in self.holders.items():
            reward = tokens * reward_per_token
            print(f"Distributing {reward} rewards to holder {holder}")

    def get_total_rewards(self):
        """
        Returns the total rewards available for distribution based on milestones.

        Returns:
            int: Total rewards calculated as sum of all rewards from milestones.
        """
        return sum(self.milestones.values())

# Example of how to use the class
if __name__ == "__main__":
    try:
        reward_system = WingTokenRewardSystem()
        
        # Adding social media milestones
        reward_system.add_milestone("Twitter Followers 1000", 10)
        reward_system.add_milestone("Instagram Followers 500", 5)

        # Adding holders
        reward_system.add_holder("0x123", 100)
        reward_system.add_holder("0x456", 200)

        # Distributing rewards for a milestone
        reward_system.distribute_rewards("Twitter Followers 1000")

        # Displaying total rewards
        print(f"Total rewards available: {reward_system.get_total_rewards()}")
        
    except ValueError as e:
        print(f"An error occurred: {e}")
```
