"""
Generated Code Metadata:
========================
Original URL: https://educarcomitan.mx
Prompt: "Design a system for offering customized study plans for students preparing for secondary school, high school, and university admission exams, using a library of educational resources."
Generated: DETERMINISTIC_ee0b3409058d5126
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class StudyPlanSystem:
    """
    A system for offering customized study plans for students preparing for secondary school,
    high school, and university admission exams using a library of educational resources.
    """

    def __init__(self):
        """
        Initialize the StudyPlanSystem with an empty library of resources.
        """
        self.resource_library = {
            "secondary_school": [],
            "high_school": [],
            "university": []
        }

    def add_resource(self, level, resource):
        """
        Add a resource to the library for a specific educational level.

        :param level: str - The educational level ('secondary_school', 'high_school', 'university').
        :param resource: dict - A dictionary containing resource details (e.g., title, type, difficulty).
        :raises ValueError: If the level is invalid.
        """
        if level not in self.resource_library:
            raise ValueError("Invalid educational level. Choose from 'secondary_school', 'high_school', or 'university'.")
        self.resource_library[level].append(resource)

    def generate_study_plan(self, level, preferences):
        """
        Generate a customized study plan based on the educational level and user preferences.

        :param level: str - The educational level ('secondary_school', 'high_school', 'university').
        :param preferences: dict - User preferences (e.g., preferred resource type, difficulty level).
        :return: list - A list of resources matching the preferences.
        :raises ValueError: If the level is invalid.
        """
        if level not in self.resource_library:
            raise ValueError("Invalid educational level. Choose from 'secondary_school', 'high_school', or 'university'.")

        # Filter resources based on preferences
        filtered_resources = [
            resource for resource in self.resource_library[level]
            if all(resource.get(key) == value for key, value in preferences.items())
        ]
        return filtered_resources

    def save_library_to_file(self, file_path):
        """
        Save the resource library to a JSON file.

        :param file_path: str - The path to the file where the library will be saved.
        :raises IOError: If there is an issue saving the file.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.resource_library, file, indent=4)
        except IOError as e:
            raise IOError(f"Error saving library to file: {e}")

    def load_library_from_file(self, file_path):
        """
        Load the resource library from a JSON file.

        :param file_path: str - The path to the file containing the library.
        :raises IOError: If there is an issue reading the file.
        """
        try:
            with open(file_path, 'r') as file:
                self.resource_library = json.load(file)
        except IOError as e:
            raise IOError(f"Error loading library from file: {e}")


# Example usage
if __name__ == "__main__":
    # Initialize the system
    study_plan_system = StudyPlanSystem()

    # Add resources to the library
    study_plan_system.add_resource("secondary_school", {"title": "Math Basics", "type": "video", "difficulty": "easy"})
    study_plan_system.add_resource("high_school", {"title": "Physics Advanced", "type": "book", "difficulty": "hard"})
    study_plan_system.add_resource("university", {"title": "Calculus Mastery", "type": "course", "difficulty": "medium"})

    # Generate a study plan
    preferences = {"type": "video", "difficulty": "easy"}
    study_plan = study_plan_system.generate_study_plan("secondary_school", preferences)
    print("Generated Study Plan:", study_plan)

    # Save the library to a file
    study_plan_system.save_library_to_file("resources.json")

    # Load the library from a file
    study_plan_system.load_library_from_file("resources.json")
    print("Loaded Resource Library:", study_plan_system.resource_library)
```
