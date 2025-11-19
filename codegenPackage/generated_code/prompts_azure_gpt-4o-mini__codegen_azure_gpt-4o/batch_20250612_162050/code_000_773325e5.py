"""
Generated Code Metadata:
========================
Original URL: https://heartofjesuscollege.com
Prompt: Generate a code snippet that implements a "Learning by Doing" educational module for a bilingual school, inspired by the HJ-THINKING methodology.
Generated: DETERMINISTIC_773325e55c7da692
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Educational Module: Learning by Doing (Inspired by HJ-THINKING Methodology)
This module is designed for a bilingual school to facilitate interactive learning.
The program allows students to engage in tasks, reflect on their actions, and learn in both languages.
"""

class LearningByDoingModule:
    """
    A class to implement the Learning by Doing educational module.
    """

    def __init__(self, language_1: str, language_2: str):
        """
        Initialize the module with two languages for bilingual support.

        :param language_1: Primary language (e.g., "English")
        :param language_2: Secondary language (e.g., "Spanish")
        """
        self.language_1 = language_1
        self.language_2 = language_2
        self.activities = []  # List to store learning activities

    def add_activity(self, activity_name: str, description_lang1: str, description_lang2: str):
        """
        Add a new activity to the module.

        :param activity_name: Name of the activity
        :param description_lang1: Description of the activity in the primary language
        :param description_lang2: Description of the activity in the secondary language
        """
        activity = {
            "name": activity_name,
            "description": {
                self.language_1: description_lang1,
                self.language_2: description_lang2
            }
        }
        self.activities.append(activity)

    def display_activities(self):
        """
        Display all activities in both languages.
        """
        if not self.activities:
            print("No activities available. Please add some activities first.")
            return

        print(f"Activities ({self.language_1} / {self.language_2}):")
        for idx, activity in enumerate(self.activities, start=1):
            print(f"{idx}. {activity['name']}")
            print(f"   {self.language_1}: {activity['description'][self.language_1]}")
            print(f"   {self.language_2}: {activity['description'][self.language_2]}")

    def start_activity(self, activity_index: int):
        """
        Start a specific activity by its index.

        :param activity_index: Index of the activity to start (1-based index)
        """
        try:
            activity = self.activities[activity_index - 1]
            print(f"Starting Activity: {activity['name']}")
            print(f"{self.language_1}: {activity['description'][self.language_1]}")
            print(f"{self.language_2}: {activity['description'][self.language_2]}")
            print("Engage in the activity and reflect on your learning!")
        except IndexError:
            print("Error: Invalid activity index. Please select a valid activity.")

# Example usage
if __name__ == "__main__":
    # Initialize the module with English and Spanish as the two languages
    module = LearningByDoingModule("English", "Spanish")

    # Add some activities
    module.add_activity(
        "Plant a Tree",
        "Learn how to plant a tree and take care of it.",
        "Aprende cómo plantar un árbol y cuidarlo."
    )
    module.add_activity(
        "Build a Birdhouse",
        "Create a birdhouse using simple materials.",
        "Crea una casita para pájaros usando materiales simples."
    )

    # Display all activities
    module.display_activities()

    # Start an activity
    module.start_activity(1)  # Start the first activity
```
