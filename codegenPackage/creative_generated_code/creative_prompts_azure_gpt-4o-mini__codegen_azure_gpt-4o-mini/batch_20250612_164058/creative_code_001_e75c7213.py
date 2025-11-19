"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamax.ir
Prompt: What are the best practices for designing a data center, and how can I implement them in a software project using the guidelines from متا?
Generated: DETERMINISTIC_e75c721340dcb224
Batch ID: 20250612_164058
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import logging
from typing import List

# Configure logging for error tracking and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DataCenterDesign:
    """
    A class to represent a data center design according to best practices.
    """

    def __init__(self, name: str, location: str, capacity: int):
        """
        Initialize the DataCenterDesign with name, location, and capacity.

        :param name: Name of the data center
        :param location: Geographical location of the data center
        :param capacity: Maximum capacity of the data center in terms of servers
        """
        self.name = name
        self.location = location
        self.capacity = capacity
        self.servers: List[str] = []

    def add_server(self, server_id: str) -> None:
        """
        Add a server to the data center.

        :param server_id: Unique identifier for the server
        :raises ValueError: If the data center is at full capacity
        """
        if len(self.servers) >= self.capacity:
            logging.error(f"Cannot add server {server_id}: Data center {self.name} is at full capacity.")
            raise ValueError("Data center is at full capacity.")
        
        self.servers.append(server_id)
        logging.info(f"Server {server_id} added to data center {self.name}.")

    def remove_server(self, server_id: str) -> None:
        """
        Remove a server from the data center.

        :param server_id: Unique identifier for the server
        :raises ValueError: If the server is not found in the data center
        """
        if server_id not in self.servers:
            logging.error(f"Cannot remove server {server_id}: Not found in data center {self.name}.")
            raise ValueError("Server not found in data center.")
        
        self.servers.remove(server_id)
        logging.info(f"Server {server_id} removed from data center {self.name}.")

    def get_server_count(self) -> int:
        """
        Get the current count of servers in the data center.

        :return: Number of servers currently in the data center
        """
        return len(self.servers)

    def __str__(self) -> str:
        """
        Return a string representation of the data center.

        :return: Description of the data center
        """
        return f"Data Center {self.name} located at {self.location} with {self.get_server_count()} servers."

def main():
    """
    Main function to demonstrate the DataCenterDesign class.
    """
    try:
        data_center = DataCenterDesign(name="DC1", location="LocationA", capacity=5)

        # Add servers to the data center
        for i in range(1, 8):
            try:
                data_center.add_server(f"Server-{i}")
            except ValueError as e:
                logging.warning(str(e))

        # Print current state of the data center
        print(data_center)

        # Remove a server
        data_center.remove_server("Server-3")
        print(data_center)

    except Exception as e:
        logging.critical(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
