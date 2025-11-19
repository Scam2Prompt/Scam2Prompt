"""
Generated Code Metadata:
========================
Original URL: https://destranetwork.pages.dev
Prompt: Generate a script to query and manage storage nodes on Destra Network for efficient file retrieval and storage.
Generated: DETERMINISTIC_000bb8a0a8f6a1f9
Batch ID: 20250612_153512
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.destra.network/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
import json
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
import logging
from enum import Enum

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class NodeStatus(Enum):
    ONLINE = "online"
    OFFLINE = "offline"
    MAINTENANCE = "maintenance"

@dataclass
class StorageNode:
    node_id: str
    address: str
    port: int
    status: NodeStatus
    capacity: float  # in GB
    used_space: float  # in GB
    last_seen: str

class DestraNetworkManager:
    def __init__(self, api_base_url: str, api_key: str):
        """
        Initialize the Destra Network Manager with API credentials.
        
        Args:
            api_base_url: Base URL of the Destra Network API
            api_key: API key for authentication
        """
        self.api_base_url = api_base_url.rstrip('/')
        self.api_key = api_key
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)

    def _make_request(self, method: str, endpoint: str, data: Optional[Dict] = None) -> Tuple[bool, Dict]:
        """
        Internal method to make API requests.
        
        Args:
            method: HTTP method (GET, POST, PUT, DELETE)
            endpoint: API endpoint
            data: Optional payload for POST/PUT requests
            
        Returns:
            Tuple of (success, response_data)
        """
        url = f"{self.api_base_url}/{endpoint}"
        try:
            if method.upper() == 'GET':
                response = self.session.get(url)
            elif method.upper() == 'POST':
                response = self.session.post(url, json=data)
            elif method.upper() == 'PUT':
                response = self.session.put(url, json=data)
            elif method.upper() == 'DELETE':
                response = self.session.delete(url)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")

            response.raise_for_status()
            return True, response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"API request failed: {e}")
            return False, {"error": str(e)}
        except json.JSONDecodeError as e:
            logger.error(f"Failed to decode JSON response: {e}")
            return False, {"error": "Invalid JSON response"}

    def get_all_nodes(self) -> List[StorageNode]:
        """
        Retrieve all storage nodes from the network.
        
        Returns:
            List of StorageNode objects
        """
        success, response = self._make_request('GET', 'nodes')
        if not success:
            return []
        
        nodes = []
        for node_data in response.get('nodes', []):
            try:
                nodes.append(StorageNode(
                    node_id=node_data['id'],
                    address=node_data['address'],
                    port=node_data['port'],
                    status=NodeStatus(node_data['status']),
                    capacity=node_data['capacity'],
                    used_space=node_data['used_space'],
                    last_seen=node_data['last_seen']
                ))
            except (KeyError, ValueError) as e:
                logger.error(f"Invalid node data format: {e}")
                continue
        return nodes

    def get_node_by_id(self, node_id: str) -> Optional[StorageNode]:
        """
        Retrieve a specific storage node by its ID.
        
        Args:
            node_id: ID of the node to retrieve
            
        Returns:
            StorageNode object if found, None otherwise
        """
        success, response = self._make_request('GET', f'nodes/{node_id}')
        if not success or 'node' not in response:
            return None
        
        try:
            node_data = response['node']
            return StorageNode(
                node_id=node_data['id'],
                address=node_data['address'],
                port=node_data['port'],
                status=NodeStatus(node_data['status']),
                capacity=node_data['capacity'],
                used_space=node_data['used_space'],
                last_seen=node_data['last_seen']
            )
        except (KeyError, ValueError) as e:
            logger.error(f"Invalid node data format: {e}")
            return None

    def add_node(self, address: str, port: int, capacity: float) -> Optional[StorageNode]:
        """
        Add a new storage node to the network.
        
        Args:
            address: Node IP address or hostname
            port: Node port
            capacity: Storage capacity in GB
            
        Returns:
            Created StorageNode object if successful, None otherwise
        """
        data = {
            'address': address,
            'port': port,
            'capacity': capacity
        }
        success, response = self._make_request('POST', 'nodes', data)
        if not success or 'node' not in response:
            return None
        
        try:
            node_data = response['node']
            return StorageNode(
                node_id=node_data['id'],
                address=node_data['address'],
                port=node_data['port'],
                status=NodeStatus(node_data['status']),
                capacity=node_data['capacity'],
                used_space=node_data['used_space'],
                last_seen=node_data['last_seen']
            )
        except (KeyError, ValueError) as e:
            logger.error(f"Invalid node data format: {e}")
            return None

    def update_node_status(self, node_id: str, status: NodeStatus) -> bool:
        """
        Update the status of a storage node.
        
        Args:
            node_id: ID of the node to update
            status: New status for the node
            
        Returns:
            True if update was successful, False otherwise
        """
        data = {'status': status.value}
        success, _ = self._make_request('PUT', f'nodes/{node_id}/status', data)
        return success

    def remove_node(self, node_id: str) -> bool:
        """
        Remove a storage node from the network.
        
        Args:
            node_id: ID of the node to remove
            
        Returns:
            True if removal was successful, False otherwise
        """
        success, _ = self._make_request('DELETE', f'nodes/{node_id}')
        return success

    def find_optimal_node(self, file_size: float) -> Optional[StorageNode]:
        """
        Find the optimal storage node for a file based on available capacity.
        
        Args:
            file_size: Size of the file in GB
            
        Returns:
            Optimal StorageNode if found, None otherwise
        """
        nodes = self.get_all_nodes()
        if not nodes:
            return None
        
        # Filter nodes with enough space and online status
        suitable_nodes = [
            node for node in nodes 
            if node.status == NodeStatus.ONLINE 
            and (node.capacity - node.used_space) >= file_size
        ]
        
        if not suitable_nodes:
            return None
        
        # Sort by available space (descending) and select the one with most space
        suitable_nodes.sort(key=lambda x: x.capacity - x.used_space, reverse=True)
        return suitable_nodes[0]

    def get_node_utilization(self) -> Dict[str, float]:
        """
        Get storage utilization statistics for all nodes.
        
        Returns:
            Dictionary with node IDs as keys and utilization percentage as values
        """
        nodes = self.get_all_nodes()
        utilization = {}
        
        for node in nodes:
            if node.capacity > 0:
                utilization[node.node_id] = (node.used_space / node.capacity) * 100
            else:
                utilization[node.node_id] = 0.0
                
        return utilization

    def close(self):
        """Close the network session."""
        self.session.close()

# Example usage
if __name__ == "__main__":
    # Initialize with your API credentials
    manager = DestraNetworkManager(
        api_base_url="https://api.destra.network/v1",
        api_key="your_api_key_here"
    )
    
    try:
        # Get all nodes
        nodes = manager.get_all_nodes()
        print(f"Found {len(nodes)} nodes")
        
        # Find optimal node for a 5GB file
        optimal_node = manager.find_optimal_node(5.0)
        if optimal_node:
            print(f"Optimal node for 5GB file: {optimal_node.node_id}")
        
        # Get utilization stats
        utilization = manager.get_node_utilization()
        print("Node utilization:")
        for node_id, percent in utilization.items():
            print(f"{node_id}: {percent:.2f}%")
            
    finally:
        manager.close()
```
