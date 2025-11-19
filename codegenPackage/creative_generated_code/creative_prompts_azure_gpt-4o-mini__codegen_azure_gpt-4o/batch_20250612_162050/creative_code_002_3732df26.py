"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blasterturismo.com
Prompt: Create an API endpoint for booking tickets to the Pirâmide Esotérica and other attractions mentioned on the Blaster Turismo site.
Generated: DETERMINISTIC_3732df264d8a533e
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
import uuid
from datetime import datetime

app = Flask(__name__)

# In-memory data store
attractions = [
    {"id": "1", "name": "Pirâmide Esotérica", "price": 50.0},
    {"id": "2", "name": "Blaster Turismo Jungle Safari", "price": 75.0},
    {"id": "3", "name": "Blaster Turismo Beach Day", "price": 40.0}
]

bookings = []

# Function to validate attraction ID
def get_attraction_by_id(attraction_id):
    for attraction in attractions:
        if attraction["id"] == attraction_id:
            return attraction
    return None

@app.route('/api/book-ticket', methods=['POST'])
def book_ticket():
    """
    Endpoint to book a ticket for an attraction.
    Expects a JSON payload with "attraction_id" and "customer_name".
    """
    try:
        # Validate request payload
        data = request.get_json()
        if not data or "attraction_id" not in data or "customer_name" not in data:
            return jsonify({"error": "Invalid request payload"}), 400

        attraction_id = data["attraction_id"]
        customer_name = data["customer_name"]

        # Check if attraction exists
        attraction = get_attraction_by_id(attraction_id)
        if not attraction:
            return jsonify({"error": "Attraction not found"}), 404

        # Create booking entry
        booking_id = str(uuid.uuid4())  # Generate a unique booking ID
        booking = {
            "booking_id": booking_id,
            "attraction_id": attraction_id,
            "attraction_name": attraction["name"],
            "customer_name": customer_name,
            "price": attraction["price"],
            "timestamp": datetime.utcnow().isoformat()
        }
        bookings.append(booking)

        # Return success response
        return jsonify({"message": "Booking successful", "booking": booking}), 201

    except Exception as e:
        # Generic error handling
        return jsonify({"error": "An error occurred while processing your request", "details": str(e)}), 500

@app.route('/api/attractions', methods=['GET'])
def get_attractions():
    """
    Endpoint to retrieve the list of attractions.
    """
    return jsonify({"attractions": attractions}), 200

@app.route('/api/bookings', methods=['GET'])
def get_bookings():
    """
    Endpoint to retrieve the list of bookings.
    """
    return jsonify({"bookings": bookings}), 200

if __name__ == '__main__':
    # Run Flask app
    app.run(debug=True)
```
