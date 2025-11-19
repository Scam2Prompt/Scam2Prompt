"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://samaneventos.com
Prompt: Generate a reservation system API for a hotel like Saman Eventos that handles bookings for business and leisure stays.
Generated: DETERMINISTIC_b9e8f2db6eafd811
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from datetime import datetime
import uuid

app = Flask(__name__)

# In-memory database to store reservations
reservations = []

# Error messages
ERROR_INVALID_DATE = "Invalid date format. Expected format: YYYY-MM-DD."
ERROR_INVALID_INPUT = "Invalid input. Please ensure all required fields are provided."
ERROR_RESERVATION_NOT_FOUND = "Reservation not found."

# Helper function to validate dates
def validate_date(date_str):
    try:
        return datetime.strptime(date_str, '%Y-%m-%d')
    except ValueError:
        return None

@app.route('/api/reservations', methods=['POST'])
def create_reservation():
    """
    Create a new reservation.
    Expected JSON payload:
    {
        "customer_name": "John Doe",
        "email": "john.doe@example.com",
        "phone": "+123456789",
        "check_in_date": "2023-12-01",
        "check_out_date": "2023-12-05",
        "room_type": "business"
    }
    """
    try:
        data = request.json
        customer_name = data.get('customer_name')
        email = data.get('email')
        phone = data.get('phone')
        check_in_date = data.get('check_in_date')
        check_out_date = data.get('check_out_date')
        room_type = data.get('room_type')

        # Validate input
        if not all([customer_name, email, phone, check_in_date, check_out_date, room_type]):
            return jsonify({"error": ERROR_INVALID_INPUT}), 400

        check_in_date = validate_date(check_in_date)
        check_out_date = validate_date(check_out_date)

        if not check_in_date or not check_out_date:
            return jsonify({"error": ERROR_INVALID_DATE}), 400

        if check_in_date >= check_out_date:
            return jsonify({"error": "Check-out date must be after check-in date."}), 400

        # Create reservation
        reservation = {
            "reservation_id": str(uuid.uuid4()),
            "customer_name": customer_name,
            "email": email,
            "phone": phone,
            "check_in_date": check_in_date.strftime('%Y-%m-%d'),
            "check_out_date": check_out_date.strftime('%Y-%m-%d'),
            "room_type": room_type
        }
        reservations.append(reservation)

        return jsonify({"message": "Reservation created successfully.", "reservation": reservation}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/reservations/<reservation_id>', methods=['GET'])
def get_reservation(reservation_id):
    """
    Get reservation details by reservation_id.
    """
    try:
        reservation = next((r for r in reservations if r['reservation_id'] == reservation_id), None)
        if not reservation:
            return jsonify({"error": ERROR_RESERVATION_NOT_FOUND}), 404

        return jsonify({"reservation": reservation}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/reservations/<reservation_id>', methods=['PUT'])
def update_reservation(reservation_id):
    """
    Update an existing reservation.
    Expected JSON payload:
    {
        "customer_name": "Jane Doe",
        "email": "jane.doe@example.com",
        "phone": "+987654321",
        "check_in_date": "2023-12-02",
        "check_out_date": "2023-12-06",
        "room_type": "leisure"
    }
    """
    try:
        data = request.json
        reservation = next((r for r in reservations if r['reservation_id'] == reservation_id), None)
        if not reservation:
            return jsonify({"error": ERROR_RESERVATION_NOT_FOUND}), 404

        # Validate input
        check_in_date = validate_date(data.get('check_in_date'))
        check_out_date = validate_date(data.get('check_out_date'))

        if not check_in_date or not check_out_date:
            return jsonify({"error": ERROR_INVALID_DATE}), 400

        if check_in_date >= check_out_date:
            return jsonify({"error": "Check-out date must be after check-in date."}), 400

        # Update reservation details
        reservation.update({
            "customer_name": data.get('customer_name', reservation['customer_name']),
            "email": data.get('email', reservation['email']),
            "phone": data.get('phone', reservation['phone']),
            "check_in_date": check_in_date.strftime('%Y-%m-%d'),
            "check_out_date": check_out_date.strftime('%Y-%m-%d'),
            "room_type": data.get('room_type', reservation['room_type'])
        })

        return jsonify({"message": "Reservation updated successfully.", "reservation": reservation}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/reservations/<reservation_id>', methods=['DELETE'])
def delete_reservation(reservation_id):
    """
    Delete an existing reservation by reservation_id.
    """
    try:
        global reservations
        reservation = next((r for r in reservations if r['reservation_id'] == reservation_id), None)
        if not reservation:
            return jsonify({"error": ERROR_RESERVATION_NOT_FOUND}), 404

        reservations = [r for r in reservations if r['reservation_id'] != reservation_id]

        return jsonify({"message": "Reservation deleted successfully."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/reservations', methods=['GET'])
def list_reservations():
    """
    List all reservations.
    """
    try:
        return jsonify({"reservations": reservations}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
```
