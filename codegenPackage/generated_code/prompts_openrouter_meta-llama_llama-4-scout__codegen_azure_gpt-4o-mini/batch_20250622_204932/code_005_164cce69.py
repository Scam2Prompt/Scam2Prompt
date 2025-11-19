"""
Generated Code Metadata:
========================
Original URL: https://atualcontabilidade.com
Prompt: "Design a RESTful API for an accounting firm's client portal, allowing clients to submit requests, view documents, and communicate with the firm."
Generated: DETERMINISTIC_164cce695a2fc20b
Batch ID: 20250622_204932
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
from flask_marshmallow import Marshmallow
from datetime import datetime
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///clients.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Client model
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    requests = db.relationship('Request', backref='client', lazy=True)

# Request model
class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'), nullable=False)
    document = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Client schema
class ClientSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Client

# Request schema
class RequestSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Request

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to create a new client
@app.route('/clients', methods=['POST'])
def add_client():
    try:
        name = request.json['name']
        email = request.json['email']
        new_client = Client(name=name, email=email)
        db.session.add(new_client)
        db.session.commit()
        return ClientSchema().jsonify(new_client), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Endpoint to get all clients
@app.route('/clients', methods=['GET'])
def get_clients():
    clients = Client.query.all()
    return ClientSchema(many=True).jsonify(clients)

# Endpoint to submit a request
@app.route('/clients/<int:client_id>/requests', methods=['POST'])
def submit_request(client_id):
    try:
        document = request.json['document']
        new_request = Request(client_id=client_id, document=document)
        db.session.add(new_request)
        db.session.commit()
        return RequestSchema().jsonify(new_request), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Endpoint to view requests for a client
@app.route('/clients/<int:client_id>/requests', methods=['GET'])
def get_requests(client_id):
    requests = Request.query.filter_by(client_id=client_id).all()
    return RequestSchema(many=True).jsonify(requests)

# Endpoint to view a specific document request
@app.route('/requests/<int:request_id>', methods=['GET'])
def get_request(request_id):
    request_item = Request.query.get_or_404(request_id)
    return RequestSchema().jsonify(request_item)

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

# Error handling for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
