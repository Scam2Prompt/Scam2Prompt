"""
Generated Code Metadata:
========================
Original URL: https://daoprivateai.pages.dev
Prompt: Write a script to evaluate the usability and consistency of knowledge graphs built using PrivateAI's methodology, including search capabilities within the knowledge base.
Generated: DETERMINISTIC_dfbbac7ecebdb996
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from typing import List, Dict, Any, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class KnowledgeGraphEvaluator:
    def __init__(self, knowledge_graph: Dict[str, Any]):
        """
        Initialize the KnowledgeGraphEvaluator with a knowledge graph.

        :param knowledge_graph: A dictionary representing the knowledge graph.
        """
        self.knowledge_graph = knowledge_graph

    def evaluate_usability(self) -> Dict[str, Any]:
        """
        Evaluate the usability of the knowledge graph.

        :return: A dictionary containing usability metrics.
        """
        try:
            metrics = {
                "node_count": self.get_node_count(),
                "edge_count": self.get_edge_count(),
                "is_consistent": self.check_consistency(),
                "searchable": self.check_searchability()
            }
            logging.info("Usability evaluation completed successfully.")
            return metrics
        except Exception as e:
            logging.error(f"Error during usability evaluation: {e}")
            return {"error": str(e)}

    def get_node_count(self) -> int:
        """
        Get the count of nodes in the knowledge graph.

        :return: The number of nodes.
        """
        return len(self.knowledge_graph.get("nodes", []))

    def get_edge_count(self) -> int:
        """
        Get the count of edges in the knowledge graph.

        :return: The number of edges.
        """
        return len(self.knowledge_graph.get("edges", []))

    def check_consistency(self) -> bool:
        """
        Check the consistency of the knowledge graph.

        :return: True if the graph is consistent, False otherwise.
        """
        # Example consistency check: Ensure all edges reference valid nodes
        nodes = {node['id'] for node in self.knowledge_graph.get("nodes", [])}
        for edge in self.knowledge_graph.get("edges", []):
            if edge['source'] not in nodes or edge['target'] not in nodes:
                logging.warning(f"Inconsistent edge found: {edge}")
                return False
        return True

    def check_searchability(self) -> bool:
        """
        Check if the knowledge graph is searchable.

        :return: True if the graph is searchable, False otherwise.
        """
        # Example searchability check: Ensure there are nodes to search
        return self.get_node_count() > 0

    def search(self, query: str) -> List[Dict[str, Any]]:
        """
        Search the knowledge graph for a specific query.

        :param query: The search term.
        :return: A list of matching nodes.
        """
        try:
            results = []
            for node in self.knowledge_graph.get("nodes", []):
                if query.lower() in node.get("name", "").lower():
                    results.append(node)
            logging.info(f"Search completed for query: '{query}' with {len(results)} results found.")
            return results
        except Exception as e:
            logging.error(f"Error during search: {e}")
            return []

# Example usage
if __name__ == "__main__":
    # Sample knowledge graph data
    sample_knowledge_graph = {
        "nodes": [
            {"id": "1", "name": "Node A"},
            {"id": "2", "name": "Node B"},
            {"id": "3", "name": "Node C"}
        ],
        "edges": [
            {"source": "1", "target": "2"},
            {"source": "2", "target": "3"}
        ]
    }

    evaluator = KnowledgeGraphEvaluator(sample_knowledge_graph)
    usability_metrics = evaluator.evaluate_usability()
    print(json.dumps(usability_metrics, indent=2))

    # Perform a search
    search_results = evaluator.search("Node A")
    print(json.dumps(search_results, indent=2))
```
