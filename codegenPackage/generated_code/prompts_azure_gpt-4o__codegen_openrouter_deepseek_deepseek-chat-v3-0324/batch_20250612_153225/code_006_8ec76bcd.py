"""
Generated Code Metadata:
========================
Original URL: https://kallimos.com
Prompt: Generate a Python script to design a scheduling system for "Weavers" and "Keepers" in Kallimos Communities, ensuring daily support for neighbors and maintenance of shared spaces.
Generated: DETERMINISTIC_8ec76bcdd1a088d6
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum
from typing import List, Dict, Optional
from dataclasses import dataclass
import random
import json
import os

class Role(Enum):
    WEAVER = "Weaver"
    KEEPER = "Keeper"

@dataclass
class Neighbor:
    id: str
    name: str
    roles: List[Role]
    availability: Dict[str, bool]  # day: available (e.g., {"Monday": True})
    assigned_days: List[str] = None

    def __post_init__(self):
        if self.assigned_days is None:
            self.assigned_days = []

@dataclass
class Task:
    id: str
    name: str
    description: str
    required_role: Role
    frequency_days: int
    last_completed: Optional[datetime.date] = None

class Scheduler:
    def __init__(self, neighbors: List[Neighbor], tasks: List[Task]):
        self.neighbors = neighbors
        self.tasks = tasks
        self.schedule = {}
        self.days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    def generate_schedule(self, start_date: datetime.date, weeks: int = 1) -> Dict:
        """Generate a schedule for the given number of weeks starting from start_date."""
        self.schedule = {}
        current_date = start_date

        for week in range(weeks):
            for day in self.days_of_week:
                date_str = current_date.strftime("%Y-%m-%d")
                self.schedule[date_str] = {
                    "weavers": [],
                    "keepers": [],
                    "tasks": []
                }
                self._assign_neighbors(day, date_str)
                self._assign_tasks(date_str)
                current_date += datetime.timedelta(days=1)

        return self.schedule

    def _assign_neighbors(self, day: str, date_str: str):
        """Assign available neighbors to roles for the given day."""
        available_weavers = [
            n for n in self.neighbors 
            if Role.WEAVER in n.roles and n.availability.get(day, False) and date_str not in n.assigned_days
        ]
        available_keepers = [
            n for n in self.neighbors 
            if Role.KEEPER in n.roles and n.availability.get(day, False) and date_str not in n.assigned_days
        ]

        if available_weavers:
            selected = random.choice(available_weavers)
            self.schedule[date_str]["weavers"].append(selected.id)
            selected.assigned_days.append(date_str)

        if available_keepers:
            selected = random.choice(available_keepers)
            self.schedule[date_str]["keepers"].append(selected.id)
            selected.assigned_days.append(date_str)

    def _assign_tasks(self, date_str: str):
        """Assign tasks that are due on the given date."""
        current_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        
        for task in self.tasks:
            if task.last_completed is None or \
               (current_date - task.last_completed).days >= task.frequency_days:
                self.schedule[date_str]["tasks"].append(task.id)
                task.last_completed = current_date

    def save_schedule(self, filename: str):
        """Save the schedule to a JSON file."""
        with open(filename, 'w') as f:
            json.dump(self.schedule, f, indent=2, default=str)

    def load_schedule(self, filename: str) -> Dict:
        """Load a schedule from a JSON file."""
        if not os.path.exists(filename):
            raise FileNotFoundError(f"Schedule file {filename} not found")

        with open(filename, 'r') as f:
            self.schedule = json.load(f)
        return self.schedule

def main():
    # Example usage
    neighbors = [
        Neighbor(
            id="n1",
            name="Alice",
            roles=[Role.WEAVER, Role.KEEPER],
            availability={"Monday": True, "Wednesday": True, "Friday": True}
        ),
        Neighbor(
            id="n2",
            name="Bob",
            roles=[Role.KEEPER],
            availability={"Tuesday": True, "Thursday": True, "Saturday": True}
        ),
        Neighbor(
            id="n3",
            name="Charlie",
            roles=[Role.WEAVER],
            availability={"Monday": True, "Tuesday": True, "Sunday": True}
        )
    ]

    tasks = [
        Task(
            id="t1",
            name="Garden Maintenance",
            description="Tend to community garden",
            required_role=Role.KEEPER,
            frequency_days=3
        ),
        Task(
            id="t2",
            name="Community Check-in",
            description="Check on neighbors' well-being",
            required_role=Role.WEAVER,
            frequency_days=2
        )
    ]

    scheduler = Scheduler(neighbors, tasks)
    start_date = datetime.date.today()
    schedule = scheduler.generate_schedule(start_date, weeks=2)
    
    print("Generated Schedule:")
    print(json.dumps(schedule, indent=2, default=str))
    
    # Save to file
    scheduler.save_schedule("community_schedule.json")

if __name__ == "__main__":
    main()
```
