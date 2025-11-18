"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dustbox.netlify.app
Prompt: Write a script to implement the interactive graph and file view features mentioned on Dustbox.netlify.app.
Generated: DETERMINISTIC_8770215d922922a6
Batch ID: 20250612_153702
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
from flask import Flask, render_template, request, jsonify
import networkx as nx
import matplotlib.pyplot as plt

app = Flask(__name__)

# Define the path for data storage
DATA_DIR = 'data'
os.makedirs(DATA_DIR, exist_ok=True)

@app.route('/')
def index():
    """Render the main index page."""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file upload for graph data."""
    try:
        if 'file' not in request.files:
            return jsonify({"error": "No file part"}), 400
        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400
        if file:
            file_path = os.path.join(DATA_DIR, file.filename)
            file.save(file_path)
            return jsonify({"message": "File uploaded successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/graph', methods=['POST'])
def create_graph():
    """Create a graph from the uploaded data."""
    try:
        data = request.get_json()
        G = nx.Graph()
        
        # Assuming the data format is a list of edges
        edges = data.get('edges', [])
        G.add_edges_from(edges)

        # Draw and save the graph
        plt.figure()
        nx.draw(G, with_labels=True)
        graph_image_path = os.path.join(DATA_DIR, 'graph.png')
        plt.savefig(graph_image_path)
        plt.close()

        return jsonify({"message": "Graph created successfully", "image": graph_image_path}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/graph/image', methods=['GET'])
def get_graph_image():
    """Serve the generated graph image."""
    try:
        image_path = os.path.join(DATA_DIR, 'graph.png')
        if not os.path.exists(image_path):
            return jsonify({"error": "Graph image not found"}), 404
        return jsonify({"image": image_path}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

**HTML Template (index.html)**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interactive Graph Viewer</title>
</head>
<body>
    <h1>Upload Graph Data</h1>
    <form id="uploadForm">
        <input type="file" name="file" accept=".json">
        <button type="submit">Upload</button>
    </form>

    <h1>Create Graph</h1>
    <button id="createGraphButton">Create Graph</button>

    <h1>View Graph</h1>
    <img id="graphImage" src="" alt="Graph will be displayed here" style="display: none;">

    <script>
        document.getElementById('uploadForm').onsubmit = async function(event) {
            event.preventDefault();
            const formData = new FormData(this);
            const response = await fetch('/upload', {
                method: 'POST',
                body: formData,
            });
            const result = await response.json();
            alert(result.message || result.error);
        };

        document.getElementById('createGraphButton').onclick = async function() {
            const response = await fetch('/graph', {
                method: 'POST',
                body: JSON.stringify({ edges: [[1, 2], [2, 3], [3, 1]] }), // Sample edges
                headers: {
                    'Content-Type': 'application/json'
                }
            });
            const result = await response.json();
            alert(result.message || result.error);
            if (result.image) {
                document.getElementById('graphImage').src = result.image;
                document.getElementById('graphImage').style.display = 'block';
            }
        };
    </script>
</body>
</html>
```
