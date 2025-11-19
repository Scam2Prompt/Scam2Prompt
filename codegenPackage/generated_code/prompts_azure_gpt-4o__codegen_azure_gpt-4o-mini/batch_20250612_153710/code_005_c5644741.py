"""
Generated Code Metadata:
========================
Original URL: https://amplatinumconsulting.com
Prompt: Write code to implement a client management system for consulting firms using Django or Flask.
Generated: DETERMINISTIC_c56447411687c2da
Batch ID: 20250612_153710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# client_management.py

from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clients.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Client model
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(15), nullable=True)

    def __repr__(self):
        return f'<Client {self.name}>'

# Define the Client schema for serialization
class ClientSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    phone = fields.Str(required=False)

# Initialize the schema
client_schema = ClientSchema()
clients_schema = ClientSchema(many=True)

# Create the database tables
with app.app_context():
    db.create_all()

# Route to create a new client
@app.route('/clients', methods=['POST'])
def add_client():
    try:
        # Validate and deserialize input
        client_data = client_schema.load(request.json)
        new_client = Client(**client_data)
        db.session.add(new_client)
        db.session.commit()
        return client_schema.jsonify(new_client), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Route to get all clients
@app.route('/clients', methods=['GET'])
def get_clients():
    clients = Client.query.all()
    return clients_schema.jsonify(clients), 200

# Route to get a client by ID
@app.route('/clients/<int:client_id>', methods=['GET'])
def get_client(client_id):
    client = Client.query.get(client_id)
    if client is None:
        abort(404, description="Client not found")
    return client_schema.jsonify(client), 200

# Route to update a client
@app.route('/clients/<int:client_id>', methods=['PUT'])
def update_client(client_id):
    client = Client.query.get(client_id)
    if client is None:
        abort(404, description="Client not found")
    
    try:
        # Validate and deserialize input
        client_data = client_schema.load(request.json)
        for key, value in client_data.items():
            setattr(client, key, value)
        db.session.commit()
        return client_schema.jsonify(client), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Route to delete a client
@app.route('/clients/<int:client_id>', methods=['DELETE'])
def delete_client(client_id):
    client = Client.query.get(client_id)
    if client is None:
        abort(404, description="Client not found")
    
    try:
        db.session.delete(client)
        db.session.commit()
        return jsonify({"message": "Client deleted"}), 204
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Instructions to Run the Code
1. Ensure you have Flask, Flask-SQLAlchemy, and Marshmallow installed:
   ```bash
   pip install Flask Flask-SQLAlchemy marshmallow
   ```
2. Save the code in a file named `client_management.py`.
3. Run the application:
   ```bash
   python client_management.py
   ```
4. Use a tool like Postman or curl to interact with the API.
