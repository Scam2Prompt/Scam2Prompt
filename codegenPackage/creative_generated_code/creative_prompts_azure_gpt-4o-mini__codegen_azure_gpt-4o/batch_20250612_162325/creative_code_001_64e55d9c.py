"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniquehomestagingandredesignbydee.com
Prompt: Write a code snippet for an API that allows users to book home staging services, similar to those offered by Unique Home Staging and Redesign in New Bern.
Generated: DETERMINISTIC_64e55d9ced292d0b
Batch ID: 20250612_162325
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

# In-memory database for simplicity (use a real database for production)
booking_database = []

# Helper function to validate booking data
def validate_booking_data(data):
    required_fields = ["name", "email", "phone", "service_date", "service_type"]
    for field in required_fields:
        if field not in data or not data[field]:
            return f"Missing or empty field: {field}"
    # Validate date format
    try:
        datetime.strptime(data["service_date"], "%Y-%m-%d")
    except ValueError:
        return "Invalid date format. Use YYYY-MM-DD."
    return None

@app.route('/api/book-home-staging', methods=['POST'])
def book_home_staging():
    """
    API endpoint to book home staging services.
    Expected JSON payload:
    {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "phone": "123-456-7890",
        "service_date": "2023-11-15",
        "service_type": "Full Staging" (or "Redesign")
    }
    """
    try:
        data = request.get_json()

        # Validate incoming data
        validation_error = validate_booking_data(data)
        if validation_error:
            return jsonify({"error": validation_error}), 400
        
        # Create booking record
        booking = {
            "id": len(booking_database) + 1,
            "name": data["name"],
            "email": data["email"],
            "phone": data["phone"],
            "service_date": data["service_date"],
            "service_type": data["service_type"],
            "created_at": datetime.now().isoformat()
        }
        
        booking_database.append(booking)
        
        # Return success response
        return jsonify({
            "message": "Booking successfully created!",
            "booking": booking
        }), 201
    
    except Exception as e:
        # Generic error handling
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

@app.route('/api/bookings', methods=['GET'])
def list_bookings():
    """
    API endpoint to retrieve all bookings.
    Returns a JSON list of all bookings.
    """
    return jsonify({"bookings": booking_database}), 200

if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=True)
```
