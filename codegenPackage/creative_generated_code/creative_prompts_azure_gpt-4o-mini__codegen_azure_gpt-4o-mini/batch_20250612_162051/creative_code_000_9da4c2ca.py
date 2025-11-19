"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://engaztop.com
Prompt: Generate a code snippet for a web application that allows users to request home cleaning services, similar to the offerings of شركة انجاز, including features for scheduling and pricing.
Generated: DETERMINISTIC_9da4c2ca8ce07c09
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
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import re

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cleaning_services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for cleaning service requests
class CleaningServiceRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    user_email = db.Column(db.String(100), nullable=False)
    service_date = db.Column(db.DateTime, nullable=False)
    service_type = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<CleaningServiceRequest {self.id} - {self.user_name}>"

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to request cleaning services
@app.route('/request_service', methods=['POST'])
def request_service():
    data = request.get_json()
    
    # Validate input data
    if not data or not all(k in data for k in ("user_name", "user_email", "service_date", "service_type")):
        return jsonify({"error": "Invalid input data"}), 400

    # Validate email format
    if not re.match(r"[^@]+@[^@]+\.[^@]+", data['user_email']):
        return jsonify({"error": "Invalid email format"}), 400

    # Parse service date
    try:
        service_date = datetime.strptime(data['service_date'], "%Y-%m-%d %H:%M")
    except ValueError:
        return jsonify({"error": "Invalid date format, please use YYYY-MM-DD HH:MM"}), 400

    # Set price based on service type
    service_type = data['service_type']
    price_mapping = {
        "standard": 100.0,
        "deep": 150.0,
        "move_out": 200.0
    }
    
    price = price_mapping.get(service_type.lower())
    if price is None:
        return jsonify({"error": "Invalid service type"}), 400

    # Create and save the new cleaning service request
    new_request = CleaningServiceRequest(
        user_name=data['user_name'],
        user_email=data['user_email'],
        service_date=service_date,
        service_type=service_type,
        price=price
    )
    
    try:
        db.session.add(new_request)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"An error occurred while saving the request: {str(e)}"}), 500

    return jsonify({"message": "Service request submitted successfully", "request_id": new_request.id}), 201

# Route to get all service requests
@app.route('/requests', methods=['GET'])
def get_requests():
    try:
        requests = CleaningServiceRequest.query.all()
        return jsonify([{
            "id": req.id,
            "user_name": req.user_name,
            "user_email": req.user_email,
            "service_date": req.service_date.strftime("%Y-%m-%d %H:%M"),
            "service_type": req.service_type,
            "price": req.price
        } for req in requests]), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred while retrieving requests: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
