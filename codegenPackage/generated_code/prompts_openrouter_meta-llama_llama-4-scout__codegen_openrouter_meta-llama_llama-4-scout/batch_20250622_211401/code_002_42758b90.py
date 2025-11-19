"""
Generated Code Metadata:
========================
Original URL: https://segroegg.gitbook.io
Prompt: "Design a high-level architecture for an AI training infrastructure using Aethir's bare metal servers, including considerations for scalability and performance optimization."
Generated: DETERMINISTIC_42758b90c85c5345
Batch ID: 20250622_211401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
import logging
from typing import List, Dict

# Set up logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AethirServer:
    """Represents a bare metal server provided by Aethir."""
    
    def __init__(self, server_id: str, gpu_count: int, memory: int):
        """
        Initializes an AethirServer instance.

        Args:
        - server_id (str): Unique identifier for the server.
        - gpu_count (int): Number of GPUs available on the server.
        - memory (int): Amount of memory available on the server in GB.
        """
        self.server_id = server_id
        self.gpu_count = gpu_count
        self.memory = memory
        self.available = True  # Initially, the server is available

class AITrainingInfrastructure:
    """Manages a cluster of Aethir bare metal servers for AI training."""
    
    def __init__(self):
        self.servers = {}  # Mapping of server IDs to AethirServer instances

    def add_server(self, server: AethirServer):
        """
        Adds a server to the infrastructure.

        Args:
        - server (AethirServer): Server to add.
        """
        self.servers[server.server_id] = server
        logger.info(f"Added server {server.server_id} to the infrastructure.")

    def remove_server(self, server_id: str):
        """
        Removes a server from the infrastructure.

        Args:
        - server_id (str): ID of the server to remove.

        Raises:
        - KeyError: If the server ID is not found in the infrastructure.
        """
        if server_id not in self.servers:
            raise KeyError(f"Server {server_id} not found in the infrastructure.")
        del self.servers[server_id]
        logger.info(f"Removed server {server_id} from the infrastructure.")

    def allocate_server(self, gpu_count: int, memory: int) -> AethirServer:
        """
        Allocates a server that meets the specified requirements.

        Args:
        - gpu_count (int): Required number of GPUs.
        - memory (int): Required amount of memory in GB.

        Returns:
        - AethirServer: Allocated server, or None if no server meets the requirements.
        """
        for server in self.servers.values():
            if server.available and server.gpu_count >= gpu_count and server.memory >= memory:
                server.available = False
                return server
        logger.warning("No server meets the requirements.")
        return None

    def deallocate_server(self, server_id: str):
        """
        Deallocates a server, making it available for future allocations.

        Args:
        - server_id (str): ID of the server to deallocate.

        Raises:
        - KeyError: If the server ID is not found in the infrastructure.
        """
        if server_id not in self.servers:
            raise KeyError(f"Server {server_id} not found in the infrastructure.")
        self.servers[server_id].available = True
        logger.info(f"Deallocated server {server_id}.")

def main():
    # Create an AI training infrastructure
    infrastructure = AITrainingInfrastructure()

    # Create and add Aethir servers to the infrastructure
    servers: List[AethirServer] = [
        AethirServer("server1", 4, 16),
        AethirServer("server2", 8, 32),
        AethirServer("server3", 2, 8),
    ]
    for server in servers:
        infrastructure.add_server(server)

    # Allocate a server for AI training
    allocated_server = infrastructure.allocate_server(4, 16)
    if allocated_server:
        logger.info(f"Allocated server {allocated_server.server_id} for AI training.")
    else:
        logger.error("Failed to allocate a server.")

    # Deallocate the server after AI training
    infrastructure.deallocate_server(allocated_server.server_id)

if __name__ == "__main__":
    main()
```
