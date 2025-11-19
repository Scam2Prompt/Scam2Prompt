"""
Generated Code Metadata:
========================
Original URL: https://budibromotour.ilmaweb.com
Prompt: Design a RESTful API to manage Budi Bromo Tour's services, including booking, payment, and customer management.
Generated: DETERMINISTIC_9ed2a3810ae8ae12
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory data storage (for demonstration purposes)
services = [
    {"id": 1, "name": "Mount Bromo Sunrise Tour", "price": 100},
    {"id": 2, "name": "Mount Bromo Jeep Adventure", "price": 150},
]
bookings = []
customers = []

# Error handling middleware
@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return jsonify({"error": e.description}), e.code
    return jsonify({"error": "Internal Server Error"}), 500

# Route: Get all services
@app.route('/services', methods=['GET'])
def get_services():
    """
    Fetch all available services.
    """
    return jsonify(services), 200

# Route: Create a new booking
@app.route('/bookings', methods=['POST'])
def create_booking():
    """
    Create a new booking.
    Request body should include:
    - customer_id
    - service_id
    """
    data = request.get_json()
    customer_id = data.get('customer_id')
    service_id = data.get('service_id')

    # Validate input
    if not customer_id or not service_id:
        return jsonify({"error": "customer_id and service_id are required"}), 400

    # Check if service exists
    service = next((s for s in services if s['id'] == service_id), None)
    if not service:
        return jsonify({"error": "Service not found"}), 404

    # Create booking
    booking_id = len(bookings) + 1
    booking = {
        "id": booking_id,
        "customer_id": customer_id,
        "service_id": service_id,
        "status": "Pending",
    }
    bookings.append(booking)
    return jsonify(booking), 201

# Route: Get all bookings
@app.route('/bookings', methods=['GET'])
def get_bookings():
    """
    Fetch all bookings.
    """
    return jsonify(bookings), 200

# Route: Create a new customer
@app.route('/customers', methods=['POST'])
def create_customer():
    """
    Create a new customer.
    Request body should include:
    - name
    - email
    """
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')

    # Validate input
    if not name or not email:
        return jsonify({"error": "name and email are required"}), 400

    # Create customer
    customer_id = len(customers) + 1
    customer = {
        "id": customer_id,
        "name": name,
        "email": email,
    }
    customers.append(customer)
    return jsonify(customer), 201

# Route: Get all customers
@app.route('/customers', methods=['GET'])
def get_customers():
    """
    Fetch all customers.
    """
    return jsonify(customers), 200

# Route: Process payment for a booking
@app.route('/payments', methods=['POST'])
def process_payment():
    """
    Process payment for a booking.
    Request body should include:
    - booking_id
    """
    data = request.get_json()
    booking_id = data.get('booking_id')

    # Validate input
    if not booking_id:
        return jsonify({"error": "booking_id is required"}), 400

    # Check if booking exists
    booking = next((b for b in bookings if b['id'] == booking_id), None)
    if not booking:
        return jsonify({"error": "Booking not found"}), 404

    # Update booking status
    booking['status'] = 'Paid'
    return jsonify({"message": "Payment processed successfully", "booking": booking}), 200

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
