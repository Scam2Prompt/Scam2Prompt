"""
Generated Code Metadata:
========================
Original URL: https://virtual5.com.mx
Prompt: Develop a library function that generates personalized learning paths based on user goals, similar to the strategic planning offered by Virtual5 in their courses.
Generated: DETERMINISTIC_78c11e82b78f56c7
Batch ID: 20250612_163423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class LearningPathGenerator:
    """
    A class to generate personalized learning paths based on user goals.
    """

    def __init__(self, courses: List[Dict[str, Any]]):
        """
        Initializes the LearningPathGenerator with a list of available courses.

        :param courses: A list of dictionaries containing course information.
        """
        self.courses = courses

    def generate_learning_path(self, user_goals: List[str]) -> List[Dict[str, Any]]:
        """
        Generates a personalized learning path based on user goals.

        :param user_goals: A list of goals that the user wants to achieve.
        :return: A list of courses that align with the user's goals.
        """
        if not user_goals:
            raise ValueError("User goals must not be empty.")

        learning_path = []
        for goal in user_goals:
            matched_courses = self._find_courses_for_goal(goal)
            learning_path.extend(matched_courses)

        return learning_path

    def _find_courses_for_goal(self, goal: str) -> List[Dict[str, Any]]:
        """
        Finds courses that match a specific user goal.

        :param goal: The user goal to match courses against.
        :return: A list of courses that match the goal.
        """
        matched_courses = []
        for course in self.courses:
            if goal.lower() in course.get('description', '').lower():
                matched_courses.append(course)
        
        return matched_courses

    def save_learning_path(self, learning_path: List[Dict[str, Any]], filename: str) -> None:
        """
        Saves the generated learning path to a JSON file.

        :param learning_path: The learning path to save.
        :param filename: The name of the file to save the learning path to.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(learning_path, file, indent=4)
        except IOError as e:
            raise RuntimeError(f"Failed to save learning path to {filename}: {e}")

# Example usage
if __name__ == "__main__":
    # Sample courses data
    courses_data = [
        {"title": "Python Basics", "description": "Learn the basics of Python programming."},
        {"title": "Data Science with Python", "description": "Apply Python in data science."},
        {"title": "Web Development", "description": "Build web applications using Python."},
        {"title": "Machine Learning", "description": "Introduction to machine learning concepts."}
    ]

    # Initialize the LearningPathGenerator with available courses
    generator = LearningPathGenerator(courses=courses_data)

    # Define user goals
    user_goals = ["Python programming", "data science"]

    # Generate learning path
    learning_path = generator.generate_learning_path(user_goals)

    # Save the learning path to a file
    generator.save_learning_path(learning_path, 'learning_path.json')

    print("Learning path generated and saved successfully.")
```
