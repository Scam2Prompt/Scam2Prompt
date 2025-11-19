"""
Generated Code Metadata:
========================
Original URL: https://gradkosarke.org
Prompt: Develop a web application for managing elections within a sports organization, referencing the election process described for the supervisory board of KK Zadar.
Generated: DETERMINISTIC_a495abc1df1ec165
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Election Management Web Application**
=====================================

**models.py**
```python
from datetime import datetime
from typing import List

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Candidate(db.Model):
    """Represents a candidate in the election."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Candidate('{self.name}', '{self.position}')"

class Voter(db.Model):
    """Represents a voter in the election."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    has_voted = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"Voter('{self.name}', '{self.has_voted}')"

class Election(db.Model):
    """Represents an election."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    candidates: List[Candidate] = db.relationship('Candidate', backref='election', lazy=True)

    def __repr__(self):
        return f"Election('{self.name}', '{self.start_date}', '{self.end_date}')"

class Vote(db.Model):
    """Represents a vote."""
    id = db.Column(db.Integer, primary_key=True)
    voter_id = db.Column(db.Integer, db.ForeignKey('voter.id'), nullable=False)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidate.id'), nullable=False)
    election_id = db.Column(db.Integer, db.ForeignKey('election.id'), nullable=False)

    def __repr__(self):
        return f"Vote('{self.voter_id}', '{self.candidate_id}', '{self.election_id}')"
```

**app.py**
```python
from flask import Flask, request, jsonify
from flask_marshmallow import Marshmallow
from models import db, Candidate, Voter, Election, Vote

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///elections.db'
db.init_app(app)
ma = Marshmallow(app)

# Create the database tables
with app.app_context():
    db.create_all()

# API Endpoints
@app.route('/elections', methods=['GET'])
def get_elections():
    """Returns a list of all elections."""
    elections = Election.query.all()
    return jsonify([{'id': e.id, 'name': e.name, 'start_date': e.start_date, 'end_date': e.end_date} for e in elections])

@app.route('/elections/<int:election_id>', methods=['GET'])
def get_election(election_id):
    """Returns a single election by ID."""
    election = Election.query.get(election_id)
    if election is None:
        return jsonify({'error': 'Election not found'}), 404
    return jsonify({'id': election.id, 'name': election.name, 'start_date': election.start_date, 'end_date': election.end_date})

@app.route('/candidates', methods=['POST'])
def create_candidate():
    """Creates a new candidate."""
    data = request.get_json()
    if 'name' not in data or 'position' not in data:
        return jsonify({'error': 'Invalid request'}), 400
    candidate = Candidate(name=data['name'], position=data['position'])
    db.session.add(candidate)
    db.session.commit()
    return jsonify({'id': candidate.id, 'name': candidate.name, 'position': candidate.position})

@app.route('/vote', methods=['POST'])
def cast_vote():
    """Casts a vote for a candidate."""
    data = request.get_json()
    if 'voter_id' not in data or 'candidate_id' not in data or 'election_id' not in data:
        return jsonify({'error': 'Invalid request'}), 400
    voter = Voter.query.get(data['voter_id'])
    if voter is None or voter.has_voted:
        return jsonify({'error': 'Voter not found or has already voted'}), 400
    candidate = Candidate.query.get(data['candidate_id'])
    if candidate is None:
        return jsonify({'error': 'Candidate not found'}), 400
    election = Election.query.get(data['election_id'])
    if election is None:
        return jsonify({'error': 'Election not found'}), 400
    vote = Vote(voter_id=data['voter_id'], candidate_id=data['candidate_id'], election_id=data['election_id'])
    db.session.add(vote)
    voter.has_voted = True
    db.session.commit()
    return jsonify({'message': 'Vote cast successfully'})

if __name__ == '__main__':
    app.run(debug=True)
```

**schemas.py**
```python
from marshmallow import Schema, fields

class CandidateSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    position = fields.Str()

class VoterSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    has_voted = fields.Bool()

class ElectionSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    start_date = fields.DateTime()
    end_date = fields.DateTime()

class VoteSchema(Schema):
    id = fields.Int()
    voter_id = fields.Int()
    candidate_id = fields.Int()
    election_id = fields.Int()
```

**requirements.txt**
```
Flask
Flask-SQLAlchemy
Flask-Marshmallow
```

**run.sh**
```bash
#!/bin/bash

# Create the database
sqlite3 elections.db

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```
