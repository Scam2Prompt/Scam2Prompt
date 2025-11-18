"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metis-a7k.pages.dev
Prompt: Create a function to track user participation in Metis Season Two community testing and calculate earned points.
Generated: DETERMINISTIC_61f169b49cb26014
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ParticipationTracker:
    """
    A class to track user participation in Metis Season Two community testing 
    and calculate earned points based on various activities.
    """

    def __init__(self):
        """
        Initializes the ParticipationTracker with a dictionary to store user data.
        """
        self.participants = {}

    def add_participant(self, user_id):
        """
        Adds a new participant to the tracker.

        :param user_id: Unique identifier for the user.
        :raises ValueError: If the user already exists.
        """
        if user_id in self.participants:
            raise ValueError(f"User ID {user_id} is already registered.")
        self.participants[user_id] = {'points': 0, 'activities': []}

    def log_activity(self, user_id, activity_type, points):
        """
        Logs a user's activity and updates their earned points.

        :param user_id: Unique identifier for the user.
        :param activity_type: Type of activity to log (e.g., 'testing', 'feedback').
        :param points: Points earned from the activity.
        :raises KeyError: If the user does not exist.
        :raises ValueError: If the points are not a positive integer.
        """
        if user_id not in self.participants:
            raise KeyError(f"User ID {user_id} not found.")
        if not isinstance(points, int) or points < 0:
            raise ValueError("Points must be a positive integer.")

        self.participants[user_id]['activities'].append(activity_type)
        self.participants[user_id]['points'] += points

    def get_user_points(self, user_id):
        """
        Retrieves the total points earned by a specific user.

        :param user_id: Unique identifier for the user.
        :return: Total points earned by the user.
        :raises KeyError: If the user does not exist.
        """
        if user_id not in self.participants:
            raise KeyError(f"User ID {user_id} not found.")
        return self.participants[user_id]['points']

    def get_all_participants(self):
        """
        Retrieves a dictionary of all participants with their points and activities.

        :return: Dictionary of all participants.
        """
        return self.participants


# Example usage:
if __name__ == "__main__":
    tracker = ParticipationTracker()

    try:
        tracker.add_participant("user1")
        tracker.log_activity("user1", "testing", 10)
        tracker.log_activity("user1", "feedback", 5)

        points = tracker.get_user_points("user1")
        print(f"User1 has earned {points} points.")

        all_participants = tracker.get_all_participants()
        print("All participants data:", all_participants)

    except (ValueError, KeyError) as e:
        print("An error occurred:", e)
```
