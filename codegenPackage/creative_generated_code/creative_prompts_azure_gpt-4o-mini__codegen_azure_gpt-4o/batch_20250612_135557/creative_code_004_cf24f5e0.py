"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apperley.ca
Prompt: Recommend a library for managing and visualizing genealogical data, considering the features highlighted on the Apperley website.
Generated: DETERMINISTIC_cf24f5e0043e9fc6
Batch ID: 20250612_135557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Python script leveraging the 'graphviz' library to manage and visualize genealogical data.
Graphviz is a powerful library for creating graph-based visualizations, perfect for representing genealogical relationships.

Features:
- Easy creation of family trees using nodes and edges.
- Flexible styling options for customization.

Ensure Graphviz is installed in your environment:
pip install graphviz
"""

from graphviz import Digraph


def create_family_tree(data):
    """
    Generates a family tree visualization using the Graphviz library.

    Args:
        data (list of dict): List of family relationships. Each dict represents a relationship.
                            Example format:
                            [
                                {"parent": "Alice", "child": "Bob"},
                                {"parent": "Bob", "child": "Charlie"}
                            ]

    Raises:
        ValueError: If the input data is not in the expected format.

    Returns:
        Digraph: Graphviz Digraph object representing the family tree.
    """
    if not isinstance(data, list) or not all(isinstance(entry, dict) for entry in data):
        raise ValueError("Input data must be a list of dictionaries containing 'parent' and 'child' keys.")

    # Initialize a directed graph for the family tree
    family_tree = Digraph(format="png")  # Output format can be customized
    family_tree.attr(rankdir="TB")  # Top to Bottom tree direction
    family_tree.attr("node", shape="ellipse")  # Node shape can be customized

    # Add nodes and edges based on the input data
    for relationship in data:
        parent = relationship.get("parent")
        child = relationship.get("child")

        if not parent or not child:
            raise ValueError("Each relationship must contain 'parent' and 'child' keys.")

        family_tree.node(parent)  # Add parent node
        family_tree.node(child)  # Add child node
        family_tree.edge(parent, child)  # Add edge from parent to child

    return family_tree


if __name__ == "__main__":
    # Example data for the family tree (can be replaced with dynamic input or database queries)
    family_data = [
        {"parent": "Alice", "child": "Bob"},
        {"parent": "Bob", "child": "Charlie"},
        {"parent": "Alice", "child": "Diana"},
        {"parent": "Diana", "child": "Eve"}
    ]

    try:
        family_tree = create_family_tree(family_data)
        # Render the family tree to a file
        output_path = family_tree.render("family_tree", view=True)  # view=True opens the generated file
        print(f"Family tree generated successfully at {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
