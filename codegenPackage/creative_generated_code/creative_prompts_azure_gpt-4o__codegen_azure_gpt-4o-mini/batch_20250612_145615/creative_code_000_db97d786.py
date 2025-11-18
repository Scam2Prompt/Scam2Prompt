"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://light-chain-ai.pages.dev
Prompt: Write a Python script to simulate the Proof-of-Intelligence (PoI) consensus mechanism described in Lightchain AI, focusing on rewarding nodes for performing AI computations like model training and inference.
Generated: DETERMINISTIC_db97d7866dd497bc
Batch ID: 20250612_145615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time
import threading
from queue import Queue

class Node:
    """Represents a node in the PoI network."""

    def __init__(self, node_id):
        self.node_id = node_id
        self.reward_balance = 0
        self.lock = threading.Lock()
    
    def perform_computation(self, task):
        """Simulates performing an AI computation."""
        print(f"Node {self.node_id} starting computation on task: {task}")
        time.sleep(random.uniform(0.5, 2))  # Simulate variable computation time
        print(f"Node {self.node_id} finished computation on task: {task}")
        return random.uniform(1, 10)  # Simulate computation result (reward points)
    
    def reward_node(self, amount):
        """Rewards the node with the specified amount."""
        with self.lock:
            self.reward_balance += amount
            print(f"Node {self.node_id} rewarded: {amount}, new balance: {self.reward_balance}")

class PoIConsensus:
    """Handles the Proof-of-Intelligence consensus mechanism."""

    def __init__(self, nodes):
        self.nodes = nodes
        self.task_queue = Queue()

    def submit_task(self, task):
        """Submits a new AI computation task to the queue."""
        self.task_queue.put(task)
        print(f"Task submitted: {task}")

    def process_tasks(self):
        """Processes tasks in the queue with available nodes."""
        while True:
            task = self.task_queue.get()
            if task is None:
                break  # Exit condition for the thread
            self.assign_task_to_node(task)

    def assign_task_to_node(self, task):
        """Assigns a task to a random node and rewards it."""
        selected_node = random.choice(self.nodes)
        result = selected_node.perform_computation(task)
        selected_node.reward_node(result)

def main():
    # Initialize nodes
    num_nodes = 5
    nodes = [Node(node_id=i) for i in range(num_nodes)]

    # Initialize PoI consensus mechanism
    poi = PoIConsensus(nodes)

    # Start a thread to process tasks
    processing_thread = threading.Thread(target=poi.process_tasks)
    processing_thread.start()

    # Simulate submitting tasks
    for i in range(10):
        poi.submit_task(f"AI Task {i + 1}")
        time.sleep(random.uniform(0.2, 1))

    # Stop processing (for demonstration purposes)
    poi.task_queue.put(None)  # Signal the processing thread to exit
    processing_thread.join()  # Wait for the thread to finish

    # Show final rewards
    for node in nodes:
        print(f"Final reward balance for Node {node.node_id}: {node.reward_balance}")

if __name__ == "__main__":
    main()
```
