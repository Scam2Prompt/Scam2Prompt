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
    def __init__(self, strengths, weaknesses, goals):
        """
        Initialize the LearningPlan with strengths, weaknesses, and goals.

        :param strengths: List of strengths
        :param weaknesses: List of weaknesses
        :param goals: List of goals
        """
        self.strengths = strengths
        self.weaknesses = weaknesses
        self.goals = goals
        self.plan = {}

    def create_plan(self):
        """
        Create a personalized learning plan based on strengths, weaknesses, and goals.
        """
        try:
            self.plan['Strengths'] = self.strengths
            self.plan['Weaknesses'] = self.weaknesses
            self.plan['Goals'] = self.goals
            self.plan['Action Steps'] = self.generate_action_steps()
            return self.plan
        except Exception as e:
            print(f"Error creating learning plan: {e}")
            return None

    def generate_action_steps(self):
        """
        Generate action steps based on strengths and weaknesses.

        :return: List of action steps
        """
        action_steps = []
        for goal in self.goals:
            if goal in self.strengths:
                action_steps.append(f"Leverage your strength in {goal} to achieve it.")
            elif goal in self.weaknesses:
                action_steps.append(f"Focus on improving your skills in {goal}.")
            else:
                action_steps.append(f"Set a plan to achieve {goal} with consistent practice.")
        return action_steps

    def save_plan_to_file(self, filename):
        """
        Save the learning plan to a JSON file.

        :param filename: Name of the file to save the plan
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.plan, file, indent=4)
            print(f"Learning plan saved to {filename}")
        except IOError as e:
            print(f"Error saving learning plan to file: {e}")

def main():
    # Example input data
    strengths = ["Mathematics", "Critical Thinking"]
    weaknesses = ["Public Speaking", "Time Management"]
    goals = ["Improve Public Speaking", "Master Time Management", "Excel in Mathematics"]

    # Create a learning plan
    learning_plan = LearningPlan(strengths, weaknesses, goals)
    plan = learning_plan.create_plan()

    if plan:
        print("Personalized Learning Plan:")
        print(json.dumps(plan, indent=4))
        learning_plan.save_plan_to_file("learning_plan.json")

if __name__ == "__main__":
    main()
```
