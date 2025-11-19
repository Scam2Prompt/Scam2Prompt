"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beraborrow.org
Prompt: How can I implement a voting system for the $BERA Rewards Proposal that provides instant liquidity and rewards users?
Generated: DETERMINISTIC_945d2322fa8d9a6d
Batch ID: 20250612_162811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///voting_system.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    votes = db.relationship('Vote', backref='user', lazy=True)

# Define the Proposal model
class Proposal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    votes = db.relationship('Vote', backref='proposal', lazy=True)

# Define the Vote model
class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    proposal_id = db.Column(db.Integer, db.ForeignKey('proposal.id'), nullable=False)

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to register a new user
@app.route('/register', methods=['POST'])
def register_user():
    data = request.json
    username = data.get('username')

    if not username:
        return jsonify({'error': 'Username is required'}), 400

    new_user = User(username=username)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully!'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Username already exists!'}), 400

# Endpoint to create a new proposal
@app.route('/proposal', methods=['POST'])
def create_proposal():
    data = request.json
    title = data.get('title')

    if not title:
        return jsonify({'error': 'Proposal title is required'}), 400

    new_proposal = Proposal(title=title)

    db.session.add(new_proposal)
    db.session.commit()
    return jsonify({'message': 'Proposal created successfully!'}), 201

# Endpoint to vote on a proposal
@app.route('/vote', methods=['POST'])
def vote():
    data = request.json
    username = data.get('username')
    proposal_id = data.get('proposal_id')

    if not username or not proposal_id:
        return jsonify({'error': 'Username and proposal_id are required'}), 400

    user = User.query.filter_by(username=username).first()
    if user is None:
        return jsonify({'error': 'User not found'}), 404

    # Check if the user has already voted for the proposal
    existing_vote = Vote.query.filter_by(user_id=user.id, proposal_id=proposal_id).first()
    if existing_vote:
        return jsonify({'error': 'User has already voted for this proposal'}), 400

    new_vote = Vote(user_id=user.id, proposal_id=proposal_id)

    db.session.add(new_vote)
    db.session.commit()
    return jsonify({'message': 'Vote recorded successfully!'}), 201

# Endpoint to get all proposals with their vote counts
@app.route('/proposals', methods=['GET'])
def get_proposals():
    proposals = Proposal.query.all()
    results = []
    for proposal in proposals:
        results.append({
            'id': proposal.id,
            'title': proposal.title,
            'vote_count': len(proposal.votes)
        })
    return jsonify(results), 200

# Error handling for unexpected errors
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({'error': 'An unexpected error occurred: ' + str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
```
