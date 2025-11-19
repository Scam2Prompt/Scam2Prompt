"""
Generated Code Metadata:
========================
Original URL: https://pulsechain.netlify.app
Prompt: Write code to set up a test network for PulseChain's region-based sharding system, including the implementation of bridge nodes for cross-region communication.
Generated: DETERMINISTIC_0f10ea1ad06cc33e
Batch ID: 20250612_154536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import random
import time
from typing import Dict, List, Optional
from dataclasses import dataclass
import hashlib
import socket
import threading
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class NodeConfig:
    node_id: str
    region: str
    is_bridge: bool = False
    peers: List[str] = None
    port: int = 5000

class Shard:
    def __init__(self, shard_id: str, region: str):
        self.shard_id = shard_id
        self.region = region
        self.nodes: Dict[str, Node] = {}
        self.consensus = "pBFT"  # Default consensus for shards

    def add_node(self, node: 'Node'):
        self.nodes[node.node_id] = node

    def remove_node(self, node_id: str):
        if node_id in self.nodes:
            del self.nodes[node_id]

    def get_nodes(self) -> List['Node']:
        return list(self.nodes.values())

class BridgeManager:
    def __init__(self):
        self.bridges: Dict[str, 'BridgeNode'] = {}
    
    def add_bridge(self, bridge: 'BridgeNode'):
        self.bridges[bridge.node_id] = bridge
    
    def get_bridge_for_region(self, region: str) -> Optional['BridgeNode']:
        for bridge in self.bridges.values():
            if bridge.region == region:
                return bridge
        return None

class Network:
    def __init__(self):
        self.shards: Dict[str, Shard] = {}
        self.bridge_manager = BridgeManager()
    
    def create_shard(self, shard_id: str, region: str) -> Shard:
        shard = Shard(shard_id, region)
        self.shards[shard_id] = shard
        return shard
    
    def get_shard(self, shard_id: str) -> Optional[Shard]:
        return self.shards.get(shard_id)
    
    def add_bridge_node(self, bridge: 'BridgeNode'):
        self.bridge_manager.add_bridge(bridge)

class Message:
    def __init__(self, sender: str, recipient: str, data: dict, msg_type: str):
        self.sender = sender
        self.recipient = recipient
        self.data = data
        self.type = msg_type
        self.timestamp = time.time()
        self.signature = self._generate_signature()
    
    def _generate_signature(self) -> str:
        msg_str = f"{self.sender}{self.recipient}{json.dumps(self.data)}{self.timestamp}"
        return hashlib.sha256(msg_str.encode()).hexdigest()
    
    def to_dict(self) -> dict:
        return {
            "sender": self.sender,
            "recipient": self.recipient,
            "data": self.data,
            "type": self.type,
            "timestamp": self.timestamp,
            "signature": self.signature
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Message':
        return cls(
            sender=data["sender"],
            recipient=data["recipient"],
            data=data["data"],
            msg_type=data["type"]
        )

class Node:
    def __init__(self, config: NodeConfig, network: Network):
        self.node_id = config.node_id
        self.region = config.region
        self.is_bridge = config.is_bridge
        self.peers = config.peers if config.peers else []
        self.port = config.port
        self.network = network
        self.message_queue = []
        self.running = False
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(('localhost', self.port))
        self.thread = threading.Thread(target=self._listen)
    
    def start(self):
        self.running = True
        self.thread.start()
        logger.info(f"Node {self.node_id} started on port {self.port}")
    
    def stop(self):
        self.running = False
        self.thread.join()
        self.socket.close()
        logger.info(f"Node {self.node_id} stopped")
    
    def _listen(self):
        while self.running:
            try:
                data, addr = self.socket.recvfrom(1024)
                message_dict = json.loads(data.decode())
                message = Message.from_dict(message_dict)
                self.message_queue.append(message)
                self._handle_message(message)
            except Exception as e:
                logger.error(f"Error receiving message: {e}")
    
    def _handle_message(self, message: Message):
        if message.recipient == self.node_id or message.recipient == "broadcast":
            logger.info(f"Node {self.node_id} received message from {message.sender}")
            # Process message based on type
            if message.type == "transaction":
                self._process_transaction(message.data)
            elif message.type == "consensus":
                self._process_consensus(message.data)
    
    def _process_transaction(self, transaction: dict):
        # Validate and process transaction
        logger.info(f"Processing transaction: {transaction}")
    
    def _process_consensus(self, consensus_data: dict):
        # Process consensus message
        logger.info(f"Processing consensus message: {consensus_data}")
    
    def send_message(self, recipient: str, data: dict, msg_type: str):
        message = Message(self.node_id, recipient, data, msg_type)
        try:
            if recipient == "broadcast":
                for peer in self.peers:
                    self._send_to_peer(peer, message)
            else:
                self._send_to_peer(recipient, message)
        except Exception as e:
            logger.error(f"Error sending message: {e}")
    
    def _send_to_peer(self, peer_id: str, message: Message):
        # In a real implementation, we'd look up the peer's address
        # For this simulation, we assume peers are on localhost with sequential ports
        peer_port = 5000 + int(peer_id.split("_")[1])  # Simple mapping for demo
        self.socket.sendto(
            json.dumps(message.to_dict()).encode(),
            ('localhost', peer_port)
        )
    
    def connect_to_peer(self, peer_id: str):
        if peer_id not in self.peers:
            self.peers.append(peer_id)
            logger.info(f"Node {self.node_id} connected to peer {peer_id}")

class BridgeNode(Node):
    def __init__(self, config: NodeConfig, network: Network):
        super().__init__(config, network)
        self.connected_regions = set()
    
    def _handle_message(self, message: Message):
        super()._handle_message(message)
        if message.type == "cross_region":
            self._relay_cross_region(message)
    
    def _relay_cross_region(self, message: Message):
        target_region = message.data.get("target_region")
        if not target_region:
            return
        
        bridge = self.network.bridge_manager.get_bridge_for_region(target_region)
        if bridge:
            self.send_message(bridge.node_id, message.data, "cross_region")
            logger.info(f"Relayed message to region {target_region} via bridge {bridge.node_id}")

def setup_test_network():
    network = Network()
    
    # Create shards in different regions
    regions = ["us-east", "eu-west", "asia-pacific"]
    for i, region in enumerate(regions):
        shard_id = f"shard_{i+1}"
        network.create_shard(shard_id, region)
    
    # Add regular nodes to shards
    for shard_id, shard in network.shards.items():
        for j in range(3):  # 3 nodes per shard
            node_id = f"node_{shard_id}_{j}"
            config = NodeConfig(
                node_id=node_id,
                region=shard.region,
                peers=[f"node_{shard_id}_{k}" for k in range(3) if k != j]
            )
            node = Node(config, network)
            shard.add_node(node)
            node.start()
    
    # Add bridge nodes
    for i, region in enumerate(regions):
        bridge_id = f"bridge_{region}"
        config = NodeConfig(
            node_id=bridge_id,
            region=region,
            is_bridge=True,
            peers=[f"bridge_{r}" for r in regions if r != region]
        )
        bridge = BridgeNode(config, network)
        network.add_bridge_node(bridge)
        network.get_shard(f"shard_{i+1}").add_node(bridge)
        bridge.start()
    
    return network

def simulate_cross_region_traffic(network: Network):
    # Simulate a cross-region transaction
    source_shard = network.get_shard("shard
