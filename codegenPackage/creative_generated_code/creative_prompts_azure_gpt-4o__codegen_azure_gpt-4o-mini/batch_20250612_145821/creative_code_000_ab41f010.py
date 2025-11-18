"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://clientfuel.digital
Prompt: Write Python code to integrate a custom booking calendar system that filters out unqualified leads, as described in Client Fuel's "self-booking process."
Generated: DETERMINISTIC_ab41f01028bc6d79
Batch ID: 20250612_145821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
import json
import logging
from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Set up basic logging
logging.basicConfig(level=logging.INFO)

# Sample data structure for qualified leads
qualified_leads = {
    "email_domains": ["@example.com", "@sample.org"],
    "min_age": 18,
    "max_age": 65
}

# Function to check if a lead is qualified
def is_qualified_lead(lead):
    """
    Check if a lead meets the qualification criteria.

    :param lead: Dictionary containing lead information
    :return: Boolean indicating if the lead is qualified
    """
    try:
        email = lead.get("email")
        age = lead.get("age")

        # Check email domain
        if not any(email.endswith(domain) for domain in qualified_leads["email_domains"]):
            return False
        
        # Check age range
        if age < qualified_leads["min_age"] or age > qualified_leads["max_age"]:
            return False

        return True
    except Exception as e:
        logging.error(f"Error while checking qualification: {e}")
        return False

# Endpoint to book a calendar slot
@app.route('/book', methods=['POST'])
def book_slot():
    """
    Endpoint for booking a calendar slot.
    
    Expected JSON payload:
    {
        "lead": {
            "email": "lead@example.com",
            "age": 30
        },
        "date": "YYYY-MM-DD",
        "time": "HH:MM"
    }
    """
    try:
        data = request.get_json()

        # Validate input data
        if not data or 'lead' not in data or 'date' not in data or 'time' not in data:
            return jsonify({"error": "Invalid input data"}), 400
        
        lead = data['lead']
        booking_date = data['date']
        booking_time = data['time']

        # Check if lead qualifies
        if not is_qualified_lead(lead):
            return jsonify({"error": "Lead does not qualify for booking"}), 403

        # Simulate booking logic
        booking_datetime = datetime.strptime(f"{booking_date} {booking_time}", "%Y-%m-%d %H:%M")
        
        # Here you would implement your logic to check availability, etc.

        logging.info(f"Booking successful for {lead['email']} on {booking_datetime}")
        return jsonify({"message": "Booking confirmed", "datetime": booking_datetime.isoformat()}), 200

    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON format"}), 400
    except ValueError as ve:
        logging.error(f"Value error: {ve}")
        return jsonify({"error": "Invalid date or time"}), 400
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return jsonify({"error": "Internal server error"}), 500

# Entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```
