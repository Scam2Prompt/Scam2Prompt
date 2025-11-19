"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://auqualhairservices.com
Prompt: Generate a code snippet for a web application that allows users to book a consultation for hair transplant services at AuQual Hair Services in Raipur.
Generated: DETERMINISTIC_a17b6642fa6c0b18
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
import re

app = Flask(__name__)

# In-memory database for storing bookings (replace with real DB in production)
bookings = []

# Function to validate email format
def is_valid_email(email):
    return re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email) is not None

# Function to validate date format
def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

@app.route('/book-consultation', methods=['POST'])
def book_consultation():
    """
    Endpoint to book a consultation for hair transplant services.
    Accepts a JSON payload with user details and preferred booking date.
    """
    try:
        # Parse JSON payload
        data = request.json
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        preferred_date = data.get('preferred_date')

        # Validate required fields
        if not all([name, email, phone, preferred_date]):
            return jsonify({"error": "Missing required fields: name, email, phone, preferred_date"}), 400

        # Validate email format
        if not is_valid_email(email):
            return jsonify({"error": "Invalid email format"}), 400

        # Validate date format
        if not is_valid_date(preferred_date):
            return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400

        # Check if the preferred date is in the future
        if datetime.strptime(preferred_date, "%Y-%m-%d").date() < datetime.now().date():
            return jsonify({"error": "Preferred date must be in the future"}), 400

        # Store booking in memory (replace with DB insert in production)
        booking = {
            "id": len(bookings) + 1,
            "name": name,
            "email": email,
            "phone": phone,
            "preferred_date": preferred_date,
            "status": "Booked"
        }
        bookings.append(booking)

        return jsonify({"message": "Consultation booked successfully", "booking": booking}), 201

    except Exception as e:
        # Catch any unexpected errors
        return jsonify({"error": "An error occurred", "details": str(e)}), 500


@app.route('/get-bookings', methods=['GET'])
def get_bookings():
    """
    Endpoint to retrieve all bookings.
    """
    return jsonify({"bookings": bookings}), 200


# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
