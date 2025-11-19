"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yourmaidinheaven.com
Prompt: Generate a code snippet for a web application that allows users to book house cleaning services similar to those offered by Maid in Heaven, including options for weekly, biweekly, and one-time cleaning plans.
Generated: DETERMINISTIC_d64d286cf0e4fc28
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
from flask import Flask, request, jsonify
from datetime import datetime, timedelta

# Initialize the Flask app
app = Flask(__name__)

# In-memory storage for bookings (In production, use a database)
bookings = []

# Available cleaning plans
CLEANING_PLANS = {
    "weekly": 7,  # Days between bookings
    "biweekly": 14,  # Days between bookings
    "onetime": 0  # No recurrence
}

# Error handler for invalid API usage
@app.errorhandler(400)
def handle_bad_request(e):
    return jsonify({"error": "Invalid request", "message": str(e)}), 400

# Route to book a cleaning service
@app.route('/book', methods=['POST'])
def book_cleaning_service():
    """
    Endpoint to book a cleaning service.
    Request JSON must include:
      - name: The name of the customer
      - email: The email of the customer
      - plan: The cleaning plan (weekly, biweekly, onetime)
      - date: The preferred date of cleaning (YYYY-MM-DD)
    Returns:
      - Confirmation of booking or an error message.
    """
    try:
        # Parse and validate incoming JSON data
        data = request.get_json()
        if not data or not all(key in data for key in ("name", "email", "plan", "date")):
            raise ValueError("Missing required fields: name, email, plan, or date.")

        name = data["name"]
        email = data["email"]
        plan = data["plan"]
        date = datetime.strptime(data["date"], "%Y-%m-%d")

        if plan not in CLEANING_PLANS:
            raise ValueError(f"Invalid plan. Available plans are: {', '.join(CLEANING_PLANS.keys())}.")

        # Generate bookings based on the selected plan
        cleaning_dates = []
        if plan == "onetime":
            cleaning_dates.append(date)
        else:
            cleaning_interval = CLEANING_PLANS[plan]
            for i in range(12):  # Generate up to 12 future bookings
                cleaning_dates.append(date + timedelta(days=i * cleaning_interval))

        # Save bookings
        booking_record = {
            "name": name,
            "email": email,
            "plan": plan,
            "cleaning_dates": [d.strftime("%Y-%m-%d") for d in cleaning_dates]
        }
        bookings.append(booking_record)

        # Return confirmation
        return jsonify({
            "message": "Booking confirmed!",
            "booking": booking_record
        }), 200

    except ValueError as ve:
        return handle_bad_request(ve)
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred", "message": str(e)}), 500

# Route to retrieve all bookings
@app.route('/bookings', methods=['GET'])
def get_all_bookings():
    """
    Endpoint to retrieve all bookings.
    Returns:
      - JSON object containing all bookings.
    """
    return jsonify({"bookings": bookings}), 200

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
```
