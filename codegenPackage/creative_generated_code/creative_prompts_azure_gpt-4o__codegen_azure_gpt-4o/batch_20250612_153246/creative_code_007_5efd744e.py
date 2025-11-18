"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ablakvaros.hu.ablak-nyilaszaro.hu
Prompt: Suggest an API for integrating a műanyag nyílászáró (plastic window and door) catalog into a website, with filtering options for légkamrák száma (number of air chambers) and hőszigetelés (thermal insulation).
Generated: DETERMINISTIC_5efd744ebe39fc05
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Sample data for the műanyag nyílászáró (plastic window and door) catalog
catalog = [
    {
        "id": 1,
        "name": "Window Model A",
        "air_chambers": 3,
        "thermal_insulation": "High",
        "price": 150
    },
    {
        "id": 2,
        "name": "Door Model B",
        "air_chambers": 5,
        "thermal_insulation": "Medium",
        "price": 250
    },
    {
        "id": 3,
        "name": "Window Model C",
        "air_chambers": 7,
        "thermal_insulation": "Low",
        "price": 180
    },
    {
        "id": 4,
        "name": "Door Model D",
        "air_chambers": 3,
        "thermal_insulation": "High",
        "price": 300
    }
]

@app.route('/api/catalog', methods=['GET'])
def get_catalog():
    """
    API endpoint to retrieve the catalog with optional filtering.
    Filters:
    - air_chambers: Filter by number of air chambers (integer).
    - thermal_insulation: Filter by thermal insulation level (string).

    Example usage:
    GET /api/catalog?air_chambers=3&thermal_insulation=High
    """
    try:
        # Extract query parameters for filtering
        air_chambers = request.args.get('air_chambers', type=int)
        thermal_insulation = request.args.get('thermal_insulation', type=str)

        # Apply filters to the catalog
        filtered_catalog = catalog
        if air_chambers is not None:
            filtered_catalog = [item for item in filtered_catalog if item['air_chambers'] == air_chambers]
        if thermal_insulation is not None:
            filtered_catalog = [item for item in filtered_catalog if item['thermal_insulation'].lower() == thermal_insulation.lower()]

        # Return the filtered catalog as JSON
        return jsonify({"success": True, "data": filtered_catalog}), 200
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"success": False, "error": str(e)}), 500


@app.route('/api/catalog/<int:item_id>', methods=['GET'])
def get_catalog_item(item_id):
    """
    API endpoint to retrieve a specific catalog item by its ID.

    Example usage:
    GET /api/catalog/1
    """
    try:
        # Find the item with the given ID
        item = next((item for item in catalog if item['id'] == item_id), None)
        if item is None:
            return jsonify({"success": False, "error": "Item not found"}), 404

        # Return the item as JSON
        return jsonify({"success": True, "data": item}), 200
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"success": False, "error": str(e)}), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
