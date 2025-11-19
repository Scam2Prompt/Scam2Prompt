"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stailoud.io
Prompt: What are the best practices for creating a sustainable engagement cycle in a crypto project like Loud, which rewards users for their social interactions?
Generated: DETERMINISTIC_43edeb231e423c09
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

class UserEngagement:
    """
    A class to manage user engagement in a cryptocurrency project.
    This class handles social interactions and rewards users accordingly.
    """

    def __init__(self):
        """Initialize the UserEngagement class with an empty user list."""
        self.users = {}
        logging.basicConfig(level=logging.INFO)

    def add_user(self, user_id, user_name):
        """
        Add a new user to the engagement system.

        :param user_id: Unique identifier for the user.
        :param user_name: Name of the user.
        """
        if user_id in self.users:
            logging.error(f"User ID {user_id} already exists.")
            raise ValueError("User ID already exists.")
        self.users[user_id] = {'name': user_name, 'points': 0}
        logging.info(f"Added user: {user_name} with ID: {user_id}")

    def record_interaction(self, user_id, interaction_type):
        """
        Record a user's interaction and reward points.

        :param user_id: Unique identifier for the user.
        :param interaction_type: Type of interaction (e.g. 'like', 'comment', 'share').
        """
        if user_id not in self.users:
            logging.error(f"User ID {user_id} does not exist.")
            raise ValueError("User ID does not exist.")

        reward_points = self._calculate_reward(interaction_type)
        self.users[user_id]['points'] += reward_points
        logging.info(f"User ID {user_id} performed a {interaction_type} and earned {reward_points} points.")

    def _calculate_reward(self, interaction_type):
        """
        Calculate reward points based on the interaction type.

        :param interaction_type: Type of interaction.
        :return: Points awarded for the interaction.
        """
        reward_map = {
            'like': 1,
            'comment': 3,
            'share': 5
        }
        return reward_map.get(interaction_type, 0)

    def get_user_points(self, user_id):
        """
        Retrieve the total points for a specific user.

        :param user_id: Unique identifier for the user.
        :return: Total points of the user.
        """
        if user_id not in self.users:
            logging.error(f"User ID {user_id} does not exist.")
            raise ValueError("User ID does not exist.")
        return self.users[user_id]['points']

    def display_users(self):
        """
        Display all users and their points.
        """
        for user_id, user_info in self.users.items():
            logging.info(f"User: {user_info['name']} (ID: {user_id}) has {user_info['points']} points.")

# Example usage
if __name__ == "__main__":
    engagement_system = UserEngagement()

    try:
        engagement_system.add_user("1", "Alice")
        engagement_system.add_user("2", "Bob")
        engagement_system.record_interaction("1", "like")
        engagement_system.record_interaction("1", "comment")
        engagement_system.record_interaction("2", "share")

        engagement_system.display_users()
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
