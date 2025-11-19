"""
Generated Code Metadata:
========================
Original URL: https://pulsechain.netlify.app
Prompt: Create a script to simulate the "Heartbeat Protocol" in a peer-to-peer network, ensuring that nodes share their state, transaction data, and environmental metrics periodically.
Generated: DETERMINISTIC_9148445523b354ed
Batch ID: 20250612_154536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import threading
import time
import random
import json

class Node:
    def __init__(self, node_id, peer_nodes):
        """
        Initialize a node in the peer-to-peer network.

        Args:
        - node_id (str): Unique identifier for the node.
        - peer_nodes (list): List of peer node IDs.
        """
        self.node_id = node_id
        self.peer_nodes = peer_nodes
        self.state = {"node_id": node_id, "status": "online"}
        self.transaction_data = []
        self.environmental_metrics = {"cpu_usage": 0, "memory_usage": 0}

    def update_state(self, state):
        """
        Update the node's state.

        Args:
        - state (dict): New state data.
        """
        self.state = state

    def add_transaction(self, transaction):
        """
        Add a transaction to the node's transaction data.

        Args:
        - transaction (str): Transaction data.
        """
        self.transaction_data.append(transaction)

    def update_environmental_metrics(self, metrics):
        """
        Update the node's environmental metrics.

        Args:
        - metrics (dict): New environmental metrics.
        """
        self.environmental_metrics = metrics

    def send_heartbeat(self, peer_node):
        """
        Simulate sending a heartbeat to a peer node.

        Args:
        - peer_node (Node): Peer node to send the heartbeat to.
        """
        try:
            # Simulate network latency
            time.sleep(random.uniform(0.1, 1.0))

            # Prepare heartbeat data
            heartbeat_data = {
                "node_id": self.node_id,
                "state": self.state,
                "transaction_data": self.transaction_data,
                "environmental_metrics": self.environmental_metrics
            }

            # Simulate receiving heartbeat data on the peer node
            peer_node.receive_heartbeat(heartbeat_data)

        except Exception as e:
            print(f"Error sending heartbeat to {peer_node.node_id}: {str(e)}")

    def receive_heartbeat(self, heartbeat_data):
        """
        Simulate receiving a heartbeat from a peer node.

        Args:
        - heartbeat_data (dict): Heartbeat data received from the peer node.
        """
        try:
            # Update peer node's state
            peer_node_id = heartbeat_data["node_id"]
            peer_state = heartbeat_data["state"]
            peer_transaction_data = heartbeat_data["transaction_data"]
            peer_environmental_metrics = heartbeat_data["environmental_metrics"]

            print(f"Received heartbeat from {peer_node_id}:")
            print(f"  State: {peer_state}")
            print(f"  Transaction Data: {peer_transaction_data}")
            print(f"  Environmental Metrics: {peer_environmental_metrics}")

        except Exception as e:
            print(f"Error receiving heartbeat: {str(e)}")

    def start_heartbeat_protocol(self):
        """
        Start the heartbeat protocol for the node.
        """
        while True:
            for peer_node in [node for node in nodes if node.node_id != self.node_id]:
                self.send_heartbeat(peer_node)
            time.sleep(5)  # Send heartbeats every 5 seconds


# Create nodes
nodes = [
    Node("Node 1", ["Node 2", "Node 3"]),
    Node("Node 2", ["Node 1", "Node 3"]),
    Node("Node 3", ["Node 1", "Node 2"])
]

# Update node states, transaction data, and environmental metrics
nodes[0].update_state({"node_id": "Node 1", "status": "online"})
nodes[0].add_transaction("Transaction 1")
nodes[0].update_environmental_metrics({"cpu_usage": 20, "memory_usage": 50})

nodes[1].update_state({"node_id": "Node 2", "status": "offline"})
nodes[1].add_transaction("Transaction 2")
nodes[1].update_environmental_metrics({"cpu_usage": 30, "memory_usage": 60})

nodes[2].update_state({"node_id": "Node 3", "status": "online"})
nodes[2].add_transaction("Transaction 3")
nodes[2].update_environmental_metrics({"cpu_usage": 10, "memory_usage": 40})

# Start heartbeat protocol for each node
threads = []
for node in nodes:
    thread = threading.Thread(target=node.start_heartbeat_protocol)
    thread.daemon = True  # Allow the program to exit even if the thread is still running
    thread.start()
    threads.append(thread)

# Keep the main thread running to see the heartbeat protocol in action
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Exiting program...")
```
