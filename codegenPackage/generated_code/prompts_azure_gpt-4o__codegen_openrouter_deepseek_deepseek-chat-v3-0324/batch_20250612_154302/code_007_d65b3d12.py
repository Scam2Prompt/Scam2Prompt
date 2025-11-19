"""
Generated Code Metadata:
========================
Original URL: https://readyplayai.com
Prompt: Generate code to implement bin-packing scheduling for consolidating GPU resources, as detailed in the ReadyPlayAI platform.
Generated: DETERMINISTIC_d65b3d126dc2c229
Batch ID: 20250612_154302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import heapq
from typing import List, Dict, Tuple, Optional

class GPUTask:
    """Represents a GPU task with resource requirements."""
    def __init__(self, task_id: str, gpu_memory: int, duration: int):
        """
        Initialize a GPU task.
        
        Args:
            task_id: Unique identifier for the task
            gpu_memory: GPU memory requirement in MB
            duration: Task duration in seconds
        """
        self.task_id = task_id
        self.gpu_memory = gpu_memory
        self.duration = duration
        self.assigned_gpu: Optional[int] = None

class GPUBin:
    """Represents a GPU bin with available resources."""
    def __init__(self, gpu_id: int, total_memory: int):
        """
        Initialize a GPU bin.
        
        Args:
            gpu_id: Unique identifier for the GPU
            total_memory: Total available GPU memory in MB
        """
        self.gpu_id = gpu_id
        self.total_memory = total_memory
        self.available_memory = total_memory
        self.tasks: List[GPUTask] = []
    
    def can_fit(self, task: GPUTask) -> bool:
        """Check if the task can fit in this GPU bin."""
        return self.available_memory >= task.gpu_memory
    
    def add_task(self, task: GPUTask) -> bool:
        """Add a task to this GPU bin if it fits."""
        if not self.can_fit(task):
            return False
        
        self.available_memory -= task.gpu_memory
        task.assigned_gpu = self.gpu_id
        self.tasks.append(task)
        return True
    
    def remove_task(self, task: GPUTask) -> bool:
        """Remove a task from this GPU bin."""
        if task not in self.tasks:
            return False
        
        self.tasks.remove(task)
        self.available_memory += task.gpu_memory
        task.assigned_gpu = None
        return True

class GPUScheduler:
    """Implements bin-packing scheduling for GPU resources."""
    def __init__(self, gpu_configs: Dict[int, int]):
        """
        Initialize the GPU scheduler.
        
        Args:
            gpu_configs: Dictionary mapping GPU IDs to their total memory in MB
        """
        self.gpu_bins = {gpu_id: GPUBin(gpu_id, memory) 
                         for gpu_id, memory in gpu_configs.items()}
        self.task_queue: List[GPUTask] = []
        self.current_time = 0
        self.completed_tasks: List[GPUTask] = []
        
        # Priority queue for tracking task completion times
        self.completion_queue: List[Tuple[int, GPUTask]] = []
    
    def add_task(self, task: GPUTask) -> bool:
        """Add a task to the scheduler."""
        self.task_queue.append(task)
        return True
    
    def schedule_tasks(self) -> None:
        """Schedule tasks using bin-packing algorithm."""
        # First, process completed tasks
        self._process_completed_tasks()
        
        # Sort tasks by descending memory requirement (Best-Fit Decreasing)
        self.task_queue.sort(key=lambda x: x.gpu_memory, reverse=True)
        
        # Try to assign each task to a GPU
        for task in self.task_queue[:]:
            assigned = False
            
            # Find the best-fit GPU (smallest available memory that can fit the task)
            best_fit = None
            min_remaining = float('inf')
            
            for gpu_id, gpu_bin in self.gpu_bins.items():
                if gpu_bin.can_fit(task):
                    remaining = gpu_bin.available_memory - task.gpu_memory
                    if remaining < min_remaining:
                        min_remaining = remaining
                        best_fit = gpu_bin
            
            if best_fit:
                best_fit.add_task(task)
                heapq.heappush(self.completion_queue, 
                              (self.current_time + task.duration, task))
                self.task_queue.remove(task)
                assigned = True
            
            if not assigned:
                print(f"Warning: Could not assign task {task.task_id} - no available GPUs with sufficient memory")
    
    def _process_completed_tasks(self) -> None:
        """Process tasks that have completed at the current time."""
        while self.completion_queue and self.completion_queue[0][0] <= self.current_time:
            completion_time, task = heapq.heappop(self.completion_queue)
            gpu_bin = self.gpu_bins[task.assigned_gpu]
            gpu_bin.remove_task(task)
            self.completed_tasks.append(task)
    
    def advance_time(self, time_units: int = 1) -> None:
        """Advance the simulation time."""
        self.current_time += time_units
        self.schedule_tasks()
    
    def get_assignment_report(self) -> Dict[str, Dict]:
        """Generate a report of current task assignments."""
        report = {
            "gpus": {},
            "unassigned_tasks": [task.task_id for task in self.task_queue],
            "completed_tasks": [task.task_id for task in self.completed_tasks]
        }
        
        for gpu_id, gpu_bin in self.gpu_bins.items():
            report["gpus"][gpu_id] = {
                "total_memory": gpu_bin.total_memory,
                "available_memory": gpu_bin.available_memory,
                "assigned_tasks": [task.task_id for task in gpu_bin.tasks]
            }
        
        return report

# Example usage
if __name__ == "__main__":
    # Initialize GPU resources (GPU ID: Total Memory in MB)
    gpu_configs = {
        1: 16000,  # 16GB GPU
        2: 24000,  # 24GB GPU
        3: 32000   # 32GB GPU
    }
    
    scheduler = GPUScheduler(gpu_configs)
    
    # Add some tasks (Task ID, GPU Memory in MB, Duration in seconds)
    tasks = [
        GPUTask("task1", 8000, 60),
        GPUTask("task2", 4000, 30),
        GPUTask("task3", 12000, 90),
        GPUTask("task4", 16000, 120),
        GPUTask("task5", 2000, 15)
    ]
    
    for task in tasks:
        scheduler.add_task(task)
    
    # Schedule tasks
    scheduler.schedule_tasks()
    
    # Print initial assignment
    print("Initial assignment:")
    print(scheduler.get_assignment_report())
    
    # Advance time to complete some tasks
    scheduler.advance_time(45)
    print("\nAfter 45 seconds:")
    print(scheduler.get_assignment_report())
    
    # Advance time to complete all tasks
    scheduler.advance_time(120)
    print("\nAfter 165 seconds:")
    print(scheduler.get_assignment_report())
```
