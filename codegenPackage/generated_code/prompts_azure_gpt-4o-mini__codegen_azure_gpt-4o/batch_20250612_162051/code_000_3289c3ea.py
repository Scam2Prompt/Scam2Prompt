"""
Generated Code Metadata:
========================
Original URL: https://aluivars.com
Prompt: Generate a code snippet for a web application that allows users to request quotes for iron and aluminum carpentry services, similar to those offered by Aluivars.
Generated: DETERMINISTIC_3289c3ea9602be5e
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Sample data for services and pricing (could be replaced with a database in production)
SERVICES = {
    "iron_carpentry": {
        "description": "Custom iron carpentry services for gates, railings, and more.",
        "base_price_per_unit": 50  # Example price per unit
    },
    "aluminum_carpentry": {
        "description": "Custom aluminum carpentry services for windows, doors, and more.",
        "base_price_per_unit": 70  # Example price per unit
    }
}

# Route to get available services
@app.route('/services', methods=['GET'])
def get_services():
    """
    Endpoint to retrieve available carpentry services.
    """
    return jsonify(SERVICES), 200

# Route to request a quote
@app.route('/request-quote', methods=['POST'])
def request_quote():
    """
    Endpoint to request a quote for carpentry services.
    Expects JSON payload with 'service_type' and 'quantity'.
    """
    try:
        # Parse the incoming JSON request
        data = request.get_json()
        service_type = data.get('service_type')
        quantity = data.get('quantity')

        # Validate input
        if not service_type or service_type not in SERVICES:
            return jsonify({"error": "Invalid or missing 'service_type'."}), 400
        if not quantity or not isinstance(quantity, int) or quantity <= 0:
            return jsonify({"error": "Invalid or missing 'quantity'. Must be a positive integer."}), 400

        # Calculate the quote
        base_price = SERVICES[service_type]['base_price_per_unit']
        total_price = base_price * quantity

        # Return the quote
        return jsonify({
            "service_type": service_type,
            "quantity": quantity,
            "unit_price": base_price,
            "total_price": total_price
        }), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred while processing your request.", "details": str(e)}), 500

# Route to handle 404 errors
@app.errorhandler(404)
def not_found(error):
    """
    Custom handler for 404 errors.
    """
    return jsonify({"error": "Endpoint not found."}), 404

# Main entry point to run the application
if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)  # Set debug=False in production
```
