"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pulsechain.netlify.app
Prompt: Create a script to simulate the "Heartbeat Protocol" in a peer-to-peer network, ensuring that nodes share their state, transaction data, and environmental metrics periodically.
Generated: DETERMINISTIC_9148445523b354ed
Batch ID: 20250612_154536
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
import json
import random
from typing import Dict, Any, List

class PeerNode:
    def __init__(self, node_id: str):
        """
        Initializes a peer node with a unique ID and empty state, transactions, and metrics.
        """
        self.node_id = node_id
        self.state = "ACTIVE"  # Node state (e.g., ACTIVE, INACTIVE, ERROR)
        self.transactions = []  # List of transaction data (e.g., [{"id": 1, "amount": 100}, ...])
        self.environment_metrics = {}  # Environmental metrics (e.g., {"cpu": 50, "memory": 2048})
        self.peers = []  # List of connected peer IDs

    def generate_environment_metrics(self) -> None:
        """
        Generates random environmental metrics for simulation purposes.
        """
        self.environment_metrics = {
            "cpu": random.randint(0, 100),  # CPU usage percentage
            "memory": random.randint(1000, 8000),  # Memory usage in megabytes
            "disk": random.randint(5000, 20000)  # Disk space in megabytes
        }

    def generate_transactions(self) -> None:
        """
        Generates random transaction data for simulation purposes.
        """
        transaction = {
            "id": random.randint(1000, 9999),
            "amount": random.randint(10, 5000),
            "timestamp": time.time()
        }
        self.transactions.append(transaction)

    def heartbeat(self) -> Dict[str, Any]:
        """
        Constructs a heartbeat message containing the node's state, transactions, and metrics.
        """
        self.generate_environment_metrics()
        self.generate_transactions()

        return {
            "node_id": self.node_id,
            "state": self.state,
            "transactions": self.transactions,
            "environment_metrics": self.environment_metrics
        }

    def send_heartbeat_to_peers(self):
        """
        Simulates sending heartbeat data to connected peers.
        """
        heartbeat_data = self.heartbeat()
        print(f"[{self.node_id}] Sending heartbeat to peers: {json.dumps(heartbeat_data, indent=2)}")
        # Normally, the heartbeat would be sent over the network. Here, we simulate this action.

    def receive_heartbeat(self, sender_id: str, heartbeat_data: Dict[str, Any]):
        """
        Simulates receiving a heartbeat message from another peer.
        """
        print(f"[{self.node_id}] Received heartbeat from {sender_id}: {json.dumps(heartbeat_data, indent=2)}")
        # Process the received heartbeat data (e.g., update peer states or metrics).

class HeartbeatProtocol:
    def __init__(self, nodes: List[PeerNode], interval: int = 5):
        """
        Initializes the heartbeat protocol for a list of nodes.
        :param nodes: List of PeerNode objects participating in the network.
        :param interval: Time interval (in seconds) for heartbeat messages.
        """
        self.nodes = nodes
        self.interval = interval
        self.running = False

    def start(self):
        """
        Starts the heartbeat protocol simulation.
        """
        self.running = True
        threading.Thread(target=self._simulate_heartbeat_loop, daemon=True).start()

    def stop(self):
        """
        Stops the heartbeat protocol simulation.
        """
        self.running = False

    def _simulate_heartbeat_loop(self):
        """
        Periodically sends heartbeat messages between nodes.
        """
        while self.running:
            for node in self.nodes:
                node.send_heartbeat_to_peers()
                # Simulate peer-to-peer communication
                for peer in self.nodes:
                    if peer.node_id != node.node_id:  # Exclude self
                        peer.receive_heartbeat(node.node_id, node.heartbeat())
            time.sleep(self.interval)

# Example usage:
if __name__ == "__main__":
    # Create nodes
    node1 = PeerNode("Node1")
    node2 = PeerNode("Node2")
    node3 = PeerNode("Node3")

    # Simulate P2P network connections
    node1.peers = ["Node2", "Node3"]
    node2.peers = ["Node1", "Node3"]
    node3.peers = ["Node1", "Node2"]

    # Start heartbeat protocol
    heartbeat_protocol = HeartbeatProtocol([node1, node2, node3], interval=3)
    heartbeat_protocol.start()

    # Run simulation for some time, then stop
    try:
        time.sleep(15)  # Let the heartbeat simulation run for 15 seconds
    except KeyboardInterrupt:
        pass
    finally:
        heartbeat_protocol.stop()
        print("Heartbeat protocol simulation stopped.")
```
