"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.purpledumpster.ca
Prompt: Create a REST API that allows users to book a dumpster rental service from Purple Dumpster, specifying the dumpster size, service area, and rental duration.
Generated: DETERMINISTIC_a33bf44e545c1229
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import datetime

# Initialize the Flask app
app = Flask(__name__)

# In-memory database for storing bookings
# NOTE: In production, use a proper database like PostgreSQL or MongoDB
bookings = []

# Define available dumpster sizes and service areas
AVAILABLE_DUMPSTER_SIZES = ['small', 'medium', 'large']
AVAILABLE_SERVICE_AREAS = ['downtown', 'suburbs', 'industrial']

# Helper function to validate booking details
def validate_booking(data):
    errors = []
    
    # Validate dumpster size
    if 'dumpster_size' not in data or data['dumpster_size'] not in AVAILABLE_DUMPSTER_SIZES:
        errors.append(f"Invalid dumpster size. Available sizes are: {AVAILABLE_DUMPSTER_SIZES}")
    
    # Validate service area
    if 'service_area' not in data or data['service_area'] not in AVAILABLE_SERVICE_AREAS:
        errors.append(f"Invalid service area. Available areas are: {AVAILABLE_SERVICE_AREAS}")
    
    # Validate rental duration
    try:
        rental_duration = int(data.get('rental_duration', 0))
        if rental_duration <= 0:
            errors.append("Rental duration must be a positive integer.")
    except ValueError:
        errors.append("Rental duration must be a positive integer.")
    
    return errors

@app.route('/api/book-dumpster', methods=['POST'])
def book_dumpster():
    """
    Endpoint to book a dumpster rental service.
    Request Payload:
        {
            "dumpster_size": "small",
            "service_area": "downtown",
            "rental_duration": 7
        }
    Response:
        Success: {"message": "Booking confirmed", "booking_id": 123}
        Error: {"error": "Invalid input", "details": ["error1", "error2"]}
    """
    try:
        # Parse the JSON request payload
        booking_data = request.get_json()
        
        # Validate the booking request
        validation_errors = validate_booking(booking_data)
        if validation_errors:
            return jsonify({"error": "Invalid input", "details": validation_errors}), 400
        
        # Generate a unique booking ID (in production, this should come from a database)
        booking_id = len(bookings) + 1
        
        # Create a booking record
        booking_record = {
            "booking_id": booking_id,
            "dumpster_size": booking_data['dumpster_size'],
            "service_area": booking_data['service_area'],
            "rental_duration": booking_data['rental_duration'],
            "timestamp": datetime.datetime.now().isoformat()
        }
        
        # Save the booking record
        bookings.append(booking_record)
        
        # Return success response
        return jsonify({"message": "Booking confirmed", "booking_id": booking_id}), 201
    
    except Exception as e:
        # Handle unexpected server errors
        return jsonify({"error": "Internal server error", "details": str(e)}), 500

@app.route('/api/bookings', methods=['GET'])
def get_bookings():
    """
    Endpoint to retrieve all bookings.
    Response:
        Success: List of all bookings
    """
    try:
        return jsonify(bookings), 200
    except Exception as e:
        return jsonify({"error": "Internal server error", "details": str(e)}), 500

# Run the app (only use this in development; use a production server like Gunicorn for deployment)
if __name__ == '__main__':
    app.run(debug=True)
```
