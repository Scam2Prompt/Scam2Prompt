"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://betbax.net
Prompt: Create a function to implement a loyalty rewards program for users, inspired by the features mentioned on the BaxBet platform.
Generated: DETERMINISTIC_76c32c2b4076400b
Batch ID: 20250612_155849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class LoyaltyRewardsProgram:
    """
    A class to represent a loyalty rewards program for users.

    Features:
    - Points are awarded based on user activity.
    - Users can redeem points for rewards if they meet the threshold.
    - Tracks user activity and manages points.
    - Provides error handling for invalid operations.
    """

    def __init__(self, point_rate=10, redemption_threshold=100):
        """
        Initialize the loyalty rewards program.

        Args:
            point_rate (int): Points awarded per unit of activity (default is 10).
            redemption_threshold (int): Minimum points required to redeem rewards (default is 100).
        """
        self.users = {}  # Store user data as a dictionary {user_id: {points, activities}}
        self.point_rate = point_rate
        self.redemption_threshold = redemption_threshold

    def register_user(self, user_id):
        """
        Register a new user in the loyalty program.

        Args:
            user_id (str): Unique identifier for the user.

        Raises:
            ValueError: If the user already exists.
        """
        if user_id in self.users:
            raise ValueError(f"User '{user_id}' is already registered.")
        self.users[user_id] = {"points": 0, "activities": []}

    def record_activity(self, user_id, activity_description):
        """
        Record an activity for the user and award points.

        Args:
            user_id (str): Unique identifier for the user.
            activity_description (str): Description of the activity.

        Raises:
            ValueError: If the user is not registered.
        """
        if user_id not in self.users:
            raise ValueError(f"User '{user_id}' is not registered.")
        
        # Record activity
        activity = {
            "description": activity_description,
            "timestamp": datetime.datetime.now()
        }
        self.users[user_id]["activities"].append(activity)
        
        # Award points
        self.users[user_id]["points"] += self.point_rate

    def redeem_points(self, user_id):
        """
        Redeem points for a reward if the user has enough points.

        Args:
            user_id (str): Unique identifier for the user.

        Returns:
            str: Message indicating the success or failure of the redemption.

        Raises:
            ValueError: If the user is not registered.
        """
        if user_id not in self.users:
            raise ValueError(f"User '{user_id}' is not registered.")
        
        if self.users[user_id]["points"] >= self.redemption_threshold:
            self.users[user_id]["points"] -= self.redemption_threshold
            return f"User '{user_id}' successfully redeemed a reward!"
        else:
            return f"User '{user_id}' does not have enough points to redeem a reward."

    def get_user_points(self, user_id):
        """
        Retrieve the current points for the user.

        Args:
            user_id (str): Unique identifier for the user.

        Returns:
            int: The number of points the user has.

        Raises:
            ValueError: If the user is not registered.
        """
        if user_id not in self.users:
            raise ValueError(f"User '{user_id}' is not registered.")
        return self.users[user_id]["points"]

    def get_user_activities(self, user_id):
        """
        Retrieve the activity log for the user.

        Args:
            user_id (str): Unique identifier for the user.

        Returns:
            list: A list of activities logged by the user.

        Raises:
            ValueError: If the user is not registered.
        """
        if user_id not in self.users:
            raise ValueError(f"User '{user_id}' is not registered.")
        return self.users[user_id]["activities"]


if __name__ == "__main__":
    # Example usage of the LoyaltyRewardsProgram
    program = LoyaltyRewardsProgram(point_rate=10, redemption_threshold=100)
    
    try:
        program.register_user("user123")
        program.record_activity("user123", "Purchased a product")
        program.record_activity("user123", "Reviewed a product")
        
        print(f"Current points for user123: {program.get_user_points('user123')}")
        print(f"Activity log for user123: {program.get_user_activities('user123')}")
        
        print(program.redeem_points("user123"))  # Redemption attempt
        print(f"Current points for user123 after redemption: {program.get_user_points('user123')}")
    except ValueError as e:
        print(f"Error: {e}")
```
