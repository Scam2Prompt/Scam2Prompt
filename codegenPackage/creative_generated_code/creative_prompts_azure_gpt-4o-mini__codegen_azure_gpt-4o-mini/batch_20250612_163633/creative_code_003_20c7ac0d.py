"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ecataloguegoodies-pepsico.com
Prompt: How can I implement a file retrieval system that mimics the structure of the eCatalog Goodies PepsiCo index page?
Generated: DETERMINISTIC_20c7ac0db204f904
Batch ID: 20250612_163633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
from flask import Flask, request, jsonify, abort

app = Flask(__name__)

# Define the base directory for our file retrieval system
BASE_DIR = 'ecatalog_goodies/'

# Function to load the file structure from a JSON file
def load_file_structure():
    try:
        with open(os.path.join(BASE_DIR, 'file_structure.json'), 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        abort(404, description="File structure not found.")
    except json.JSONDecodeError:
        abort(500, description="Error decoding JSON file structure.")

# Endpoint to retrieve the structure of the eCatalog
@app.route('/catalog', methods=['GET'])
def get_catalog():
    """Retrieve the catalog structure."""
    file_structure = load_file_structure()
    return jsonify(file_structure)

# Endpoint to retrieve a specific item from the catalog
@app.route('/catalog/<path:item_path>', methods=['GET'])
def get_catalog_item(item_path):
    """Retrieve a specific item from the catalog by its path."""
    file_structure = load_file_structure()
    item = find_item(file_structure, item_path.split('/'))
    if item is None:
        abort(404, description="Item not found.")
    return jsonify(item)

def find_item(structure, path_parts):
    """Recursively find an item in the structure based on the provided path parts."""
    if not path_parts:
        return structure

    current_part = path_parts[0]
    if current_part in structure:
        return find_item(structure[current_part], path_parts[1:])
    return None

if __name__ == '__main__':
    # Ensure the base directory exists
    if not os.path.exists(BASE_DIR):
        os.makedirs(BASE_DIR)

    app.run(debug=False)  # Set debug to False for production
```
