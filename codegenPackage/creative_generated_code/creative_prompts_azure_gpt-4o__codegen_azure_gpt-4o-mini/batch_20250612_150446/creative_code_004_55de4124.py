"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eunitedcryptofx.com
Prompt: Develop a ranking badge system for users based on their investment activity, as described on eunitedcryptofx.com.
Generated: DETERMINISTIC_55de41248ed0d4eb
Batch ID: 20250612_150446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class User:
    """
    A class to represent a user in the investment ranking system.
    """

    def __init__(self, user_id, investment_amount):
        """
        Initializes a new user with an ID and initial investment amount.

        :param user_id: Unique identifier for the user
        :param investment_amount: Initial investment amount made by the user
        """
        self.user_id = user_id
        self.investment_amount = investment_amount
        self.badge = self.assign_badge(investment_amount)

    def assign_badge(self, investment_amount):
        """
        Assigns a badge based on the investment amount.

        :param investment_amount: The amount the user has invested
        :return: A string representing the user's badge
        """
        if investment_amount < 1000:
            return "Novice"
        elif 1000 <= investment_amount < 5000:
            return "Intermediate"
        elif 5000 <= investment_amount < 20000:
            return "Advanced"
        else:
            return "Expert"

    def update_investment(self, new_investment):
        """
        Updates the investment amount and reassigns the badge if necessary.

        :param new_investment: The new investment amount to be added
        """
        if new_investment < 0:
            raise ValueError("Investment amount must be positive.")
        
        self.investment_amount += new_investment
        self.badge = self.assign_badge(self.investment_amount)


class BadgeSystem:
    """
    A class to manage the ranking badge system for multiple users.
    """

    def __init__(self):
        """
        Initializes the badge system with an empty user list.
        """
        self.users = {}

    def add_user(self, user_id, investment_amount):
        """
        Adds a new user to the badge system.

        :param user_id: Unique identifier for the user
        :param investment_amount: Initial investment amount made by the user
        """
        if user_id in self.users:
            raise ValueError("User ID already exists.")
        
        self.users[user_id] = User(user_id, investment_amount)

    def update_user_investment(self, user_id, new_investment):
        """
        Updates the investment amount for a given user.

        :param user_id: Unique identifier for the user
        :param new_investment: The amount to be added to the user's investment
        """
        if user_id not in self.users:
            raise KeyError("User ID not found.")

        self.users[user_id].update_investment(new_investment)

    def get_user_badge(self, user_id):
        """
        Retrieves the badge for a given user.

        :param user_id: Unique identifier for the user
        :return: The user's badge
        """
        if user_id not in self.users:
            raise KeyError("User ID not found.")

        return self.users[user_id].badge


# Example usage of the BadgeSystem
if __name__ == "__main__":
    try:
        badge_system = BadgeSystem()
        
        # Adding users with their initial investments
        badge_system.add_user("user1", 1500)
        badge_system.add_user("user2", 7000)
        
        # Updating investments
        badge_system.update_user_investment("user1", 500)
        badge_system.update_user_investment("user2", 5000)

        # Retrieving badges
        print(f"User1 Badge: {badge_system.get_user_badge('user1')}")  # Output: Intermediate
        print(f"User2 Badge: {badge_system.get_user_badge('user2')}")  # Output: Expert

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
