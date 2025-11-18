"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://malkeenz.com
Prompt: Create a REST API endpoint in Flask to handle custom jewelry orders, allowing users to specify attributes like ring size, plating type, and gemstone preferences.
Generated: DETERMINISTIC_b85b6637d1dd7efc
Batch ID: 20250612_154506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# Sample in-memory storage for orders (production systems should use a database)
orders = []
order_id_counter = 1

@app.route('/api/orders', methods=['POST'])
def create_order():
    """
    Endpoint to create a custom jewelry order.
    Accepts attributes like ring size, plating type, and gemstone preferences.
    """
    global order_id_counter
    
    # Parse and validate input data
    try:
        data = request.json
        if not data:
            raise BadRequest("Request body must be JSON formatted.")
        
        ring_size = data.get('ring_size')
        plating_type = data.get('plating_type')
        gemstone_preferences = data.get('gemstone_preferences')
        
        # Validate required fields
        if not ring_size or not plating_type or not gemstone_preferences:
            raise BadRequest("Missing required fields: ring_size, plating_type, gemstone_preferences.")
        
        # Validate ring size (example constraint)
        if not isinstance(ring_size, int) or ring_size < 4 or ring_size > 15:
            raise BadRequest("Invalid ring_size. Must be an integer between 4 and 15.")
        
        # Validate plating type (example constraint)
        valid_plating_types = ['gold', 'silver', 'platinum', 'rose gold']
        if plating_type.lower() not in valid_plating_types:
            raise BadRequest(f"Invalid plating_type. Must be one of: {', '.join(valid_plating_types)}.")
        
        # Validate gemstone preferences (example constraint)
        if not isinstance(gemstone_preferences, list) or len(gemstone_preferences) == 0:
            raise BadRequest("Invalid gemstone_preferences. Must be a non-empty list.")
        
        # Create the order
        order = {
            "order_id": order_id_counter,
            "ring_size": ring_size,
            "plating_type": plating_type.lower(),
            "gemstone_preferences": gemstone_preferences
        }
        orders.append(order)
        order_id_counter += 1
        
        # Return the created order
        return jsonify({
            "status": "success",
            "order": order
        }), 201
    except BadRequest as e:
        # Handle validation errors
        return jsonify({"status": "error", "message": str(e)}), 400
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"status": "error", "message": "Internal server error"}), 500

@app.route('/api/orders', methods=['GET'])
def list_orders():
    """
    Endpoint to list all custom jewelry orders.
    """
    return jsonify({
        "status": "success",
        "orders": orders
    }), 200

if __name__ == '__main__':
    # Only enable debug mode in development; not recommended for production
    app.run(debug=True)
```
