"""
Generated Code Metadata:
========================
Original URL: https://dcsprayfoamsolutions.com
Prompt: Create an API endpoint that provides information about different types of spray foam insulation, including residential, commercial, and industrial applications.
Generated: DETERMINISTIC_3ce99dc0f9458475
Batch ID: 20250612_155742
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

# Sample data for spray foam insulation types
SPRAY_FOAM_INSULATION_DATA = [
    {
        "type": "Residential",
        "description": "Used in homes for energy efficiency, soundproofing, and moisture control.",
        "applications": ["Attics", "Walls", "Basements"]
    },
    {
        "type": "Commercial",
        "description": "Used in commercial buildings for insulation and structural reinforcement.",
        "applications": ["Warehouses", "Office Buildings", "Retail Spaces"]
    },
    {
        "type": "Industrial",
        "description": "Used in industrial settings for temperature control and equipment protection.",
        "applications": ["Factories", "Storage Tanks", "Pipelines"]
    }
]

@app.route('/api/spray-foam-insulation', methods=['GET'])
def get_spray_foam_insulation():
    """
    API endpoint to retrieve information about spray foam insulation types.
    Returns:
        JSON response containing details about residential, commercial, and industrial spray foam insulation.
    """
    try:
        # Return the spray foam insulation data as JSON
        return jsonify({
            "success": True,
            "data": SPRAY_FOAM_INSULATION_DATA
        }), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({
            "success": False,
            "error": "An error occurred while processing your request.",
            "details": str(e)
        }), 500

@app.route('/api/spray-foam-insulation/<string:insulation_type>', methods=['GET'])
def get_insulation_by_type(insulation_type):
    """
    API endpoint to retrieve information about a specific type of spray foam insulation.
    Args:
        insulation_type (str): The type of insulation to retrieve (e.g., Residential, Commercial, Industrial).
    Returns:
        JSON response containing details about the specified insulation type.
    """
    try:
        # Filter the data to find the requested insulation type
        insulation = next((item for item in SPRAY_FOAM_INSULATION_DATA if item["type"].lower() == insulation_type.lower()), None)
        
        if insulation:
            return jsonify({
                "success": True,
                "data": insulation
            }), 200
        else:
            # Return a 404 if the insulation type is not found
            return jsonify({
                "success": False,
                "error": f"Insulation type '{insulation_type}' not found."
            }), 404
    except Exception as e:
        # Handle unexpected errors
        return jsonify({
            "success": False,
            "error": "An error occurred while processing your request.",
            "details": str(e)
        }), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
