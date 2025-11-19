"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://engaztop.com
Prompt: Create a sample API endpoint for a home services company that includes functionalities for booking water tank cleaning and thermal insulation services, reflecting the services provided by شركة انجاز.
Generated: DETERMINISTIC_98eb94bd342ff7ef
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

app = Flask(__name__)

# In-memory database to store bookings
bookings = []

@app.route('/api/book-service', methods=['POST'])
def book_service():
    """
    Endpoint to book a service for water tank cleaning or thermal insulation.
    Request JSON should include:
        - service_type: "water_tank_cleaning" or "thermal_insulation"
        - customer_name: Name of the customer
        - contact_number: Phone number of the customer
        - date: Preferred date for the service in YYYY-MM-DD format
    """
    try:
        # Parse the JSON request body
        data = request.get_json()

        # Validate required fields
        if not all(field in data for field in ['service_type', 'customer_name', 'contact_number', 'date']):
            return jsonify({"error": "Missing required fields: service_type, customer_name, contact_number, date"}), 400

        # Validate service type
        if data['service_type'] not in ["water_tank_cleaning", "thermal_insulation"]:
            return jsonify({"error": "Invalid service_type. Choose 'water_tank_cleaning' or 'thermal_insulation'"}), 400

        # Validate date format
        try:
            service_date = datetime.strptime(data['date'], '%Y-%m-%d')
            if service_date < datetime.now():
                return jsonify({"error": "Date must be in the future"}), 400
        except ValueError:
            return jsonify({"error": "Invalid date format. Use YYYY-MM-DD"}), 400

        # Create a booking entry
        booking = {
            "id": len(bookings) + 1,
            "service_type": data['service_type'],
            "customer_name": data['customer_name'],
            "contact_number": data['contact_number'],
            "date": service_date.strftime('%Y-%m-%d'),
        }

        # Store the booking
        bookings.append(booking)

        return jsonify({"message": "Booking successful", "booking": booking}), 201

    except Exception as e:
        # Generic error handler
        return jsonify({"error": "An error occurred while processing your request", "details": str(e)}), 500

@app.route('/api/bookings', methods=['GET'])
def get_bookings():
    """
    Endpoint to retrieve all bookings.
    Returns a list of all bookings with their details.
    """
    try:
        return jsonify({"bookings": bookings}), 200
    except Exception as e:
        # Generic error handler
        return jsonify({"error": "An error occurred while fetching bookings", "details": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
