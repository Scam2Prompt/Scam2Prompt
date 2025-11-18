"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.virtualmediaevents.com
Prompt: Write code to integrate a virtual passport feature for event participants, as described on the Virtual Media Events platform, ensuring secure attendee identification and management.
Generated: DETERMINISTIC_7208ee300511c54b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
import json
import hashlib
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from itsdangerous import URLSafeTimedSerializer, BadSignature, SignatureExpired

# Initialize the Flask application
app = Flask(__name__)

# Configuration for the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///event_participants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Serializer for generating secure tokens
s = URLSafeTimedSerializer(app.secret_key)

# Database model for event participants
class Participant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    passport_id = db.Column(db.String(36), unique=True, nullable=False)

    def __repr__(self):
        return f"<Participant {self.name}>"

# Function to generate a secure virtual passport
def generate_passport(email):
    """
    Generate a unique passport ID for the participant using UUID and hashing.
    """
    unique_id = uuid.uuid4()
    hashed_id = hashlib.sha256(unique_id.bytes).hexdigest()
    return hashed_id

# Route to register a new participant
@app.route('/register', methods=['POST'])
def register():
    """
    Register a new participant and generate a virtual passport.
    """
    data = request.get_json()
    
    # Input validation
    if 'name' not in data or 'email' not in data:
        return jsonify({"error": "Name and email are required."}), 400
    
    # Check if the email is already registered
    existing_participant = Participant.query.filter_by(email=data['email']).first()
    if existing_participant:
        return jsonify({"error": "Email is already registered."}), 400

    try:
        # Create a new participant
        passport_id = generate_passport(data['email'])
        participant = Participant(name=data['name'], email=data['email'], passport_id=passport_id)
        db.session.add(participant)
        db.session.commit()
        
        return jsonify({"message": "Participant registered successfully.", "passport_id": passport_id}), 201
    except Exception as e:
        # Handle any database errors
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Route to verify a passport
@app.route('/verify_passport/<passport_id>', methods=['GET'])
def verify_passport(passport_id):
    """
    Verify the passport ID to identify the participant.
    """
    try:
        participant = Participant.query.filter_by(passport_id=passport_id).first()
        if participant:
            return jsonify({"name": participant.name, "email": participant.email}), 200
        else:
            return jsonify({"error": "Passport ID not found."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Initialize the database on startup
@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    # Run the application in debug mode
    app.run(debug=False)
```
