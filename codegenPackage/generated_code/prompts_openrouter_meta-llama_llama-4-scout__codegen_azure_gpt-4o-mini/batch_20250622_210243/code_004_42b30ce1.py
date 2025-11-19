"""
Generated Code Metadata:
========================
Original URL: https://mocaverse-b29.pages.dev
Prompt: "Create a library to track and manage Moca XP Rankings and Experiences on the Mocaverse platform."
Generated: DETERMINISTIC_42b30ce1f7686ca6
Batch ID: 20250622_210243
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# mocaverse.py

class MocaXPTracker:
    """
    A class to track and manage Moca XP Rankings and Experiences on the Mocaverse platform.
    """

    def __init__(self):
        """
        Initializes the MocaXPTracker with an empty list of users.
        """
        self.users = {}

    def add_user(self, user_id, user_name):
        """
        Adds a new user to the tracker.

        :param user_id: Unique identifier for the user
        :param user_name: Name of the user
        :raises ValueError: If the user already exists
        """
        if user_id in self.users:
            raise ValueError(f"User with ID {user_id} already exists.")
        self.users[user_id] = {'name': user_name, 'xp': 0, 'rank': 'Novice'}

    def add_experience(self, user_id, xp_amount):
        """
        Adds experience points to a user's total.

        :param user_id: Unique identifier for the user
        :param xp_amount: Amount of experience points to add
        :raises ValueError: If the user does not exist or xp_amount is negative
        """
        if user_id not in self.users:
            raise ValueError(f"User with ID {user_id} does not exist.")
        if xp_amount < 0:
            raise ValueError("Experience points cannot be negative.")

        self.users[user_id]['xp'] += xp_amount
        self.update_rank(user_id)

    def update_rank(self, user_id):
        """
        Updates the rank of a user based on their experience points.

        :param user_id: Unique identifier for the user
        """
        xp = self.users[user_id]['xp']
        if xp < 100:
            self.users[user_id]['rank'] = 'Novice'
        elif xp < 500:
            self.users[user_id]['rank'] = 'Intermediate'
        elif xp < 1000:
            self.users[user_id]['rank'] = 'Advanced'
        else:
            self.users[user_id]['rank'] = 'Expert'

    def get_user_info(self, user_id):
        """
        Retrieves the information of a user.

        :param user_id: Unique identifier for the user
        :return: A dictionary containing user information
        :raises ValueError: If the user does not exist
        """
        if user_id not in self.users:
            raise ValueError(f"User with ID {user_id} does not exist.")
        return self.users[user_id]

    def get_all_users(self):
        """
        Retrieves a list of all users and their information.

        :return: A dictionary of all users
        """
        return self.users

# Example usage (commented out for production)
# if __name__ == "__main__":
#     tracker = MocaXPTracker()
#     tracker.add_user("1", "Alice")
#     tracker.add_experience("1", 150)
#     print(tracker.get_user_info("1"))
#     print(tracker.get_all_users())
```
