"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://readyplayai.com
Prompt: Write code to dynamically allocate GPU resources across multiple AI workloads using hierarchical quotas and fair-share scheduling, as outlined by ReadyPlayAI.
Generated: DETERMINISTIC_9b5ca5fbc84cdf25
Batch ID: 20250612_154302
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
from collections import defaultdict

class GPUResourceManager:
    def __init__(self, total_gpu_memory):
        """
        Initialize the GPU Resource Manager.
        :param total_gpu_memory: Total GPU memory available (in MB)
        """
        self.total_gpu_memory = total_gpu_memory  # Total GPU memory
        self.available_gpu_memory = total_gpu_memory  # Memory available for allocation
        self.lock = threading.Lock()  # Lock for thread safety
        self.workload_quotas = defaultdict(lambda: {'quota': 0, 'allocated': 0})  # Store workload quotas and allocations

    def set_quota(self, workload_id, quota):
        """
        Set a hierarchical quota for a workload.
        :param workload_id: Unique identifier for the workload
        :param quota: Quota in MB
        """
        with self.lock:
            if quota > self.total_gpu_memory:
                raise ValueError("Quota exceeds total GPU memory.")
            self.workload_quotas[workload_id]['quota'] = quota

    def allocate_resources(self, workload_id, memory_request):
        """
        Allocate GPU resources to a workload respecting quotas and fair-share scheduling.
        :param workload_id: Unique identifier for the workload
        :param memory_request: Amount of memory to allocate (in MB)
        :return: Boolean indicating allocation success
        """
        with self.lock:
            # Check if workload quota is set and sufficient memory is available
            workload_quota = self.workload_quotas[workload_id]['quota']
            allocated_memory = self.workload_quotas[workload_id]['allocated']
            remaining_quota = workload_quota - allocated_memory

            if memory_request > remaining_quota:
                return False  # Memory request exceeds quota
            if memory_request > self.available_gpu_memory:
                return False  # Insufficient available GPU memory

            # Allocate memory
            self.workload_quotas[workload_id]['allocated'] += memory_request
            self.available_gpu_memory -= memory_request
            return True

    def release_resources(self, workload_id, memory_release):
        """
        Release allocated GPU resources from a workload.
        :param workload_id: Unique identifier for the workload
        :param memory_release: Amount of memory to release (in MB)
        """
        with self.lock:
            allocated_memory = self.workload_quotas[workload_id]['allocated']
            if memory_release > allocated_memory:
                raise ValueError("Release exceeds allocated memory.")

            # Release memory
            self.workload_quotas[workload_id]['allocated'] -= memory_release
            self.available_gpu_memory += memory_release

    def get_status(self):
        """
        Get the current status of GPU resource allocation.
        :return: Dictionary showing available memory and per-workload allocations
        """
        with self.lock:
            return {
                "available_memory": self.available_gpu_memory,
                "workloads": {
                    workload_id: {
                        "quota": info['quota'],
                        "allocated": info['allocated']
                    }
                    for workload_id, info in self.workload_quotas.items()
                }
            }


# Example Usage:
if __name__ == "__main__":
    manager = GPUResourceManager(total_gpu_memory=8000)  # 8000 MB total GPU memory

    # Set quotas for workloads
    manager.set_quota("workload_1", 4000)
    manager.set_quota("workload_2", 3000)
    manager.set_quota("workload_3", 1000)

    # Allocate resources
    print(manager.allocate_resources("workload_1", 2000))  # True: Allocation succeeds
    print(manager.allocate_resources("workload_2", 3000))  # True: Allocation succeeds
    print(manager.allocate_resources("workload_3", 1500))  # False: Exceeds quota

    # Release resources
    manager.release_resources("workload_2", 1000)

    # Check status
    status = manager.get_status()
    print(status)
```
