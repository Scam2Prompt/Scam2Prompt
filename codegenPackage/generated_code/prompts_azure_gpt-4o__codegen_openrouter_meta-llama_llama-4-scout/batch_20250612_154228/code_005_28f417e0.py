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
# cleaning_task_assigner.py

from enum import Enum
from typing import List, Dict

class CleaningService(Enum):
    """Enum for different cleaning services provided by BlocPrest"""
    DAILY = 1
    WEEKLY = 2
    MONTHLY = 3

class ResidentialBlock:
    """Class representing a residential block"""
    def __init__(self, block_id: int, name: str):
        self.block_id = block_id
        self.name = name
        self.tasks = []

    def add_task(self, task: str):
        """Add a cleaning task to the residential block"""
        self.tasks.append(task)

class CleaningTaskAssigner:
    """Class responsible for assigning cleaning tasks to residential blocks"""
    def __init__(self):
        self.blocks: Dict[int, ResidentialBlock] = {}
        self.services: Dict[CleaningService, List[str]] = {
            CleaningService.DAILY: [],
            CleaningService.WEEKLY: [],
            CleaningService.MONTHLY: []
        }

    def add_residential_block(self, block_id: int, name: str):
        """Add a residential block to the assigner"""
        self.blocks[block_id] = ResidentialBlock(block_id, name)

    def assign_cleaning_tasks(self, block_id: int, service: CleaningService, tasks: List[str]):
        """Assign cleaning tasks to a residential block"""
        if block_id not in self.blocks:
            raise ValueError(f"Residential block with ID {block_id} does not exist")

        block = self.blocks[block_id]
        self.services[service].extend(tasks)
        for task in tasks:
            block.add_task(task)

    def get_block_tasks(self, block_id: int) -> List[str]:
        """Get the cleaning tasks assigned to a residential block"""
        if block_id not in self.blocks:
            raise ValueError(f"Residential block with ID {block_id} does not exist")

        return self.blocks[block_id].tasks

    def get_service_tasks(self, service: CleaningService) -> List[str]:
        """Get the cleaning tasks for a specific service"""
        return self.services[service]

def main():
    assigner = CleaningTaskAssigner()

    # Add residential blocks
    assigner.add_residential_block(1, "Block A")
    assigner.add_residential_block(2, "Block B")

    # Assign cleaning tasks
    daily_tasks = ["Sweep floors", "Empty trash"]
    weekly_tasks = ["Mop floors", "Clean windows"]
    monthly_tasks = ["Deep clean floors", "Clean appliances"]

    assigner.assign_cleaning_tasks(1, CleaningService.DAILY, daily_tasks)
    assigner.assign_cleaning_tasks(1, CleaningService.WEEKLY, weekly_tasks)
    assigner.assign_cleaning_tasks(2, CleaningService.MONTHLY, monthly_tasks)

    # Get and print block tasks
    print("Block 1 Tasks:")
    for task in assigner.get_block_tasks(1):
        print(task)

    print("\nBlock 2 Tasks:")
    for task in assigner.get_block_tasks(2):
        print(task)

    # Get and print service tasks
    print("\nDaily Tasks:")
    for task in assigner.get_service_tasks(CleaningService.DAILY):
        print(task)

if __name__ == "__main__":
    main()
```
