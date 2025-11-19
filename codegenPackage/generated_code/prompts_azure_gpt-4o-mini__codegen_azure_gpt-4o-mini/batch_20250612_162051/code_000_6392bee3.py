"""
Generated Code Metadata:
========================
Original URL: https://www.viviresconvivir.cl
Prompt: Write a Python script that implements educational activities for children aged 4 to 9, focusing on values such as respect, participation, and responsibility as outlined in the "Vivir es Convivir" program.
Generated: DETERMINISTIC_6392bee3b81cc289
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class EducationalActivity:
    """
    A class to represent an educational activity focused on values for children.
    """

    def __init__(self, name, description, age_group, value):
        """
        Initializes an EducationalActivity instance.

        :param name: str - The name of the activity
        :param description: str - A brief description of the activity
        :param age_group: tuple - The age range for which the activity is suitable
        :param value: str - The core value the activity promotes
        """
        self.name = name
        self.description = description
        self.age_group = age_group
        self.value = value

    def is_suitable_for_age(self, age):
        """
        Checks if the activity is suitable for a given age.

        :param age: int - The age of the child
        :return: bool - True if suitable, False otherwise
        """
        return self.age_group[0] <= age <= self.age_group[1]


class ActivityManager:
    """
    A class to manage a collection of educational activities.
    """

    def __init__(self):
        """
        Initializes the ActivityManager with an empty list of activities.
        """
        self.activities = []

    def add_activity(self, activity):
        """
        Adds an educational activity to the manager.

        :param activity: EducationalActivity - The activity to add
        """
        if not isinstance(activity, EducationalActivity):
            raise ValueError("activity must be an instance of EducationalActivity")
        self.activities.append(activity)

    def get_activities_for_age(self, age):
        """
        Retrieves a list of activities suitable for a given age.

        :param age: int - The age of the child
        :return: list - A list of suitable activities
        """
        suitable_activities = [activity for activity in self.activities if activity.is_suitable_for_age(age)]
        return suitable_activities


def main():
    """
    Main function to demonstrate the EducationalActivity and ActivityManager classes.
    """
    # Create an instance of ActivityManager
    activity_manager = ActivityManager()

    # Define some educational activities
    activities = [
        EducationalActivity("Respect Relay", 
                            "A fun relay race where children pass a baton while saying something respectful about their teammates.", 
                            (4, 9), 
                            "Respect"),
        EducationalActivity("Participation Puzzle", 
                            "A group puzzle activity where each child contributes a piece to complete the picture.", 
                            (4, 9), 
                            "Participation"),
        EducationalActivity("Responsibility Role Play", 
                            "Children take turns acting out different roles that require responsibility, like being a teacher or a parent.", 
                            (4, 9), 
                            "Responsibility"),
        EducationalActivity("Kindness Cards", 
                            "Children create cards with kind messages to give to others, promoting kindness and respect.", 
                            (4, 9), 
                            "Respect"),
    ]

    # Add activities to the manager
    for activity in activities:
        activity_manager.add_activity(activity)

    # Get activities for a specific age
    age = random.randint(4, 9)  # Simulate a random age for demonstration
    print(f"Activities suitable for age {age}:")
    suitable_activities = activity_manager.get_activities_for_age(age)

    # Display suitable activities
    for activity in suitable_activities:
        print(f"- {activity.name}: {activity.description} (Value: {activity.value})")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
