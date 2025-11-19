"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://y45y45hy45y45y54.pages.dev
Prompt: Provide an example of how to create a participant tracking system that allows users to connect and register, based on the features outlined in the Sophon Time documentation.
Generated: DETERMINISTIC_6a238337b5f8725c
Batch ID: 20250612_164316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError
import os
import bcrypt

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///participants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Participant model
class Participant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

# Create a schema for input validation
class ParticipantSchema(Schema):
    username = fields.Str(required=True, validate=lambda s: len(s) > 0)
    password = fields.Str(required=True, validate=lambda s: len(s) >= 6)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to register a new participant
@app.route('/register', methods=['POST'])
def register():
    # Validate request data
    try:
        schema = ParticipantSchema()
        data = schema.load(request.json)
    except ValidationError as e:
        return jsonify({"error": e.messages}), 400

    # Check if username already exists
    if Participant.query.filter_by(username=data['username']).first():
        return jsonify({"error": "Username already exists."}), 400

    # Hash the password
    hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())

    # Create new participant
    new_participant = Participant(username=data['username'], password_hash=hashed_password)
    db.session.add(new_participant)
    db.session.commit()

    return jsonify({"message": "Participant registered successfully."}), 201

# Endpoint to connect (login) a participant
@app.route('/login', methods=['POST'])
def login():
    # Validate request data
    try:
        schema = ParticipantSchema(partial=('password',))
        data = schema.load(request.json)
    except ValidationError as e:
        return jsonify({"error": e.messages}), 400

    # Retrieve participant by username
    participant = Participant.query.filter_by(username=data['username']).first()
    if participant is None or not bcrypt.checkpw(data['password'].encode('utf-8'), participant.password_hash.encode('utf-8')):
        return jsonify({"error": "Invalid username or password."}), 401

    return jsonify({"message": "Login successful."}), 200

# Run the app
if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', True))
```
