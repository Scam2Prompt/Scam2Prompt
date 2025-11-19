"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.tubellaesteticaduepuntozero.it
Prompt: Suggest an API that can help beauty centers manage customer bookings and inquiries, similar to the services offered by TuBella Estetica 2.0.
Generated: DETERMINISTIC_bf7bcf02de73ee68
Batch ID: 20250612_164049
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: beauty_center_api.py

from flask import Flask, request, jsonify
from datetime import datetime
import uuid

app = Flask(__name__)

# In-memory database for demonstration purposes
customers = {}
bookings = {}

# Helper function to generate unique IDs
def generate_id():
    return str(uuid.uuid4())

# Error response helper function
def error_response(message, status_code=400):
    return jsonify({"success": False, "error": message}), status_code

# Endpoint: Add a new customer
@app.route('/customers', methods=['POST'])
def add_customer():
    """
    Adds a new customer to the system.
    Request JSON should contain:
    - name (string): Full name of the customer
    - email (string): Email address of the customer
    - phone (string): Phone number of the customer
    """
    try:
        data = request.json
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')

        # Validate input
        if not name or not email or not phone:
            return error_response("Missing required fields: name, email, or phone.")

        customer_id = generate_id()
        customers[customer_id] = {
            "id": customer_id,
            "name": name,
            "email": email,
            "phone": phone
        }

        return jsonify({"success": True, "customer": customers[customer_id]}), 201
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}")

# Endpoint: Create a new booking
@app.route('/bookings', methods=['POST'])
def create_booking():
    """
    Creates a new booking for a customer.
    Request JSON should contain:
    - customer_id (string): ID of the existing customer
    - date (string): Date of the booking in YYYY-MM-DD format
    - time (string): Time of the booking in HH:MM format (24-hour clock)
    - service (string): Description of the beauty service
    """
    try:
        data = request.json
        customer_id = data.get('customer_id')
        date = data.get('date')
        time = data.get('time')
        service = data.get('service')

        # Validate input
        if not customer_id or not date or not time or not service:
            return error_response("Missing required fields: customer_id, date, time, or service.")
        if customer_id not in customers:
            return error_response("Invalid customer_id. Customer does not exist.")

        # Validate date and time format
        try:
            datetime.strptime(date, "%Y-%m-%d")
            datetime.strptime(time, "%H:%M")
        except ValueError:
            return error_response("Invalid date or time format.")

        booking_id = generate_id()
        bookings[booking_id] = {
            "id": booking_id,
            "customer_id": customer_id,
            "date": date,
            "time": time,
            "service": service
        }

        return jsonify({"success": True, "booking": bookings[booking_id]}), 201
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}")

# Endpoint: List all bookings for a customer
@app.route('/customers/<customer_id>/bookings', methods=['GET'])
def get_customer_bookings(customer_id):
    """
    Retrieves all bookings for a specific customer.
    Path parameter:
    - customer_id (string): ID of the customer
    """
    try:
        if customer_id not in customers:
            return error_response("Invalid customer_id. Customer does not exist.")

        customer_bookings = [booking for booking in bookings.values() if booking['customer_id'] == customer_id]
        return jsonify({"success": True, "bookings": customer_bookings}), 200
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}")

# Endpoint: General inquiry
@app.route('/inquiries', methods=['POST'])
def create_inquiry():
    """
    Records a general inquiry from a customer or potential customer.
    Request JSON should contain:
    - name (string): Full name of the individual making the inquiry
    - email (string): Email address of the individual making the inquiry
    - message (string): Inquiry message or details
    """
    try:
        data = request.json
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')

        # Validate input
        if not name or not email or not message:
            return error_response("Missing required fields: name, email, or message.")

        inquiry_id = generate_id()
        inquiry = {
            "id": inquiry_id,
            "name": name,
            "email": email,
            "message": message,
            "created_at": datetime.now().isoformat()
        }

        return jsonify({"success": True, "inquiry": inquiry}), 201
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}")

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

This code implements a basic API for managing customer bookings and inquiries for a beauty center. It uses Flask, a popular Python web framework, and adheres to best practices for API development.
