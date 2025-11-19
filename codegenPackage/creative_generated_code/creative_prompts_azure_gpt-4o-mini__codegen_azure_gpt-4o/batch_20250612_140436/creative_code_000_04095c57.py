"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yaisatangwell.com
Prompt: Generate a code snippet for a web application that allows users to book wedding photography services in Trinidad and Tobago, similar to Yaisa Tangwell's offerings.
Generated: DETERMINISTIC_04095c570eaa35e7
Batch ID: 20250612_140436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)

# Simulated database for bookings
bookings = []

def is_date_available(date):
    """Check if the requested date is available for booking."""
    for booking in bookings:
        if booking['date'] == date:
            return False
    return True

@app.route('/book', methods=['POST'])
def book_photography_service():
    """
    Endpoint for booking wedding photography services.
    Accepts JSON data with 'name', 'email', and 'date'.
    Returns success or error message.
    """
    try:
        # Parse incoming JSON request
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        date = data.get('date')

        # Validate input
        if not name or not email or not date:
            return jsonify({'error': 'Missing required fields: name, email, or date'}), 400

        # Ensure date format is valid
        try:
            booking_date = datetime.datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD.'}), 400

        # Check availability
        if not is_date_available(date):
            return jsonify({'error': 'Requested date is not available.'}), 400

        # Save booking
        new_booking = {
            'name': name,
            'email': email,
            'date': date
        }
        bookings.append(new_booking)

        return jsonify({'message': 'Booking confirmed!', 'booking': new_booking}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': f'An unexpected error occurred: {str(e)}'}), 500

@app.route('/availability/<date>', methods=['GET'])
def check_availability(date):
    """
    Endpoint for checking availability for a specific date.
    Returns available or unavailable.
    """
    try:
        # Ensure date format is valid
        try:
            datetime.datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD.'}), 400

        # Check availability
        available = is_date_available(date)
        return jsonify({'date': date, 'available': available}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': f'An unexpected error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
