"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nodoitalia.com
Prompt: Develop an API that allows users to search for outdoor furniture collections by material properties such as "100% recyclable," "super resistant," or "ultra soft," as described in Nodo Italia's product offerings.
Generated: DETERMINISTIC_2e0c1ba8dd8947c0
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request

# Initialize Flask App
app = Flask(__name__)

# Example data simulating outdoor furniture collections from Nodo Italia
OUTDOOR_FURNITURE_COLLECTIONS = [
    {
        "id": 1,
        "name": "EcoComfort Sofa Set",
        "material_properties": ["100% recyclable", "ultra soft"],
    },
    {
        "id": 2,
        "name": "SuperResist Dining Set",
        "material_properties": ["super resistant", "weatherproof"],
    },
    {
        "id": 3,
        "name": "NatureHarmony Lounge Chair",
        "material_properties": ["100% recyclable", "lightweight"],
    },
    {
        "id": 4,
        "name": "LuxuryRelax Hammock",
        "material_properties": ["ultra soft", "durable"],
    }
]

@app.route('/api/furniture/search', methods=['GET'])
def search_furniture_by_material():
    """
    API Endpoint to search outdoor furniture collections by material properties.
    Query Parameter:
        material (str): The material property to filter on (e.g., '100% recyclable').
    Returns:
        JSON response with furniture matching the material property.
    """
    try:
        # Get the 'material' query parameter
        material = request.args.get('material', '').strip().lower()

        if not material:
            return jsonify({
                "error": "Material property query parameter is required."
            }), 400

        # Filter collections based on the material property
        matching_collections = [
            collection for collection in OUTDOOR_FURNITURE_COLLECTIONS
            if material in [prop.lower() for prop in collection['material_properties']]
        ]

        # Return the filtered collections
        return jsonify({
            "query": material,
            "results": matching_collections
        }), 200

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({
            "error": "An unexpected error occurred.",
            "details": str(e)
        }), 500

# Run the Flask application (if this script is executed directly)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

This code provides a RESTful API using Flask that allows users to search outdoor furniture by material properties. It includes proper error handling and adheres to best practices for Python and Flask development.
