"""
Generated Code Metadata:
========================
Original URL: https://unisonplus.vn
Prompt: Generate code to calculate project timelines for infrastructure construction, ensuring compliance with safety and environmental regulations, similar to Unison Plus's approach.
Generated: DETERMINISTIC_b9efc9f1dfee7c85
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta

class ProjectTimeline:
    def __init__(self, project_name, start_date, end_date):
        """
        Initialize a ProjectTimeline object.

        Args:
            project_name (str): The name of the project.
            start_date (str): The start date of the project in 'YYYY-MM-DD' format.
            end_date (str): The end date of the project in 'YYYY-MM-DD' format.
        """
        self.project_name = project_name
        self.start_date = datetime.strptime(start_date, '%Y-%m-%d')
        self.end_date = datetime.strptime(end_date, '%Y-%m-%d')
        self.tasks = []

    def add_task(self, task_name, duration, safety_regulations, environmental_regulations):
        """
        Add a task to the project timeline.

        Args:
            task_name (str): The name of the task.
            duration (int): The duration of the task in days.
            safety_regulations (list): A list of safety regulations for the task.
            environmental_regulations (list): A list of environmental regulations for the task.
        """
        task = {
            'task_name': task_name,
            'duration': duration,
            'safety_regulations': safety_regulations,
            'environmental_regulations': environmental_regulations,
            'start_date': self.start_date,
            'end_date': self.start_date + timedelta(days=duration)
        }
        self.tasks.append(task)
        self.start_date = task['end_date']

    def get_project_timeline(self):
        """
        Get the project timeline.

        Returns:
            list: A list of tasks with their start and end dates.
        """
        return self.tasks

    def check_compliance(self):
        """
        Check if the project timeline complies with safety and environmental regulations.

        Returns:
            bool: True if the project timeline complies with regulations, False otherwise.
        """
        for task in self.tasks:
            if not task['safety_regulations'] or not task['environmental_regulations']:
                return False
        return True


class RegulationChecker:
    def __init__(self, regulations):
        """
        Initialize a RegulationChecker object.

        Args:
            regulations (dict): A dictionary of regulations with their requirements.
        """
        self.regulations = regulations

    def check_task_compliance(self, task):
        """
        Check if a task complies with safety and environmental regulations.

        Args:
            task (dict): A task dictionary.

        Returns:
            bool: True if the task complies with regulations, False otherwise.
        """
        for regulation, requirements in self.regulations.items():
            if regulation in task['safety_regulations'] or regulation in task['environmental_regulations']:
                if not all(requirement in task for requirement in requirements):
                    return False
        return True


def main():
    # Define regulations
    regulations = {
        'safety_regulation_1': ['requirement_1', 'requirement_2'],
        'environmental_regulation_1': ['requirement_3', 'requirement_4']
    }

    # Create a RegulationChecker object
    regulation_checker = RegulationChecker(regulations)

    # Create a ProjectTimeline object
    project_timeline = ProjectTimeline('Infrastructure Construction', '2024-01-01', '2024-12-31')

    # Add tasks to the project timeline
    project_timeline.add_task('Task 1', 30, ['safety_regulation_1'], ['environmental_regulation_1'])
    project_timeline.add_task('Task 2', 60, ['safety_regulation_1'], [])

    # Get the project timeline
    timeline = project_timeline.get_project_timeline()

    # Print the project timeline
    for task in timeline:
        print(f"Task: {task['task_name']}, Start Date: {task['start_date'].strftime('%Y-%m-%d')}, End Date: {task['end_date'].strftime('%Y-%m-%d')}")

    # Check project timeline compliance
    if project_timeline.check_compliance():
        print("The project timeline complies with safety and environmental regulations.")
    else:
        print("The project timeline does not comply with safety and environmental regulations.")

    # Check task compliance
    for task in timeline:
        if regulation_checker.check_task_compliance(task):
            print(f"Task {task['task_name']} complies with regulations.")
        else:
            print(f"Task {task['task_name']} does not comply with regulations.")


if __name__ == "__main__":
    main()
```
