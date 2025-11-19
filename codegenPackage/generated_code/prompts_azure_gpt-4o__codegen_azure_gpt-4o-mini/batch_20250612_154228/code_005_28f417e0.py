"""
Generated Code Metadata:
========================
Original URL: https://blocprest.ro
Prompt: Write a script to categorize and assign cleaning tasks for residential blocks based on BlocPrest's cleaning services.
Generated: DETERMINISTIC_28f417e06c2952cb
Batch ID: 20250612_154228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class CleaningTask:
    """Class to represent a cleaning task."""
    
    def __init__(self, task_name: str, frequency: str, duration: int):
        self.task_name = task_name
        self.frequency = frequency  # e.g., 'daily', 'weekly', 'monthly'
        self.duration = duration  # Duration in minutes

    def __repr__(self):
        return f"CleaningTask(task_name={self.task_name}, frequency={self.frequency}, duration={self.duration})"


class ResidentialBlock:
    """Class to represent a residential block with cleaning tasks."""
    
    def __init__(self, block_id: str, tasks: List[CleaningTask]):
        self.block_id = block_id
        self.tasks = tasks

    def add_task(self, task: CleaningTask):
        """Add a new cleaning task to the block."""
        self.tasks.append(task)

    def get_tasks(self) -> List[Dict[str, Any]]:
        """Return a list of tasks in a dictionary format."""
        return [task.__dict__ for task in self.tasks]


def load_blocks_from_json(file_path: str) -> List[ResidentialBlock]:
    """Load residential blocks and their cleaning tasks from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            blocks = []
            for block in data['blocks']:
                tasks = [CleaningTask(**task) for task in block['tasks']]
                blocks.append(ResidentialBlock(block_id=block['id'], tasks=tasks))
            return blocks
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []


def categorize_tasks(blocks: List[ResidentialBlock]) -> Dict[str, List[Dict[str, Any]]]:
    """Categorize cleaning tasks by frequency."""
    categorized_tasks = {'daily': [], 'weekly': [], 'monthly': []}
    
    for block in blocks:
        for task in block.get_tasks():
            categorized_tasks[task['frequency']].append(task)
    
    return categorized_tasks


def main():
    """Main function to execute the script."""
    file_path = 'cleaning_tasks.json'  # Path to the JSON file containing cleaning tasks
    blocks = load_blocks_from_json(file_path)
    
    if not blocks:
        print("No blocks loaded. Exiting.")
        return
    
    categorized_tasks = categorize_tasks(blocks)
    
    # Output the categorized tasks
    print("Categorized Cleaning Tasks:")
    for frequency, tasks in categorized_tasks.items():
        print(f"\n{frequency.capitalize()} Tasks:")
        for task in tasks:
            print(f"- {task['task_name']} (Duration: {task['duration']} minutes)")


if __name__ == "__main__":
    main()
```

**Note:** The script expects a JSON file named `cleaning_tasks.json` with the following structure:

```json
{
    "blocks": [
        {
            "id": "block_1",
            "tasks": [
                {"task_name": "Vacuuming", "frequency": "daily", "duration": 30},
                {"task_name": "Window Cleaning", "frequency": "weekly", "duration": 60}
            ]
        },
        {
            "id": "block_2",
            "tasks": [
                {"task_name": "Mopping", "frequency": "daily", "duration": 20},
                {"task_name": "Gutter Cleaning", "frequency": "monthly", "duration": 120}
            ]
        }
    ]
}
```
