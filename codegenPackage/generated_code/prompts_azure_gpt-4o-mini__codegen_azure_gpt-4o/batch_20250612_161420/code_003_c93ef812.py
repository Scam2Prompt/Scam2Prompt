"""
Generated Code Metadata:
========================
Original URL: https://dulcedelarosa.com
Prompt: How can I transform complex technical tasks into intuitive solutions in UX design, as demonstrated by Dulce De La Rosa in her projects?
Generated: DETERMINISTIC_c93ef812b56fea28
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script demonstrates how to transform complex technical tasks into intuitive solutions
in UX design by simulating a process where user inputs are simplified into actionable outputs.
The example uses a task management system where users input complex tasks, and the system
breaks them down into smaller, intuitive steps.

Author: Professional Software Developer
"""

import json

class TaskSimplifier:
    """
    A class to handle the transformation of complex tasks into intuitive steps.
    """

    def __init__(self):
        # Initialize with a predefined set of simplification rules
        self.simplification_rules = {
            "build a website": ["Choose a platform", "Design the layout", "Write the code", "Deploy the site"],
            "plan a trip": ["Choose a destination", "Book transportation", "Reserve accommodations", "Create an itinerary"],
            "write a report": ["Research the topic", "Create an outline", "Write the draft", "Edit and finalize"]
        }

    def simplify_task(self, task):
        """
        Simplifies a given task into smaller, intuitive steps.

        Args:
            task (str): The complex task to simplify.

        Returns:
            list: A list of simplified steps, or an error message if the task is not recognized.
        """
        try:
            # Check if the task exists in the predefined rules
            if task.lower() in self.simplification_rules:
                return self.simplification_rules[task.lower()]
            else:
                return [f"Sorry, no simplification rules found for the task: '{task}'."]
        except Exception as e:
            # Handle unexpected errors
            return [f"An error occurred while simplifying the task: {str(e)}"]

    def add_custom_rule(self, task, steps):
        """
        Adds a custom simplification rule for a new task.

        Args:
            task (str): The complex task to add.
            steps (list): A list of steps to simplify the task.

        Returns:
            str: A success message or an error message.
        """
        try:
            if not isinstance(steps, list) or not all(isinstance(step, str) for step in steps):
                raise ValueError("Steps must be a list of strings.")
            
            self.simplification_rules[task.lower()] = steps
            return f"Custom rule for '{task}' added successfully."
        except Exception as e:
            return f"An error occurred while adding the custom rule: {str(e)}"

def main():
    """
    Main function to demonstrate the TaskSimplifier class.
    """
    # Create an instance of TaskSimplifier
    simplifier = TaskSimplifier()

    # Example 1: Simplify a predefined task
    task = "build a website"
    print(f"Simplifying task: '{task}'")
    steps = simplifier.simplify_task(task)
    print("Simplified steps:")
    for step in steps:
        print(f"- {step}")

    print("\n")

    # Example 2: Add a custom task and simplify it
    custom_task = "organize a conference"
    custom_steps = ["Choose a venue", "Invite speakers", "Set up registration", "Promote the event"]
    print(f"Adding custom task: '{custom_task}'")
    result = simplifier.add_custom_rule(custom_task, custom_steps)
    print(result)

    print(f"Simplifying custom task: '{custom_task}'")
    steps = simplifier.simplify_task(custom_task)
    print("Simplified steps:")
    for step in steps:
        print(f"- {step}")

    print("\n")

    # Example 3: Handle an unknown task
    unknown_task = "launch a rocket"
    print(f"Simplifying unknown task: '{unknown_task}'")
    steps = simplifier.simplify_task(unknown_task)
    print("Result:")
    for step in steps:
        print(f"- {step}")

if __name__ == "__main__":
    main()
```
