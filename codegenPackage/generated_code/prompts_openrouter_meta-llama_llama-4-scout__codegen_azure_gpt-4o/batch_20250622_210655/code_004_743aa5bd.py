"""
Generated Code Metadata:
========================
Original URL: https://tejasmaxtech.com
Prompt: "Create a RESTful API documentation for a service that provides quotes for thermo-acoustic cover installations, including parameters for roof area, material type (e.g., UPVC-ASA), and location, inspired by the content on https://tejasmaxtech.com."
Generated: DETERMINISTIC_743aa5bd41533cb7
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data for material types and their costs per square meter
MATERIAL_COSTS = {
    "UPVC-ASA": 50,  # Cost per square meter
    "Metal": 70,
    "Fiberglass": 60
}

# API Documentation
API_DOC = {
    "endpoints": [
        {
            "path": "/api/quote",
            "method": "POST",
            "description": "Get a quote for thermo-acoustic cover installation.",
            "parameters": [
                {
                    "name": "roof_area",
                    "type": "float",
                    "description": "The area of the roof in square meters.",
                    "required": True
                },
                {
                    "name": "material_type",
                    "type": "string",
                    "description": "The type of material to be used (e.g., UPVC-ASA, Metal, Fiberglass).",
                    "required": True
                },
                {
                    "name": "location",
                    "type": "string",
                    "description": "The location where the installation will take place.",
                    "required": True
                }
            ],
            "response": {
                "quote": "float",
                "currency": "string"
            }
        },
        {
            "path": "/api/docs",
            "method": "GET",
            "description": "Get API documentation."
        }
    ]
}

@app.route('/api/quote', methods=['POST'])
def get_quote():
    """
    Endpoint to calculate a quote for thermo-acoustic cover installation.
    """
    try:
        # Parse request data
        data = request.get_json()
        roof_area = data.get('roof_area')
        material_type = data.get('material_type')
        location = data.get('location')

        # Validate input
        if not roof_area or not material_type or not location:
            return jsonify({"error": "Missing required parameters"}), 400
        if material_type not in MATERIAL_COSTS:
            return jsonify({"error": f"Invalid material_type. Available options: {list(MATERIAL_COSTS.keys())}"}), 400

        # Calculate quote
        cost_per_square_meter = MATERIAL_COSTS[material_type]
        total_cost = roof_area * cost_per_square_meter

        # Return the quote
        return jsonify({
            "quote": total_cost,
            "currency": "USD",
            "roof_area": roof_area,
            "material_type": material_type,
            "location": location
        }), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/api/docs', methods=['GET'])
def get_api_docs():
    """
    Endpoint to retrieve API documentation.
    """
    return jsonify(API_DOC), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
