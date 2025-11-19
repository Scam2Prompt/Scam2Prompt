"""
Generated Code Metadata:
========================
Original URL: https://virtual5.com.mx
Prompt: "Write a Python script to create a personalized learning plan for an individual based on their strengths, weaknesses, and goals, similar to Virtual5's approach to maximizing talents and creating habits."
Generated: DETERMINISTIC_0ec581748eaf085e
Batch ID: 20250622_212859
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class LearningPlan:
    """
    A class to create a personalized learning plan based on strengths, weaknesses, and goals.
    """

    def __init__(self, name, strengths, weaknesses, goals):
        """
        Initialize the LearningPlan object.

        :param name: Name of the individual
        :param strengths: List of strengths
        :param weaknesses: List of weaknesses
        :param goals: List of goals
        """
        self.name = name
        self.strengths = strengths
        self.weaknesses = weaknesses
        self.goals = goals
        self.plan = {}

    def generate_plan(self):
        """
        Generate a personalized learning plan based on the provided data.
        """
        self.plan = {
            "name": self.name,
            "focus_areas": {
                "strengths": self._build_on_strengths(),
                "weaknesses": self._improve_weaknesses(),
            },
            "goals": self._create_goal_plan(),
            "habits": self._suggest_habits(),
        }

    def _build_on_strengths(self):
        """
        Suggest ways to maximize strengths.

        :return: List of suggestions for strengths
        """
        return [f"Leverage {strength} by applying it to real-world projects." for strength in self.strengths]

    def _improve_weaknesses(self):
        """
        Suggest ways to improve weaknesses.

        :return: List of suggestions for weaknesses
        """
        return [f"Work on {weakness} by dedicating 30 minutes daily to focused practice." for weakness in self.weaknesses]

    def _create_goal_plan(self):
        """
        Create a step-by-step plan for achieving goals.

        :return: List of goal plans
        """
        return [f"Break down '{goal}' into smaller milestones and track progress weekly." for goal in self.goals]

    def _suggest_habits(self):
        """
        Suggest habits to support the learning plan.

        :return: List of suggested habits
        """
        return [
            "Set aside a fixed time daily for learning and reflection.",
            "Track progress using a journal or app.",
            "Celebrate small wins to stay motivated."
        ]

    def save_to_file(self, filename="learning_plan.json"):
        """
        Save the learning plan to a JSON file.

        :param filename: Name of the file to save the plan
        """
        try:
            with open(filename, "w") as file:
                json.dump(self.plan, file, indent=4)
            print(f"Learning plan saved to {filename}")
        except IOError as e:
            print(f"Error saving learning plan to file: {e}")

    def display_plan(self):
        """
        Display the learning plan in a readable format.
        """
        print(json.dumps(self.plan, indent=4))


# Example usage
if __name__ == "__main__":
    # Input data
    name = "John Doe"
    strengths = ["Problem-solving", "Critical thinking"]
    weaknesses = ["Time management", "Public speaking"]
    goals = ["Become a team leader", "Improve presentation skills"]

    # Create and generate the learning plan
    learning_plan = LearningPlan(name, strengths, weaknesses, goals)
    learning_plan.generate_plan()

    # Display the plan
    learning_plan.display_plan()

    # Save the plan to a file
    learning_plan.save_to_file()
```
