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
# Import necessary modules
import json

class DatingProfile:
    """
    A class to represent a dating profile template.
    Allows users to showcase their interests, preferences, expectations, and relationship goals.
    """

    def __init__(self, name, age, gender, location):
        """
        Initialize the basic profile information.
        :param name: str - User's name (can be a nickname for discretion)
        :param age: int - User's age
        :param gender: str - User's gender
        :param location: str - User's location (city/state/country)
        """
        self.name = name
        self.age = age
        self.gender = gender
        self.location = location
        self.interests = []
        self.preferences = {}
        self.expectations = ""
        self.relationship_goals = ""

    def add_interest(self, interest):
        """
        Add an interest to the user's profile.
        :param interest: str - A hobby or activity the user enjoys
        """
        if interest and isinstance(interest, str):
            self.interests.append(interest)
        else:
            raise ValueError("Interest must be a non-empty string.")

    def set_preferences(self, preferences):
        """
        Set user preferences for a potential match.
        :param preferences: dict - A dictionary containing preferences (e.g., age range, gender, etc.)
        """
        if preferences and isinstance(preferences, dict):
            self.preferences = preferences
        else:
            raise ValueError("Preferences must be a dictionary.")

    def set_expectations(self, expectations):
        """
        Set user expectations for a relationship.
        :param expectations: str - A brief description of what the user expects in a relationship
        """
        if expectations and isinstance(expectations, str):
            self.expectations = expectations
        else:
            raise ValueError("Expectations must be a non-empty string.")

    def set_relationship_goals(self, goals):
        """
        Set user relationship goals.
        :param goals: str - A brief description of the user's relationship goals
        """
        if goals and isinstance(goals, str):
            self.relationship_goals = goals
        else:
            raise ValueError("Relationship goals must be a non-empty string.")

    def to_dict(self):
        """
        Convert the profile to a dictionary format for serialization or display.
        :return: dict - A dictionary representation of the profile
        """
        return {
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "location": self.location,
            "interests": self.interests,
            "preferences": self.preferences,
            "expectations": self.expectations,
            "relationship_goals": self.relationship_goals,
        }

    def to_json(self):
        """
        Convert the profile to a JSON string for storage or transmission.
        :return: str - A JSON string representation of the profile
        """
        return json.dumps(self.to_dict(), indent=4)

# Example usage
if __name__ == "__main__":
    try:
        # Create a new dating profile
        profile = DatingProfile(name="Alex", age=30, gender="Non-binary", location="New York")

        # Add interests
        profile.add_interest("Hiking")
        profile.add_interest("Reading")
        profile.add_interest("Cooking")

        # Set preferences
        profile.set_preferences({
            "age_range": "25-35",
            "gender": "Any",
            "location_preference": "Within 50 miles"
        })

        # Set expectations
        profile.set_expectations("Looking for someone who values honesty and communication.")

        # Set relationship goals
        profile.set_relationship_goals("Seeking a long-term, committed relationship.")

        # Display the profile as JSON
        print(profile.to_json())

    except Exception as e:
        # Handle any errors gracefully
        print(f"An error occurred: {e}")
```
