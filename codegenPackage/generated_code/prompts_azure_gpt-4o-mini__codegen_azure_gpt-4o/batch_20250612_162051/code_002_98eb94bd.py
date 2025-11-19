"""
Generated Code Metadata:
========================
Original URL: https://engaztop.com
Prompt: Create a sample API endpoint for a home services company that includes functionalities for booking water tank cleaning and thermal insulation services, reflecting the services provided by شركة انجاز.
Generated: DETERMINISTIC_98eb94bd342ff7ef
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory database simulation
services = [
    {"id": 1, "name": "Water Tank Cleaning"},
    {"id": 2, "name": "Thermal Insulation"}
]

bookings = []

# Helper function to validate service ID
def get_service_by_id(service_id):
    for service in services:
        if service["id"] == service_id:
            return service
    return None

@app.route('/services', methods=['GET'])
def list_services():
    """
    Endpoint to list all available services.
    """
    return jsonify({"services": services}), 200

@app.route('/book', methods=['POST'])
def book_service():
    """
    Endpoint to book a service.
    Request JSON format:
    {
        "service_id": int,
        "customer_name": str,
        "customer_phone": str,
        "appointment_date": str (YYYY-MM-DD)
    }
    """
    try:
        # Parse request data
        data = request.get_json()
        service_id = data.get("service_id")
        customer_name = data.get("customer_name")
        customer_phone = data.get("customer_phone")
        appointment_date = data.get("appointment_date")

        # Validate input
        if not service_id or not customer_name or not customer_phone or not appointment_date:
            return jsonify({"error": "Missing required fields"}), 400

        # Validate service ID
        service = get_service_by_id(service_id)
        if not service:
            return jsonify({"error": "Invalid service ID"}), 404

        # Validate appointment date format
        try:
            appointment_date_obj = datetime.strptime(appointment_date, "%Y-%m-%d")
        except ValueError:
            return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400

        # Create booking
        booking = {
            "id": len(bookings) + 1,
            "service_id": service_id,
            "service_name": service["name"],
            "customer_name": customer_name,
            "customer_phone": customer_phone,
            "appointment_date": appointment_date_obj.strftime("%Y-%m-%d")
        }
        bookings.append(booking)

        return jsonify({"message": "Booking successful", "booking": booking}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred", "details": str(e)}), 500

@app.route('/bookings', methods=['GET'])
def list_bookings():
    """
    Endpoint to list all bookings.
    """
    return jsonify({"bookings": bookings}), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
