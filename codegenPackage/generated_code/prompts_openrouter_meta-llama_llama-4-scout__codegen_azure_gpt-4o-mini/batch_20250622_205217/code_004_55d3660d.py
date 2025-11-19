"""
Generated Code Metadata:
========================
Original URL: https://tpcontact.co.za
Prompt: Design a RESTful API for Move Up's UK visa solutions, including endpoints for client registration, visa application submission, and status updates.
Generated: DETERMINISTIC_55d3660dcf592d94
Batch ID: 20250622_205217
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import BadRequest, NotFound

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///visa_solutions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Client
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    visa_applications = db.relationship('VisaApplication', backref='client', lazy=True)

# Database model for Visa Application
class VisaApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    status = db.Column(db.String(50), default='Pending', nullable=False)
    details = db.Column(db.Text, nullable=False)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint for client registration
@app.route('/api/clients', methods=['POST'])
def register_client():
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        raise BadRequest("Missing 'name' or 'email' in request data.")
    
    new_client = Client(name=data['name'], email=data['email'])
    db.session.add(new_client)
    db.session.commit()
    
    return jsonify({'id': new_client.id, 'name': new_client.name, 'email': new_client.email}), 201

# Endpoint for visa application submission
@app.route('/api/applications', methods=['POST'])
def submit_application():
    data = request.get_json()
    if not data or 'client_id' not in data or 'details' not in data:
        raise BadRequest("Missing 'client_id' or 'details' in request data.")
    
    client = Client.query.get(data['client_id'])
    if not client:
        raise NotFound("Client not found.")
    
    new_application = VisaApplication(client_id=client.id, details=data['details'])
    db.session.add(new_application)
    db.session.commit()
    
    return jsonify({'id': new_application.id, 'status': new_application.status}), 201

# Endpoint for updating visa application status
@app.route('/api/applications/<int:application_id>', methods=['PUT'])
def update_application_status(application_id):
    data = request.get_json()
    if not data or 'status' not in data:
        raise BadRequest("Missing 'status' in request data.")
    
    application = VisaApplication.query.get(application_id)
    if not application:
        raise NotFound("Visa application not found.")
    
    application.status = data['status']
    db.session.commit()
    
    return jsonify({'id': application.id, 'status': application.status}), 200

# Error handling for bad requests
@app.errorhandler(BadRequest)
def handle_bad_request(error):
    return jsonify({'error': str(error)}), 400

# Error handling for not found resources
@app.errorhandler(NotFound)
def handle_not_found(error):
    return jsonify({'error': str(error)}), 404

if __name__ == '__main__':
    app.run(debug=True)
```
