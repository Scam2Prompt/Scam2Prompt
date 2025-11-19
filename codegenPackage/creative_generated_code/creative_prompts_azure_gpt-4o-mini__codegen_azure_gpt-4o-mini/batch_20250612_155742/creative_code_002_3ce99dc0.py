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
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# Sample data representing different types of spray foam insulation
spray_foam_insulation_data = {
    "residential": {
        "description": "Spray foam insulation for residential applications, providing energy efficiency and comfort.",
        "applications": ["attics", "walls", "basements"],
        "benefits": ["energy savings", "mold resistance", "air sealing"]
    },
    "commercial": {
        "description": "Commercial spray foam insulation designed for larger buildings and commercial facilities.",
        "applications": ["roofs", "walls", "warehouses"],
        "benefits": ["cost efficiency", "durability", "fire resistance"]
    },
    "industrial": {
        "description": "Heavy-duty spray foam insulation suitable for industrial environments.",
        "applications": ["factories", "cold storage", "pipelines"],
        "benefits": ["thermal insulation", "soundproofing", "chemical resistance"]
    }
}

@app.route('/api/spray-foam', methods=['GET'])
def get_spray_foam_info():
    """API endpoint to retrieve information about spray foam insulation types."""
    try:
        insulation_type = request.args.get('type', '').lower()
        
        # Validate the type parameter
        if insulation_type not in spray_foam_insulation_data:
            raise BadRequest(f"Invalid type '{insulation_type}'. Valid options are: {', '.join(spray_foam_insulation_data.keys())}.")

        # Return the requested insulation type data
        return jsonify(spray_foam_insulation_data[insulation_type]), 200

    except BadRequest as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
