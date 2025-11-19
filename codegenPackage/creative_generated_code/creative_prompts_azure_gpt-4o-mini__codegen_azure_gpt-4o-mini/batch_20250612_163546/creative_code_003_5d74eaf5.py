"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proximus-client.was-systems.com
Prompt: Suggest an API for managing client information and callback requests, taking cues from the Proximus client form structure.
Generated: DETERMINISTIC_5d74eaf5ed5de4b4
Batch ID: 20250612_163546
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
from werkzeug.exceptions import NotFound, BadRequest

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clients.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define Client model
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    callback_requested = db.Column(db.Boolean, default=False)

    def to_dict(self):
        """Convert the Client model to a dictionary representation."""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'callback_requested': self.callback_requested
        }

# Error handling for HTTP exceptions
@app.errorhandler(NotFound)
def handle_not_found(error):
    return jsonify({'error': 'Resource not found'}), 404

@app.errorhandler(BadRequest)
def handle_bad_request(error):
    return jsonify({'error': 'Bad request'}), 400

# Route to create a new client
@app.route('/clients', methods=['POST'])
def create_client():
    """Create a new client with provided information."""
    data = request.get_json()
    if not all(k in data for k in ('name', 'email', 'phone')):
        raise BadRequest("Missing required fields: 'name', 'email', 'phone'")

    new_client = Client(
        name=data['name'],
        email=data['email'],
        phone=data['phone'],
        callback_requested=data.get('callback_requested', False)
    )
    
    db.session.add(new_client)
    db.session.commit()
    
    return jsonify(new_client.to_dict()), 201

# Route to get client information by ID
@app.route('/clients/<int:client_id>', methods=['GET'])
def get_client(client_id):
    """Retrieve client information by ID."""
    client = Client.query.get(client_id)
    if not client:
        raise NotFound("Client not found")
    return jsonify(client.to_dict()), 200

# Route to list all clients
@app.route('/clients', methods=['GET'])
def list_clients():
    """List all clients."""
    clients = Client.query.all()
    return jsonify([client.to_dict() for client in clients]), 200

# Route to update client information
@app.route('/clients/<int:client_id>', methods=['PUT'])
def update_client(client_id):
    """Update client information based on provided ID."""
    client = Client.query.get(client_id)
    if not client:
        raise NotFound("Client not found")
    
    data = request.get_json()
    if 'name' in data:
        client.name = data['name']
    if 'email' in data:
        client.email = data['email']
    if 'phone' in data:
        client.phone = data['phone']
    if 'callback_requested' in data:
        client.callback_requested = data['callback_requested']
    
    db.session.commit()
    
    return jsonify(client.to_dict()), 200

# Route to delete a client
@app.route('/clients/<int:client_id>', methods=['DELETE'])
def delete_client(client_id):
    """Delete a client based on provided ID."""
    client = Client.query.get(client_id)
    if not client:
        raise NotFound("Client not found")
    
    db.session.delete(client)
    db.session.commit()
    
    return jsonify({'message': 'Client deleted successfully'}), 204

# Initialize the database and start the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Start the Flask application
```
