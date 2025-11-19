"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wwwstayloud.io
Prompt: Generate a code snippet that tracks user mindshare contributions and calculates weekly rewards in SOL for a project like Loud.
Generated: DETERMINISTIC_3f860ffc8231bf2e
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from collections import defaultdict
from decimal import Decimal, getcontext

# Set the precision for Decimal calculations
getcontext().prec = 10

class UserMindshareTracker:
    def __init__(self):
        # Dictionary to store user contributions
        self.contributions = defaultdict(lambda: defaultdict(Decimal))
        # Reward rate per contribution unit in SOL
        self.reward_rate = Decimal("0.01")  # Example reward rate

    def add_contribution(self, user_id, contribution_amount):
        """
        Adds a user's mindshare contribution for the current date.
        
        :param user_id: Unique identifier for the user
        :param contribution_amount: Amount of contribution
        """
        if contribution_amount < 0:
            raise ValueError("Contribution amount must be non-negative.")
        
        today = datetime.date.today()
        self.contributions[user_id][today] += Decimal(contribution_amount)
        print(f"Added contribution for user {user_id}: {contribution_amount} on {today}")

    def calculate_weekly_rewards(self, user_id):
        """
        Calculates the total rewards for a specified user over the last week.
        
        :param user_id: Unique identifier for the user
        :return: Total rewards in SOL for the user
        """
        total_rewards = Decimal("0.0")
        today = datetime.date.today()
        week_start = today - datetime.timedelta(days=today.weekday())

        # Iterate over the contributions for the user
        for date, amount in self.contributions[user_id].items():
            if week_start <= date <= today:
                total_rewards += amount * self.reward_rate
        
        print(f"Total rewards for user {user_id} from {week_start} to {today}: {total_rewards} SOL")
        return total_rewards

# Example usage
if __name__ == "__main__":
    tracker = UserMindshareTracker()
    
    # Simulate adding contributions
    try:
        tracker.add_contribution("user123", 10)
        tracker.add_contribution("user123", 15)
        tracker.add_contribution("user456", 20)
        
        # Calculate rewards for user123
        rewards_user123 = tracker.calculate_weekly_rewards("user123")
        print(f"User user123 has earned {rewards_user123} SOL in rewards.")
        
        # Calculate rewards for user456
        rewards_user456 = tracker.calculate_weekly_rewards("user456")
        print(f"User user456 has earned {rewards_user456} SOL in rewards.")
        
    except ValueError as e:
        print(f"Error: {e}")
```
