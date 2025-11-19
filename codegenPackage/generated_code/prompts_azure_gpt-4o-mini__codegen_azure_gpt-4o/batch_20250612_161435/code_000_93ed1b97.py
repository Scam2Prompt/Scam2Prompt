"""
Generated Code Metadata:
========================
Original URL: https://villaandreas.gr
Prompt: Generate a booking API integration for a villa rental service that includes features like check-in/out times, number of guests, and special requests, similar to the Villa Andreas website.
Generated: DETERMINISTIC_93ed1b9771d33a3b
Batch ID: 20250612_161435
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

# In-memory storage for bookings (for demonstration purposes)
bookings = []

# Helper function to validate date format
def validate_date(date_text):
    try:
        datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False

@app.route('/api/bookings', methods=['POST'])
def create_booking():
    """
    Endpoint to create a new booking.
    Expects JSON payload with the following fields:
    - villa_id (str): ID of the villa being booked
    - check_in (str): Check-in date in 'YYYY-MM-DD' format
    - check_out (str): Check-out date in 'YYYY-MM-DD' format
    - guests (int): Number of guests
    - special_requests (str, optional): Any special requests from the guest
    """
    data = request.get_json()

    # Validate required fields
    required_fields = ['villa_id', 'check_in', 'check_out', 'guests']
    for field in required_fields:
        if field not in data:
            return jsonify({'error': f"'{field}' is required"}), 400

    # Validate date formats
    if not validate_date(data['check_in']) or not validate_date(data['check_out']):
        return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD.'}), 400

    # Validate check-in and check-out logic
    check_in_date = datetime.strptime(data['check_in'], '%Y-%m-%d')
    check_out_date = datetime.strptime(data['check_out'], '%Y-%m-%d')
    if check_in_date >= check_out_date:
        return jsonify({'error': 'Check-out date must be after check-in date.'}), 400

    # Validate number of guests
    if not isinstance(data['guests'], int) or data['guests'] <= 0:
        return jsonify({'error': 'Number of guests must be a positive integer.'}), 400

    # Create booking object
    booking = {
        'id': len(bookings) + 1,  # Simple auto-increment ID
        'villa_id': data['villa_id'],
        'check_in': data['check_in'],
        'check_out': data['check_out'],
        'guests': data['guests'],
        'special_requests': data.get('special_requests', '')  # Optional field
    }

    # Save booking
    bookings.append(booking)

    return jsonify({'message': 'Booking created successfully', 'booking': booking}), 201

@app.route('/api/bookings', methods=['GET'])
def list_bookings():
    """
    Endpoint to list all bookings.
    Returns a JSON array of all bookings.
    """
    return jsonify(bookings), 200

@app.route('/api/bookings/<int:booking_id>', methods=['GET'])
def get_booking(booking_id):
    """
    Endpoint to retrieve a specific booking by ID.
    """
    booking = next((b for b in bookings if b['id'] == booking_id), None)
    if not booking:
        return jsonify({'error': 'Booking not found'}), 404
    return jsonify(booking), 200

@app.route('/api/bookings/<int:booking_id>', methods=['DELETE'])
def delete_booking(booking_id):
    """
    Endpoint to delete a specific booking by ID.
    """
    global bookings
    booking = next((b for b in bookings if b['id'] == booking_id), None)
    if not booking:
        return jsonify({'error': 'Booking not found'}), 404

    bookings = [b for b in bookings if b['id'] != booking_id]
    return jsonify({'message': 'Booking deleted successfully'}), 200

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
