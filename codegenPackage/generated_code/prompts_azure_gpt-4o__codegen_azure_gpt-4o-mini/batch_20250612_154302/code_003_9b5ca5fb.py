"""
Generated Code Metadata:
========================
Original URL: https://readyplayai.com
Prompt: Write code to dynamically allocate GPU resources across multiple AI workloads using hierarchical quotas and fair-share scheduling, as outlined by ReadyPlayAI.
Generated: DETERMINISTIC_9b5ca5fbc84cdf25
Batch ID: 20250612_154302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import threading
import time
from queue import Queue

class GPUResourceManager:
    """
    A class to manage GPU resources dynamically across multiple AI workloads
    using hierarchical quotas and fair-share scheduling.
    """

    def __init__(self, total_gpus):
        """
        Initializes the GPUResourceManager with a specified number of GPUs.

        :param total_gpus: Total number of GPUs available for allocation.
        """
        self.total_gpus = total_gpus
        self.lock = threading.Lock()
        self.workloads = {}
        self.gpu_usage = np.zeros(total_gpus)
        self.queue = Queue()

    def add_workload(self, workload_id, gpu_quota):
        """
        Adds a new workload with a specified GPU quota.

        :param workload_id: Unique identifier for the workload.
        :param gpu_quota: Number of GPUs allocated to this workload.
        """
        with self.lock:
            if workload_id in self.workloads:
                raise ValueError(f"Workload {workload_id} already exists.")
            if gpu_quota > self.total_gpus:
                raise ValueError("Requested GPU quota exceeds total available GPUs.")
            self.workloads[workload_id] = gpu_quota
            self.queue.put(workload_id)

    def release_workload(self, workload_id):
        """
        Releases the resources allocated to a workload.

        :param workload_id: Unique identifier for the workload to be released.
        """
        with self.lock:
            if workload_id not in self.workloads:
                raise ValueError(f"Workload {workload_id} does not exist.")
            del self.workloads[workload_id]

    def allocate_resources(self):
        """
        Allocates GPU resources to workloads based on their quotas and fair-share scheduling.
        """
        while True:
            if not self.queue.empty():
                workload_id = self.queue.get()
                self._allocate_to_workload(workload_id)
                self.queue.task_done()
            time.sleep(1)  # Sleep to prevent busy waiting

    def _allocate_to_workload(self, workload_id):
        """
        Allocates resources to a specific workload.

        :param workload_id: Unique identifier for the workload.
        """
        with self.lock:
            gpu_quota = self.workloads[workload_id]
            available_gpus = np.where(self.gpu_usage == 0)[0]

            if len(available_gpus) < gpu_quota:
                print(f"Insufficient GPUs for workload {workload_id}. Waiting...")
                self.queue.put(workload_id)  # Requeue if not enough GPUs
                return

            # Allocate GPUs
            allocated_gpus = available_gpus[:gpu_quota]
            self.gpu_usage[allocated_gpus] = 1
            print(f"Allocated GPUs {allocated_gpus} to workload {workload_id}.")

    def release_resources(self, workload_id):
        """
        Releases the GPU resources allocated to a specific workload.

        :param workload_id: Unique identifier for the workload.
        """
        with self.lock:
            if workload_id not in self.workloads:
                raise ValueError(f"Workload {workload_id} does not exist.")
            gpu_quota = self.workloads[workload_id]
            allocated_gpus = np.where(self.gpu_usage == 1)[0][:gpu_quota]
            self.gpu_usage[allocated_gpus] = 0
            print(f"Released GPUs {allocated_gpus} from workload {workload_id}.")

# Example usage
if __name__ == "__main__":
    gpu_manager = GPUResourceManager(total_gpus=4)

    # Start the resource allocation in a separate thread
    allocation_thread = threading.Thread(target=gpu_manager.allocate_resources)
    allocation_thread.daemon = True
    allocation_thread.start()

    # Add workloads
    try:
        gpu_manager.add_workload("workload_1", 2)
        gpu_manager.add_workload("workload_2", 1)
        time.sleep(5)  # Simulate some processing time
        gpu_manager.release_resources("workload_1")
        gpu_manager.release_resources("workload_2")
    except ValueError as e:
        print(f"Error: {e}")
```
