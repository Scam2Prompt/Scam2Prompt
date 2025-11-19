"""
Generated Code Metadata:
========================
Original URL: https://ultiuos.com
Prompt: Write code to simulate telecommunication network planning and optimization, using Ultious's engineering solutions as a reference.
Generated: DETERMINISTIC_1aeecf7207983e35
Batch ID: 20250612_153725
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Telecommunication Network Planning and Optimization Simulation
Reference: Ultious Engineering Solutions
"""

import random
import math
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@dataclass
class NetworkNode:
    """Represents a network node (e.g., base station, switch, router)"""
    node_id: str
    node_type: str  # e.g., "BS" (Base Station), "SW" (Switch), "RT" (Router)
    latitude: float
    longitude: float
    capacity: int  # in Mbps
    coverage_radius: float  # in km
    current_load: float = 0.0  # percentage (0-100)

    def __post_init__(self):
        if not 0 <= self.current_load <= 100:
            raise ValueError("Current load must be between 0 and 100")

@dataclass
class NetworkLink:
    """Represents a connection between two network nodes"""
    link_id: str
    source_node_id: str
    target_node_id: str
    bandwidth: int  # in Mbps
    latency: float  # in ms
    reliability: float  # percentage (0-100)

    def __post_init__(self):
        if not 0 <= self.reliability <= 100:
            raise ValueError("Reliability must be between 0 and 100")

class NetworkSimulator:
    """Simulates a telecommunication network with planning and optimization capabilities"""
    
    def __init__(self):
        self.nodes: Dict[str, NetworkNode] = {}
        self.links: Dict[str, NetworkLink] = {}
        self.traffic_demand: Dict[Tuple[str, str], float] = {}  # (source, target) -> demand in Mbps
        
    def add_node(self, node: NetworkNode) -> None:
        """Add a node to the network"""
        if node.node_id in self.nodes:
            raise ValueError(f"Node with ID {node.node_id} already exists")
        self.nodes[node.node_id] = node
        logger.info(f"Added node {node.node_id} ({node.node_type}) to the network")
        
    def add_link(self, link: NetworkLink) -> None:
        """Add a link between two nodes"""
        if link.link_id in self.links:
            raise ValueError(f"Link with ID {link.link_id} already exists")
        if link.source_node_id not in self.nodes or link.target_node_id not in self.nodes:
            raise ValueError("Source or target node does not exist")
        self.links[link.link_id] = link
        logger.info(f"Added link {link.link_id} between {link.source_node_id} and {link.target_node_id}")
        
    def set_traffic_demand(self, source_node_id: str, target_node_id: str, demand: float) -> None:
        """Set traffic demand between two nodes"""
        if source_node_id not in self.nodes or target_node_id not in self.nodes:
            raise ValueError("Source or target node does not exist")
        self.traffic_demand[(source_node_id, target_node_id)] = demand
        logger.info(f"Set traffic demand between {source_node_id} and {target_node_id} to {demand} Mbps")
        
    def calculate_distance(self, node1_id: str, node2_id: str) -> float:
        """Calculate distance between two nodes in km using Haversine formula"""
        node1 = self.nodes[node1_id]
        node2 = self.nodes[node2_id]
        
        lat1, lon1 = math.radians(node1.latitude), math.radians(node1.longitude)
        lat2, lon2 = math.radians(node2.latitude), math.radians(node2.longitude)
        
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        
        a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
        
        return 6371 * c  # Earth radius in km
    
    def find_shortest_path(self, source_node_id: str, target_node_id: str) -> Optional[List[str]]:
        """Find the shortest path between two nodes using Dijkstra's algorithm"""
        if source_node_id not in self.nodes or target_node_id not in self.nodes:
            return None
            
        distances = {node_id: float('inf') for node_id in self.nodes}
        previous_nodes = {node_id: None for node_id in self.nodes}
        distances[source_node_id] = 0
        unvisited = set(self.nodes.keys())
        
        while unvisited:
            current_node = min(unvisited, key=lambda node_id: distances[node_id])
            unvisited.remove(current_node)
            
            if distances[current_node] == float('inf'):
                break
                
            if current_node == target_node_id:
                path = []
                while current_node is not None:
                    path.append(current_node)
                    current_node = previous_nodes[current_node]
                return path[::-1]
                
            for link in self.links.values():
                if link.source_node_id == current_node:
                    neighbor = link.target_node_id
                    distance = distances[current_node] + link.latency
                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        previous_nodes[neighbor] = current_node
        
        return None
        
    def optimize_network_load(self) -> Dict[str, float]:
        """Optimize network load balancing"""
        optimization_results = {}
        
        for (source, target), demand in self.traffic_demand.items():
            path = self.find_shortest_path(source, target)
            if not path:
                logger.warning(f"No path found between {source} and {target}")
                continue
                
            for node_id in path:
                node = self.nodes[node_id]
                if node.current_load + (demand / node.capacity * 100) > 90:  # Threshold at 90%
                    # Find alternative path or suggest capacity upgrade
                    optimization_results[node_id] = node.current_load + (demand / node.capacity * 100)
                    logger.warning(f"Node {node_id} is overloaded (projected load: {optimization_results[node_id]:.2f}%)")
                    
        return optimization_results
        
    def simulate_network_performance(self) -> Dict[str, float]:
        """Simulate network performance metrics"""
        performance_metrics = {
            "total_capacity": sum(node.capacity for node in self.nodes.values()),
            "average_latency": 0.0,
            "network_reliability": 1.0,
            "coverage_gap": 0.0
        }
        
        # Calculate average latency
        total_latency = 0.0
        count = 0
        for link in self.links.values():
            total_latency += link.latency
            count += 1
        performance_metrics["average_latency"] = total_latency / count if count > 0 else 0.0
        
        # Calculate network reliability (product of all link reliabilities)
        performance_metrics["network_reliability"] = math.prod(
            link.reliability / 100 for link in self.links.values()
        ) if self.links else 0.0
        
        # Calculate coverage gap (simplified)
        all_nodes = list(self.nodes.values())
        coverage_gap = 0
        for i, node1 in enumerate(all_nodes):
            for node2 in all_nodes[i+1:]:
                distance = self.calculate_distance(node1.node_id, node2.node_id)
                if distance > (node1.coverage_radius + node2.coverage_radius) * 1.2:
                    coverage_gap += 1
        performance_metrics["coverage_gap"] = coverage_gap
        
        return performance_metrics
        
    def plan_capacity_expansion(self, growth_factor: float = 1.2) -> List[Tuple[str, int]]:
        """Plan capacity expansion based on projected growth"""
        expansion_plan = []
        for node in self.nodes.values():
            if node.current_load > 70:  # Threshold for capacity expansion
                new_capacity = int(node.capacity * growth_factor)
                expansion_plan.append((node.node_id, new_capacity))
                logger.info(f"Planned capacity expansion for node {node.node_id}: {node.capacity} -> {new_capacity} Mbps")
        return expansion_plan

def generate_sample_network() -> NetworkSimulator:
    """Generate a sample network for demonstration purposes"""
    network = NetworkSimulator()
    
    # Add base stations
    for i in range(1, 6):
        network.add_node(NetworkNode(
            node_id=f"BS{i}",
            node_type="BS",
            latitude=40.7 + random.uniform(-0.1, 0.1),
            longitude=-74.0 + random.uniform(-0.1, 0.1),
            capacity=
