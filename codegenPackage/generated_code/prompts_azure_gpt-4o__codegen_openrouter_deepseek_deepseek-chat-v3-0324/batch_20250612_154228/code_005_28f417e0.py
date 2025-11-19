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
from enum import Enum
from typing import List, Dict, Optional
from dataclasses import dataclass
import random
from datetime import datetime, timedelta

class CleaningPriority(Enum):
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"

class CleaningTaskType(Enum):
    VACUUMING = "Vacuuming"
    DUSTING = "Dusting"
    MOOPING = "Mopping"
    WINDOW_CLEANING = "Window Cleaning"
    BATHROOM_SANITIZATION = "Bathroom Sanitization"
    KITCHEN_CLEANING = "Kitchen Cleaning"
    TRASH_REMOVAL = "Trash Removal"

@dataclass
class ResidentialBlock:
    block_id: str
    block_name: str
    floors: int
    units_per_floor: int
    last_cleaned: Optional[datetime] = None

@dataclass
class CleaningTask:
    task_id: str
    task_type: CleaningTaskType
    priority: CleaningPriority
    block_id: str
    floor: int
    unit: Optional[int] = None  # None means common area
    assigned_to: Optional[str] = None
    estimated_duration: timedelta = timedelta(minutes=30)
    completed: bool = False

class CleaningScheduler:
    def __init__(self):
        self.blocks: Dict[str, ResidentialBlock] = {}
        self.tasks: Dict[str, CleaningTask] = {}
        self.cleaners: List[str] = []
    
    def add_block(self, block: ResidentialBlock) -> None:
        """Add a residential block to the scheduler."""
        if block.block_id in self.blocks:
            raise ValueError(f"Block with ID {block.block_id} already exists")
        self.blocks[block.block_id] = block
    
    def add_cleaner(self, cleaner_id: str) -> None:
        """Add a cleaner to the available pool."""
        if cleaner_id in self.cleaners:
            raise ValueError(f"Cleaner {cleaner_id} already exists")
        self.cleaners.append(cleaner_id)
    
    def generate_tasks_for_block(self, block_id: str) -> List[CleaningTask]:
        """Generate standard cleaning tasks for a residential block."""
        if block_id not in self.blocks:
            raise ValueError(f"Block {block_id} not found")
        
        block = self.blocks[block_id]
        tasks = []
        
        # Common area tasks
        common_tasks = [
            (CleaningTaskType.VACUUMING, CleaningPriority.MEDIUM),
            (CleaningTaskType.DUSTING, CleaningPriority.LOW),
            (CleaningTaskType.MOOPING, CleaningPriority.HIGH),
            (CleaningTaskType.WINDOW_CLEANING, CleaningPriority.LOW),
            (CleaningTaskType.TRASH_REMOVAL, CleaningPriority.HIGH)
        ]
        
        for floor in range(1, block.floors + 1):
            # Common area tasks per floor
            for task_type, priority in common_tasks:
                task_id = f"{block_id}-{floor}-common-{task_type.value.lower().replace(' ', '_')}"
                tasks.append(CleaningTask(
                    task_id=task_id,
                    task_type=task_type,
                    priority=priority,
                    block_id=block_id,
                    floor=floor
                ))
            
            # Unit-specific tasks
            for unit in range(1, block.units_per_floor + 1):
                unit_tasks = [
                    (CleaningTaskType.BATHROOM_SANITIZATION, CleaningPriority.HIGH),
                    (CleaningTaskType.KITCHEN_CLEANING, CleaningPriority.HIGH),
                    (CleaningTaskType.VACUUMING, CleaningPriority.MEDIUM)
                ]
                
                for task_type, priority in unit_tasks:
                    task_id = f"{block_id}-{floor}-{unit}-{task_type.value.lower().replace(' ', '_')}"
                    tasks.append(CleaningTask(
                        task_id=task_id,
                        task_type=task_type,
                        priority=priority,
                        block_id=block_id,
                        floor=floor,
                        unit=unit
                    ))
        
        return tasks
    
    def assign_tasks(self) -> None:
        """Assign all unassigned tasks to available cleaners."""
        if not self.cleaners:
            raise ValueError("No cleaners available for assignment")
        
        unassigned_tasks = [task for task in self.tasks.values() if not task.assigned_to]
        if not unassigned_tasks:
            return
        
        # Sort tasks by priority (High first)
        unassigned_tasks.sort(key=lambda x: x.priority.value, reverse=True)
        
        # Simple round-robin assignment
        cleaner_index = 0
        for task in unassigned_tasks:
            task.assigned_to = self.cleaners[cleaner_index]
            cleaner_index = (cleaner_index + 1) % len(self.cleaners)
    
    def add_task(self, task: CleaningTask) -> None:
        """Add a single task to the scheduler."""
        if task.task_id in self.tasks:
            raise ValueError(f"Task with ID {task.task_id} already exists")
        if task.block_id not in self.blocks:
            raise ValueError(f"Block {task.block_id} not found")
        self.tasks[task.task_id] = task
    
    def complete_task(self, task_id: str) -> None:
        """Mark a task as completed."""
        if task_id not in self.tasks:
            raise ValueError(f"Task {task_id} not found")
        self.tasks[task_id].completed = True
        block_id = self.tasks[task_id].block_id
        self.blocks[block_id].last_cleaned = datetime.now()
    
    def get_tasks_for_cleaner(self, cleaner_id: str) -> List[CleaningTask]:
        """Get all tasks assigned to a specific cleaner."""
        if cleaner_id not in self.cleaners:
            raise ValueError(f"Cleaner {cleaner_id} not found")
        return [task for task in self.tasks.values() if task.assigned_to == cleaner_id]
    
    def get_block_tasks(self, block_id: str) -> List[CleaningTask]:
        """Get all tasks for a specific block."""
        if block_id not in self.blocks:
            raise ValueError(f"Block {block_id} not found")
        return [task for task in self.tasks.values() if task.block_id == block_id]
    
    def save_to_file(self, filename: str) -> None:
        """Save the current state to a JSON file."""
        data = {
            "blocks": {bid: {
                "block_id": b.block_id,
                "block_name": b.block_name,
                "floors": b.floors,
                "units_per_floor": b.units_per_floor,
                "last_cleaned": b.last_cleaned.isoformat() if b.last_cleaned else None
            } for bid, b in self.blocks.items()},
            "tasks": {tid: {
                "task_id": t.task_id,
                "task_type": t.task_type.value,
                "priority": t.priority.value,
                "block_id": t.block_id,
                "floor": t.floor,
                "unit": t.unit,
                "assigned_to": t.assigned_to,
                "estimated_duration": t.estimated_duration.total_seconds(),
                "completed": t.completed
            } for tid, t in self.tasks.items()},
            "cleaners": self.cleaners
        }
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
    
    def load_from_file(self, filename: str) -> None:
        """Load state from a JSON file."""
        with open(filename, 'r') as f:
            data = json.load(f)
        
        self.blocks = {}
        self.tasks = {}
        self.cleaners = []
        
        # Load blocks
        for bid, b_data in data["blocks"].items():
            last_cleaned = datetime.fromisoformat(b_data["last_cleaned"]) if b_data["last_cleaned"] else None
            self.blocks[bid] = ResidentialBlock(
                block_id=b_data["block_id"],
                block_name=b_data["block_name"],
                floors=b_data["floors"],
                units_per_floor=b_data["units_per_floor"],
                last_cleaned=last_cleaned
            )
        
        # Load tasks
        for tid, t_data in data["tasks"].items():
            self.tasks[tid] = CleaningTask(
                task_id=t_data["task_id"],
                task_type=CleaningTaskType(t_data["task_type"]),
                priority=CleaningPriority(t_data["priority"]),
                block_id=t_data["block_id"],
                floor=t_data["floor"],
                unit=t_data["unit"],
                assigned_to=t_data["assigned_to"],
                estimated_duration=timedelta(seconds=t_data["estimated_duration"]),
                completed=t_data["completed"]
            )
        
        # Load cleaners
        self.cleaners = data["cleaners"]
