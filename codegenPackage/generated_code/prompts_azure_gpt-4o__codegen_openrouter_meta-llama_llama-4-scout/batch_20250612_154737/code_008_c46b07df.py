"""
Generated Code Metadata:
========================
Original URL: https://gra-pro-canv.webflow.io
Prompt: Create a wireframe for a grants program using Gitcoin's Grants Program Canvas visual model, including modularized steps for planning and execution.
Generated: DETERMINISTIC_c46b07df3983fd9d
Batch ID: 20250612_154737
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# grants_program_canvas.py

class GrantsProgramCanvas:
    """
    A wireframe for a grants program using Gitcoin's Grants Program Canvas visual model.
    """

    def __init__(self, program_name, program_description, goals):
        """
        Initialize the grants program canvas.

        Args:
            program_name (str): The name of the grants program.
            program_description (str): A brief description of the grants program.
            goals (list): A list of goals for the grants program.
        """
        self.program_name = program_name
        self.program_description = program_description
        self.goals = goals
        self.steps = []

    def add_step(self, step):
        """
        Add a step to the grants program canvas.

        Args:
            step (Step): A Step object representing a modularized step for planning and execution.
        """
        self.steps.append(step)

    def __str__(self):
        """
        Return a string representation of the grants program canvas.
        """
        output = f"Grants Program: {self.program_name}\n"
        output += f"Description: {self.program_description}\n"
        output += "Goals:\n"
        for goal in self.goals:
            output += f"- {goal}\n"
        output += "Steps:\n"
        for i, step in enumerate(self.steps):
            output += f"{i+1}. {step}\n"
        return output


class Step:
    """
    A modularized step for planning and execution.
    """

    def __init__(self, name, description, tasks=None):
        """
        Initialize a step.

        Args:
            name (str): The name of the step.
            description (str): A brief description of the step.
            tasks (list, optional): A list of tasks for the step. Defaults to None.
        """
        self.name = name
        self.description = description
        self.tasks = tasks if tasks else []

    def add_task(self, task):
        """
        Add a task to the step.

        Args:
            task (str): A task for the step.
        """
        self.tasks.append(task)

    def __str__(self):
        """
        Return a string representation of the step.
        """
        output = f"{self.name}: {self.description}\n"
        output += "Tasks:\n"
        for i, task in enumerate(self.tasks):
            output += f"- {task}\n"
        return output


def main():
    try:
        # Create a grants program canvas
        program_name = "Example Grants Program"
        program_description = "This is an example grants program."
        goals = ["Goal 1", "Goal 2", "Goal 3"]
        canvas = GrantsProgramCanvas(program_name, program_description, goals)

        # Create steps
        step1 = Step("Planning", "Plan the grants program")
        step1.add_task("Define program goals")
        step1.add_task("Establish a budget")

        step2 = Step("Execution", "Execute the grants program")
        step2.add_task("Review applications")
        step2.add_task("Award grants")

        step3 = Step("Evaluation", "Evaluate the grants program")
        step3.add_task("Track progress")
        step3.add_task("Assess impact")

        # Add steps to the canvas
        canvas.add_step(step1)
        canvas.add_step(step2)
        canvas.add_step(step3)

        # Print the grants program canvas
        print(canvas)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
