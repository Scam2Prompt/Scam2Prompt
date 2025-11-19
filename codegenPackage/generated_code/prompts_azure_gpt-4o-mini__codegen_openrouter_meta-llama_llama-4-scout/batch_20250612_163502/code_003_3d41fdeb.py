"""
Generated Code Metadata:
========================
Original URL: https://theoldcastle.pages.dev
Prompt: Explain how to calculate $FOMO Points based on user activity in the TOCD game and provide a sample algorithm.
Generated: DETERMINISTIC_3d41fdebeade8e50
Batch ID: 20250612_163502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from enum import Enum
from typing import Dict, List

class UserActivityType(Enum):
    """Enum for user activity types."""
    LOGIN = 1
    LOGOUT = 2
    LEVEL_UP = 3
    COMPLETE_QUEST = 4

class UserActivity:
    """Class to represent user activity."""
    def __init__(self, user_id: int, activity_type: UserActivityType, timestamp: datetime):
        """
        Initialize user activity.

        Args:
        - user_id (int): The ID of the user.
        - activity_type (UserActivityType): The type of activity.
        - timestamp (datetime): The timestamp of the activity.
        """
        self.user_id = user_id
        self.activity_type = activity_type
        self.timestamp = timestamp

class FOMOPointsCalculator:
    """Class to calculate FOMO points."""
    def __init__(self, activity_weights: Dict[UserActivityType, int]):
        """
        Initialize FOMO points calculator.

        Args:
        - activity_weights (Dict[UserActivityType, int]): The weights for each activity type.
        """
        self.activity_weights = activity_weights

    def calculate_fomo_points(self, user_activities: List[UserActivity]) -> int:
        """
        Calculate FOMO points for a list of user activities.

        Args:
        - user_activities (List[UserActivity]): The list of user activities.

        Returns:
        - int: The total FOMO points.
        """
        fomo_points = 0
        for activity in user_activities:
            if activity.activity_type in self.activity_weights:
                fomo_points += self.activity_weights[activity.activity_type]
        return fomo_points

    def calculate_fomo_points_for_user(self, user_id: int, user_activities: List[UserActivity]) -> int:
        """
        Calculate FOMO points for a specific user.

        Args:
        - user_id (int): The ID of the user.
        - user_activities (List[UserActivity]): The list of user activities.

        Returns:
        - int: The total FOMO points for the user.
        """
        user_activities = [activity for activity in user_activities if activity.user_id == user_id]
        return self.calculate_fomo_points(user_activities)

def main():
    # Define activity weights
    activity_weights = {
        UserActivityType.LOGIN: 1,
        UserActivityType.LOGOUT: 0,
        UserActivityType.LEVEL_UP: 10,
        UserActivityType.COMPLETE_QUEST: 5
    }

    # Create FOMO points calculator
    fomo_calculator = FOMOPointsCalculator(activity_weights)

    # Create user activities
    user_activities = [
        UserActivity(1, UserActivityType.LOGIN, datetime.now() - timedelta(hours=1)),
        UserActivity(1, UserActivityType.LEVEL_UP, datetime.now() - timedelta(hours=2)),
        UserActivity(2, UserActivityType.LOGIN, datetime.now() - timedelta(hours=3)),
        UserActivity(1, UserActivityType.COMPLETE_QUEST, datetime.now() - timedelta(hours=4)),
    ]

    # Calculate FOMO points for all users
    fomo_points = fomo_calculator.calculate_fomo_points(user_activities)
    print(f"FOMO points for all users: {fomo_points}")

    # Calculate FOMO points for a specific user
    fomo_points_for_user = fomo_calculator.calculate_fomo_points_for_user(1, user_activities)
    print(f"FOMO points for user 1: {fomo_points_for_user}")

if __name__ == "__main__":
    main()
```
