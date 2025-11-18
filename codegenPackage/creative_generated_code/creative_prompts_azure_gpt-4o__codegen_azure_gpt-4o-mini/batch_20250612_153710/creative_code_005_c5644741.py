"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amplatinumconsulting.com
Prompt: Write code to implement a client management system for consulting firms using Django or Flask.
Generated: DETERMINISTIC_c56447411687c2da
Batch ID: 20250612_153710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# client_management.py
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clients.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Client model definition
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(15), nullable=True)

# Client schema for serialization/deserialization
class ClientSchema(Schema):
    id = fields.Integer()
    name = fields.String(required=True)
    email = fields.Email(required=True)
    phone = fields.String()

# Initialize the database
with app.app_context():
    db.create_all()

# Create a new client
@app.route('/clients', methods=['POST'])
def add_client():
    try:
        client_data = ClientSchema().load(request.json)  # Validate input data
        new_client = Client(**client_data)
        db.session.add(new_client)
        db.session.commit()
        return ClientSchema().dump(new_client), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Retrieve all clients
@app.route('/clients', methods=['GET'])
def get_clients():
    clients = Client.query.all()
    return ClientSchema(many=True).dump(clients), 200

# Retrieve a specific client by ID
@app.route('/clients/<int:client_id>', methods=['GET'])
def get_client(client_id):
    client = Client.query.get(client_id)
    if client is None:
        abort(404)  # Not Found
    return ClientSchema().dump(client), 200

# Update an existing client
@app.route('/clients/<int:client_id>', methods=['PUT'])
def update_client(client_id):
    client = Client.query.get(client_id)
    if client is None:
        abort(404)  # Not Found
    try:
        client_data = ClientSchema().load(request.json)  # Validate input data
        for key, value in client_data.items():
            setattr(client, key, value)
        db.session.commit()
        return ClientSchema().dump(client), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Delete a client
@app.route('/clients/<int:client_id>', methods=['DELETE'])
def delete_client(client_id):
    client = Client.query.get(client_id)
    if client is None:
        abort(404)  # Not Found
    try:
        db.session.delete(client)
        db.session.commit()
        return jsonify({"message": "Client deleted"}), 204
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```

Make sure to install the necessary packages by running:
```bash
pip install Flask Flask-SQLAlchemy marshmallow
```
This code defines a simple client management system using Flask, SQLite for the database, and Marshmallow for validation and serialization.
