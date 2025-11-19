"""
Generated Code Metadata:
========================
Original URL: https://thebase.network
Prompt: Write a basic code snippet to simulate network traffic analysis for a simple network setup.
Generated: DETERMINISTIC_12e0f65309624526
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
from collections import defaultdict
from typing import Dict, List, Tuple

class NetworkTrafficAnalyzer:
    """
    Simulates network traffic analysis by monitoring packet flows between nodes.
    """
    
    def __init__(self, nodes: List[str]):
        """
        Initialize the analyzer with network nodes.
        
        Args:
            nodes: List of node identifiers in the network
        """
        self.nodes = nodes
        self.traffic_log = defaultdict(list)
        self.packet_count = 0
        
    def generate_traffic(self, duration: int = 60) -> None:
        """
        Simulate network traffic for a given duration.
        
        Args:
            duration: Duration in seconds to simulate traffic
        """
        start_time = time.time()
        while time.time() - start_time < duration:
            # Randomly select source and destination
            src = random.choice(self.nodes)
            dst = random.choice([n for n in self.nodes if n != src])
            
            # Generate random packet size (100-1500 bytes)
            size = random.randint(100, 1500)
            
            # Log the traffic
            timestamp = time.time()
            self.traffic_log[(src, dst)].append((timestamp, size))
            self.packet_count += 1
            
            # Sleep to simulate network delay
            time.sleep(random.uniform(0.01, 0.1))
    
    def get_traffic_summary(self) -> Dict[Tuple[str, str], Dict[str, float]]:
        """
        Generate a summary of traffic statistics between nodes.
        
        Returns:
            Dictionary with traffic statistics per node pair
        """
        summary = {}
        for (src, dst), packets in self.traffic_log.items():
            sizes = [size for (_, size) in packets]
            summary[(src, dst)] = {
                'packet_count': len(packets),
                'total_bytes': sum(sizes),
                'avg_packet_size': sum(sizes) / len(sizes) if sizes else 0
            }
        return summary
    
    def detect_anomalies(self, threshold: int = 1000) -> List[Tuple[str, str]]:
        """
        Detect potential anomalies based on traffic volume.
        
        Args:
            threshold: Byte count threshold to consider as anomaly
            
        Returns:
            List of node pairs with suspicious traffic
        """
        anomalies = []
        summary = self.get_traffic_summary()
        for (src, dst), stats in summary.items():
            if stats['total_bytes'] > threshold:
                anomalies.append((src, dst))
        return anomalies

if __name__ == "__main__":
    # Example usage
    nodes = ["node1", "node2", "node3", "node4"]
    analyzer = NetworkTrafficAnalyzer(nodes)
    
    print("Simulating network traffic for 30 seconds...")
    analyzer.generate_traffic(duration=30)
    
    print("\nTraffic Summary:")
    summary = analyzer.get_traffic_summary()
    for pair, stats in summary.items():
        print(f"{pair}: {stats}")
    
    print("\nDetecting anomalies...")
    anomalies = analyzer.detect_anomalies()
    if anomalies:
        print("Potential anomalies detected between:")
        for pair in anomalies:
            print(f"  {pair}")
    else:
        print("No anomalies detected.")
```
