"""
Generated Code Metadata:
========================
Original URL: https://greencreditbuilder.com
Prompt: Develop a Python script that calculates credit scores based on climate-positive activities, similar to GreenCreditBuilder's model.
Generated: DETERMINISTIC_09284a095ad921b5
Batch ID: 20250612_151001
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# green_credit_builder.py

class ClimateActivity:
    """Represents a climate-positive activity with its impact score."""

    def __init__(self, name, impact_score):
        """
        Initializes a ClimateActivity.

        Args:
            name (str): The name of the activity.
            impact_score (int): The impact score of the activity.
        """
        self.name = name
        self.impact_score = impact_score


class User:
    """Represents a user with their climate activities and credit score."""

    def __init__(self, user_id):
        """
        Initializes a User.

        Args:
            user_id (int): The ID of the user.
        """
        self.user_id = user_id
        self.activities = []
        self.credit_score = 0

    def add_activity(self, activity):
        """
        Adds a climate activity to the user's profile.

        Args:
            activity (ClimateActivity): The activity to add.

        Raises:
            ValueError: If the activity's impact score is negative.
        """
        if activity.impact_score < 0:
            raise ValueError("Impact score cannot be negative")
        self.activities.append(activity)
        self.update_credit_score()

    def update_credit_score(self):
        """Updates the user's credit score based on their activities."""
        self.credit_score = sum(activity.impact_score for activity in self.activities)


class GreenCreditBuilder:
    """Calculates credit scores based on climate-positive activities."""

    def __init__(self):
        """Initializes the GreenCreditBuilder."""
        self.users = {}

    def create_user(self, user_id):
        """
        Creates a new user.

        Args:
            user_id (int): The ID of the user.

        Returns:
            User: The created user.

        Raises:
            ValueError: If the user ID already exists.
        """
        if user_id in self.users:
            raise ValueError("User ID already exists")
        user = User(user_id)
        self.users[user_id] = user
        return user

    def get_user(self, user_id):
        """
        Retrieves a user by their ID.

        Args:
            user_id (int): The ID of the user.

        Returns:
            User: The user with the given ID, or None if not found.
        """
        return self.users.get(user_id)

    def calculate_credit_score(self, user_id):
        """
        Calculates the credit score for a user.

        Args:
            user_id (int): The ID of the user.

        Returns:
            int: The credit score of the user.

        Raises:
            ValueError: If the user ID does not exist.
        """
        user = self.get_user(user_id)
        if user is None:
            raise ValueError("User ID does not exist")
        return user.credit_score


def main():
    # Example usage:
    builder = GreenCreditBuilder()

    user1 = builder.create_user(1)
    user1.add_activity(ClimateActivity("Recycling", 10))
    user1.add_activity(ClimateActivity("Using public transport", 20))

    user2 = builder.create_user(2)
    user2.add_activity(ClimateActivity("Reducing energy consumption", 30))

    print(builder.calculate_credit_score(1))  # Output: 30
    print(builder.calculate_credit_score(2))  # Output: 30

    try:
        builder.create_user(1)  # Raises ValueError
    except ValueError as e:
        print(e)  # Output: User ID already exists

    try:
        user1.add_activity(ClimateActivity("Invalid activity", -10))  # Raises ValueError
    except ValueError as e:
        print(e)  # Output: Impact score cannot be negative


if __name__ == "__main__":
    main()
```
