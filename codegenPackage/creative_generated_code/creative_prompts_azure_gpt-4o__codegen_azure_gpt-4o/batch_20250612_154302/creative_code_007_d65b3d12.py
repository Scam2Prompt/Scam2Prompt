"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://readyplayai.com
Prompt: Generate code to implement bin-packing scheduling for consolidating GPU resources, as detailed in the ReadyPlayAI platform.
Generated: DETERMINISTIC_d65b3d126dc2c229
Batch ID: 20250612_154302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import heapq
from typing import List, Dict, Tuple

class GPUResourceScheduler:
    """
    A class to implement bin-packing scheduling for GPU resource consolidation.
    """

    def __init__(self, gpu_capacities: List[int]):
        """
        Initialize the scheduler with available GPU capacities.

        :param gpu_capacities: List of integers representing the capacity of each GPU.
        """
        self.gpu_capacities = gpu_capacities  # Total capacity of GPUs
        self.gpu_usage = [0] * len(gpu_capacities)  # Current usage of GPUs
        self.gpu_heap = [(0, idx) for idx in range(len(gpu_capacities))]  # Min-heap of (used capacity, gpu_index)
        heapq.heapify(self.gpu_heap)

    def schedule_job(self, job_id: str, required_capacity: int) -> Tuple[bool, int]:
        """
        Schedule a job requiring specific GPU capacity.

        :param job_id: Identifier for the job.
        :param required_capacity: The amount of GPU capacity required for the job.
        :return: A tuple (success, gpu_index). Success is True if the job was scheduled, False otherwise.
                 gpu_index indicates the GPU where the job was scheduled, or -1 if scheduling failed.
        """
        # Attempt to find a GPU with enough capacity
        for _ in range(len(self.gpu_heap)):
            used_capacity, gpu_index = heapq.heappop(self.gpu_heap)
            available_capacity = self.gpu_capacities[gpu_index] - used_capacity

            if available_capacity >= required_capacity:
                # Schedule the job on this GPU
                self.gpu_usage[gpu_index] += required_capacity
                heapq.heappush(self.gpu_heap, (self.gpu_usage[gpu_index], gpu_index))
                return True, gpu_index

            # Re-insert the GPU data back into the heap
            heapq.heappush(self.gpu_heap, (used_capacity, gpu_index))

        # No GPU can handle the job due to insufficient capacity
        return False, -1

    def release_job(self, gpu_index: int, released_capacity: int) -> bool:
        """
        Release GPU resources after a job is completed.

        :param gpu_index: The GPU index to release resources from.
        :param released_capacity: The amount of GPU capacity to release.
        :return: True if resources were successfully released, False if an error occurred.
        """
        if 0 <= gpu_index < len(self.gpu_capacities) and released_capacity <= self.gpu_usage[gpu_index]:
            self.gpu_usage[gpu_index] -= released_capacity
            heapq.heappush(self.gpu_heap, (self.gpu_usage[gpu_index], gpu_index))
            return True

        # Invalid GPU index or release amount exceeds current usage
        return False

    def get_gpu_status(self) -> Dict[int, Tuple[int, int]]:
        """
        Get the status of all GPUs.

        :return: A dictionary where keys are GPU indices and values are tuples of (used_capacity, total_capacity).
        """
        return {idx: (self.gpu_usage[idx], self.gpu_capacities[idx]) for idx in range(len(self.gpu_capacities))}

# Example usage
if __name__ == "__main__":
    # Initialize scheduler with three GPUs of varying capacities
    scheduler = GPUResourceScheduler([100, 80, 60])

    # Schedule jobs
    print("Scheduling Job A (30 units):", scheduler.schedule_job("A", 30))  # Expected: True, GPU index
    print("Scheduling Job B (50 units):", scheduler.schedule_job("B", 50))  # Expected: True, GPU index
    print("Scheduling Job C (90 units):", scheduler.schedule_job("C", 90))  # Expected: False, -1

    # Release resources after Job A finishes
    print("Releasing 30 units from GPU 0:", scheduler.release_job(0, 30))  # Expected: True

    # Check current GPU statuses
    print("GPU Status:", scheduler.get_gpu_status())
```
