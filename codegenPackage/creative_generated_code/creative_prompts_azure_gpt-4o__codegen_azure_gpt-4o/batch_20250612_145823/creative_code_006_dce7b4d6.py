"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappbay-bnbchain-org.pages.dev
Prompt: Generate code to track user participation in BNB Chain's anniversary campaigns and calculate rewards earned across multiple weeks.
Generated: DETERMINISTIC_dce7b4d6b0bae518
Batch ID: 20250612_145823
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict

class CampaignParticipationTracker:
    """
    Class to track user participation in BNB Chain's anniversary campaigns 
    and calculate rewards across multiple weeks.
    """
    def __init__(self):
        # Dictionary to store user participation data
        # Format: {user_id: [{'week': 1, 'activity_points': 50}, {'week': 2, 'activity_points': 60}]}
        self.user_data: Dict[str, List[Dict[str, int]]] = {}

    def add_participation(self, user_id: str, week: int, activity_points: int) -> None:
        """
        Adds participation data for a user in a specific week.

        :param user_id: Unique identifier for the user
        :param week: Week number (e.g., 1, 2, etc.)
        :param activity_points: Points earned by the user in the campaign
        """
        if user_id not in self.user_data:
            self.user_data[user_id] = []
        
        # Check if participation for the week is already recorded
        for record in self.user_data[user_id]:
            if record['week'] == week:
                raise ValueError(f"Participation for week {week} is already recorded for user {user_id}.")

        # Append the new participation record
        self.user_data[user_id].append({'week': week, 'activity_points': activity_points})

    def calculate_total_rewards(self, user_id: str) -> int:
        """
        Calculates total rewards earned by the user across all weeks.

        :param user_id: Unique identifier for the user
        :return: Total rewards (sum of activity points)
        """
        if user_id not in self.user_data:
            raise ValueError(f"No participation data found for user {user_id}.")
        
        # Sum up activity points across all weeks
        return sum(record['activity_points'] for record in self.user_data[user_id])

    def get_weekly_participation(self, user_id: str) -> List[Dict[str, int]]:
        """
        Retrieves weekly participation data for a user.

        :param user_id: Unique identifier for the user
        :return: List of dictionaries containing participation data per week
        """
        if user_id not in self.user_data:
            raise ValueError(f"No participation data found for user {user_id}.")
        
        return self.user_data[user_id]

if __name__ == "__main__":
    # Example usage of the CampaignParticipationTracker class
    
    # Create an instance of the tracker
    tracker = CampaignParticipationTracker()

    try:
        # Add participation data
        tracker.add_participation(user_id="user123", week=1, activity_points=50)
        tracker.add_participation(user_id="user123", week=2, activity_points=70)
        tracker.add_participation(user_id="user456", week=1, activity_points=80)

        # Calculate total rewards
        print(f"Total rewards for user123: {tracker.calculate_total_rewards('user123')}")
        print(f"Total rewards for user456: {tracker.calculate_total_rewards('user456')}")

        # Get weekly participation data
        print(f"Weekly participation for user123: {tracker.get_weekly_participation('user123')}")
        print(f"Weekly participation for user456: {tracker.get_weekly_participation('user456')}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
