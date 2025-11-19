"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://everyworld.pages.dev
Prompt: Create a function that calculates the rewards payout ratio for Everyworld participants based on their engagement activities.
Generated: DETERMINISTIC_70db9235f9d3ed0f
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class EngagementActivities:
    def __init__(self, activity_points, total_rewards):
        """
        Initializes the EngagementActivities instance with provided activity points and total rewards.

        :param activity_points: List of engagement points earned by participants
        :param total_rewards: Total rewards available for distribution
        """
        if total_rewards <= 0:
            raise ValueError("Total rewards must be greater than zero.")
        
        self.activity_points = activity_points
        self.total_rewards = total_rewards

    def calculate_rewards_ratio(self):
        """
        Calculates the rewards payout ratio for participants based on their engagement activities.

        :return: List of rewards ratios for each participant
        :raises ValueError: If activity points are negative or total rewards is zero
        """
        if not all(point >= 0 for point in self.activity_points):
            raise ValueError("All activity points must be non-negative.")

        total_points = sum(self.activity_points)

        if total_points == 0:
            return [0] * len(self.activity_points)  # No engagement, no rewards

        # Calculate the rewards ratio for each participant
        rewards_ratios = [
            (points / total_points) * self.total_rewards for points in self.activity_points
        ]
        
        return rewards_ratios


if __name__ == "__main__":
    try:
        # Example usage
        activity_points = [10, 20, 30]  # Points earned by participants
        total_rewards = 100  # Total rewards available

        engagement = EngagementActivities(activity_points, total_rewards)
        rewards_ratios = engagement.calculate_rewards_ratio()

        print("Rewards Payout Ratios:", rewards_ratios)
    except ValueError as e:
        print("Error:", e)
```
