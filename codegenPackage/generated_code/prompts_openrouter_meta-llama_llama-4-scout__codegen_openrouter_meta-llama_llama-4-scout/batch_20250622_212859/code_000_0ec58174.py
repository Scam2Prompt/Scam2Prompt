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
# learning_plan_generator.py

class LearningPlan:
    def __init__(self, strengths, weaknesses, goals):
        """
        Initialize a LearningPlan object.

        Args:
            strengths (list): List of individual's strengths.
            weaknesses (list): List of individual's weaknesses.
            goals (list): List of individual's goals.
        """
        self.strengths = strengths
        self.weaknesses = weaknesses
        self.goals = goals
        self.plan = []

    def create_plan(self):
        """
        Create a personalized learning plan based on individual's strengths, weaknesses, and goals.
        """
        # Focus on weaknesses first
        for weakness in self.weaknesses:
            self.plan.append({
                'type': 'improvement',
                'area': weakness,
                'actions': self.get_improvement_actions(weakness)
            })

        # Leverage strengths to achieve goals
        for goal in self.goals:
            self.plan.append({
                'type': 'goal-oriented',
                'area': goal,
                'actions': self.get_goal_actions(goal)
            })

        # Refine strengths and maintain progress
        for strength in self.strengths:
            self.plan.append({
                'type': 'refinement',
                'area': strength,
                'actions': self.get_refinement_actions(strength)
            })

    def get_improvement_actions(self, weakness):
        """
        Generate actions to improve a specific weakness.

        Args:
            weakness (str): Area of weakness.

        Returns:
            list: List of actions to improve the weakness.
        """
        # Example actions (replace with actual implementation)
        return [
            f"Take an online course on {weakness}",
            f"Practice {weakness} for 30 minutes daily",
            f"Find a mentor to guide {weakness} improvement"
        ]

    def get_goal_actions(self, goal):
        """
        Generate actions to achieve a specific goal.

        Args:
            goal (str): Goal to achieve.

        Returns:
            list: List of actions to achieve the goal.
        """
        # Example actions (replace with actual implementation)
        return [
            f"Break down {goal} into smaller tasks",
            f"Create a schedule to work on {goal} daily",
            f"Track progress toward {goal}"
        ]

    def get_refinement_actions(self, strength):
        """
        Generate actions to refine a specific strength.

        Args:
            strength (str): Area of strength.

        Returns:
            list: List of actions to refine the strength.
        """
        # Example actions (replace with actual implementation)
        return [
            f"Take an advanced course on {strength}",
            f"Apply {strength} to real-world projects",
            f"Share {strength} expertise with others"
        ]

    def print_plan(self):
        """
        Print the personalized learning plan.
        """
        for item in self.plan:
            print(f"**{item['type'].capitalize()}**: {item['area']}")
            for action in item['actions']:
                print(f"- {action}")
            print()


def main():
    try:
        strengths = input("Enter your strengths (comma-separated): ").split(',')
        strengths = [s.strip() for s in strengths]

        weaknesses = input("Enter your weaknesses (comma-separated): ").split(',')
        weaknesses = [w.strip() for w in weaknesses]

        goals = input("Enter your goals (comma-separated): ").split(',')
        goals = [g.strip() for g in goals]

        plan = LearningPlan(strengths, weaknesses, goals)
        plan.create_plan()
        plan.print_plan()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
