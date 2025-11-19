"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dcsprayfoamsolutions.com
Prompt: Create an API endpoint that provides information about different types of spray foam insulation, including residential, commercial, and industrial applications.
Generated: DETERMINISTIC_3ce99dc0f9458475
Batch ID: 20250612_155742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data for spray foam insulation types
SPRAY_FOAM_INSULATION_DATA = [
    {
        "type": "Residential",
        "description": "Designed for use in homes, offering energy efficiency and comfort.",
        "benefits": ["Improved insulation", "Noise reduction", "Moisture barrier"],
        "applications": ["Attics", "Crawlspaces", "Walls"]
    },
    {
        "type": "Commercial",
        "description": "Used in commercial buildings to provide high-performance insulation.",
        "benefits": ["Energy savings", "Durability", "Fire resistance"],
        "applications": ["Warehouses", "Office spaces", "Retail stores"]
    },
    {
        "type": "Industrial",
        "description": "Engineered for industrial facilities with unique insulation needs.",
        "benefits": ["Chemical resistance", "High R-value", "Structural integrity"],
        "applications": ["Factories", "Storage tanks", "Cold rooms"]
    }
]

@app.route('/api/spray-foam-insulation', methods=['GET'])
def get_spray_foam_insulation():
    """
    API endpoint to retrieve information about spray foam insulation types.

    Returns:
        JSON response containing details about residential, commercial,
        and industrial spray foam insulation applications.
    """
    try:
        # Return the spray foam insulation data as JSON
        return jsonify({
            "success": True,
            "data": SPRAY_FOAM_INSULATION_DATA
        }), 200
    except Exception as e:
        # Handle any unexpected errors gracefully
        return jsonify({
            "success": False,
            "message": "An error occurred while processing your request.",
            "error": str(e)
        }), 500

@app.route('/api/spray-foam-insulation/<string:type>', methods=['GET'])
def get_insulation_by_type(type):
    """
    API endpoint to retrieve information about a specific type of spray foam insulation.

    Args:
        type (str): The type of insulation (e.g., Residential, Commercial, Industrial).

    Returns:
        JSON response containing details about the specified spray foam insulation type.
    """
    try:
        # Filter the data based on the requested type
        insulation = next((item for item in SPRAY_FOAM_INSULATION_DATA if item['type'].lower() == type.lower()), None)
        
        if insulation:
            return jsonify({
                "success": True,
                "data": insulation
            }), 200
        else:
            return jsonify({
                "success": False,
                "message": f"No insulation data found for type: {type}"
            }), 404
    except Exception as e:
        # Handle any unexpected errors gracefully
        return jsonify({
            "success": False,
            "message": "An error occurred while processing your request.",
            "error": str(e)
        }), 500

if __name__ == '__main__':
    # Run the Flask application on localhost and port 5000
    app.run(debug=True)
```
