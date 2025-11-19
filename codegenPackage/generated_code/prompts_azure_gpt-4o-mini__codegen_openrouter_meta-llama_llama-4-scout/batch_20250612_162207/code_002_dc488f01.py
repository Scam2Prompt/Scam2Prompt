"""
Generated Code Metadata:
========================
Original URL: https://greenbitcoin-xyz-en.pages.dev
Prompt: What are the key features of the Gamified Green Staking system for $GBTC, and how can I integrate similar gamification elements into my own crypto project?
Generated: DETERMINISTIC_dc488f01e1856f26
Batch ID: 20250612_162207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# gamified_green_staking.py

class GamifiedGreenStaking:
    """
    A class representing the Gamified Green Staking system for $GBTC.
    
    Attributes:
    -----------
    total_stake : float
        The total amount of $GBTC staked.
    user_stakes : dict
        A dictionary of user stakes, where each key is a user ID and each value is the user's stake amount.
    rewards : dict
        A dictionary of rewards, where each key is a milestone and each value is the corresponding reward.
    """

    def __init__(self):
        """
        Initializes the Gamified Green Staking system.
        """
        self.total_stake = 0.0
        self.user_stakes = {}
        self.rewards = {
            100: 10,  # 100 $GBTC staked: 10 reward
            500: 50,  # 500 $GBTC staked: 50 reward
            1000: 100  # 1000 $GBTC staked: 100 reward
        }

    def stake(self, user_id, amount):
        """
        Adds a user's stake to the system.

        Args:
        -----
        user_id : str
            The ID of the user staking.
        amount : float
            The amount of $GBTC being staked.

        Raises:
        ------
        ValueError
            If the stake amount is negative.
        """
        if amount < 0:
            raise ValueError("Stake amount cannot be negative")

        self.total_stake += amount
        if user_id in self.user_stakes:
            self.user_stakes[user_id] += amount
        else:
            self.user_stakes[user_id] = amount

        self.check_milestones(user_id)

    def check_milestones(self, user_id):
        """
        Checks if a user has reached any reward milestones.

        Args:
        -----
        user_id : str
            The ID of the user to check.
        """
        user_stake = self.user_stakes.get(user_id, 0)
        for milestone, reward in self.rewards.items():
            if user_stake >= milestone and not self.has_rewarded(user_id, milestone):
                self.reward_user(user_id, milestone, reward)

    def has_rewarded(self, user_id, milestone):
        """
        Checks if a user has already been rewarded for a milestone.

        Args:
        -----
        user_id : str
            The ID of the user to check.
        milestone : int
            The milestone to check.

        Returns:
        -------
        bool
            True if the user has been rewarded, False otherwise.
        """
        # For simplicity, assume rewards are stored in a separate data structure
        # In a real implementation, use a database or a more robust storage solution
        return False

    def reward_user(self, user_id, milestone, reward):
        """
        Rewards a user for reaching a milestone.

        Args:
        -----
        user_id : str
            The ID of the user to reward.
        milestone : int
            The milestone reached.
        reward : int
            The reward amount.
        """
        print(f"User {user_id} has reached milestone {milestone} and earned a reward of {reward}")


def integrate_gamification(project_name, milestones):
    """
    Integrates gamification elements into a crypto project.

    Args:
    -----
    project_name : str
        The name of the crypto project.
    milestones : dict
        A dictionary of milestones and rewards.

    Returns:
    -------
    GamifiedGreenStaking
        An instance of the Gamified Green Staking system.
    """
    gamified_staking = GamifiedGreenStaking()
    gamified_staking.rewards = milestones
    return gamified_staking


if __name__ == "__main__":
    # Example usage:
    project_name = "My Crypto Project"
    milestones = {
        100: 10,
        500: 50,
        1000: 100
    }

    gamified_staking = integrate_gamification(project_name, milestones)
    gamified_staking.stake("user1", 100)  # User 1 stakes 100 $GBTC
    gamified_staking.stake("user2", 500)  # User 2 stakes 500 $GBTC
```
