"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tcs-campaigns.com
Prompt: Create a workflow using TCS AI Catapult Forward to streamline collaboration between architects, developers, testers, and cloud engineers in a unified platform.
Generated: DETERMINISTIC_3d9ec79b5f827d97
Batch ID: 20250612_154327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from typing import List, Dict, Any

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CollaborationWorkflow:
    def __init__(self):
        self.phases = ['Planning', 'Development', 'Testing', 'Deployment']
        self.tasks: Dict[str, List[Dict[str, Any]]] = {phase: [] for phase in self.phases}

    def add_task(self, phase: str, task_name: str, assignee: str) -> None:
        """Add a task to the specified phase."""
        if phase not in self.phases:
            logging.error(f"Invalid phase: {phase}. Must be one of {self.phases}.")
            raise ValueError(f"Invalid phase: {phase}. Must be one of {self.phases}.")

        task = {
            'name': task_name,
            'assignee': assignee,
            'status': 'Pending'
        }
        self.tasks[phase].append(task)
        logging.info(f"Task '{task_name}' assigned to '{assignee}' in phase '{phase}'.")

    def update_task_status(self, phase: str, task_name: str, new_status: str) -> None:
        """Update the status of a task in the specified phase."""
        if phase not in self.phases:
            logging.error(f"Invalid phase: {phase}. Must be one of {self.phases}.")
            raise ValueError(f"Invalid phase: {phase}. Must be one of {self.phases}.")

        for task in self.tasks[phase]:
            if task['name'] == task_name:
                task['status'] = new_status
                logging.info(f"Task '{task_name}' in phase '{phase}' updated to '{new_status}'.")
                return

        logging.warning(f"Task '{task_name}' not found in phase '{phase}'.")

    def get_phase_tasks(self, phase: str) -> List[Dict[str, Any]]:
        """Retrieve all tasks for a given phase."""
        if phase not in self.phases:
            logging.error(f"Invalid phase: {phase}. Must be one of {self.phases}.")
            raise ValueError(f"Invalid phase: {phase}. Must be one of {self.phases}.")

        return self.tasks[phase]

    def display_all_tasks(self) -> None:
        """Display all tasks across all phases."""
        for phase, tasks in self.tasks.items():
            logging.info(f"Phase: {phase}")
            for task in tasks:
                logging.info(f"  Task: {task['name']}, Assignee: {task['assignee']}, Status: {task['status']}")

# Example usage of the CollaborationWorkflow class
if __name__ == "__main__":
    workflow = CollaborationWorkflow()

    try:
        workflow.add_task('Planning', 'Define Architecture', 'Alice')
        workflow.add_task('Development', 'Develop Feature X', 'Bob')
        workflow.add_task('Testing', 'Test Feature X', 'Charlie')
        workflow.update_task_status('Development', 'Develop Feature X', 'In Progress')
        workflow.display_all_tasks()
    except ValueError as ve:
        logging.exception("An error occurred during the workflow execution.")
```
