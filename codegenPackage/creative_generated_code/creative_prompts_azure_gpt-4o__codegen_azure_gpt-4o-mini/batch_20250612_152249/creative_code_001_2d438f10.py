"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeidmmx6ovrkgb7pb5l6vt5iccg5zig3n4kdoo3t6qc7oswvkxckfy4.ipfs.dweb.link
Prompt: Generate code to calculate quarterly points multipliers for users with consecutive trading activity, based on the rules mentioned on the Blitz platform.
Generated: DETERMINISTIC_2d438f10b68da468
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
from collections import defaultdict
from typing import List, Tuple, Dict

class UserActivity:
    """Class to represent user activity for trading."""
    
    def __init__(self, user_id: str, activity_date: datetime):
        self.user_id = user_id
        self.activity_date = activity_date

def calculate_quarterly_multipliers(user_activities: List[UserActivity]) -> Dict[str, float]:
    """
    Calculate quarterly points multipliers for users based on their consecutive trading activity.

    Args:
        user_activities: A list of UserActivity objects representing user trading activities.

    Returns:
        A dictionary with user IDs as keys and their corresponding multipliers as values.
    """
    # Dictionary to hold user activity dates
    user_activity_map = defaultdict(list)

    # Organize activities by user id
    for activity in user_activities:
        user_activity_map[activity.user_id].append(activity.activity_date)

    # Dictionary to hold multipliers
    multipliers = {}

    # Define quarterly periods
    current_year = datetime.now().year
    quarters = [(1, datetime(current_year, 1, 1)), 
                (2, datetime(current_year, 4, 1)), 
                (3, datetime(current_year, 7, 1)), 
                (4, datetime(current_year, 10, 1))]

    for user_id, activities in user_activity_map.items():
        # Sort activities by date
        activities.sort()
        consecutive_days = 0
        multiplier = 1.0

        # Analyze activities for multipliers
        for i in range(len(activities)):
            if i == 0 or (activities[i] - activities[i - 1]).days == 1:
                consecutive_days += 1
            else:
                # Check for quarter completion based on consecutive days
                if consecutive_days >= 5:
                    multiplier += 0.1  # Increase multiplier for every 5 consecutive days
                consecutive_days = 1  # Reset for new streak

        # Final check for multiplier
        if consecutive_days >= 5:
            multiplier += 0.1

        # Assign calculated multiplier
        multipliers[user_id] = round(multiplier, 2)

    return multipliers

def main():
    # Sample data
    user_activities = [
        UserActivity("user1", datetime(2023, 1, 2)),
        UserActivity("user1", datetime(2023, 1, 3)),
        UserActivity("user1", datetime(2023, 1, 4)),
        UserActivity("user1", datetime(2023, 1, 5)),
        UserActivity("user1", datetime(2023, 1, 6)),
        UserActivity("user2", datetime(2023, 1, 2)),
        UserActivity("user2", datetime(2023, 1, 4)),
        UserActivity("user2", datetime(2023, 1, 5)),
        UserActivity("user2", datetime(2023, 1, 6)),
        UserActivity("user2", datetime(2023, 1, 7)),
    ]

    try:
        multipliers = calculate_quarterly_multipliers(user_activities)
        print("Quarterly Point Multipliers:", multipliers)
    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    main()
```
