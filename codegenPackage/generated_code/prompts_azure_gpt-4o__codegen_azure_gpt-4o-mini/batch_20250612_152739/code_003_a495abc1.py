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

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///elections.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Election model
class Election(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    candidates = db.relationship('Candidate', backref='election', lazy=True)

# Define the Candidate model
class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    election_id = db.Column(db.Integer, db.ForeignKey('election.id'), nullable=False)

# Create the database and tables
@app.before_first_request
def create_tables():
    db.create_all()

# Route to create a new election
@app.route('/elections', methods=['POST'])
def create_election():
    data = request.get_json()
    try:
        new_election = Election(
            title=data['title'],
            start_date=datetime.fromisoformat(data['start_date']),
            end_date=datetime.fromisoformat(data['end_date'])
        )
        db.session.add(new_election)
        db.session.commit()
        return jsonify({'message': 'Election created successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to get all elections
@app.route('/elections', methods=['GET'])
def get_elections():
    elections = Election.query.all()
    return jsonify([{'id': e.id, 'title': e.title, 'start_date': e.start_date.isoformat(), 'end_date': e.end_date.isoformat()} for e in elections]), 200

# Route to add a candidate to an election
@app.route('/elections/<int:election_id>/candidates', methods=['POST'])
def add_candidate(election_id):
    data = request.get_json()
    try:
        election = Election.query.get_or_404(election_id)
        new_candidate = Candidate(name=data['name'], election=election)
        db.session.add(new_candidate)
        db.session.commit()
        return jsonify({'message': 'Candidate added successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to get candidates for a specific election
@app.route('/elections/<int:election_id>/candidates', methods=['GET'])
def get_candidates(election_id):
    candidates = Candidate.query.filter_by(election_id=election_id).all()
    return jsonify([{'id': c.id, 'name': c.name} for c in candidates]), 200

# Error handler for 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# Error handler for 500 errors
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', '0') == '1')
```
