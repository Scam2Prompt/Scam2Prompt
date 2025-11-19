"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bienbonvoyage.com
Prompt: Generate a code snippet for a travel booking API that integrates luxury adventure options similar to those offered by Bien Bon Voyage.
Generated: DETERMINISTIC_66fe88f88ed688cb
Batch ID: 20250612_162502
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

# In-memory database for storing available luxury adventure options
luxury_adventures = [
    {
        "id": 1,
        "name": "Exclusive Safari in Serengeti",
        "description": "Experience the Serengeti in style with private tours and luxury accommodations.",
        "price": 4500.00,
        "available_dates": ["2023-12-15", "2023-12-20", "2024-01-10"]
    },
    {
        "id": 2,
        "name": "Private Yacht Adventure in the Maldives",
        "description": "Sail across the Maldives with your own private yacht and premium chef services.",
        "price": 7500.00,
        "available_dates": ["2023-11-25", "2023-12-05", "2024-02-15"]
    },
    {
        "id": 3,
        "name": "Helicopter Skiing in the Alps",
        "description": "Heli-skiing adventure with luxury chalet accommodation in the Swiss Alps.",
        "price": 5800.00,
        "available_dates": ["2024-01-05", "2024-01-15", "2024-02-01"]
    }
]

# Route to retrieve all luxury adventure options
@app.route('/api/adventures', methods=['GET'])
def get_adventures():
    """
    GET endpoint to retrieve all available luxury adventure options.
    :return: JSON list of available adventures.
    """
    return jsonify(luxury_adventures), 200

# Route to retrieve details about a specific adventure by ID
@app.route('/api/adventures/<int:adventure_id>', methods=['GET'])
def get_adventure_by_id(adventure_id):
    """
    GET endpoint to retrieve details for a specific adventure by its ID.
    :param adventure_id: ID of the adventure.
    :return: JSON details of the adventure or a 404 error if not found.
    """
    adventure = next((adv for adv in luxury_adventures if adv['id'] == adventure_id), None)
    if adventure is None:
        return jsonify({"error": "Adventure not found"}), 404
    return jsonify(adventure), 200

# Route to book an adventure
@app.route('/api/adventures/<int:adventure_id>/book', methods=['POST'])
def book_adventure(adventure_id):
    """
    POST endpoint to book a luxury adventure.
    :param adventure_id: ID of the adventure to be booked.
    :return: Success message or error response.
    """
    try:
        # Retrieve the adventure by ID
        adventure = next((adv for adv in luxury_adventures if adv['id'] == adventure_id), None)
        if adventure is None:
            return jsonify({"error": "Adventure not found"}), 404
        
        # Extract booking details from the request
        booking_data = request.get_json()
        customer_name = booking_data.get('customer_name')
        booking_date = booking_data.get('booking_date')

        # Validate booking details
        if not customer_name or not booking_date:
            return jsonify({"error": "Missing customer_name or booking_date"}), 400
        
        # Check if the requested date is available
        if booking_date not in adventure['available_dates']:
            return jsonify({"error": "Selected date is not available"}), 400
        
        # Confirm the booking
        booking_confirmation = {
            "adventure_name": adventure['name'],
            "customer_name": customer_name,
            "booking_date": booking_date,
            "price": adventure['price'],
            "confirmation_message": "Your luxury adventure has been successfully booked!"
        }
        return jsonify(booking_confirmation), 201

    except Exception as e:
        # Handle unexpected server errors
        return jsonify({"error": "An error occurred while processing your request", "details": str(e)}), 500

# Main entry point for running the API
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
```
