"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bplservicescenter.com
Prompt: Create a REST API endpoint that allows users to request same-day repair services for BPL appliances, specifically targeting locations in Delhi and Noida.
Generated: DETERMINISTIC_63ced550ca425237
Batch ID: 20250612_163552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import re

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///repairs.db'
db = SQLAlchemy(app)

# Define the RepairRequest model
class RepairRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    appliance_type = db.Column(db.String(50), nullable=False)
    request_time = db.Column(db.DateTime, default=datetime.utcnow)

# Create the database tables
with app.app_context():
    db.create_all()

# Define a function to validate phone numbers
def is_valid_phone(phone):
    # Simple regex for Indian phone numbers
    return re.match(r'^[789]\d{9}$', phone)

# Endpoint to request same-day repair service
@app.route('/api/request_repair', methods=['POST'])
def request_repair():
    try:
        # Get JSON data from the request
        data = request.get_json()

        # Validate input data
        if not data or 'name' not in data or 'phone' not in data or 'address' not in data or 'appliance_type' not in data:
            return jsonify({"error": "Missing required fields"}), 400
        
        name = data['name']
        phone = data['phone']
        address = data['address']
        appliance_type = data['appliance_type']

        # Validate phone number format
        if not is_valid_phone(phone):
            return jsonify({"error": "Invalid phone number format"}), 400
        
        # Validate location (Delhi or Noida)
        if "Delhi" not in address and "Noida" not in address:
            return jsonify({"error": "Service available only in Delhi and Noida"}), 400

        # Create a new repair request
        new_request = RepairRequest(name=name, phone=phone, address=address, appliance_type=appliance_type)
        db.session.add(new_request)
        db.session.commit()

        # Return success response
        return jsonify({"message": "Repair request submitted successfully", "request_id": new_request.id}), 201

    except Exception as e:
        # Log the exception (logging not implemented here for brevity)
        return jsonify({"error": "An error occurred while processing your request", "details": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
