"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://drivemiami.com
Prompt: Create a script for scheduling service and parts inquiries on a vehicle dealership website, as described in DriveCities' offerings.
Generated: DETERMINISTIC_463a938694b4ead6
Batch ID: 20250612_135839
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for inquiries (to be replaced with a database in production)
inquiries = []

class Inquiry:
    """
    A class representing a service or parts inquiry.
    """
    def __init__(self, name, email, phone, inquiry_type, vehicle_details, preferred_date, message=None):
        self.id = len(inquiries) + 1
        self.name = name
        self.email = email
        self.phone = phone
        self.inquiry_type = inquiry_type
        self.vehicle_details = vehicle_details
        self.preferred_date = preferred_date
        self.message = message
        self.created_at = datetime.datetime.now()

    def to_dict(self):
        """Convert the Inquiry object into a dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "inquiry_type": self.inquiry_type,
            "vehicle_details": self.vehicle_details,
            "preferred_date": self.preferred_date.strftime("%Y-%m-%d"),
            "message": self.message,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        }


@app.route('/schedule_inquiry', methods=['POST'])
def schedule_inquiry():
    """
    Endpoint to schedule a service or parts inquiry.
    Expecting JSON data with the following fields:
    - name: Customer name (string, required)
    - email: Customer email (string, required)
    - phone: Customer phone number (string, required)
    - inquiry_type: Type of inquiry ('service' or 'parts') (string, required)
    - vehicle_details: Details about the vehicle (string, required)
    - preferred_date: Preferred date for the inquiry (YYYY-MM-DD format, required)
    - message: Additional message (string, optional)
    """
    try:
        # Get JSON data from the request
        data = request.json

        # Validate required fields
        required_fields = ['name', 'email', 'phone', 'inquiry_type', 'vehicle_details', 'preferred_date']
        for field in required_fields:
            if field not in data or not data[field]:
                return jsonify({"error": f"'{field}' is required."}), 400

        # Validate inquiry type
        if data['inquiry_type'] not in ['service', 'parts']:
            return jsonify({"error": "Invalid inquiry type. Must be 'service' or 'parts'."}), 400

        # Validate preferred date
        try:
            preferred_date = datetime.datetime.strptime(data['preferred_date'], "%Y-%m-%d").date()
            if preferred_date < datetime.date.today():
                return jsonify({"error": "Preferred date cannot be in the past."}), 400
        except ValueError:
            return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400

        # Create new inquiry
        inquiry = Inquiry(
            name=data['name'],
            email=data['email'],
            phone=data['phone'],
            inquiry_type=data['inquiry_type'],
            vehicle_details=data['vehicle_details'],
            preferred_date=preferred_date,
            message=data.get('message')
        )

        # Store the inquiry (in production, this would be saved to a database)
        inquiries.append(inquiry)

        # Return success response
        return jsonify({"message": "Inquiry scheduled successfully!", "inquiry": inquiry.to_dict()}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500


@app.route('/get_inquiries', methods=['GET'])
def get_inquiries():
    """
    Endpoint to retrieve all scheduled inquiries.
    """
    return jsonify([inquiry.to_dict() for inquiry in inquiries]), 200


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
