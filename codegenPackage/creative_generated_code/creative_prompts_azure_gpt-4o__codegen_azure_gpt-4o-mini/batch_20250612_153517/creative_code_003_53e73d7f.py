"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://videtisconsultores.es
Prompt: Suggest tools or frameworks to build a candidate tracking system for Videtis Consultores' talent acquisition services.
Generated: DETERMINISTIC_53e73d7fb67402f3
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Candidate Tracking System - Videtis Consultores

This script provides a basic structure for a candidate tracking system using Flask, SQLAlchemy, and Marshmallow.
It includes models for candidates and job postings, a simple REST API, and basic error handling.
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.exc import IntegrityError

# Initialize Flask app
app = Flask(__name__)

# Set up database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///candidates.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and Marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Candidate Model
class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(15), nullable=True)
    resume = db.Column(db.Text, nullable=True)

    def __init__(self, name, email, phone, resume):
        self.name = name
        self.email = email
        self.phone = phone
        self.resume = resume

# Candidate Schema
class CandidateSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Candidate

# Create the database
with app.app_context():
    db.create_all()

# Create a new candidate
@app.route('/candidates', methods=['POST'])
def add_candidate():
    try:
        data = request.json
        new_candidate = Candidate(
            name=data['name'],
            email=data['email'],
            phone=data.get('phone'),
            resume=data.get('resume')
        )
        db.session.add(new_candidate)
        db.session.commit()
        return CandidateSchema().jsonify(new_candidate), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Candidate with this email already exists."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Get all candidates
@app.route('/candidates', methods=['GET'])
def get_candidates():
    candidates = Candidate.query.all()
    return CandidateSchema(many=True).jsonify(candidates)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```
