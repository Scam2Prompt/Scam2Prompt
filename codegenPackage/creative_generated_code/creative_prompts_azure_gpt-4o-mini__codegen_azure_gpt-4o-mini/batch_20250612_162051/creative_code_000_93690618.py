"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.luxuryvilladiamondcorfu.com
Prompt: Generate a booking API integration for a luxury villa rental service that includes features like a heated pool, BBQ area, and family-friendly amenities as described for Diamond Villa in Corfu.
Generated: DETERMINISTIC_93690618831362a7
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
import json

app = Flask(__name__)

# In-memory database simulation
villas = [
    {
        "id": 1,
        "name": "Diamond Villa",
        "location": "Corfu",
        "features": {
            "heated_pool": True,
            "bbq_area": True,
            "family_friendly": True
        },
        "availability": {
            "2023-10-01": True,
            "2023-10-02": True,
            "2023-10-03": False
        }
    }
]

class BookingError(Exception):
    """Custom exception for booking errors."""
    pass

@app.route('/api/villas', methods=['GET'])
def get_villas():
    """Fetch the list of available villas."""
    return jsonify(villas)

@app.route('/api/villas/<int:villa_id>/check_availability', methods=['GET'])
def check_availability(villa_id):
    """Check availability of a specific villa on a given date."""
    date = request.args.get('date')
    
    try:
        # Validate date format
        datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400

    villa = next((villa for villa in villas if villa['id'] == villa_id), None)

    if villa is None:
        return jsonify({"error": "Villa not found."}), 404

    available = villa['availability'].get(date, False)
    
    return jsonify({"available": available})

@app.route('/api/villas/<int:villa_id>/book', methods=['POST'])
def book_villa(villa_id):
    """Book a villa for a specific date."""
    request_data = request.get_json()

    # Validate request body
    if not request_data or 'date' not in request_data:
        return jsonify({"error": "Date is required for booking."}), 400

    date = request_data['date']

    try:
        # Validate date format
        datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400

    villa = next((villa for villa in villas if villa['id'] == villa_id), None)

    if villa is None:
        return jsonify({"error": "Villa not found."}), 404

    # Check if the date is available
    if villa['availability'].get(date) is not True:
        raise BookingError("Date is not available for booking.")

    # Mark the date as booked
    villa['availability'][date] = False
    
    return jsonify({"message": "Villa booked successfully.", "villa": villa}), 201

@app.errorhandler(BookingError)
def handle_booking_error(error):
    """Handle booking errors gracefully."""
    return jsonify({"error": str(error)}), 400

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True, host='0.0.0.0', port=5000)
```
