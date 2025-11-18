"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mesogia.com
Prompt: Suggest an API for managing categorized listings (e.g., "Ξενοδοχεία," "Ταπετσαρίες Επίπλων") and provide example code for adding, updating, and deleting entries.
Generated: DETERMINISTIC_54615154c05359bf
Batch ID: 20250612_151044
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

app = Flask(__name__)

# In-memory storage for listings
listings = {}

# Helper function to generate unique IDs
def generate_id():
    return str(uuid.uuid4())

@app.route('/listings', methods=['POST'])
def add_listing():
    """
    Add a new listing to a category.
    Expected JSON format:
    {
        "category": "Ξενοδοχεία",
        "name": "Hotel XYZ",
        "description": "A luxury hotel in Athens"
    }
    """
    try:
        data = request.json
        if not data or 'category' not in data or 'name' not in data or 'description' not in data:
            return jsonify({"error": "Invalid data"}), 400

        listing_id = generate_id()
        category = data['category']

        if category not in listings:
            listings[category] = {}

        listings[category][listing_id] = {
            "name": data['name'],
            "description": data['description']
        }

        return jsonify({"message": "Listing added successfully", "id": listing_id}), 201

    except Exception as e:
        return jsonify({"error": "An error occurred while adding the listing", "details": str(e)}), 500


@app.route('/listings/<category>/<listing_id>', methods=['PUT'])
def update_listing(category, listing_id):
    """
    Update an existing listing.
    Expected JSON format:
    {
        "name": "Updated Hotel Name",
        "description": "Updated description"
    }
    """
    try:
        if category not in listings or listing_id not in listings[category]:
            return jsonify({"error": "Listing not found"}), 404

        data = request.json
        if not data or 'name' not in data or 'description' not in data:
            return jsonify({"error": "Invalid data"}), 400

        listings[category][listing_id] = {
            "name": data['name'],
            "description": data['description']
        }

        return jsonify({"message": "Listing updated successfully"}), 200

    except Exception as e:
        return jsonify({"error": "An error occurred while updating the listing", "details": str(e)}), 500


@app.route('/listings/<category>/<listing_id>', methods=['DELETE'])
def delete_listing(category, listing_id):
    """
    Delete a listing from a category.
    """
    try:
        if category not in listings or listing_id not in listings[category]:
            return jsonify({"error": "Listing not found"}), 404

        del listings[category][listing_id]

        # Remove the category if it's empty
        if not listings[category]:
            del listings[category]

        return jsonify({"message": "Listing deleted successfully"}), 200

    except Exception as e:
        return jsonify({"error": "An error occurred while deleting the listing", "details": str(e)}), 500


@app.route('/listings/<category>', methods=['GET'])
def get_listings_by_category(category):
    """
    Retrieve all listings in a specific category.
    """
    try:
        if category not in listings:
            return jsonify({"error": "Category not found"}), 404

        return jsonify({"category": category, "listings": listings[category]}), 200

    except Exception as e:
        return jsonify({"error": "An error occurred while retrieving the listings", "details": str(e)}), 500


@app.route('/listings', methods=['GET'])
def get_all_listings():
    """
    Retrieve all listings across all categories.
    """
    try:
        return jsonify({"listings": listings}), 200

    except Exception as e:
        return jsonify({"error": "An error occurred while retrieving the listings", "details": str(e)}), 500


if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=True)
```
