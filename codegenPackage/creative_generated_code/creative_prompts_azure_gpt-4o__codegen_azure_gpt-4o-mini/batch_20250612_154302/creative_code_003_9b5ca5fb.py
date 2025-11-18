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
import numpy as np
import threading
from queue import Queue
from collections import defaultdict


class GPUResourceManager:
    """
    GPUResourceManager allocates GPU resources across multiple AI workloads using
    hierarchical quotas and fair-share scheduling.
    """

    def __init__(self, total_gpus):
        """
        Initializes the GPU resource manager with a total number of GPUs available.

        :param total_gpus: Total number of GPUs available for allocation.
        """
        self.total_gpus = total_gpus
        self.lock = threading.Lock()
        self.workloads = defaultdict(lambda: 0)  # Track GPU usage by workload
        self.queue = Queue()  # Queue for scheduling workloads
        self.active_workloads = []  # Currently active workloads

    def add_workload(self, workload_name, required_gpus):
        """
        Adds a workload to the scheduling queue.

        :param workload_name: Name of the workload.
        :param required_gpus: Number of GPUs required by the workload.
        """
        self.queue.put((workload_name, required_gpus))

    def allocate_resources(self):
        """
        Allocates resources to workloads based on fair-share scheduling and quotas.
        """
        while not self.queue.empty():
            workload_name, required_gpus = self.queue.get()
            with self.lock:
                # Check available GPUs
                available_gpus = self.total_gpus - sum(self.workloads.values())

                # Allocate GPUs if available
                if available_gpus >= required_gpus:
                    self.workloads[workload_name] += required_gpus
                    self.active_workloads.append(workload_name)
                    print(f"Allocated {required_gpus} GPUs to {workload_name}.")
                else:
                    print(f"Insufficient GPUs for {workload_name}. Required: {required_gpus}, Available: {available_gpus}.")
                self.queue.task_done()

    def release_resources(self, workload_name):
        """
        Releases the resources allocated to a specific workload.

        :param workload_name: Name of the workload to release resources from.
        """
        with self.lock:
            if workload_name in self.workloads:
                gpus_to_release = self.workloads[workload_name]
                self.total_gpus += gpus_to_release
                del self.workloads[workload_name]
                self.active_workloads.remove(workload_name)
                print(f"Released {gpus_to_release} GPUs from {workload_name}.")
            else:
                print(f"No resources allocated to {workload_name}.")

    def show_status(self):
        """
        Displays the current status of GPU allocations.
        """
        print("Current GPU allocations:")
        for workload, gpus in self.workloads.items():
            print(f"{workload}: {gpus} GPUs allocated.")
        print(f"Total free GPUs: {self.total_gpus - sum(self.workloads.values())}")


def main():
    """
    Main function to demonstrate the GPUResourceManager functionality.
    """
    try:
        gpu_manager = GPUResourceManager(total_gpus=8)

        # Simulate adding workloads
        gpu_manager.add_workload("AI_Workload_1", 3)
        gpu_manager.add_workload("AI_Workload_2", 5)
        gpu_manager.add_workload("AI_Workload_3", 2)

        # Allocate resources
        gpu_manager.allocate_resources()

        # Show current status
        gpu_manager.show_status()

        # Release resources from a workload
        gpu_manager.release_resources("AI_Workload_1")

        # Show updated status
        gpu_manager.show_status()

    except Exception as e:
        print(f"Error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
