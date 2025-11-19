"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://filmdailyweb.com
Prompt: How can I implement a feature to book visits to showflats using a web API? Provide a sample code for this functionality.
Generated: DETERMINISTIC_a141e07b5c415728
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
import uuid

app = Flask(__name__)

# In-memory database for storing bookings (for demonstration purposes)
bookings = []

# Helper function to validate booking data
def validate_booking(data):
    required_fields = ["name", "email", "phone", "showflat_id", "visit_date"]
    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"
    try:
        visit_date = datetime.strptime(data["visit_date"], "%Y-%m-%d %H:%M:%S")
        if visit_date < datetime.now():
            return False, "Visit date cannot be in the past"
    except ValueError:
        return False, "Invalid date format. Use YYYY-MM-DD HH:MM:SS"
    return True, None

@app.route('/book_visit', methods=['POST'])
def book_visit():
    """Endpoint to book a visit to a showflat."""
    try:
        # Parse and validate input data
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid input"}), 400

        # Validate booking details
        is_valid, error_message = validate_booking(data)
        if not is_valid:
            return jsonify({"error": error_message}), 400

        # Create booking entry
        booking_id = str(uuid.uuid4())
        booking = {
            "booking_id": booking_id,
            "name": data["name"],
            "email": data["email"],
            "phone": data["phone"],
            "showflat_id": data["showflat_id"],
            "visit_date": data["visit_date"],
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        bookings.append(booking)

        # Return success response
        return jsonify({"message": "Booking successful", "booking_id": booking_id}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

@app.route('/view_bookings', methods=['GET'])
def view_bookings():
    """Endpoint to view all bookings."""
    return jsonify({"bookings": bookings}), 200

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
