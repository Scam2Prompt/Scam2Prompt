"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dpai-migrate.pages.dev
Prompt: Provide code examples for scaling decentralized infrastructure using Scalia's optimization strategies for storage and computing resources.
Generated: DETERMINISTIC_c1fe49dabc2145c7
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script provides an example of scaling decentralized infrastructure using optimization strategies for storage and computing resources. 
It employs techniques like resource balancing and distributed task scheduling based on Scalia's principles.
"""

import threading
import queue
import random

# Define a mock resource pool for storage and computing nodes
class ResourceNode:
    """
    Represents a node in the decentralized infrastructure.
    Each node has a certain capacity for storage and computing resources.
    """
    def __init__(self, node_id, storage_capacity, compute_capacity):
        self.node_id = node_id
        self.storage_capacity = storage_capacity  # GB
        self.compute_capacity = compute_capacity  # GHz
        self.current_storage_usage = 0           # GB
        self.current_compute_usage = 0           # GHz
        
    def allocate_resources(self, storage_request, compute_request):
        """
        Allocates resources to a task if sufficient resources are available.
        Returns True if allocation is successful, otherwise False.
        """
        if (self.current_storage_usage + storage_request <= self.storage_capacity and
                self.current_compute_usage + compute_request <= self.compute_capacity):
            self.current_storage_usage += storage_request
            self.current_compute_usage += compute_request
            return True
        return False
    
    def release_resources(self, storage_request, compute_request):
        """
        Releases resources after a task is completed.
        """
        self.current_storage_usage -= storage_request
        self.current_compute_usage -= compute_request


# Define a decentralized resource pool
class DecentralizedResourcePool:
    """
    Represents a pool of decentralized nodes optimized for scaling infrastructure.
    """
    def __init__(self):
        self.nodes = []

    def add_node(self, node: ResourceNode):
        """
        Adds a node to the resource pool.
        """
        self.nodes.append(node)

    def allocate_task(self, storage_request, compute_request):
        """
        Allocates tasks across nodes using Scalia's optimization strategies.
        Uses a round-robin approach for balanced resource distribution.
        """
        for node in self.nodes:
            if node.allocate_resources(storage_request, compute_request):
                return node
        raise Exception("Insufficient resources available in the pool.")

    def release_task(self, node: ResourceNode, storage_request, compute_request):
        """
        Releases resources after task completion.
        """
        node.release_resources(storage_request, compute_request)


# Simulate decentralized task execution
class TaskScheduler:
    """
    Simulates a scheduler that distributes tasks across the decentralized infrastructure.
    """
    def __init__(self, resource_pool: DecentralizedResourcePool):
        self.resource_pool = resource_pool
        self.task_queue = queue.Queue()

    def add_task(self, storage_request, compute_request):
        """
        Adds a task to the queue.
        """
        self.task_queue.put((storage_request, compute_request))

    def execute_task(self):
        """
        Executes tasks from the queue and allocates resources dynamically.
        """
        while not self.task_queue.empty():
            try:
                storage_request, compute_request = self.task_queue.get()
                node = self.resource_pool.allocate_task(storage_request, compute_request)
                
                # Simulate task execution
                print(f"Task executed on Node {node.node_id}. "
                      f"Storage: {storage_request}GB, Compute: {compute_request}GHz.")
                
                # Release resources after task completion
                self.resource_pool.release_task(node, storage_request, compute_request)
            except Exception as e:
                print(f"Task execution failed: {str(e)}")


# Main function to initialize and simulate the infrastructure
def main():
    # Create decentralized resource pool
    resource_pool = DecentralizedResourcePool()

    # Add nodes to the resource pool
    for i in range(5):  # Adding 5 nodes
        resource_pool.add_node(ResourceNode(node_id=f"Node-{i+1}", 
                                            storage_capacity=random.randint(50, 100),  # GB
                                            compute_capacity=random.randint(10, 20)))  # GHz

    # Initialize task scheduler
    scheduler = TaskScheduler(resource_pool)

    # Generate mock tasks
    for _ in range(10):  # Adding 10 tasks
        scheduler.add_task(storage_request=random.randint(5, 20),  # GB
                           compute_request=random.randint(2, 10))  # GHz

    # Execute tasks
    scheduler.execute_task()


# Entry point for the script
if __name__ == "__main__":
    main()
```
