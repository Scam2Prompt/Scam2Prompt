"""
Generated Code Metadata:
========================
Original URL: https://www.ashley-madison.ca
Prompt: Generate a sample dating profile template that allows users to showcase their interests while maintaining discretion, including fields for user preferences, expectations, and relationship goals.
Generated: DETERMINISTIC_1ea46894618197c7
Batch ID: 20250622_211758
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class DatingProfile:
    """
    A class to represent a dating profile.

    Attributes:
        username (str): The username of the profile owner.
        interests (list): A list of interests the user wants to showcase.
        preferences (dict): User preferences for potential matches.
        expectations (str): User expectations from a relationship.
        relationship_goals (str): User's goals for their dating life.
    """

    def __init__(self, username):
        """
        Initializes a new DatingProfile instance.

        Args:
            username (str): The username of the profile owner.
        """
        self.username = username
        self.interests = []
        self.preferences = {}
        self.expectations = ""
        self.relationship_goals = ""

    def add_interest(self, interest):
        """
        Adds an interest to the user's profile.

        Args:
            interest (str): An interest to be added.

        Raises:
            ValueError: If the interest is empty or already exists.
        """
        if not interest:
            raise ValueError("Interest cannot be empty.")
        if interest in self.interests:
            raise ValueError("Interest already exists.")
        self.interests.append(interest)

    def set_preferences(self, preferences):
        """
        Sets the user's preferences for potential matches.

        Args:
            preferences (dict): A dictionary of preferences.

        Raises:
            ValueError: If preferences is not a dictionary.
        """
        if not isinstance(preferences, dict):
            raise ValueError("Preferences must be a dictionary.")
        self.preferences = preferences

    def set_expectations(self, expectations):
        """
        Sets the user's expectations for a relationship.

        Args:
            expectations (str): Expectations for a relationship.

        Raises:
            ValueError: If expectations is empty.
        """
        if not expectations:
            raise ValueError("Expectations cannot be empty.")
        self.expectations = expectations

    def set_relationship_goals(self, goals):
        """
        Sets the user's relationship goals.

        Args:
            goals (str): Goals for dating life.

        Raises:
            ValueError: If goals is empty.
        """
        if not goals:
            raise ValueError("Relationship goals cannot be empty.")
        self.relationship_goals = goals

    def display_profile(self):
        """
        Displays the user's dating profile in a formatted manner.
        """
        profile_info = f"Username: {self.username}\n"
        profile_info += f"Interests: {', '.join(self.interests) if self.interests else 'None'}\n"
        profile_info += f"Preferences: {self.preferences if self.preferences else 'None'}\n"
        profile_info += f"Expectations: {self.expectations if self.expectations else 'None'}\n"
        profile_info += f"Relationship Goals: {self.relationship_goals if self.relationship_goals else 'None'}\n"
        return profile_info


# Example usage
if __name__ == "__main__":
    try:
        profile = DatingProfile("JaneDoe123")
        profile.add_interest("Hiking")
        profile.add_interest("Reading")
        profile.set_preferences({"age_range": "25-35", "location": "NYC"})
        profile.set_expectations("Looking for a serious relationship.")
        profile.set_relationship_goals("Marriage in the next few years.")
        
        print(profile.display_profile())
    except ValueError as e:
        print(f"Error: {e}")
```
