"""
Generated Code Metadata:
========================
Original URL: https://villaandreas.gr
Prompt: "Create a RESTful API endpoint to handle villa reservations, including parameters for arrival and departure dates, number of guests, and villa ID, similar to the reservation system on villaandreas.gr."
Generated: DETERMINISTIC_ca07c4ed7833c657
Batch ID: 20250622_212318
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

# In-memory storage for reservations (for demonstration purposes)
reservations = []

# Helper function to validate date format
def validate_date(date_string):
    try:
        datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False

# Helper function to check for overlapping reservations
def is_overlapping(villa_id, arrival_date, departure_date):
    for reservation in reservations:
        if reservation['villa_id'] == villa_id:
            if not (departure_date <= reservation['arrival_date'] or arrival_date >= reservation['departure_date']):
                return True
    return False

@app.route('/api/reservations', methods=['POST'])
def create_reservation():
    """
    Endpoint to create a villa reservation.
    Expects JSON payload with the following fields:
    - villa_id (int): ID of the villa to reserve
    - arrival_date (str): Arrival date in 'YYYY-MM-DD' format
    - departure_date (str): Departure date in 'YYYY-MM-DD' format
    - guests (int): Number of guests
    """
    try:
        # Parse and validate input data
        data = request.get_json()
        villa_id = data.get('villa_id')
        arrival_date = data.get('arrival_date')
        departure_date = data.get('departure_date')
        guests = data.get('guests')

        if not villa_id or not arrival_date or not departure_date or not guests:
            return jsonify({'error': 'Missing required fields'}), 400

        if not validate_date(arrival_date) or not validate_date(departure_date):
            return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD.'}), 400

        arrival_date = datetime.strptime(arrival_date, '%Y-%m-%d').date()
        departure_date = datetime.strptime(departure_date, '%Y-%m-%d').date()

        if arrival_date >= departure_date:
            return jsonify({'error': 'Arrival date must be before departure date.'}), 400

        if guests <= 0:
            return jsonify({'error': 'Number of guests must be greater than zero.'}), 400

        # Check for overlapping reservations
        if is_overlapping(villa_id, arrival_date, departure_date):
            return jsonify({'error': 'Reservation dates overlap with an existing reservation.'}), 409

        # Create reservation
        reservation = {
            'villa_id': villa_id,
            'arrival_date': arrival_date,
            'departure_date': departure_date,
            'guests': guests
        }
        reservations.append(reservation)

        return jsonify({'message': 'Reservation created successfully', 'reservation': reservation}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': 'An error occurred', 'details': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
