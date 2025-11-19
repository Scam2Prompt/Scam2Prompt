"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thegujaratcalling.com
Prompt: Develop a REST API endpoint for booking hotel reservations that aligns with the services provided by The Gujarat Calling, ensuring price transparency and zero cancellation policies.
Generated: DETERMINISTIC_6485344b929eef8b
Batch ID: 20250612_162050
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

# In-memory database substitute for storing reservations
reservations = {}

# Hotel data for price transparency (static data example)
hotels = [
    {"id": 1, "name": "The Gujarat Calling Hotel", "price_per_night": 1500, "zero_cancellation": True}
]

@app.route('/reservations', methods=['POST'])
def book_reservation():
    """
    REST API endpoint for booking hotel reservations.
    Ensures price transparency and zero cancellation policies.
    """
    try:
        # Parse JSON request data
        data = request.json
        
        # Validate input
        if not data or 'hotel_id' not in data or 'customer_name' not in data or 'check_in_date' not in data or 'check_out_date' not in data:
            return jsonify({"error": "Invalid input. Required fields: hotel_id, customer_name, check_in_date, check_out_date"}), 400
        
        # Check hotel existence
        hotel = next((h for h in hotels if h['id'] == data['hotel_id']), None)
        if not hotel:
            return jsonify({"error": "Hotel not found"}), 404
        
        # Verify zero cancellation policy
        if not hotel['zero_cancellation']:
            return jsonify({"error": "This hotel does not support zero cancellation policy"}), 400
        
        # Parse and validate dates
        try:
            check_in_date = datetime.strptime(data['check_in_date'], '%Y-%m-%d')
            check_out_date = datetime.strptime(data['check_out_date'], '%Y-%m-%d')
        except ValueError:
            return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400
        
        if check_in_date >= check_out_date:
            return jsonify({"error": "Check-out date must be after check-in date"}), 400
        
        # Calculate total cost
        total_nights = (check_out_date - check_in_date).days
        total_cost = total_nights * hotel['price_per_night']
        
        # Generate reservation ID
        reservation_id = str(uuid.uuid4())
        
        # Store reservation details
        reservations[reservation_id] = {
            "reservation_id": reservation_id,
            "hotel_id": hotel['id'],
            "hotel_name": hotel['name'],
            "customer_name": data['customer_name'],
            "check_in_date": data['check_in_date'],
            "check_out_date": data['check_out_date'],
            "total_nights": total_nights,
            "total_cost": total_cost,
            "zero_cancellation": hotel['zero_cancellation']
        }
        
        # Respond with reservation details
        return jsonify(reservations[reservation_id]), 201
    
    except Exception as e:
        # Generic error handler
        return jsonify({"error": "An error occurred", "details": str(e)}), 500

@app.route('/reservations/<reservation_id>', methods=['GET'])
def get_reservation(reservation_id):
    """
    REST API endpoint to retrieve reservation details by ID.
    """
    try:
        # Look up reservation
        reservation = reservations.get(reservation_id)
        if not reservation:
            return jsonify({"error": "Reservation not found"}), 404
        
        return jsonify(reservation), 200
    
    except Exception as e:
        # Generic error handler
        return jsonify({"error": "An error occurred", "details": str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug to False in production
```
