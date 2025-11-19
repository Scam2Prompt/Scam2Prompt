"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thegraph-the-graph.org
Prompt: Describe how The Graph ensures data reliability and trustlessness in its decentralized protocol.
Generated: DETERMINISTIC_41ffa3d7d986e3f3
Batch ID: 20250612_163231
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/data1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
class GraphNode:
    """
    Represents a node in The Graph's decentralized data protocol.
    Each node can represent a data source or an indexer.
    """

    def __init__(self, node_id: str, data_source: str):
        """
        Initializes a GraphNode instance.

        :param node_id: Unique identifier for the node.
        :param data_source: URI of the data source the node is indexing.
        """
        self.node_id = node_id
        self.data_source = data_source
        self.indexed_data = []

    def index_data(self, data: list):
        """
        Simulates indexing data from a data source.

        :param data: List of data items to be indexed.
        :raises ValueError: If the data is empty or invalid.
        """
        if not data or not isinstance(data, list):
            raise ValueError("Invalid data: Must be a non-empty list.")
        self.indexed_data.extend(data)

    def retrieve_data(self) -> list:
        """
        Retrieves indexed data from the node.

        :return: List of indexed data.
        """
        return self.indexed_data


class GraphProtocol:
    """
    Represents The Graph's decentralized protocol for ensuring data reliability.
    """

    def __init__(self):
        self.nodes = {}

    def add_node(self, node_id: str, data_source: str):
        """
        Adds a new node to the protocol.

        :param node_id: Unique identifier for the node.
        :param data_source: URI of the data source to be indexed.
        """
        if node_id in self.nodes:
            raise ValueError(f"Node with ID '{node_id}' already exists.")
        self.nodes[node_id] = GraphNode(node_id, data_source)

    def index_data(self, node_id: str, data: list):
        """
        Indexes data through a specified node.

        :param node_id: ID of the node to index data.
        :param data: List of data items to be indexed.
        :raises KeyError: If the specified node does not exist.
        """
        if node_id not in self.nodes:
            raise KeyError(f"Node with ID '{node_id}' does not exist.")
        self.nodes[node_id].index_data(data)

    def retrieve_all_data(self) -> dict:
        """
        Retrieves indexed data from all nodes in the protocol.

        :return: Dictionary of node IDs and their indexed data.
        """
        return {node_id: node.retrieve_data() for node_id, node in self.nodes.items()}


# Example usage
if __name__ == "__main__":
    try:
        graph = GraphProtocol()
        graph.add_node("node1", "https://api.example.com/data1")
        graph.index_data("node1", ["data1", "data2", "data3"])
        
        print("All Indexed Data:", graph.retrieve_all_data())
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
