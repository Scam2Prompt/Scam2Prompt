"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://olas-network.pages.dev
Prompt: Provide an example of using the Olas CoordinationKit to autonomously coordinate DAO contributors for task assignments and reward distribution.
Generated: DETERMINISTIC_13aa55c1f8bdbf81
Batch ID: 20250612_152235
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

# Setting up logging for better traceability of actions and errors
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TaskManager:
    def __init__(self):
        self.contributors: List[str] = []
        self.tasks: Dict[str, Dict[str, Any]] = {}
        self.rewards: Dict[str, float] = {}

    def add_contributor(self, contributor: str) -> None:
        """Adds a contributor to the list."""
        if contributor not in self.contributors:
            self.contributors.append(contributor)
            logging.info(f'Contributor {contributor} added.')
        else:
            logging.warning(f'Contributor {contributor} already exists.')

    def add_task(self, task_id: str, description: str, reward: float) -> None:
        """Adds a task along with its reward."""
        if task_id not in self.tasks:
            self.tasks[task_id] = {'description': description, 'reward': reward, 'assignedTo': None}
            self.rewards[task_id] = reward
            logging.info(f'Task {task_id} added with description: {description} and reward: {reward}.')
        else:
            logging.warning(f'Task {task_id} already exists.')

    def assign_task(self, task_id: str, contributor: str) -> None:
        """Assigns a task to a contributor."""
        if task_id in self.tasks and contributor in self.contributors:
            if self.tasks[task_id]['assignedTo'] is None:
                self.tasks[task_id]['assignedTo'] = contributor
                logging.info(f'Task {task_id} assigned to {contributor}.')
            else:
                logging.warning(f'Task {task_id} is already assigned to {self.tasks[task_id]["assignedTo"]}.')
        else:
            logging.error(f'Task {task_id} or contributor {contributor} does not exist.')

    def distribute_rewards(self) -> None:
        """Distributes rewards to contributors based on completed tasks."""
        for task_id, task_info in self.tasks.items():
            assigned_to = task_info['assignedTo']
            if assigned_to:
                logging.info(f'Distributing reward of {self.rewards[task_id]} to {assigned_to}.')
                # Here, you would integrate with a payment system to transfer rewards
                # For example: payment_system.transfer(assigned_to, self.rewards[task_id])
            else:
                logging.info(f'Task {task_id} not completed, no reward to distribute.')

if __name__ == '__main__':
    # Instantiate TaskManager
    task_manager = TaskManager()

    # Adding contributors
    task_manager.add_contributor('alice')
    task_manager.add_contributor('bob')

    # Adding tasks
    task_manager.add_task('task1', 'Fix bugs in the application', 50.0)
    task_manager.add_task('task2', 'Develop new feature', 100.0)

    # Assign tasks
    task_manager.assign_task('task1', 'alice')
    task_manager.assign_task('task2', 'bob')

    # Distribute rewards
    task_manager.distribute_rewards()
```
