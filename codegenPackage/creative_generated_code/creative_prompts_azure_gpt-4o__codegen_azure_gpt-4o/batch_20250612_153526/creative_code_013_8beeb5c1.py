"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wealthbhai.com
Prompt: Suggest an API to model the effect of wall thickness (WT) on the strength and flexibility of stainless steel pipes used in automotive engine systems.
Generated: DETERMINISTIC_8beeb5c14a240d6f
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import math

app = Flask(__name__)

# Constants
YIELD_STRENGTH = 250  # Yield strength of stainless steel in MPa
ELASTIC_MODULUS = 200000  # Elastic modulus of stainless steel in MPa
DEFAULT_PIPE_DIAMETER = 50  # Default outer diameter of the pipe in mm

def calculate_strength(wall_thickness, diameter):
    """
    Calculate the strength of a stainless steel pipe.
    Formula: Strength is proportional to the wall thickness and yield strength.
    """
    return YIELD_STRENGTH * wall_thickness / diameter

def calculate_flexibility(wall_thickness, diameter):
    """
    Calculate the flexibility of a stainless steel pipe.
    Formula: Flexibility is inversely proportional to wall thickness and diameter.
    """
    moment_of_inertia = math.pi * (diameter**4 - (diameter - 2 * wall_thickness)**4) / 64
    return moment_of_inertia / (ELASTIC_MODULUS * diameter)

@app.route('/pipe-properties', methods=['POST'])
def pipe_properties():
    """
    API endpoint to calculate pipe properties based on wall thickness and diameter.
    Expects JSON input with 'wall_thickness' and optional 'diameter'.
    """
    try:
        # Parse input data
        data = request.get_json()
        wall_thickness = data.get('wall_thickness')
        diameter = data.get('diameter', DEFAULT_PIPE_DIAMETER)  # Use default if diameter is not provided

        # Validate inputs
        if wall_thickness is None or wall_thickness <= 0:
            return jsonify({"error": "Invalid wall thickness. Must be a positive number."}), 400
        if diameter <= 0:
            return jsonify({"error": "Invalid diameter. Must be a positive number."}), 400
        if wall_thickness >= diameter / 2:
            return jsonify({"error": "Wall thickness must be less than half the pipe's diameter."}), 400

        # Calculate properties
        strength = calculate_strength(wall_thickness, diameter)
        flexibility = calculate_flexibility(wall_thickness, diameter)

        # Return results
        return jsonify({
            "wall_thickness": wall_thickness,
            "diameter": diameter,
            "strength": round(strength, 2),
            "flexibility": round(flexibility, 6)
        }), 200

    except Exception as e:
        # Handle unexpected server errors
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

# Run the Flask web server
if __name__ == '__main__':
    app.run(debug=False)
```

Note: This code provides a REST API where users can send a POST request to `/pipe-properties` with a JSON payload containing `wall_thickness` and optionally `diameter`. The API calculates the pipe's strength and flexibility based on the input values.
