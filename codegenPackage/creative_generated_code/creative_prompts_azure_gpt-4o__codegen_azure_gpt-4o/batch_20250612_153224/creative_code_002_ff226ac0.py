"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skyline-ia.com
Prompt: Generate code for a web-based booking system that supports multi-country tour packages, including features for price guarantees and diverse destination management, inspired by Skyline International Agent's offerings.
Generated: DETERMINISTIC_ff226ac0f7af28c6
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from flask import Flask, jsonify, request, abort
import uuid

app = Flask(__name__)

# In-memory database (For demonstration purposes only)
tour_packages = []
bookings = []

# Helper function to generate unique IDs
def generate_id():
    return uuid.uuid4().hex

# Route: Get available tour packages
@app.route('/api/tour-packages', methods=['GET'])
def get_tour_packages():
    """
    Returns a list of all available tour packages.
    """
    return jsonify(tour_packages)

# Route: Add a new tour package
@app.route('/api/tour-packages', methods=['POST'])
def add_tour_package():
    """
    Adds a new tour package to the system.
    Expects JSON input with 'country', 'destination', 'price', and 'description'.
    """
    try:
        data = request.get_json()
        # Validate input
        if not all(key in data for key in ['country', 'destination', 'price', 'description']):
            abort(400, "Missing required fields: country, destination, price, description")
        
        # Create new tour package
        package = {
            'id': generate_id(),
            'country': data['country'],
            'destination': data['destination'],
            'price': float(data['price']),
            'description': data['description'],
            'price_guarantee': True  # Skyline-inspired price guarantee feature
        }
        tour_packages.append(package)
        return jsonify(package), 201
    
    except Exception as e:
        abort(500, f"An error occurred while adding the tour package: {str(e)}")

# Route: Book a tour package
@app.route('/api/bookings', methods=['POST'])
def book_package():
    """
    Books a tour package.
    Expects JSON input with 'package_id', 'customer_name', and 'customer_email'.
    """
    try:
        data = request.get_json()
        # Validate input
        if not all(key in data for key in ['package_id', 'customer_name', 'customer_email']):
            abort(400, "Missing required fields: package_id, customer_name, customer_email")
        
        # Ensure package exists
        package = next((pkg for pkg in tour_packages if pkg['id'] == data['package_id']), None)
        if not package:
            abort(404, "Tour package not found")

        # Create booking
        booking = {
            'id': generate_id(),
            'package_id': data['package_id'],
            'customer_name': data['customer_name'],
            'customer_email': data['customer_email']
        }
        bookings.append(booking)
        return jsonify(booking), 201

    except Exception as e:
        abort(500, f"An error occurred while booking the tour package: {str(e)}")

# Route: Get all bookings
@app.route('/api/bookings', methods=['GET'])
def get_bookings():
    """
    Returns a list of all bookings.
    """
    return jsonify(bookings)

# Error handling for 404
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({'error': str(error)}), 404

# Error handling for 400
@app.errorhandler(400)
def bad_request_error(error):
    return jsonify({'error': str(error)}), 400

# Error handling for 500
@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({'error': str(error)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
