"""
Generated Code Metadata:
========================
Original URL: https://atualcontabilidade.com
Prompt: "Design a RESTful API for an accounting firm's client portal, allowing clients to submit requests, view documents, and communicate with the firm."
Generated: DETERMINISTIC_164cce695a2fc20b
Batch ID: 20250622_204932
URLs Found: 8
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:5000/login`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:5000/documents?client_id=1`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:5000/messages`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:5000/messages?client_id=1`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:5000/documents`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:5000/requests`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:5000/requests?client_id=1`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:5000/register`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

**Client Portal API**
======================

### Dependencies

* `flask`: For building the RESTful API
* `flask_sqlalchemy`: For database interactions
* `flask_marshmallow`: For serialization and deserialization
* `werkzeug`: For password hashing and verification

### Code

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///client_portal.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Models
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password)

class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(50), nullable=False, default='pending')

    def __init__(self, client_id, description):
        self.client_id = client_id
        self.description = description

class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    filename = db.Column(db.String(100), nullable=False)
    file_data = db.Column(db.LargeBinary, nullable=False)

    def __init__(self, client_id, filename, file_data):
        self.client_id = client_id
        self.filename = filename
        self.file_data = file_data

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    message = db.Column(db.Text, nullable=False)

    def __init__(self, client_id, message):
        self.client_id = client_id
        self.message = message

# Schemas
class ClientSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Client

class RequestSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Request

class DocumentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Document

class MessageSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Message

# API Endpoints
@app.route('/register', methods=['POST'])
def register_client():
    try:
        data = request.get_json()
        client = Client(data['name'], data['email'], data['password'])
        db.session.add(client)
        db.session.commit()
        return jsonify({'message': 'Client registered successfully'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@app.route('/login', methods=['POST'])
def login_client():
    try:
        data = request.get_json()
        client = Client.query.filter_by(email=data['email']).first()
        if client and check_password_hash(client.password, data['password']):
            return jsonify({'message': 'Client logged in successfully'}), 200
        return jsonify({'message': 'Invalid credentials'}), 401
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@app.route('/requests', methods=['POST'])
def create_request():
    try:
        data = request.get_json()
        client_id = data['client_id']
        request = Request(client_id, data['description'])
        db.session.add(request)
        db.session.commit()
        return jsonify({'message': 'Request created successfully'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@app.route('/requests', methods=['GET'])
def get_requests():
    try:
        client_id = request.args.get('client_id')
        requests = Request.query.filter_by(client_id=client_id).all()
        request_schema = RequestSchema(many=True)
        return jsonify(request_schema.dump(requests)), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@app.route('/documents', methods=['POST'])
def upload_document():
    try:
        data = request.files['file']
        client_id = request.form['client_id']
        document = Document(client_id, data.filename, data.read())
        db.session.add(document)
        db.session.commit()
        return jsonify({'message': 'Document uploaded successfully'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@app.route('/documents', methods=['GET'])
def get_documents():
    try:
        client_id = request.args.get('client_id')
        documents = Document.query.filter_by(client_id=client_id).all()
        document_schema = DocumentSchema(many=True)
        return jsonify(document_schema.dump(documents)), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@app.route('/messages', methods=['POST'])
def send_message():
    try:
        data = request.get_json()
        client_id = data['client_id']
        message = Message(client_id, data['message'])
        db.session.add(message)
        db.session.commit()
        return jsonify({'message': 'Message sent successfully'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@app.route('/messages', methods=['GET'])
def get_messages():
    try:
        client_id = request.args.get('client_id')
        messages = Message.query.filter_by(client_id=client_id).all()
        message_schema = MessageSchema(many=True)
        return jsonify(message_schema.dump(messages)), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 400

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
```

### Example Usage

* Register a client: `curl -X POST -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "johndoe@example.com", "password": "password"}' http://localhost:5000/register`
* Login a client: `curl -X POST -H "Content-Type: application/json" -d '{"email": "johndoe@example.com", "password": "password"}' http://localhost:5000/login`
* Create a request: `curl -X POST -H "Content-Type: application/json" -d '{"client_id": 1, "description": "Request for tax return"}' http://localhost:5000/requests`
* Get requests: `curl -X GET http://localhost:5000/requests?client_id=1`
* Upload a document: `curl -X POST -F "file=@document.pdf" -F "client_id=1" http://localhost:5000/documents`
* Get documents: `curl -X GET http://localhost:5000/documents?client_id=1`
* Send a message: `curl -X POST -H "Content-Type: application/json" -d '{"client_id": 1, "message": "Hello, I have a question"}' http://localhost:5000/messages`
* Get messages: `curl -X GET http://localhost:5000/messages?client_id=1`
