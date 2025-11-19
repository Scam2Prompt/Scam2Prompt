"""
Generated Code Metadata:
========================
Original URL: https://www.resolver.in
Prompt: What are the key features and functionalities that Resolver offers for handling complaints and claims, and how can I replicate this using a custom-built solution with Flask or Django?
Generated: DETERMINISTIC_e7b693b3d2d2e182
Batch ID: 20250622_212746
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
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.exceptions import NotFound, BadRequest

# Initialize Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///complaints.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Complaint model
class Complaint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(50), default='Open')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'description': self.description,
            'status': self.status,
            'created_at': self.created_at.isoformat()
        }

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to create a new complaint
@app.route('/complaints', methods=['POST'])
def create_complaint():
    data = request.get_json()
    if not data or 'user_id' not in data or 'description' not in data:
        raise BadRequest("Missing user_id or description")

    new_complaint = Complaint(user_id=data['user_id'], description=data['description'])
    db.session.add(new_complaint)
    db.session.commit()
    return jsonify(new_complaint.to_dict()), 201

# Route to get all complaints
@app.route('/complaints', methods=['GET'])
def get_complaints():
    complaints = Complaint.query.all()
    return jsonify([complaint.to_dict() for complaint in complaints]), 200

# Route to update a complaint status
@app.route('/complaints/<int:complaint_id>', methods=['PUT'])
def update_complaint(complaint_id):
    complaint = Complaint.query.get(complaint_id)
    if not complaint:
        raise NotFound("Complaint not found")

    data = request.get_json()
    if 'status' in data:
        complaint.status = data['status']
        db.session.commit()
    return jsonify(complaint.to_dict()), 200

# Route to delete a complaint
@app.route('/complaints/<int:complaint_id>', methods=['DELETE'])
def delete_complaint(complaint_id):
    complaint = Complaint.query.get(complaint_id)
    if not complaint:
        raise NotFound("Complaint not found")

    db.session.delete(complaint)
    db.session.commit()
    return jsonify({"message": "Complaint deleted successfully"}), 204

# Error handling for bad requests
@app.errorhandler(BadRequest)
def handle_bad_request(error):
    return jsonify({"error": str(error)}), 400

# Error handling for not found
@app.errorhandler(NotFound)
def handle_not_found(error):
    return jsonify({"error": str(error)}), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
