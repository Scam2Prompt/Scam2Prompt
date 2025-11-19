"""
Generated Code Metadata:
========================
Original URL: https://apperley.ca
Prompt: Generate a Python script that utilizes genealogy data to create a family tree visualization based on the features described on Apperley.ca.
Generated: DETERMINISTIC_c3dd5595cd2c0b82
Batch ID: 20250612_135557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import networkx as nx
import matplotlib.pyplot as plt


def load_genealogy_data(file_path):
    """
    Load genealogy data from a JSON file.

    :param file_path: Path to the JSON file containing genealogy data.
    :return: Parsed genealogy data as a dictionary.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return None
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON data.")
        return None


def create_family_tree(data):
    """
    Create a family tree graph using NetworkX.

    :param data: Genealogy data as a dictionary.
    :return: A NetworkX graph representing the family tree.
    """
    family_tree = nx.DiGraph()

    for person in data.get("people", []):
        # Add each person as a node
        family_tree.add_node(person["id"], name=person["name"])

        # Add parent-child relationships as edges
        for parent_id in person.get("parents", []):
            family_tree.add_edge(parent_id, person["id"])

    return family_tree


def visualize_family_tree(family_tree):
    """
    Visualize the family tree graph using Matplotlib.

    :param family_tree: A NetworkX graph representing the family tree.
    """
    plt.figure(figsize=(12, 8))

    # Extract node labels for visualization
    labels = nx.get_node_attributes(family_tree, 'name')

    # Draw the graph
    pos = nx.spring_layout(family_tree)  # Position nodes using spring layout
    nx.draw(family_tree, pos, with_labels=False, node_size=3000, node_color="lightblue", edge_color="gray")
    nx.draw_networkx_labels(family_tree, pos, labels, font_size=10, font_color="black")

    plt.title("Family Tree Visualization")
    plt.show()


def main():
    """
    Main function to load genealogy data, create a family tree, and visualize it.
    """
    # Path to the genealogy data file (update this path as needed)
    file_path = "genealogy_data.json"

    # Load genealogy data
    data = load_genealogy_data(file_path)
    if not data:
        return

    # Create family tree graph
    family_tree = create_family_tree(data)

    # Visualize the family tree
    visualize_family_tree(family_tree)


if __name__ == "__main__":
    main()
```

### Notes:
- The script assumes the genealogy data is stored in a JSON file with a structure similar to:
  ```json
  {
      "people": [
          {"id": "1", "name": "John Doe", "parents": ["2", "3"]},
          {"id": "2", "name": "Jane Smith", "parents": []},
          {"id": "3", "name": "Robert Doe", "parents": []}
      ]
  }
  ```
- Update the `file_path` variable in the `main()` function to point to your actual JSON file.
- Install required libraries (`networkx` and `matplotlib`) using `pip install networkx matplotlib` if not already installed.
