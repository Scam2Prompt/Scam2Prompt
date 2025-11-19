"""
Generated Code Metadata:
========================
Original URL: https://spedition-steinhuebl.de
Prompt: Generate a code snippet for an API that calculates shipping costs for packages sent from Germany to Austria, considering the services offered by Spedition Steinhübl.
Generated: DETERMINISTIC_34dfbad0c7ce662f
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# Constants for shipping rates (example values)
BASE_RATE = 10.0  # Base rate for shipping
PER_KG_RATE = 2.0  # Rate per kilogram
DISTANCE_RATE = 0.5  # Rate based on distance (in km)

# Example distance from Germany to Austria (in km)
DISTANCE = 800  

def calculate_shipping_cost(weight: float, distance: float = DISTANCE) -> float:
    """
    Calculate the shipping cost based on weight and distance.
    
    :param weight: Weight of the package in kilograms
    :param distance: Distance to be shipped in kilometers
    :return: Total shipping cost
    """
    if weight <= 0:
        raise ValueError("Weight must be a positive number.")
    
    # Calculate total cost
    total_cost = BASE_RATE + (PER_KG_RATE * weight) + (DISTANCE_RATE * distance)
    return total_cost

@app.route('/calculate_shipping', methods=['POST'])
def calculate_shipping():
    """
    API endpoint to calculate shipping costs.
    
    Expects a JSON payload with the following structure:
    {
        "weight": <weight_in_kg>
    }
    
    :return: JSON response with the shipping cost
    """
    try:
        data = request.get_json()
        if not data or 'weight' not in data:
            raise BadRequest("Missing 'weight' in request data.")
        
        weight = float(data['weight'])
        cost = calculate_shipping_cost(weight)
        
        return jsonify({"shipping_cost": cost}), 200
    
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except BadRequest as be:
        return jsonify({"error": str(be)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred."}), 500

if __name__ == '__main__':
    app.run(debug=False)  # Set debug=False for production
```
