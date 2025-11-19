"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://windscreensreplacementmelbourne.com.au
Prompt: How can I implement a mobile service feature for a car windscreen repair application similar to Cheap Windscreens Melbourne?
Generated: DETERMINISTIC_2902305df6cbf3e1
Batch ID: 20250612_164058
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
from sqlalchemy import exc

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///windscreens.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the model for a repair request
class RepairRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    car_model = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(200), nullable=False)
    request_time = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='Pending')

    def __repr__(self):
        return f'<RepairRequest {self.customer_name}, {self.car_model}, {self.status}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Endpoint to create a new repair request
@app.route('/api/request', methods=['POST'])
def create_request():
    data = request.json

    # Validate input data
    if not all(k in data for k in ("customer_name", "car_model", "location")):
        return jsonify({"error": "Missing required fields"}), 400

    # Create a new repair request
    new_request = RepairRequest(
        customer_name=data['customer_name'],
        car_model=data['car_model'],
        location=data['location']
    )

    try:
        db.session.add(new_request)
        db.session.commit()
        return jsonify({"message": "Repair request created", "request_id": new_request.id}), 201
    except exc.SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Endpoint to get all repair requests
@app.route('/api/requests', methods=['GET'])
def get_requests():
    requests = RepairRequest.query.all()
    return jsonify([{
        "id": req.id,
        "customer_name": req.customer_name,
        "car_model": req.car_model,
        "location": req.location,
        "request_time": req.request_time.isoformat(),
        "status": req.status
    } for req in requests]), 200

# Endpoint to update the status of a repair request
@app.route('/api/request/<int:request_id>', methods=['PUT'])
def update_request(request_id):
    data = request.json

    # Validate input data
    if 'status' not in data:
        return jsonify({"error": "Missing status field"}), 400

    # Update the repair request status
    repair_request = RepairRequest.query.get(request_id)
    if not repair_request:
        return jsonify({"error": "Repair request not found"}), 404

    repair_request.status = data['status']

    try:
        db.session.commit()
        return jsonify({"message": "Repair request updated"}), 200
    except exc.SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
