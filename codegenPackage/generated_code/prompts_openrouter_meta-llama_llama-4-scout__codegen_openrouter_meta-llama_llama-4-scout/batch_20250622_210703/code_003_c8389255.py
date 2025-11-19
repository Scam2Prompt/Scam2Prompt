"""
Generated Code Metadata:
========================
Original URL: https://pp4.swiebodzin.pl
Prompt: Generate a list of educational activities suitable for preschoolers using a specific programming language (e.g., ScratchJr).
Generated: DETERMINISTIC_c83892558d1f6b36
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# educational_activities.py

class EducationalActivity:
    """Represents an educational activity for preschoolers."""

    def __init__(self, name, description, age_group, programming_language):
        """
        Initializes an EducationalActivity.

        Args:
            name (str): The name of the activity.
            description (str): A brief description of the activity.
            age_group (str): The age group suitable for the activity.
            programming_language (str): The programming language used in the activity.
        """
        self.name = name
        self.description = description
        self.age_group = age_group
        self.programming_language = programming_language

    def __str__(self):
        return f"{self.name}: {self.description}"


class ActivityGenerator:
    """Generates a list of educational activities suitable for preschoolers."""

    def __init__(self):
        self.activities = []

    def add_activity(self, activity):
        """
        Adds an educational activity to the list.

        Args:
            activity (EducationalActivity): The activity to add.
        """
        self.activities.append(activity)

    def get_activities(self, programming_language=None):
        """
        Retrieves a list of educational activities.

        Args:
            programming_language (str, optional): Filters activities by programming language. Defaults to None.

        Returns:
            list: A list of educational activities.
        """
        if programming_language:
            return [activity for activity in self.activities if activity.programming_language == programming_language]
        return self.activities


def main():
    try:
        generator = ActivityGenerator()

        # Add activities for ScratchJr
        generator.add_activity(EducationalActivity(
            "Animal Adventure",
            "Create an interactive story with animals using ScratchJr.",
            "3-5 years",
            "ScratchJr"
        ))
        generator.add_activity(EducationalActivity(
            "Coding Dance Party",
            "Use ScratchJr to create a dance party with coded animations.",
            "3-5 years",
            "ScratchJr"
        ))
        generator.add_activity(EducationalActivity(
            "Garden Growth",
            "Learn about cause-and-effect relationships by coding a virtual garden with ScratchJr.",
            "3-5 years",
            "ScratchJr"
        ))

        # Retrieve activities for ScratchJr
        scratchjr_activities = generator.get_activities("ScratchJr")

        # Print activities
        print("Educational Activities for Preschoolers using ScratchJr:")
        for activity in scratchjr_activities:
            print(activity)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
