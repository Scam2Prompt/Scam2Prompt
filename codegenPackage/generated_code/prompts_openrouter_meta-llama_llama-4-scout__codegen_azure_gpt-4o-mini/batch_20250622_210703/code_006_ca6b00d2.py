"""
Generated Code Metadata:
========================
Original URL: https://whitelist-tensorians.pages.dev
Prompt: "What are some best practices for building a community around a digital art collection, and how can API/library integration enhance user experience?"
Generated: DETERMINISTIC_ca6b00d2f6548b62
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data structure to hold digital art collections
art_collections = {
    "1": {
        "title": "Starry Night",
        "artist": "Vincent van Gogh",
        "year": 1889,
        "description": "A depiction of a night sky filled with swirling clouds and stars."
    },
    "2": {
        "title": "Mona Lisa",
        "artist": "Leonardo da Vinci",
        "year": 1503,
        "description": "A portrait of a woman with a mysterious smile."
    }
}

@app.route('/collections', methods=['GET'])
def get_collections():
    """
    Retrieve all digital art collections.
    Returns a JSON response with the art collections.
    """
    return jsonify(art_collections), 200

@app.route('/collections/<collection_id>', methods=['GET'])
def get_collection(collection_id):
    """
    Retrieve a specific digital art collection by ID.
    :param collection_id: ID of the art collection
    Returns a JSON response with the art collection details or a 404 error if not found.
    """
    collection = art_collections.get(collection_id)
    if collection:
        return jsonify(collection), 200
    else:
        return jsonify({"error": "Collection not found"}), 404

@app.route('/collections', methods=['POST'])
def add_collection():
    """
    Add a new digital art collection.
    Expects a JSON body with title, artist, year, and description.
    Returns the created collection with a 201 status code.
    """
    try:
        new_collection = request.get_json()
        collection_id = str(len(art_collections) + 1)
        art_collections[collection_id] = new_collection
        return jsonify({"id": collection_id, **new_collection}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/collections/<collection_id>', methods=['DELETE'])
def delete_collection(collection_id):
    """
    Delete a specific digital art collection by ID.
    :param collection_id: ID of the art collection
    Returns a success message or a 404 error if not found.
    """
    if collection_id in art_collections:
        del art_collections[collection_id]
        return jsonify({"message": "Collection deleted successfully"}), 200
    else:
        return jsonify({"error": "Collection not found"}), 404

def fetch_external_data(api_url):
    """
    Fetch data from an external API.
    :param api_url: URL of the external API
    Returns the JSON response or raises an error if the request fails.
    """
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {api_url}: {e}")
        return None

if __name__ == '__main__':
    app.run(debug=True)
```
