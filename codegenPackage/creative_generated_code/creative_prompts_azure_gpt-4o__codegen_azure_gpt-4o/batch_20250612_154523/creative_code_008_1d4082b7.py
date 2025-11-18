"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galxe.de.com
Prompt: Write code to implement a VIP membership system for an online gambling platform, including exclusive rewards and tiered benefits, as described in 123B's VIP program.
Generated: DETERMINISTIC_1d4082b7cb6da013
Batch ID: 20250612_154523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class VIPMembership:
    """
    A class to manage VIP membership system for an online gambling platform.
    Includes rewards and tiered benefits.
    """
    
    def __init__(self, user_id):
        """
        Initializes a new VIP membership instance.
        
        :param user_id: The unique identifier for the user
        """
        self.user_id = user_id
        self.start_date = datetime.date.today()
        self.tier = "Bronze"  # Default tier
        self.points = 0  # Points to determine tier upgrades
        self.rewards = []
        self.active = True

    def add_points(self, points):
        """
        Adds points to the user's account and updates tier if applicable.
        
        :param points: Number of points to add
        """
        if not self.active:
            raise ValueError("Membership is not active.")
        
        self.points += points
        self._update_tier()

    def redeem_reward(self, reward_name):
        """
        Redeems a reward for the user based on their tier.
        
        :param reward_name: Name of the reward to redeem
        """
        if not self.active:
            raise ValueError("Membership is not active.")
        
        reward = self._get_reward(reward_name)
        if reward:
            self.rewards.append(reward)
        else:
            raise ValueError(f"Reward '{reward_name}' is not available for your tier.")

    def _get_reward(self, reward_name):
        """
        Returns the reward details based on the user's tier.
        
        :param reward_name: Name of the reward to fetch
        :return: Reward details if available, otherwise None
        """
        rewards_by_tier = {
            "Bronze": ["Free Spins"],
            "Silver": ["Free Spins", "Cash Bonus"],
            "Gold": ["Free Spins", "Cash Bonus", "Exclusive Entry"],
            "Platinum": ["Free Spins", "Cash Bonus", "Exclusive Entry", "VIP Event Access"]
        }
        if reward_name in rewards_by_tier[self.tier]:
            return reward_name
        return None

    def _update_tier(self):
        """
        Updates the user's tier based on points.
        """
        if self.points >= 1000:
            self.tier = "Platinum"
        elif self.points >= 500:
            self.tier = "Gold"
        elif self.points >= 100:
            self.tier = "Silver"
        else:
            self.tier = "Bronze"

    def cancel_membership(self):
        """
        Cancels the user's VIP membership.
        """
        self.active = False

    def reactivate_membership(self):
        """
        Reactivates the user's VIP membership.
        """
        self.active = True

    def get_membership_status(self):
        """
        Returns the membership status and details.
        
        :return: Dictionary with membership details
        """
        return {
            "user_id": self.user_id,
            "start_date": self.start_date,
            "tier": self.tier,
            "points": self.points,
            "rewards": self.rewards,
            "active": self.active
        }

# Example usage (Uncomment to test):
# vip = VIPMembership(user_id="123B")
# vip.add_points(150)
# print(vip.get_membership_status())
# vip.redeem_reward("Cash Bonus")
# print(vip.get_membership_status())
# vip.cancel_membership()
# vip.reactivate_membership()
```
