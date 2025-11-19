"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.merchandiso.com
Prompt: Generate a code snippet for an API that allows users to customize and order promotional souvenirs like tumblers and notebooks from Merchandiso.
Generated: DETERMINISTIC_7f07cb9aa24c1fdc
Batch ID: 20250612_160720
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

# Mock database for storing orders
orders = []

# Endpoint to customize and order promotional souvenirs
@app.route('/api/order', methods=['POST'])
def create_order():
    """
    API for creating a promotional souvenir order.
    Accepts POST requests with customization details.
    """
    try:
        # Parse JSON request data
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid request, JSON data is required'}), 400

        # Validate required fields
        required_fields = ['item_type', 'quantity', 'customization']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'Missing required field: {field}'}), 400

        # Extract fields from request
        item_type = data['item_type']
        quantity = data['quantity']
        customization = data['customization']

        # Input validation
        if item_type not in ['tumbler', 'notebook']:
            return jsonify({'error': 'Invalid item type. Allowed types: tumbler, notebook'}), 400
        if not isinstance(quantity, int) or quantity <= 0:
            return jsonify({'error': 'Quantity must be a positive integer'}), 400
        if not isinstance(customization, dict) or not customization:
            return jsonify({'error': 'Customization must be a non-empty dictionary'}), 400

        # Create order object
        order_id = len(orders) + 1
        order = {
            'order_id': order_id,
            'item_type': item_type,
            'quantity': quantity,
            'customization': customization
        }

        # Store order in mock database
        orders.append(order)

        # Return success response
        return jsonify({
            'message': 'Order created successfully',
            'order': order
        }), 201

    except Exception as e:
        # Handle unexpected errors with proper logging
        app.logger.error(f'Error creating order: {e}')
        return jsonify({'error': 'An unexpected error occurred'}), 500


# Endpoint to retrieve all orders
@app.route('/api/orders', methods=['GET'])
def get_orders():
    """
    API for retrieving all orders.
    """
    return jsonify({'orders': orders}), 200


# Custom error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """
    Custom error handler for HTTP exceptions.
    """
    response = e.get_response()
    response.data = jsonify({'error': e.description}).data
    response.content_type = 'application/json'
    return response


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
