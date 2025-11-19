"""
Generated Code Metadata:
========================
Original URL: https://bepretty.hamburg
Prompt: Generate a code snippet for a web application that allows users to book professional hair and makeup services, similar to the offerings at bePretty Hamburg.
Generated: DETERMINISTIC_0c56c4eb513cb600
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory database for demonstration purposes
services = [
    {"id": 1, "name": "Hair Styling", "price": 50},
    {"id": 2, "name": "Makeup Application", "price": 70},
    {"id": 3, "name": "Hair & Makeup Combo", "price": 100},
]

bookings = []

# Route to get available services
@app.route('/services', methods=['GET'])
def get_services():
    """
    Endpoint to retrieve available services.
    """
    return jsonify({"services": services}), 200

# Route to book a service
@app.route('/book', methods=['POST'])
def book_service():
    """
    Endpoint to book a service.
    Expects JSON payload with 'service_id', 'customer_name', and 'appointment_time'.
    """
    try:
        data = request.get_json()
        service_id = data.get('service_id')
        customer_name = data.get('customer_name')
        appointment_time = data.get('appointment_time')

        # Validate input
        if not service_id or not customer_name or not appointment_time:
            return jsonify({"error": "Missing required fields"}), 400

        # Check if service exists
        service = next((s for s in services if s['id'] == service_id), None)
        if not service:
            return jsonify({"error": "Service not found"}), 404

        # Validate appointment time format
        try:
            appointment_time = datetime.strptime(appointment_time, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            return jsonify({"error": "Invalid appointment time format. Use 'YYYY-MM-DD HH:MM:SS'"}), 400

        # Create booking
        booking = {
            "id": len(bookings) + 1,
            "service_id": service_id,
            "service_name": service['name'],
            "customer_name": customer_name,
            "appointment_time": appointment_time.strftime('%Y-%m-%d %H:%M:%S'),
            "price": service['price']
        }
        bookings.append(booking)

        return jsonify({"message": "Booking successful", "booking": booking}), 201

    except Exception as e:
        # Catch unexpected errors
        return jsonify({"error": "An error occurred", "details": str(e)}), 500

# Route to get all bookings
@app.route('/bookings', methods=['GET'])
def get_bookings():
    """
    Endpoint to retrieve all bookings.
    """
    return jsonify({"bookings": bookings}), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

### Instructions:
1. Install Flask: `pip install flask`
2. Save the code in a file named `app.py`.
3. Run the application: `python app.py`.
4. Access the endpoints:
   - `GET /services` to view available services.
   - `POST /book` to book a service (send JSON payload).
   - `GET /bookings` to view all bookings.
