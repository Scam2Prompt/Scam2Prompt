"""
Generated Code Metadata:
========================
Original URL: https://lavanet-app.pages.dev
Prompt: Explain the concept of QoS (Quality of Service) scoring in Lava's node provider selection process and its impact on response times.
Generated: DETERMINISTIC_f31f22ad8110b0e5
Batch ID: 20250622_210027
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This module demonstrates QoS (Quality of Service) scoring in Lava's node provider selection process.
It simulates how QoS metrics impact node selection and response times.
"""

import random
import time
from dataclasses import dataclass
from typing import List, Dict, Optional
from enum import Enum, auto

class QoSMetric(Enum):
    """Enum representing different QoS metrics"""
    UPTIME = auto()
    LATENCY = auto()
    THROUGHPUT = auto()
    SUCCESS_RATE = auto()

@dataclass
class Node:
    """Represents a node provider with QoS metrics"""
    id: str
    uptime: float  # 0-1 representing percentage
    latency: float  # in milliseconds
    throughput: float  # in requests per second
    success_rate: float  # 0-1 representing percentage

class QoSScorer:
    """Calculates and manages QoS scores for node providers"""
    
    def __init__(self, weights: Optional[Dict[QoSMetric, float]] = None):
        """
        Initialize with optional custom weights for QoS metrics.
        Default weights prioritize uptime and latency.
        """
        self.weights = weights or {
            QoSMetric.UPTIME: 0.4,
            QoSMetric.LATENCY: 0.3,
            QoSMetric.THROUGHPUT: 0.2,
            QoSMetric.SUCCESS_RATE: 0.1
        }
        self._validate_weights()
    
    def _validate_weights(self):
        """Ensure weights sum to 1"""
        total = sum(self.weights.values())
        if not abs(total - 1.0) < 0.0001:
            raise ValueError("QoS weights must sum to 1.0")
    
    def normalize_metric(self, value: float, metric: QoSMetric) -> float:
        """Normalize metric values to 0-1 scale"""
        if metric == QoSMetric.LATENCY:
            # Lower latency is better, so we invert the normalized value
            return 1.0 - min(max(value / 1000, 0), 1)  # Assuming 1000ms is max acceptable
        return min(max(value, 0), 1)
    
    def calculate_score(self, node: Node) -> float:
        """Calculate overall QoS score for a node"""
        normalized_metrics = {
            QoSMetric.UPTIME: self.normalize_metric(node.uptime, QoSMetric.UPTIME),
            QoSMetric.LATENCY: self.normalize_metric(node.latency, QoSMetric.LATENCY),
            QoSMetric.THROUGHPUT: self.normalize_metric(node.throughput/1000, QoSMetric.THROUGHPUT),
            QoSMetric.SUCCESS_RATE: self.normalize_metric(node.success_rate, QoSMetric.SUCCESS_RATE)
        }
        
        score = sum(
            normalized_metrics[metric] * weight
            for metric, weight in self.weights.items()
        )
        return score

class NodeSelector:
    """Selects nodes based on QoS scores and simulates response times"""
    
    def __init__(self, nodes: List[Node], scorer: QoSScorer):
        self.nodes = nodes
        self.scorer = scorer
        self._score_nodes()
    
    def _score_nodes(self):
        """Calculate and store QoS scores for all nodes"""
        self.scored_nodes = [
            (node, self.scorer.calculate_score(node))
            for node in self.nodes
        ]
        # Sort by score descending
        self.scored_nodes.sort(key=lambda x: x[1], reverse=True)
    
    def select_node(self) -> Node:
        """Select a node probabilistically based on QoS scores"""
        total_score = sum(score for _, score in self.scored_nodes)
        if total_score <= 0:
            raise ValueError("No nodes with positive QoS scores available")
        
        rand = random.uniform(0, total_score)
        cumulative = 0
        for node, score in self.scored_nodes:
            cumulative += score
            if rand <= cumulative:
                return node
        return self.scored_nodes[-1][0]  # Fallback to lowest score
    
    def simulate_response_time(self, node: Node) -> float:
        """Simulate response time based on node's latency and QoS score"""
        # Base response time is the node's latency
        # Higher QoS score reduces variability
        base_latency = node.latency
        variability = random.uniform(0.8, 1.2) * (1 - self.scorer.calculate_score(node))
        return base_latency * variability

# Example usage
def demonstrate_qos_selection():
    """Demonstrate QoS scoring and node selection"""
    # Create sample nodes with varying QoS metrics
    nodes = [
        Node("node1", 0.99, 150, 800, 0.98),
        Node("node2", 0.95, 200, 700, 0.95),
        Node("node3", 0.90, 100, 500, 0.90),
        Node("node4", 0.85, 300, 400, 0.85)
    ]
    
    # Initialize QoS scorer with default weights
    scorer = QoSScorer()
    
    # Create node selector
    selector = NodeSelector(nodes, scorer)
    
    # Simulate multiple selections and response times
    for i in range(5):
        selected_node = selector.select_node()
        response_time = selector.simulate_response_time(selected_node)
        print(f"Request {i+1}: Selected {selected_node.id} "
              f"(QoS score: {scorer.calculate_score(selected_node):.2f}) "
              f"Response time: {response_time:.2f}ms")

if __name__ == "__main__":
    demonstrate_qos_selection()
```
