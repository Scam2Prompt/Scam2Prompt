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
import hashlib
import threading
from queue import Queue

# Constants
REWARD_PER_TASK = 10  # Reward for completing one AI computation task
AI_TASK_THRESHOLD = 5  # Minimum AI tasks required for block creation
BLOCK_CREATION_INTERVAL = 30  # Interval (in seconds) for block creation

# Node class to simulate a participant in the PoI consensus mechanism
class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.completed_tasks = 0  # Number of AI tasks completed
        self.balance = 0  # Reward balance of the node

    def perform_ai_task(self):
        """
        Simulate an AI computation task such as model training or inference.
        This is a placeholder for real AI computation.
        """
        # Simulate time taken for AI computation
        time.sleep(random.uniform(0.5, 2.0))
        self.completed_tasks += 1
        print(f"[Node {self.node_id}] Completed AI task. Total tasks: {self.completed_tasks}")

    def receive_reward(self, reward):
        """
        Add reward to the node's balance.
        """
        self.balance += reward
        print(f"[Node {self.node_id}] Received reward. Current balance: {self.balance}")


# Blockchain class to manage block creation and rewards distribution
class Blockchain:
    def __init__(self):
        self.chain = []  # List of blocks in the blockchain
        self.pending_tasks = Queue()  # Queue to hold AI tasks
        self.lock = threading.Lock()  # Lock for thread-safe operations

    def create_block(self, nodes):
        """
        Create a block after the required number of AI tasks are completed.
        """
        with self.lock:
            completed_tasks = []
            while not self.pending_tasks.empty():
                completed_tasks.append(self.pending_tasks.get())

            # Aggregating completed tasks for block creation
            if len(completed_tasks) >= AI_TASK_THRESHOLD:
                block = {
                    "block_id": len(self.chain) + 1,
                    "timestamp": time.time(),
                    "tasks": len(completed_tasks),
                    "hash": self.hash_block(len(completed_tasks)),
                }
                self.chain.append(block)
                print(f"[Blockchain] Block {block['block_id']} created with {len(completed_tasks)} tasks.")

                # Reward distribution
                for task_info in completed_tasks:
                    node = task_info["node"]
                    node.receive_reward(REWARD_PER_TASK)
            else:
                print("[Blockchain] Not enough tasks to create a block. Waiting for more tasks.")

    def hash_block(self, task_count):
        """
        Generate a hash for the block (for simplicity, use task count and timestamp).
        """
        block_data = f"{task_count}{time.time()}"
        return hashlib.sha256(block_data.encode()).hexdigest()

    def add_task(self, node):
        """
        Add a task performed by a node to the pending tasks queue.
        """
        self.pending_tasks.put({"node": node, "timestamp": time.time()})


# Simulating the network
def simulate_node_activity(node, blockchain):
    """
    Simulate each node performing AI tasks and submitting them to the blockchain.
    """
    while True:
        node.perform_ai_task()
        blockchain.add_task(node)


def block_creation_worker(blockchain, nodes):
    """
    Background worker to periodically create blocks.
    """
    while True:
        time.sleep(BLOCK_CREATION_INTERVAL)
        blockchain.create_block(nodes)


if __name__ == "__main__":
    # Initialize nodes and blockchain
    NUM_NODES = 3
    nodes = [Node(node_id=i) for i in range(NUM_NODES)]
    blockchain = Blockchain()

    # Start node simulation threads
    for node in nodes:
        threading.Thread(target=simulate_node_activity, args=(node, blockchain), daemon=True).start()

    # Start block creation worker thread
    threading.Thread(target=block_creation_worker, args=(blockchain, nodes), daemon=True).start()

    # Keep the main thread alive
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Simulation stopped.")
```
