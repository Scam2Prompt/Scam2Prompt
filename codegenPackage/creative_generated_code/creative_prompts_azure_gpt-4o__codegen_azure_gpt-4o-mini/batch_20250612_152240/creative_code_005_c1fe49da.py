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
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO)

class ResourceOptimizer:
    """
    A class to optimize storage and computing resources in a decentralized infrastructure.
    """

    def __init__(self, storage_nodes: List[str], compute_nodes: List[str]):
        """
        Initializes the ResourceOptimizer with storage and compute nodes.
        
        :param storage_nodes: List of storage node identifiers
        :param compute_nodes: List of compute node identifiers
        """
        self.storage_nodes = storage_nodes
        self.compute_nodes = compute_nodes

    def scale_storage(self, required_capacity: float) -> List[str]:
        """
        Scales storage resources based on the required capacity.
        
        :param required_capacity: Required storage capacity in GB
        :return: List of storage nodes allocated
        :raises ValueError: If required_capacity is negative
        """
        if required_capacity < 0:
            raise ValueError("Required capacity must be non-negative.")

        logging.info(f"Scaling storage to meet required capacity: {required_capacity} GB")
        allocated_nodes = []
        total_capacity = 0.0

        for node in self.storage_nodes:
            if total_capacity < required_capacity:
                allocated_nodes.append(node)
                total_capacity += self._get_node_capacity(node)

        if total_capacity < required_capacity:
            logging.warning("Not enough storage capacity available.")
            return []

        logging.info(f"Allocated storage nodes: {allocated_nodes}")
        return allocated_nodes

    def scale_computing(self, required_computing_power: float) -> List[str]:
        """
        Scales computing resources based on the required computing power.
        
        :param required_computing_power: Required computing power in GHz
        :return: List of compute nodes allocated
        :raises ValueError: If required_computing_power is negative
        """
        if required_computing_power < 0:
            raise ValueError("Required computing power must be non-negative.")

        logging.info(f"Scaling computing to meet required power: {required_computing_power} GHz")
        allocated_nodes = []
        total_power = 0.0

        for node in self.compute_nodes:
            if total_power < required_computing_power:
                allocated_nodes.append(node)
                total_power += self._get_node_power(node)

        if total_power < required_computing_power:
            logging.warning("Not enough computing power available.")
            return []

        logging.info(f"Allocated compute nodes: {allocated_nodes}")
        return allocated_nodes

    def _get_node_capacity(self, node: str) -> float:
        """
        Retrieves the capacity of a given storage node.
        
        :param node: Node identifier
        :return: Capacity of the node in GB
        """
        # Mock implementation: replace with actual logic to get node capacity
        return 100.0  # Assume each node has 100 GB capacity

    def _get_node_power(self, node: str) -> float:
        """
        Retrieves the computing power of a given compute node.
        
        :param node: Node identifier
        :return: Computing power of the node in GHz
        """
        # Mock implementation: replace with actual logic to get node power
        return 2.5  # Assume each node has 2.5 GHz computing power

def optimize_resources(storage_nodes: List[str], compute_nodes: List[str], 
                       required_capacity: float, required_computing_power: float) -> Dict[str, List[str]]:
    """
    Optimizes the resources based on the required capacity and computing power.
    
    :param storage_nodes: List of storage node identifiers
    :param compute_nodes: List of compute node identifiers
    :param required_capacity: Required storage capacity in GB
    :param required_computing_power: Required computing power in GHz
    :return: A dictionary with allocated storage and compute nodes
    """
    optimizer = ResourceOptimizer(storage_nodes, compute_nodes)
    
    # Using ThreadPoolExecutor to scale resources concurrently
    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = {
            executor.submit(optimizer.scale_storage, required_capacity): "storage",
            executor.submit(optimizer.scale_computing, required_computing_power): "computing"
        }
        
        results = {}
        for future in as_completed(futures):
            resource_type = futures[future]
            try:
                results[resource_type] = future.result()
            except Exception as e:
                logging.error(f"Error scaling {resource_type}: {e}")
                results[resource_type] = []

    return results

# Example usage
if __name__ == "__main__":
    storage_nodes = ['storage1', 'storage2', 'storage3']
    compute_nodes = ['compute1', 'compute2', 'compute3']
    
    required_capacity = 150.0  # GB
    required_computing_power = 5.0  # GHz

    allocated_resources = optimize_resources(storage_nodes, compute_nodes, required_capacity, required_computing_power)
    logging.info(f"Allocated Resources: {allocated_resources}")
```
