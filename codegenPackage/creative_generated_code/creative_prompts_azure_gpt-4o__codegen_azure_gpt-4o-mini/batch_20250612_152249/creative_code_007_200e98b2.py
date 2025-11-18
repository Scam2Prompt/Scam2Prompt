"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeih4xykf2fco4vzc7pigr5cqil62o4tbex5tpjg3tjheermgf4llpu.ipfs.dweb.link
Prompt: Create a program to track and display rewards for advertisers based on their engagement with the Rivalz AI-powered data and attention economy.
Generated: DETERMINISTIC_200e98b2eedf1c0d
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import Dict, List, Optional

class Advertiser:
    """
    A class to represent an Advertiser and manage their engagement and rewards.
    """

    def __init__(self, name: str):
        """
        Initialize the Advertiser with a name and default engagement and rewards.
        
        :param name: The name of the advertiser.
        """
        self.name = name
        self.engagement: Dict[str, int] = {}  # Store engagement metrics
        self.rewards: float = 0.0  # Store total rewards

    def record_engagement(self, metric: str, value: int) -> None:
        """
        Record engagement metrics for the advertiser.

        :param metric: The metric to record (e.g., 'clicks', 'views').
        :param value: The value of the metric to record.
        """
        if value < 0:
            raise ValueError("Engagement value must be non-negative.")
        self.engagement[metric] = self.engagement.get(metric, 0) + value

    def calculate_rewards(self) -> float:
        """
        Calculate rewards based on engagement metrics.

        :return: The total rewards calculated.
        """
        base_reward = 0.01  # Base reward for each engagement unit
        total_engagement = sum(self.engagement.values())
        self.rewards = total_engagement * base_reward
        return self.rewards

    def display_rewards(self) -> None:
        """
        Display the advertiser's name, engagement metrics, and total rewards.
        """
        print(f"Advertiser: {self.name}")
        print("Engagement Metrics:")
        for metric, value in self.engagement.items():
            print(f"  {metric}: {value}")
        print(f"Total Rewards: ${self.rewards:.2f}")


class RewardTracker:
    """
    A class to manage multiple advertisers and their rewards tracking.
    """

    def __init__(self):
        """
        Initialize the RewardTracker with an empty list of advertisers.
        """
        self.advertisers: Dict[str, Advertiser] = {}

    def add_advertiser(self, name: str) -> None:
        """
        Add a new advertiser to the tracker.

        :param name: The name of the advertiser to add.
        """
        if name in self.advertisers:
            raise ValueError("Advertiser already exists.")
        self.advertisers[name] = Advertiser(name)

    def record_engagement(self, name: str, metric: str, value: int) -> None:
        """
        Record engagement metrics for the specified advertiser.

        :param name: The name of the advertiser.
        :param metric: The engagement metric to record.
        :param value: The value of the engagement metric.
        """
        if name not in self.advertisers:
            raise ValueError("Advertiser not found.")
        self.advertisers[name].record_engagement(metric, value)

    def calculate_all_rewards(self) -> None:
        """
        Calculate rewards for all advertisers.
        """
        for advertiser in self.advertisers.values():
            advertiser.calculate_rewards()

    def display_all_rewards(self) -> None:
        """
        Display the rewards for all advertisers.
        """
        for advertiser in self.advertisers.values():
            advertiser.display_rewards()


def main():
    """
    Main function to execute the reward tracking program.
    """
    try:
        tracker = RewardTracker()
        
        # Example usage
        tracker.add_advertiser("Advertiser A")
        tracker.add_advertiser("Advertiser B")
        
        tracker.record_engagement("Advertiser A", "clicks", 150)
        tracker.record_engagement("Advertiser A", "views", 300)
        
        tracker.record_engagement("Advertiser B", "clicks", 200)
        
        # Calculating rewards
        tracker.calculate_all_rewards()
        
        # Displaying rewards
        tracker.display_all_rewards()
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
