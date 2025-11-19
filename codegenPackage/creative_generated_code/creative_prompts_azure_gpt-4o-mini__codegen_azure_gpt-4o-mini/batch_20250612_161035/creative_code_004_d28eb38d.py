"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeibpiht7izgwflj7ruju4tcwrl7b45xmoifhhch7hi47n5ip5du4c4.ipfs.dweb.link
Prompt: Illustrate how to implement a community voting system for a cryptocurrency project, taking cues from the SharkCat community ownership model.
Generated: DETERMINISTIC_d28eb38d48f1e1df
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///community_voting.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Community Proposal
class Proposal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    votes_for = db.Column(db.Integer, default=0)
    votes_against = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Model for User Vote
class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    proposal_id = db.Column(db.Integer, db.ForeignKey('proposal.id'), nullable=False)
    user_id = db.Column(db.String(100), nullable=False)  # Assuming user_id is a string
    vote_choice = db.Column(db.String(10), nullable=False)  # 'for' or 'against'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to create a new proposal
@app.route('/proposals', methods=['POST'])
def create_proposal():
    data = request.get_json()
    new_proposal = Proposal(title=data['title'], description=data['description'])

    try:
        db.session.add(new_proposal)
        db.session.commit()
        return jsonify({"message": "Proposal created", "id": new_proposal.id}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"message": "Failed to create proposal"}), 400

# Endpoint to vote on a proposal
@app.route('/proposals/<int:proposal_id>/vote', methods=['POST'])
def vote(proposal_id):
    data = request.get_json()
    user_id = data['user_id']
    vote_choice = data['vote_choice']

    if vote_choice not in ['for', 'against']:
        return jsonify({"message": "Invalid vote choice"}), 400

    # Check if the proposal exists
    proposal = Proposal.query.get(proposal_id)
    if not proposal:
        return jsonify({"message": "Proposal not found"}), 404

    # Check if the user has already voted
    existing_vote = Vote.query.filter_by(proposal_id=proposal_id, user_id=user_id).first()
    if existing_vote:
        return jsonify({"message": "User has already voted"}), 400

    # Create and save the vote
    new_vote = Vote(proposal_id=proposal_id, user_id=user_id, vote_choice=vote_choice)

    try:
        db.session.add(new_vote)
        if vote_choice == 'for':
            proposal.votes_for += 1
        else:
            proposal.votes_against += 1
        db.session.commit()
        return jsonify({"message": "Vote recorded"}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"message": "Failed to record vote"}), 400

# Endpoint to get proposal results
@app.route('/proposals/<int:proposal_id>', methods=['GET'])
def get_proposal(proposal_id):
    proposal = Proposal.query.get(proposal_id)
    if not proposal:
        return jsonify({"message": "Proposal not found"}), 404
    
    return jsonify({
        "id": proposal.id,
        "title": proposal.title,
        "description": proposal.description,
        "votes_for": proposal.votes_for,
        "votes_against": proposal.votes_against,
        "created_at": proposal.created_at
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
```
