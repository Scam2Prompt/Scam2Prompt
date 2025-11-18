"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apperley.ca
Prompt: Suggest a method to visualize family trees using data exported from "Family Historian" software and display it on a genealogy website.
Generated: DETERMINISTIC_70c58058055e736c
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import networkx as nx
import matplotlib.pyplot as plt
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Load family data from a JSON file exported from Family Historian
def load_family_data(file_path):
    """Load family data from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        raise Exception("Family data file not found.")
    except json.JSONDecodeError:
        raise Exception("Error decoding JSON data.")

# Create a family tree graph from the family data
def create_family_tree(data):
    """Create a directed graph representing the family tree."""
    G = nx.DiGraph()  # Create a directed graph

    for person in data['people']:
        G.add_node(person['id'], name=person['name'])

        # Add relationships (parents)
        for parent_id in person.get('parents', []):
            G.add_edge(parent_id, person['id'])  # Parent to child edge

    return G

# Render the family tree using Matplotlib
def visualize_family_tree(tree):
    """Visualize the family tree using Matplotlib."""
    pos = nx.spring_layout(tree)  # Positioning of nodes
    nx.draw(tree, pos, with_labels=True, labels=nx.get_node_attributes(tree, 'name'), node_size=2000, node_color='lightblue')
    plt.title("Family Tree Visualization")
    plt.show()

@app.route('/family-tree')
def family_tree():
    """API endpoint to fetch and visualize family tree."""
    try:
        data = load_family_data('family_data.json')  # Replace with your actual file path
        family_tree_graph = create_family_tree(data)
        visualize_family_tree(family_tree_graph)
        return jsonify({"status": "Family tree visualized successfully."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

### Note:
- Make sure to install the required libraries using pip:
  ```bash
  pip install Flask networkx matplotlib
  ```
- Create a JSON file named `family_data.json` with appropriate family data structure for the code to run without errors.
