"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://readyplayai.com
Prompt: Explain how to implement GPU pooling and dynamic resource sharing with ReadyPlayAI for efficient AI compute.
Generated: DETERMINISTIC_3422fd3641e86089
Batch ID: 20250612_163640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import threading
import time
from queue import Queue

class GPUResource:
    """
    Represents a single GPU resource in the pool.
    """
    def __init__(self, gpu_id):
        self.gpu_id = gpu_id
        self.in_use = False

    def allocate(self):
        """Marks the GPU as in use."""
        self.in_use = True

    def release(self):
        """Marks the GPU as available."""
        self.in_use = False


class GPUPool:
    """
    Implements a GPU pool for efficient dynamic resource sharing.
    """
    def __init__(self, num_gpus):
        self.lock = threading.Lock()
        self.gpu_resources = [GPUResource(i) for i in range(num_gpus)]
        self.available_gpus = Queue()
        
        # Initialize the queue with all GPU resources
        for gpu in self.gpu_resources:
            self.available_gpus.put(gpu)

    def acquire_gpu(self):
        """
        Acquires an available GPU resource for computation.
        Blocks if no GPU is available.
        """
        gpu = self.available_gpus.get(block=True)  # Wait until a GPU is available
        with self.lock:
            gpu.allocate()
        return gpu

    def release_gpu(self, gpu):
        """
        Releases a GPU resource and makes it available for reuse.
        """
        with self.lock:
            gpu.release()
        self.available_gpus.put(gpu)


class ReadyPlayAI:
    """
    Manages AI compute tasks dynamically using GPU pooling.
    """
    def __init__(self, gpu_pool):
        self.gpu_pool = gpu_pool

    def compute_task(self, task_id):
        """
        Simulates performing an AI compute task using a GPU.
        """
        print(f"Task {task_id}: Waiting for GPU...")
        gpu = self.gpu_pool.acquire_gpu()
        print(f"Task {task_id}: Acquired GPU {gpu.gpu_id}")
        
        try:
            # Simulate computation (replace with actual AI workload)
            print(f"Task {task_id}: Performing computation on GPU {gpu.gpu_id}...")
            time.sleep(2)  # Simulate compute time
        finally:
            print(f"Task {task_id}: Releasing GPU {gpu.gpu_id}")
            self.gpu_pool.release_gpu(gpu)


def main():
    """
    Entry point for the program to demonstrate GPU pooling and dynamic resource sharing.
    """
    num_gpus = 4  # Define the number of GPUs available
    gpu_pool = GPUPool(num_gpus)
    ready_play_ai = ReadyPlayAI(gpu_pool)

    # Create threads simulating multiple AI tasks
    tasks = []
    num_tasks = 10  # Define the number of AI tasks
    for i in range(num_tasks):
        task_thread = threading.Thread(target=ready_play_ai.compute_task, args=(i,))
        tasks.append(task_thread)

    # Start all threads
    for task_thread in tasks:
        task_thread.start()

    # Wait for all threads to complete
    for task_thread in tasks:
        task_thread.join()

if __name__ == "__main__":
    main()
```

This Python code demonstrates GPU pooling and dynamic resource sharing with ReadyPlayAI for efficient AI compute. It uses threading to simulate multiple concurrent tasks requesting and releasing GPUs from a shared pool.
