"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://richpepe.vercel.app
Prompt: Generate code for a community-based voting system to manage decisions for a cryptocurrency token, inspired by the decentralized nature of "Rich Pepe."
Generated: DETERMINISTIC_52dd473feb1d03dd
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# community_voting_system.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///voting_system.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for storing voting proposals
class Proposal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    vote_yes_count = db.Column(db.Integer, default=0)
    vote_no_count = db.Column(db.Integer, default=0)
    
    def __repr__(self):
        return f'<Proposal {self.title}>'

# Model for storing votes
class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    proposal_id = db.Column(db.Integer, db.ForeignKey('proposal.id'), nullable=False)
    vote_value = db.Column(db.Boolean, nullable=False)  # True for yes, False for no

    def __repr__(self):
        return f'<Vote {self.id} for Proposal {self.proposal_id}>'

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to create a new proposal
@app.route('/proposals', methods=['POST'])
def create_proposal():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    
    if not title or not description:
        return jsonify({'error': 'Title and description are required'}), 400
    
    new_proposal = Proposal(title=title, description=description)
    
    try:
        db.session.add(new_proposal)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Failed to create proposal'}), 500
    
    return jsonify({'message': 'Proposal created', 'proposal_id': new_proposal.id}), 201

# Route to vote on a proposal
@app.route('/proposals/<int:proposal_id>/vote', methods=['POST'])
def vote_on_proposal(proposal_id):
    data = request.get_json()
    vote_value = data.get('vote_value')

    if vote_value not in [True, False]:
        return jsonify({'error': 'Invalid vote value, must be True (yes) or False (no)'}), 400

    # Check if the proposal exists
    proposal = Proposal.query.get(proposal_id)
    if not proposal:
        return jsonify({'error': 'Proposal not found'}), 404

    # Ensure that the user hasn't already voted (for simplicity, we are not tracking users in this example)
    new_vote = Vote(proposal_id=proposal_id, vote_value=vote_value)
    
    try:
        db.session.add(new_vote)
        if vote_value:
            proposal.vote_yes_count += 1
        else:
            proposal.vote_no_count += 1
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Failed to record vote'}), 500

    return jsonify({'message': 'Vote recorded', 'proposal_id': proposal_id}), 201

# Route to get the results of a proposal
@app.route('/proposals/<int:proposal_id>', methods=['GET'])
def get_proposal_results(proposal_id):
    proposal = Proposal.query.get(proposal_id)
    
    if not proposal:
        return jsonify({'error': 'Proposal not found'}), 404

    return jsonify({
        'title': proposal.title,
        'description': proposal.description,
        'yes_votes': proposal.vote_yes_count,
        'no_votes': proposal.vote_no_count,
        'created_at': proposal.created_at.isoformat()
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
```
