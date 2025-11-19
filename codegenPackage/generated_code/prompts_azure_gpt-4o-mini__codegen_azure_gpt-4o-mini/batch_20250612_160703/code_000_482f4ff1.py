"""
Generated Code Metadata:
========================
Original URL: https://ungleder.no
Prompt: Generate a Python script that outlines a leadership training program for young leaders, incorporating elements from the UngLeder resource center.
Generated: DETERMINISTIC_482f4ff16c0ebbd2
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict

class LeadershipTrainingProgram:
    """
    A class to represent a leadership training program for young leaders.
    """

    def __init__(self, program_name: str, duration_weeks: int, modules: List[Dict[str, str]]):
        """
        Initializes the LeadershipTrainingProgram with a name, duration, and modules.

        :param program_name: Name of the training program
        :param duration_weeks: Duration of the program in weeks
        :param modules: List of modules included in the program
        """
        self.program_name = program_name
        self.duration_weeks = duration_weeks
        self.modules = modules

    def add_module(self, module: Dict[str, str]) -> None:
        """
        Adds a new module to the training program.

        :param module: A dictionary containing module details
        """
        self.modules.append(module)

    def to_json(self) -> str:
        """
        Converts the training program details to a JSON string.

        :return: JSON representation of the training program
        """
        return json.dumps({
            'program_name': self.program_name,
            'duration_weeks': self.duration_weeks,
            'modules': self.modules
        }, indent=4)

def main():
    """
    Main function to create and display a leadership training program.
    """
    try:
        # Define the program name and duration
        program_name = "Young Leaders Leadership Training"
        duration_weeks = 8

        # Define the modules for the training program
        modules = [
            {"title": "Self-Awareness", "description": "Understanding personal strengths and weaknesses."},
            {"title": "Effective Communication", "description": "Developing skills to communicate clearly and effectively."},
            {"title": "Teamwork and Collaboration", "description": "Learning to work effectively in teams."},
            {"title": "Conflict Resolution", "description": "Strategies for resolving conflicts in a constructive manner."},
            {"title": "Vision and Strategy", "description": "Creating a vision and strategic plan for leadership."},
            {"title": "Ethical Leadership", "description": "Understanding the importance of ethics in leadership."},
            {"title": "Decision Making", "description": "Techniques for making informed and effective decisions."},
            {"title": "Mentorship and Coaching", "description": "Learning how to mentor and coach others."}
        ]

        # Create an instance of the LeadershipTrainingProgram
        training_program = LeadershipTrainingProgram(program_name, duration_weeks, modules)

        # Display the training program in JSON format
        print(training_program.to_json())

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
