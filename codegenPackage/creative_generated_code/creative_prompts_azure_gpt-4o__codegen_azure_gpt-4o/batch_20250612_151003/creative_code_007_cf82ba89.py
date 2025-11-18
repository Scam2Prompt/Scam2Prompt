"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daoprivateai.pages.dev
Prompt: Create a data visualization tool to process and understand multi-source scientific data faster, incorporating the features of PrivateAI's knowledge graph system.
Generated: DETERMINISTIC_cf82ba898d54d3b4
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from typing import List, Dict

class ScientificDataProcessor:
    """
    A class to process multi-source scientific data and visualize relationships using PrivateAI's knowledge graph system.
    """

    def __init__(self):
        """
        Initialize the ScientificDataProcessor.
        """
        self.data_sources = {}
        self.knowledge_graph = nx.Graph()

    def add_data_source(self, name: str, data: pd.DataFrame):
        """
        Add a new data source to the processor.

        Args:
            name (str): Name of the data source.
            data (pd.DataFrame): Data to be added. Must contain 'Entity1', 'Entity2', 'Relationship'.
        """
        if 'Entity1' not in data.columns or 'Entity2' not in data.columns or 'Relationship' not in data.columns:
            raise ValueError("Data must contain columns: 'Entity1', 'Entity2', 'Relationship'.")
        self.data_sources[name] = data
        print(f"Data source '{name}' added successfully.")

    def build_knowledge_graph(self):
        """
        Build a knowledge graph from all data sources.
        """
        for name, data in self.data_sources.items():
            for _, row in data.iterrows():
                entity1 = row['Entity1']
                entity2 = row['Entity2']
                relationship = row['Relationship']

                # Add nodes and edges to the graph
                self.knowledge_graph.add_node(entity1, source=name)
                self.knowledge_graph.add_node(entity2, source=name)
                self.knowledge_graph.add_edge(entity1, entity2, relationship=relationship)

        print("Knowledge graph built successfully.")

    def visualize_knowledge_graph(self):
        """
        Visualize the knowledge graph using Matplotlib.
        """
        plt.figure(figsize=(12, 8))
        pos = nx.spring_layout(self.knowledge_graph)  # Layout for the graph

        # Extract edge labels for visualization
        edge_labels = nx.get_edge_attributes(self.knowledge_graph, 'relationship')

        # Draw nodes, edges, and labels
        nx.draw(self.knowledge_graph, pos, with_labels=True, node_color="skyblue", node_size=3000, edge_color="black", font_size=12)
        nx.draw_networkx_edge_labels(self.knowledge_graph, pos, edge_labels=edge_labels, font_color="red")

        plt.title("Knowledge Graph Visualization")
        plt.show()

    def query_relationships(self, entity: str) -> List[Dict[str, str]]:
        """
        Query all relationships for a given entity.

        Args:
            entity (str): The entity to query.

        Returns:
            List[Dict[str, str]]: A list of relationships involving the entity.
        """
        if entity not in self.knowledge_graph.nodes:
            raise ValueError(f"Entity '{entity}' is not found in the knowledge graph.")

        relationships = []
        for neighbor in self.knowledge_graph.neighbors(entity):
            relationship = self.knowledge_graph[entity][neighbor].get('relationship', 'Unknown')
            relationships.append({"Entity": neighbor, "Relationship": relationship})

        return relationships


# Example usage
if __name__ == "__main__":
    # Create mock data sources
    data1 = pd.DataFrame({
        "Entity1": ["A", "B", "C"],
        "Entity2": ["B", "C", "D"],
        "Relationship": ["friend", "colleague", "mentor"]
    })

    data2 = pd.DataFrame({
        "Entity1": ["X", "Y", "Z"],
        "Entity2": ["Y", "Z", "X"],
        "Relationship": ["supports", "advises", "collaborates"]
    })

    # Initialize processor and add data sources
    processor = ScientificDataProcessor()
    processor.add_data_source("Source1", data1)
    processor.add_data_source("Source2", data2)

    # Build and visualize knowledge graph
    processor.build_knowledge_graph()
    processor.visualize_knowledge_graph()

    # Query relationships for an entity
    entity = "B"
    print(f"Relationships for entity '{entity}':")
    relationships = processor.query_relationships(entity)
    for relationship in relationships:
        print(relationship)
```
