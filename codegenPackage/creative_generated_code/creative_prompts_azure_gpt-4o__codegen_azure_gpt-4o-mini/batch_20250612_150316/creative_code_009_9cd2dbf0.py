"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jobbo.com.au
Prompt: Recommend tools or libraries for creating a family tree visualization, inspired by the Jobling Family Tree section on jobbo.com.au.
Generated: DETERMINISTIC_9cd2dbf0d51cbadd
Batch ID: 20250612_150316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# family_tree_visualization.py

import matplotlib.pyplot as plt
import networkx as nx

class FamilyTree:
    """
    A class to represent a family tree using a directed graph.
    """

    def __init__(self):
        """
        Initializes the FamilyTree with an empty directed graph.
        """
        self.tree = nx.DiGraph()

    def add_relationship(self, parent: str, child: str) -> None:
        """
        Adds a parent-child relationship to the family tree.

        :param parent: The name of the parent.
        :param child: The name of the child.
        """
        self.tree.add_edge(parent, child)

    def visualize(self) -> None:
        """
        Visualizes the family tree using matplotlib and networkx.
        """
        plt.figure(figsize=(12, 8))
        pos = nx.spring_layout(self.tree)  # positions for all nodes
        nx.draw(self.tree, pos, with_labels=True, arrows=True,
                node_size=3000, node_color='lightblue', font_size=10,
                font_color='black', font_weight='bold')

        plt.title("Family Tree")
        plt.show()

def main():
    """
    Main function to demonstrate the FamilyTree class.
    """
    try:
        # Create a family tree instance
        family_tree = FamilyTree()

        # Add relationships
        family_tree.add_relationship("Grandparent", "Parent1")
        family_tree.add_relationship("Grandparent", "Parent2")
        family_tree.add_relationship("Parent1", "Child1")
        family_tree.add_relationship("Parent1", "Child2")
        family_tree.add_relationship("Parent2", "Child3")

        # Visualize the family tree
        family_tree.visualize()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

### Required Libraries
Make sure to install the required libraries using:
```bash
pip install matplotlib networkx
``` 

### Running the Code
Run the script using:
```bash
python family_tree_visualization.py
``` 

This script creates a family tree visualization based on parent-child relationships and includes error handling for robustness.
