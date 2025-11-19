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
from typing import List, Dict

class GPU:
    def __init__(self, id: int, memory: int):
        """
        Initialize a GPU object.

        Args:
        id (int): Unique identifier for the GPU.
        memory (int): Available memory of the GPU.
        """
        self.id = id
        self.memory = memory
        self.available_memory = memory
        self.tasks: List[Task] = []

class Task:
    def __init__(self, id: int, required_memory: int):
        """
        Initialize a Task object.

        Args:
        id (int): Unique identifier for the task.
        required_memory (int): Required memory for the task.
        """
        self.id = id
        self.required_memory = required_memory

def first_fit_decreasing(gpus: List[GPU], tasks: List[Task]) -> Dict[int, List[int]]:
    """
    Implement the First-Fit Decreasing (FFD) bin-packing algorithm for GPU scheduling.

    Args:
    gpus (List[GPU]): List of available GPUs.
    tasks (List[Task]): List of tasks to be scheduled.

    Returns:
    Dict[int, List[int]]: A dictionary mapping GPU IDs to task IDs.
    """
    # Sort tasks in decreasing order of required memory
    tasks.sort(key=lambda task: task.required_memory, reverse=True)

    gpu_task_mapping: Dict[int, List[int]] = {gpu.id: [] for gpu in gpus}

    for task in tasks:
        # Find the first GPU with enough available memory
        for gpu in gpus:
            if gpu.available_memory >= task.required_memory:
                gpu.tasks.append(task)
                gpu.available_memory -= task.required_memory
                gpu_task_mapping[gpu.id].append(task.id)
                break
        else:
            # If no GPU has enough memory, raise an exception
            raise Exception(f"Unable to schedule task {task.id} due to insufficient GPU memory")

    return gpu_task_mapping

def best_fit_decreasing(gpus: List[GPU], tasks: List[Task]) -> Dict[int, List[int]]:
    """
    Implement the Best-Fit Decreasing (BFD) bin-packing algorithm for GPU scheduling.

    Args:
    gpus (List[GPU]): List of available GPUs.
    tasks (List[Task]): List of tasks to be scheduled.

    Returns:
    Dict[int, List[int]]: A dictionary mapping GPU IDs to task IDs.
    """
    # Sort tasks in decreasing order of required memory
    tasks.sort(key=lambda task: task.required_memory, reverse=True)

    gpu_task_mapping: Dict[int, List[int]] = {gpu.id: [] for gpu in gpus}

    for task in tasks:
        best_gpu = None
        min_waste = float('inf')

        # Find the GPU with the minimum waste of memory
        for gpu in gpus:
            if gpu.available_memory >= task.required_memory:
                waste = gpu.available_memory - task.required_memory
                if waste < min_waste:
                    min_waste = waste
                    best_gpu = gpu

        if best_gpu:
            best_gpu.tasks.append(task)
            best_gpu.available_memory -= task.required_memory
            gpu_task_mapping[best_gpu.id].append(task.id)
        else:
            # If no GPU has enough memory, raise an exception
            raise Exception(f"Unable to schedule task {task.id} due to insufficient GPU memory")

    return gpu_task_mapping

def main():
    # Example usage
    gpus = [
        GPU(1, 1024),
        GPU(2, 512),
        GPU(3, 2048)
    ]

    tasks = [
        Task(1, 256),
        Task(2, 512),
        Task(3, 128),
        Task(4, 1024)
    ]

    try:
        gpu_task_mapping_ffd = first_fit_decreasing(gpus, tasks)
        print("First-Fit Decreasing (FFD) GPU Task Mapping:")
        for gpu_id, task_ids in gpu_task_mapping_ffd.items():
            print(f"GPU {gpu_id}: Tasks {task_ids}")

        gpus = [
            GPU(1, 1024),
            GPU(2, 512),
            GPU(3, 2048)
        ]

        gpu_task_mapping_bfd = best_fit_decreasing(gpus, tasks)
        print("\nBest-Fit Decreasing (BFD) GPU Task Mapping:")
        for gpu_id, task_ids in gpu_task_mapping_bfd.items():
            print(f"GPU {gpu_id}: Tasks {task_ids}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
