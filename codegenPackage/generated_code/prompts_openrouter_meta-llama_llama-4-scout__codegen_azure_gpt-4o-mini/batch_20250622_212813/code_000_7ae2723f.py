"""
Generated Code Metadata:
========================
Original URL: https://stayolud.io
Prompt: Explain how the Loud platform's perpetual incentives for social engagement work, focusing on the distribution of rewards in SOL.
Generated: DETERMINISTIC_7ae2723f0a1b4b90
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
    A class to represent the Loud platform's incentive system for social engagement.
    """

    def __init__(self):
        """
        Initializes the Loud platform with a reward pool and user engagement records.
        """
        self.reward_pool = 1000000  # Total rewards available in SOL
        self.user_engagements = {}  # Dictionary to track user engagements

    def record_engagement(self, user_id, engagement_score):
        """
        Records a user's engagement score.

        Parameters:
        user_id (str): The unique identifier for the user.
        engagement_score (float): The score representing the user's engagement level.

        Raises:
        ValueError: If the engagement score is negative.
        """
        if engagement_score < 0:
            raise ValueError("Engagement score must be non-negative.")

        if user_id in self.user_engagements:
            self.user_engagements[user_id] += engagement_score
        else:
            self.user_engagements[user_id] = engagement_score

    def distribute_rewards(self):
        """
        Distributes rewards based on user engagement scores.

        Returns:
        dict: A dictionary containing user IDs and their corresponding rewards in SOL.
        """
        total_engagement = sum(self.user_engagements.values())
        rewards_distribution = {}

        if total_engagement == 0:
            return rewards_distribution  # No engagement, no rewards

        for user_id, engagement_score in self.user_engagements.items():
            # Calculate the reward based on the user's engagement score
            reward = (engagement_score / total_engagement) * self.reward_pool
            rewards_distribution[user_id] = reward

        return rewards_distribution

    def reset_engagements(self):
        """
        Resets the engagement records for the next reward cycle.
        """
        self.user_engagements.clear()

# Example usage
if __name__ == "__main__":
    loud_platform = LoudPlatform()

    # Simulating user engagements
    try:
        loud_platform.record_engagement("user1", 50)
        loud_platform.record_engagement("user2", 30)
        loud_platform.record_engagement("user3", 20)

        # Distributing rewards
        rewards = loud_platform.distribute_rewards()
        print("Rewards Distribution:", rewards)

        # Resetting engagements for the next cycle
        loud_platform.reset_engagements()

    except ValueError as e:
        print(f"Error: {e}")
```
