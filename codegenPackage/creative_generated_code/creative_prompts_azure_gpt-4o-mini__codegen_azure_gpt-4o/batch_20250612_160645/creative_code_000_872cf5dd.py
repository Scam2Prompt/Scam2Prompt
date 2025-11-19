"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://panam.su
Prompt: Generate a code snippet for a web application that calculates the cost of apartment renovation based on the provided pricing structure from Панам's services.
Generated: DETERMINISTIC_872cf5dd023fcf5d
Batch ID: 20250612_160645
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import traceback

app = Flask(__name__)

# Pricing structure for Панам's services (example values)
PRICING_STRUCTURE = {
    "paint": 15.0,  # Cost per square meter for painting
    "flooring": 20.0,  # Cost per square meter for flooring
    "plumbing": 300.0,  # Fixed cost per bathroom for plumbing
    "electrical": 250.0,  # Fixed cost per room for electrical work
}

def calculate_cost(area, num_bathrooms, num_rooms, selected_services):
    """
    Calculate the total renovation cost based on selected services and their pricing.

    :param area: Total area of the apartment (in square meters)
    :param num_bathrooms: Number of bathrooms in the apartment
    :param num_rooms: Number of rooms in the apartment
    :param selected_services: List of services selected for renovation
    :return: Total cost of renovation
    """
    total_cost = 0.0

    # Calculate cost for each selected service
    for service in selected_services:
        if service == "paint":
            total_cost += PRICING_STRUCTURE["paint"] * area
        elif service == "flooring":
            total_cost += PRICING_STRUCTURE["flooring"] * area
        elif service == "plumbing":
            total_cost += PRICING_STRUCTURE["plumbing"] * num_bathrooms
        elif service == "electrical":
            total_cost += PRICING_STRUCTURE["electrical"] * num_rooms
        else:
            raise ValueError(f"Unknown service: {service}")

    return total_cost


@app.route('/calculate-renovation-cost', methods=['POST'])
def calculate_renovation_cost():
    """
    API endpoint to calculate the renovation cost.

    Expects JSON payload with the following fields:
    - area: Total area of the apartment (in square meters)
    - num_bathrooms: Number of bathrooms in the apartment
    - num_rooms: Number of rooms in the apartment
    - selected_services: List of services selected for renovation

    :return: JSON response with the total renovation cost or error message
    """
    try:
        # Parse JSON input
        data = request.get_json()
        area = data.get('area')
        num_bathrooms = data.get('num_bathrooms')
        num_rooms = data.get('num_rooms')
        selected_services = data.get('selected_services')

        # Validate input
        if not all(isinstance(value, (int, float)) for value in [area, num_bathrooms, num_rooms]):
            return jsonify({"error": "Invalid input: area, num_bathrooms, and num_rooms must be numbers"}), 400

        if not isinstance(selected_services, list) or not all(isinstance(service, str) for service in selected_services):
            return jsonify({"error": "Invalid input: selected_services must be a list of strings"}), 400

        # Calculate total cost
        total_cost = calculate_cost(area, num_bathrooms, num_rooms, selected_services)

        # Return the result
        return jsonify({"total_cost": total_cost}), 200

    except Exception as e:
        # Log the error and return error response
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
