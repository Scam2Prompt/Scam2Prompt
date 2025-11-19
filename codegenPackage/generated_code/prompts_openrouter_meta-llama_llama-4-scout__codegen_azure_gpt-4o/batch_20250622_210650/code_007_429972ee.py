"""
Generated Code Metadata:
========================
Original URL: https://birlikjenerator.com
Prompt: "Design a RESTful API for managing generator rentals, including endpoints for booking, payment, and maintenance scheduling."
Generated: DETERMINISTIC_429972eed83cd15e
Batch ID: 20250622_210650
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

# In-memory database for simplicity (use a real database in production)
generators = [
    {"id": 1, "name": "Generator A", "status": "available"},
    {"id": 2, "name": "Generator B", "status": "available"},
]
bookings = []
payments = []
maintenance_schedule = []

# Helper function to find a generator by ID
def find_generator(generator_id):
    return next((g for g in generators if g["id"] == generator_id), None)

# Endpoint: List all generators
@app.route('/generators', methods=['GET'])
def list_generators():
    return jsonify(generators), 200

# Endpoint: Book a generator
@app.route('/bookings', methods=['POST'])
def book_generator():
    try:
        data = request.json
        generator_id = data.get("generator_id")
        customer_name = data.get("customer_name")
        rental_date = data.get("rental_date")

        # Validate input
        if not generator_id or not customer_name or not rental_date:
            return jsonify({"error": "Missing required fields"}), 400

        generator = find_generator(generator_id)
        if not generator:
            return jsonify({"error": "Generator not found"}), 404

        if generator["status"] != "available":
            return jsonify({"error": "Generator is not available"}), 400

        # Book the generator
        booking = {
            "id": len(bookings) + 1,
            "generator_id": generator_id,
            "customer_name": customer_name,
            "rental_date": rental_date,
        }
        bookings.append(booking)
        generator["status"] = "booked"

        return jsonify(booking), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint: Make a payment
@app.route('/payments', methods=['POST'])
def make_payment():
    try:
        data = request.json
        booking_id = data.get("booking_id")
        amount = data.get("amount")

        # Validate input
        if not booking_id or not amount:
            return jsonify({"error": "Missing required fields"}), 400

        booking = next((b for b in bookings if b["id"] == booking_id), None)
        if not booking:
            return jsonify({"error": "Booking not found"}), 404

        # Record the payment
        payment = {
            "id": len(payments) + 1,
            "booking_id": booking_id,
            "amount": amount,
            "date": datetime.now().isoformat(),
        }
        payments.append(payment)

        return jsonify(payment), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint: Schedule maintenance
@app.route('/maintenance', methods=['POST'])
def schedule_maintenance():
    try:
        data = request.json
        generator_id = data.get("generator_id")
        maintenance_date = data.get("maintenance_date")

        # Validate input
        if not generator_id or not maintenance_date:
            return jsonify({"error": "Missing required fields"}), 400

        generator = find_generator(generator_id)
        if not generator:
            return jsonify({"error": "Generator not found"}), 404

        # Schedule maintenance
        maintenance = {
            "id": len(maintenance_schedule) + 1,
            "generator_id": generator_id,
            "maintenance_date": maintenance_date,
        }
        maintenance_schedule.append(maintenance)
        generator["status"] = "maintenance"

        return jsonify(maintenance), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint: List all bookings
@app.route('/bookings', methods=['GET'])
def list_bookings():
    return jsonify(bookings), 200

# Endpoint: List all payments
@app.route('/payments', methods=['GET'])
def list_payments():
    return jsonify(payments), 200

# Endpoint: List all maintenance schedules
@app.route('/maintenance', methods=['GET'])
def list_maintenance():
    return jsonify(maintenance_schedule), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
