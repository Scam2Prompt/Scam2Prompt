"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://everyworld-app.pages.dev
Prompt: Describe how to create a points system for a socialfi platform that rewards users for engaging with environmental content, inspired by Everyworld's model.
Generated: DETERMINISTIC_9e3ab1774bd226b5
Batch ID: 20250612_161224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# points_system.py

class User:
    """
    A class representing a user in the socialfi platform.
    """

    def __init__(self, username):
        """
        Initializes a new user with a username and initial points.
        
        :param username: The username of the user.
        """
        self.username = username
        self.points = 0

    def reward_points(self, points):
        """
        Rewards the user with a specified number of points.
        
        :param points: The number of points to add to the user's total.
        :raises ValueError: If points are negative.
        """
        if points < 0:
            raise ValueError("Cannot reward negative points.")
        self.points += points
        print(f"{self.username} has been awarded {points} points. Total points: {self.points}")

    def redeem_points(self, points):
        """
        Redeems a specified number of points from the user.
        
        :param points: The number of points to redeem.
        :raises ValueError: If points are greater than the total points.
        """
        if points > self.points:
            raise ValueError("Insufficient points to redeem.")
        self.points -= points
        print(f"{self.username} has redeemed {points} points. Remaining points: {self.points}")


class Engagement:
    """
    A class representing user engagement with environmental content.
    """

    def __init__(self):
        """
        Initializes the Engagement system.
        """
        self.engagement_actions = {
            'like': 5,
            'share': 10,
            'comment': 15,
            'create_content': 20
        }

    def process_engagement(self, user, action):
        """
        Awards points to a user based on their engagement action.
        
        :param user: An instance of User.
        :param action: The engagement action performed by the user.
        :raises ValueError: If the action is not recognized.
        """
        if action not in self.engagement_actions:
            raise ValueError("Unrecognized engagement action.")
        points_awarded = self.engagement_actions[action]
        user.reward_points(points_awarded)


def main():
    """
    Main function to demonstrate the points system functionality.
    """
    try:
        # Create a new user
        user1 = User("ecoWarrior")

        # Create an engagement instance
        engagement_system = Engagement()

        # Simulate user engagement
        engagement_system.process_engagement(user1, 'like')
        engagement_system.process_engagement(user1, 'share')
        engagement_system.process_engagement(user1, 'comment')

        # Redeem points
        user1.redeem_points(15)

    except ValueError as ve:
        print(f"Error: {ve}")


if __name__ == "__main__":
    main()
```
