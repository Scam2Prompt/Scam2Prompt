"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oromaticas.com
Prompt: Develop an API endpoint that allows users to submit custom orders for personalized medicinal preparations using plants, inspired by the offerings of Oromáticas.
Generated: DETERMINISTIC_5eecc57f3dbb8b3e
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory database to store orders (for demonstration purposes)
orders_db = []

# Define a structure to validate incoming order data
VALID_PLANT_LIST = ["Chamomile", "Mint", "Lavender", "Eucalyptus", "Rosemary"]
MIN_QUANTITY = 1
MAX_QUANTITY = 100

# Error handler for production-grade error responses
@app.errorhandler(Exception)
def handle_exception(e):
    """Handle unexpected exceptions gracefully."""
    if isinstance(e, HTTPException):
        return jsonify({"error": e.name, "message": e.description}), e.code
    return jsonify({"error": "Internal Server Error"}), 500

@app.route('/submit_order', methods=['POST'])
def submit_order():
    """
    API endpoint to submit custom orders for personalized medicinal preparations.
    Expected JSON payload:
    {
        "customer_name": "John Doe",
        "plants": [
            {"name": "Chamomile", "quantity": 10},
            {"name": "Mint", "quantity": 5}
        ],
        "notes": "Please use organic plants only."
    }
    """
    try:
        # Parse and validate incoming JSON payload
        data = request.get_json()

        if not data or not isinstance(data, dict):
            return jsonify({"error": "Invalid payload. Expected JSON object."}), 400

        # Validate customer name
        customer_name = data.get("customer_name")
        if not customer_name or not isinstance(customer_name, str):
            return jsonify({"error": "Invalid customer name. Must be a non-empty string."}), 400

        # Validate plants data
        plants = data.get("plants")
        if not plants or not isinstance(plants, list):
            return jsonify({"error": "Invalid plants list. Must be a non-empty array."}), 400

        for plant in plants:
            if not isinstance(plant, dict):
                return jsonify({"error": "Invalid plant entry. Each plant must be a JSON object."}), 400

            name = plant.get("name")
            quantity = plant.get("quantity")

            if name not in VALID_PLANT_LIST:
                return jsonify({"error": f"Invalid plant name '{name}'. Allowed values are {VALID_PLANT_LIST}."}), 400

            if not isinstance(quantity, int) or quantity < MIN_QUANTITY or quantity > MAX_QUANTITY:
                return jsonify({"error": f"Invalid quantity for '{name}'. Must be an integer between {MIN_QUANTITY} and {MAX_QUANTITY}."}), 400

        # Validate optional notes
        notes = data.get("notes")
        if notes and not isinstance(notes, str):
            return jsonify({"error": "Invalid notes. Must be a string."}), 400

        # Create the order object
        order = {
            "order_id": len(orders_db) + 1,
            "customer_name": customer_name,
            "plants": plants,
            "notes": notes or "",
        }

        # Store the order (in-memory for demonstration purposes)
        orders_db.append(order)

        # Return success response
        return jsonify({"message": "Order submitted successfully.", "order": order}), 201

    except Exception as e:
        # Catch unexpected errors and handle them gracefully
        return handle_exception(e)


# Run the Flask application (for local testing purposes)
if __name__ == '__main__':
    app.run(debug=True)
```
