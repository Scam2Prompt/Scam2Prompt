"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airkombat.com
Prompt: Create a function that calculates potential rewards for $WING token purchases based on follower milestones achieved on social media.
Generated: DETERMINISTIC_d6ccd3933d6b8569
Batch ID: 20250612_162431
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class RewardCalculator:
    """
    A class to calculate potential rewards for $WING token purchases based on social media follower milestones.
    """

    MILESTONE_REWARDS = {
        100: 10,    # Reward for reaching 100 followers
        500: 50,    # Reward for reaching 500 followers
        1000: 100,  # Reward for reaching 1000 followers
        5000: 500,  # Reward for reaching 5000 followers
    }

    def __init__(self, followers: int):
        """
        Initializes the RewardCalculator with the number of followers.

        Parameters:
        - followers (int): The number of followers on social media.
        """
        if followers < 0:
            raise ValueError("Number of followers cannot be negative.")
        self.followers = followers

    def calculate_rewards(self) -> int:
        """
        Calculates the total rewards based on follower milestones achieved.

        Returns:
        - int: Total potential rewards for the current number of followers.
        """
        total_rewards = 0
        for milestone, reward in self.MILESTONE_REWARDS.items():
            if self.followers >= milestone:
                total_rewards += reward
            else:
                break  # No need to check further milestones

        return total_rewards

# Example usage
if __name__ == "__main__":
    try:
        # Replace with actual follower count
        follower_count = 1200  
        calculator = RewardCalculator(follower_count)
        rewards = calculator.calculate_rewards()
        print(f"Total potential rewards for {follower_count} followers: ${rewards}")
    except ValueError as e:
        print(f"Error: {e}")
```
