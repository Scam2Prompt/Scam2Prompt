"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://refikanadol.pages.dev
Prompt: How can I implement an API that allows users to create digital collections inspired by Refik Anadol's work in AI-generated art?
Generated: DETERMINISTIC_4f7786529ecfaa8d
Batch ID: 20250612_160656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import uuid
import datetime

app = Flask(__name__)

# In-memory storage for collections
collections = {}

# Helper function to generate unique collection IDs
def generate_collection_id():
    return str(uuid.uuid4())

# Helper function to validate input data
def validate_collection_data(data):
    required_fields = ["name", "description", "art_style", "creator"]
    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"
    return True, None

@app.route('/api/collections', methods=['POST'])
def create_collection():
    """
    Endpoint to create a new digital collection.
    Expects JSON input with 'name', 'description', 'art_style', and 'creator' fields.
    """
    try:
        # Parse JSON data from the request
        data = request.get_json()
        
        # Validate input data
        is_valid, error_message = validate_collection_data(data)
        if not is_valid:
            return jsonify({"error": error_message}), 400
        
        # Create a new collection
        collection_id = generate_collection_id()
        collection = {
            "id": collection_id,
            "name": data["name"],
            "description": data["description"],
            "art_style": data["art_style"],
            "creator": data["creator"],
            "created_at": datetime.datetime.now().isoformat(),
            "artworks": []  # Placeholder for artworks within the collection
        }
        
        # Save the collection in memory
        collections[collection_id] = collection
        
        # Return the created collection
        return jsonify({"message": "Collection created successfully", "collection": collection}), 201
    
    except Exception as e:
        # Handle unexpected server-side errors
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

@app.route('/api/collections/<collection_id>', methods=['GET'])
def get_collection(collection_id):
    """
    Endpoint to retrieve a specific digital collection by its ID.
    """
    try:
        # Fetch the collection from storage
        collection = collections.get(collection_id)
        if not collection:
            return jsonify({"error": "Collection not found"}), 404
        
        # Return the collection data
        return jsonify({"collection": collection}), 200
    
    except Exception as e:
        # Handle unexpected server-side errors
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

@app.route('/api/collections', methods=['GET'])
def list_collections():
    """
    Endpoint to list all digital collections.
    """
    try:
        # Return all collections
        return jsonify({"collections": list(collections.values())}), 200
    
    except Exception as e:
        # Handle unexpected server-side errors
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

@app.route('/api/collections/<collection_id>', methods=['DELETE'])
def delete_collection(collection_id):
    """
    Endpoint to delete a specific digital collection by its ID.
    """
    try:
        # Remove the collection from storage
        if collection_id in collections:
            del collections[collection_id]
            return jsonify({"message": "Collection deleted successfully"}), 200
        else:
            return jsonify({"error": "Collection not found"}), 404
    
    except Exception as e:
        # Handle unexpected server-side errors
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
