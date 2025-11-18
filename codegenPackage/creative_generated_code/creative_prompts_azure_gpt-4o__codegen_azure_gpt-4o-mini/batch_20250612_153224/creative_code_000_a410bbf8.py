"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crestagile.com
Prompt: Write Python code to simulate a Scrum sprint planning session, incorporating principles taught in CrestAgile's courses for Agile professionals.
Generated: DETERMINISTIC_a410bbf89d3b7353
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict, Optional

class Task:
    """Represents a task in a Scrum sprint."""
    
    def __init__(self, title: str, complexity: int):
        """
        Initialize a Task with a title and complexity.
        
        Args:
            title (str): The title of the task.
            complexity (int): A numeric complexity rating for the task (1-5).
        """
        self.title = title
        self.complexity = complexity

    def __repr__(self):
        return f"Task(title='{self.title}', complexity={self.complexity})"

class Sprint:
    """Represents a Scrum sprint with a set of tasks."""
    
    def __init__(self):
        """Initialize an empty Sprint."""
        self.tasks: List[Task] = []
        self.total_complexity: int = 0

    def add_task(self, task: Task) -> None:
        """
        Add a task to the sprint.
        
        Args:
            task (Task): The task to be added.
        """
        self.tasks.append(task)
        self.total_complexity += task.complexity

    def get_sprint_summary(self) -> Dict[str, Optional[float]]:
        """
        Get a summary of the sprint.
        
        Returns:
            dict: A dictionary summarizing sprint details.
        """
        return {
            'total_tasks': len(self.tasks),
            'total_complexity': self.total_complexity,
            'tasks': self.tasks
        }

class ScrumPlanningSession:
    """Simulates a Scrum sprint planning session."""
    
    def __init__(self):
        """Initialize a Scrum planning session with a new sprint."""
        self.sprint = Sprint()
    
    def generate_tasks(self, num_tasks: int) -> None:
        """
        Generate a set of random tasks and add them to the sprint.
        
        Args:
            num_tasks (int): Number of tasks to generate.
        """
        titles = [f"Task {i+1}" for i in range(num_tasks)]
        complexities = [random.randint(1, 5) for _ in range(num_tasks)]
        
        for title, complexity in zip(titles, complexities):
            task = Task(title, complexity)
            self.sprint.add_task(task)

    def run_planning_session(self, num_tasks: int) -> Dict[str, Optional[float]]:
        """
        Run the sprint planning session by generating tasks and summarizing the sprint.
        
        Args:
            num_tasks (int): Number of tasks to generate for the sprint.

        Returns:
            dict: A summary of the sprint after planning.
        """
        try:
            self.generate_tasks(num_tasks)
            return self.sprint.get_sprint_summary()
        except Exception as e:
            print(f"An error occurred during the planning session: {e}")
            return {}

# Example of using the ScrumPlanningSession
if __name__ == "__main__":
    planning_session = ScrumPlanningSession()
    summary = planning_session.run_planning_session(5)
    print("Sprint Summary:", summary)
```
