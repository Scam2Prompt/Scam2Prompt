"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.vracarbvk.rs
Prompt: Develop a RESTful API endpoint for managing reservations at Vila Vračar, ensuring it includes features for checking availability and confirming bookings.
Generated: DETERMINISTIC_979eec2ed0fa8055
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

app = Flask(__name__)

# In-memory database for storing reservations (for simplicity)
reservations = []

# Utility function to check availability
def is_available(start_date, end_date):
    for reservation in reservations:
        if not (end_date < reservation['start_date'] or start_date > reservation['end_date']):
            return False
    return True

@app.route('/reservations/check', methods=['POST'])
def check_availability():
    """
    Endpoint to check availability for a date range.

    Request JSON Format:
    {
        "start_date": "YYYY-MM-DD",
        "end_date": "YYYY-MM-DD"
    }

    Response JSON Format:
    {
        "available": true/false
    }
    """
    try:
        data = request.get_json()
        start_date = datetime.strptime(data['start_date'], "%Y-%m-%d").date()
        end_date = datetime.strptime(data['end_date'], "%Y-%m-%d").date()
        
        # Validate date range
        if start_date > end_date:
            return jsonify({"error": "start_date must be before end_date"}), 400

        available = is_available(start_date, end_date)
        return jsonify({"available": available}), 200

    except (KeyError, ValueError) as e:
        return jsonify({"error": "Invalid request format or date values"}), 400

@app.route('/reservations/book', methods=['POST'])
def book_reservation():
    """
    Endpoint to confirm a reservation.

    Request JSON Format:
    {
        "start_date": "YYYY-MM-DD",
        "end_date": "YYYY-MM-DD",
        "customer_name": "string",
        "contact_info": "string"
    }

    Response JSON Format:
    {
        "success": true/false,
        "message": "string"
    }
    """
    try:
        data = request.get_json()
        start_date = datetime.strptime(data['start_date'], "%Y-%m-%d").date()
        end_date = datetime.strptime(data['end_date'], "%Y-%m-%d").date()
        customer_name = data['customer_name']
        contact_info = data['contact_info']

        # Validate date range
        if start_date > end_date:
            return jsonify({"success": False, "message": "start_date must be before end_date"}), 400

        # Check availability
        if not is_available(start_date, end_date):
            return jsonify({"success": False, "message": "The requested date range is not available"}), 409

        # Create reservation
        reservation = {
            "start_date": start_date,
            "end_date": end_date,
            "customer_name": customer_name,
            "contact_info": contact_info
        }
        reservations.append(reservation)

        return jsonify({"success": True, "message": "Reservation confirmed"}), 201

    except (KeyError, ValueError) as e:
        return jsonify({"success": False, "message": "Invalid request format or data values"}), 400

@app.route('/reservations', methods=['GET'])
def get_reservations():
    """
    Endpoint to retrieve all reservations.

    Response JSON Format:
    [
        {
            "start_date": "YYYY-MM-DD",
            "end_date": "YYYY-MM-DD",
            "customer_name": "string",
            "contact_info": "string"
        }
    ]
    """
    try:
        # Serialize reservations for output
        serialized_reservations = [
            {
                "start_date": str(reservation["start_date"]),
                "end_date": str(reservation["end_date"]),
                "customer_name": reservation["customer_name"],
                "contact_info": reservation["contact_info"]
            }
            for reservation in reservations
        ]
        return jsonify(serialized_reservations), 200

    except Exception as e:
        return jsonify({"error": "An error occurred while retrieving reservations"}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
