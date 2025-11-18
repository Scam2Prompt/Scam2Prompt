"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daoprivateai.pages.dev
Prompt: Write a script to evaluate the usability and consistency of knowledge graphs built using PrivateAI's methodology, including search capabilities within the knowledge base.
Generated: DETERMINISTIC_dfbbac7ecebdb996
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import networkx as nx
import json
import logging


class KnowledgeGraphEvaluator:
    """
    A class to evaluate the usability and consistency of knowledge graphs
    built using PrivateAI's methodology.
    """

    def __init__(self, graph_data):
        """
        Initializes the KnowledgeGraphEvaluator with a knowledge graph.
        
        :param graph_data: JSON-like dictionary containing nodes and edges of the graph
        """
        self.graph = nx.DiGraph()
        self._load_graph(graph_data)

    def _load_graph(self, graph_data):
        """
        Loads nodes and edges into the knowledge graph.
        
        :param graph_data: JSON-like dictionary containing nodes and edges of the graph
        """
        try:
            nodes = graph_data.get("nodes", [])
            edges = graph_data.get("edges", [])

            # Add nodes to the graph
            for node in nodes:
                self.graph.add_node(node["id"], **node)

            # Add edges to the graph
            for edge in edges:
                self.graph.add_edge(edge["source"], edge["target"], **edge)
        except Exception as e:
            logging.error("Failed to load graph data: %s", str(e))
            raise ValueError("Invalid graph data format.")

    def evaluate_usability(self):
        """
        Evaluates the usability of the knowledge graph. In this case, checks for isolated nodes.

        :return: List of isolated nodes
        """
        try:
            isolated_nodes = list(nx.isolates(self.graph))
            return {
                "isolated_nodes": isolated_nodes,
                "num_isolated_nodes": len(isolated_nodes)
            }
        except Exception as e:
            logging.error("Failed to evaluate usability: %s", str(e))
            raise RuntimeError("Error during usability evaluation.")

    def evaluate_consistency(self):
        """
        Evaluates the consistency of the knowledge graph. In this case, checks for cycles.

        :return: Information about cycles in the graph
        """
        try:
            has_cycles = not nx.is_directed_acyclic_graph(self.graph)
            cycles = list(nx.simple_cycles(self.graph)) if has_cycles else []
            return {
                "has_cycles": has_cycles,
                "cycles": cycles,
                "num_cycles": len(cycles)
            }
        except Exception as e:
            logging.error("Failed to evaluate consistency: %s", str(e))
            raise RuntimeError("Error during consistency evaluation.")

    def search_node(self, node_id):
        """
        Searches for a node in the knowledge graph.

        :param node_id: ID of the node to search
        :return: Node attributes if the node exists, None otherwise
        """
        try:
            if self.graph.has_node(node_id):
                return self.graph.nodes[node_id]
            else:
                return None
        except Exception as e:
            logging.error("Failed to search node: %s", str(e))
            raise RuntimeError("Error during node search.")

    def search_path(self, source, target):
        """
        Searches for a path between two nodes in the knowledge graph.

        :param source: Source node ID
        :param target: Target node ID
        :return: Path as a list of node IDs, None if no path exists
        """
        try:
            if nx.has_path(self.graph, source, target):
                return nx.shortest_path(self.graph, source=source, target=target)
            else:
                return None
        except Exception as e:
            logging.error("Failed to search path: %s", str(e))
            raise RuntimeError("Error during path search.")


def main():
    """
    Main function to demonstrate functionality.
    """
    logging.basicConfig(level=logging.INFO)

    # Sample graph data
    graph_data = {
        "nodes": [
            {"id": "A", "label": "Node A"},
            {"id": "B", "label": "Node B"},
            {"id": "C", "label": "Node C"}
        ],
        "edges": [
            {"source": "A", "target": "B", "type": "relation"},
            {"source": "B", "target": "C", "type": "relation"}
        ]
    }

    try:
        evaluator = KnowledgeGraphEvaluator(graph_data)

        # Evaluate usability
        usability = evaluator.evaluate_usability()
        logging.info("Usability Evaluation: %s", usability)

        # Evaluate consistency
        consistency = evaluator.evaluate_consistency()
        logging.info("Consistency Evaluation: %s", consistency)

        # Search for a node
        node = evaluator.search_node("A")
        logging.info("Search Node 'A': %s", node)

        # Search for a path
        path = evaluator.search_path("A", "C")
        logging.info("Search Path from 'A' to 'C': %s", path)

    except Exception as e:
        logging.error("Error in main function: %s", str(e))


if __name__ == "__main__":
    main()
```
