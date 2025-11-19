"""
Generated Code Metadata:
========================
Original URL: https://stars-ksa.com
Prompt: Generate a code snippet for a web application that allows users to book residential cleaning services, incorporating features like scheduling and service customization as described by Star Cleaning Services.
Generated: DETERMINISTIC_6981e3f03408f2ea
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# In-memory database for simplicity (use a real database in production)
bookings = []

# Available cleaning services
services = {
    "basic_cleaning": 50,  # Price in USD
    "deep_cleaning": 100,
    "move_in_out_cleaning": 150,
    "custom_cleaning": 75
}

@app.route('/services', methods=['GET'])
def get_services():
    """
    Endpoint to retrieve available cleaning services and their prices.
    """
    return jsonify({"services": services}), 200

@app.route('/book', methods=['POST'])
def book_service():
    """
    Endpoint to book a cleaning service.
    Expects JSON payload with:
    - name: str (User's name)
    - email: str (User's email)
    - service: str (Service type)
    - date: str (Scheduled date in YYYY-MM-DD format)
    - time: str (Scheduled time in HH:MM format)
    """
    try:
        # Parse request data
        data = request.json
        name = data.get('name')
        email = data.get('email')
        service = data.get('service')
        date = data.get('date')
        time = data.get('time')

        # Validate input
        if not all([name, email, service, date, time]):
            return jsonify({"error": "All fields (name, email, service, date, time) are required."}), 400
        if service not in services:
            return jsonify({"error": f"Invalid service type. Available services: {list(services.keys())}"}), 400

        # Validate date and time format
        try:
            scheduled_datetime = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
        except ValueError:
            return jsonify({"error": "Invalid date or time format. Use YYYY-MM-DD for date and HH:MM for time."}), 400

        # Create booking record
        booking = {
            "id": len(bookings) + 1,
            "name": name,
            "email": email,
            "service": service,
            "date": date,
            "time": time,
            "price": services[service]
        }
        bookings.append(booking)

        return jsonify({"message": "Booking successful!", "booking": booking}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/bookings', methods=['GET'])
def get_bookings():
    """
    Endpoint to retrieve all bookings.
    """
    return jsonify({"bookings": bookings}), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
