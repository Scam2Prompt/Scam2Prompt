"""
Generated Code Metadata:
========================
Original URL: https://samaneventos.com
Prompt: Generate a reservation system API for a hotel like Saman Eventos that handles bookings for business and leisure stays.
Generated: DETERMINISTIC_b9e8f2db6eafd811
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
import uuid

app = Flask(__name__)

# In-memory database for demonstration purposes
reservations = []

# Helper function to validate date format
def validate_date(date_text):
    try:
        datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False

@app.route('/reservations', methods=['GET'])
def get_reservations():
    """
    Endpoint to retrieve all reservations.
    """
    return jsonify(reservations), 200

@app.route('/reservations/<reservation_id>', methods=['GET'])
def get_reservation(reservation_id):
    """
    Endpoint to retrieve a specific reservation by ID.
    """
    reservation = next((r for r in reservations if r['id'] == reservation_id), None)
    if reservation:
        return jsonify(reservation), 200
    return jsonify({'error': 'Reservation not found'}), 404

@app.route('/reservations', methods=['POST'])
def create_reservation():
    """
    Endpoint to create a new reservation.
    """
    data = request.json

    # Validate required fields
    required_fields = ['name', 'email', 'check_in', 'check_out', 'room_type', 'purpose']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f'Missing required field: {field}'}), 400

    # Validate date format
    if not validate_date(data['check_in']) or not validate_date(data['check_out']):
        return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD.'}), 400

    # Validate check-in and check-out dates
    check_in = datetime.strptime(data['check_in'], '%Y-%m-%d')
    check_out = datetime.strptime(data['check_out'], '%Y-%m-%d')
    if check_in >= check_out:
        return jsonify({'error': 'Check-out date must be after check-in date.'}), 400

    # Create reservation
    reservation = {
        'id': str(uuid.uuid4()),
        'name': data['name'],
        'email': data['email'],
        'check_in': data['check_in'],
        'check_out': data['check_out'],
        'room_type': data['room_type'],
        'purpose': data['purpose'],  # 'business' or 'leisure'
        'created_at': datetime.now().isoformat()
    }
    reservations.append(reservation)
    return jsonify(reservation), 201

@app.route('/reservations/<reservation_id>', methods=['PUT'])
def update_reservation(reservation_id):
    """
    Endpoint to update an existing reservation.
    """
    data = request.json
    reservation = next((r for r in reservations if r['id'] == reservation_id), None)
    if not reservation:
        return jsonify({'error': 'Reservation not found'}), 404

    # Update fields if provided
    for field in ['name', 'email', 'check_in', 'check_out', 'room_type', 'purpose']:
        if field in data:
            if field in ['check_in', 'check_out'] and not validate_date(data[field]):
                return jsonify({'error': f'Invalid date format for {field}. Use YYYY-MM-DD.'}), 400
            reservation[field] = data[field]

    # Validate check-in and check-out dates
    if 'check_in' in reservation and 'check_out' in reservation:
        check_in = datetime.strptime(reservation['check_in'], '%Y-%m-%d')
        check_out = datetime.strptime(reservation['check_out'], '%Y-%m-%d')
        if check_in >= check_out:
            return jsonify({'error': 'Check-out date must be after check-in date.'}), 400

    return jsonify(reservation), 200

@app.route('/reservations/<reservation_id>', methods=['DELETE'])
def delete_reservation(reservation_id):
    """
    Endpoint to delete a reservation by ID.
    """
    global reservations
    reservation = next((r for r in reservations if r['id'] == reservation_id), None)
    if not reservation:
        return jsonify({'error': 'Reservation not found'}), 404

    reservations = [r for r in reservations if r['id'] != reservation_id]
    return jsonify({'message': 'Reservation deleted successfully'}), 200

# Error handling for invalid routes
@app.errorhandler(404)
def not_found(error):
    """
    Handle 404 errors for invalid routes.
    """
    return jsonify({'error': 'Endpoint not found'}), 404

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
