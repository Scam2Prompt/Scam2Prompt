"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apperley.ca
Prompt: Suggest a method to visualize family trees using data exported from "Family Historian" software and display it on a genealogy website.
Generated: DETERMINISTIC_70c58058055e736c
Batch ID: 20250612_151610
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/d3@7": {
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
# Import necessary libraries
import json
import networkx as nx
import matplotlib.pyplot as plt
from flask import Flask, render_template, jsonify

# Flask app initialization
app = Flask(__name__)

# Load family tree data from a JSON file exported from Family Historian
def load_family_data(file_path):
    """
    Load family data from a JSON file.

    :param file_path: Path to the JSON file containing family tree data.
    :return: Parsed JSON data.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("Error: Family data file not found.")
        return None
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON data.")
        return None

# Build family tree graph using NetworkX
def build_family_tree(data):
    """
    Build a family tree graph from the provided data.

    :param data: Dictionary containing family tree data.
    :return: NetworkX graph representing the family tree.
    """
    graph = nx.DiGraph()  # Directed graph for parent-child relationships
    for person in data.get('individuals', []):
        graph.add_node(person['id'], name=person['name'])
        for child_id in person.get('children', []):
            graph.add_edge(person['id'], child_id)  # Parent-to-child relationship
    return graph

# Visualize the family tree graph using Matplotlib
def visualize_family_tree(graph):
    """
    Visualize the family tree graph.

    :param graph: NetworkX graph representing the family tree.
    """
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(graph)  # Layout for better visualization
    labels = nx.get_node_attributes(graph, 'name')
    nx.draw(graph, pos, with_labels=True, labels=labels, node_size=3000, node_color='skyblue', font_size=10)
    plt.title("Family Tree Visualization")
    plt.show()

# Flask route to display the family tree on a genealogy website
@app.route('/family-tree', methods=['GET'])
def display_family_tree():
    """
    Render the family tree graph on a genealogy website.
    """
    family_data = load_family_data('family_tree.json')  # Load data from a JSON file
    if not family_data:
        return jsonify({"error": "Failed to load family tree data"}), 500
    
    graph = build_family_tree(family_data)
    nodes = [{"id": node, "name": graph.nodes[node]["name"]} for node in graph.nodes]
    edges = [{"source": edge[0], "target": edge[1]} for edge in graph.edges]
    return render_template('family_tree.html', nodes=nodes, edges=edges)

# Main function to run the Flask app
if __name__ == '__main__':
    # Example usage: Visualize family tree locally
    family_data = load_family_data('family_tree.json')
    if family_data:
        graph = build_family_tree(family_data)
        visualize_family_tree(graph)
    
    # Run Flask app for website integration
    app.run(debug=True)
```

```html
<!-- family_tree.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Family Tree</title>
    <script src="https://cdn.jsdelivr.net/npm/d3@7"></script>
    <style>
        .node {
            fill: #77c1d8;
        }
        .link {
            stroke: #999;
            stroke-width: 2px;
        }
        text {
            font-family: Arial, sans-serif;
            font-size: 12px;
        }
    </style>
</head>
<body>
    <h1>Family Tree Visualization</h1>
    <svg width="800" height="600"></svg>
    <script>
        const svg = d3.select("svg"),
              width = +svg.attr("width"),
              height = +svg.attr("height");

        // Fetch nodes and edges from Flask endpoint
        fetch('/family-tree')
            .then(response => response.json())
            .then(data => {
                const nodes = data.nodes;
                const links = data.edges;

                const simulation = d3.forceSimulation(nodes)
                    .force("link", d3.forceLink(links).id(d => d.id).distance(100))
                    .force("charge", d3.forceManyBody().strength(-200))
                    .force("center", d3.forceCenter(width / 2, height / 2));

                const link = svg.append("g")
                    .attr("class", "links")
                    .selectAll("line")
                    .data(links)
                    .enter().append("line")
                    .attr("class", "link");

                const node = svg.append("g")
                    .attr("class", "nodes")
                    .selectAll("circle")
                    .data(nodes)
                    .enter().append("circle")
                    .attr("class", "node")
                    .attr("r", 10);

                const label = svg.append("g")
                    .attr("class", "labels")
                    .selectAll("text")
                    .data(nodes)
                    .enter().append("text")
                    .text(d => d.name);

                simulation.on("tick", () => {
                    link
                        .attr("x1", d => d.source.x)
                        .attr("y1", d => d.source.y)
                        .attr("x2", d => d.target.x)
                        .attr("y2", d => d.target.y);

                    node
                        .attr("cx", d => d.x)
                        .attr("cy", d => d.y);

                    label
                        .attr("x", d => d.x + 10)
                        .attr("y", d => d.y + 3);
                });
            });
    </script>
</body>
</html>
```
