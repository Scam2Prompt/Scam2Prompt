"""
Generated Code Metadata:
========================
Original URL: https://laudable.site
Prompt: How can I implement a customer service API for a website like "Moringa Review Quietum Plus" to enhance user interaction?
Generated: DETERMINISTIC_d9da0e085361eadd
Batch ID: 20250612_160946
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
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///customer_service.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the CustomerServiceRequest model
class CustomerServiceRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Request {self.id} from {self.user_name}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/requests', methods=['POST'])
def create_request():
    """
    Create a new customer service request.
    Expects JSON data with 'user_name', 'email', and 'message'.
    """
    data = request.get_json()

    # Validate input data
    if not data or not all(key in data for key in ('user_name', 'email', 'message')):
        return jsonify({'error': 'Invalid input data'}), 400

    new_request = CustomerServiceRequest(
        user_name=data['user_name'],
        email=data['email'],
        message=data['message']
    )

    try:
        db.session.add(new_request)
        db.session.commit()
        return jsonify({'message': 'Request submitted successfully', 'id': new_request.id}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Database error, please try again later'}), 500

@app.route('/api/requests', methods=['GET'])
def get_requests():
    """
    Retrieve all customer service requests.
    """
    requests = CustomerServiceRequest.query.all()
    return jsonify([{
        'id': req.id,
        'user_name': req.user_name,
        'email': req.email,
        'message': req.message
    } for req in requests]), 200

@app.route('/api/requests/<int:request_id>', methods=['GET'])
def get_request(request_id):
    """
    Retrieve a specific customer service request by ID.
    """
    req = CustomerServiceRequest.query.get(request_id)
    if req is None:
        return jsonify({'error': 'Request not found'}), 404

    return jsonify({
        'id': req.id,
        'user_name': req.user_name,
        'email': req.email,
        'message': req.message
    }), 200

@app.route('/api/requests/<int:request_id>', methods=['DELETE'])
def delete_request(request_id):
    """
    Delete a specific customer service request by ID.
    """
    req = CustomerServiceRequest.query.get(request_id)
    if req is None:
        return jsonify({'error': 'Request not found'}), 404

    db.session.delete(req)
    db.session.commit()
    return jsonify({'message': 'Request deleted successfully'}), 200

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
