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
import datetime


class Advertiser:
    """
    Class to represent an Advertiser with engagement tracking and reward calculation.
    """

    def __init__(self, name):
        """
        Initialize an Advertiser with a name and empty engagement data.
        :param name: Name of the advertiser.
        """
        self.name = name
        self.engagement = 0  # Tracks total engagement score
        self.rewards = 0  # Tracks total rewards earned

    def add_engagement(self, score):
        """
        Add engagement data for the advertiser.
        :param score: Engagement score to add (must be positive).
        """
        if score < 0:
            raise ValueError("Engagement score must be positive.")
        self.engagement += score
        self._calculate_rewards()

    def _calculate_rewards(self):
        """
        Calculates rewards based on engagement. 
        For simplicity: 1 reward point per 100 engagement points.
        """
        self.rewards = self.engagement // 100

    def display_rewards(self):
        """
        Display the advertiser's rewards summary.
        """
        print(f"Advertiser: {self.name}")
        print(f"Total Engagement: {self.engagement}")
        print(f"Total Rewards: {self.rewards}")


class RewardsTracker:
    """
    Class to manage and track multiple Advertisers and display rewards.
    """

    def __init__(self):
        """
        Initialize the RewardsTracker with an empty list of advertisers.
        """
        self.advertisers = {}

    def add_advertiser(self, name):
        """
        Add a new advertiser to the tracker.
        :param name: Name of the advertiser.
        """
        if name in self.advertisers:
            raise ValueError(f"Advertiser '{name}' already exists.")
        self.advertisers[name] = Advertiser(name)

    def record_engagement(self, name, score):
        """
        Record engagement for an advertiser.
        :param name: Name of the advertiser.
        :param score: Engagement score to record.
        """
        if name not in self.advertisers:
            raise ValueError(f"Advertiser '{name}' does not exist.")
        self.advertisers[name].add_engagement(score)

    def display_all_rewards(self):
        """
        Display rewards summary for all advertisers.
        """
        print("=== Rewards Summary ===")
        for advertiser in self.advertisers.values():
            advertiser.display_rewards()


# Example usage
def main():
    """
    Main function to demonstrate the functionality of the RewardsTracker system.
    """
    tracker = RewardsTracker()

    try:
        # Add advertisers
        tracker.add_advertiser("Advertiser A")
        tracker.add_advertiser("Advertiser B")

        # Record engagement
        tracker.record_engagement("Advertiser A", 450)
        tracker.record_engagement("Advertiser B", 120)

        # Show rewards summary
        tracker.display_all_rewards()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
