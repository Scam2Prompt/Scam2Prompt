"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://worldlibertyfinanciallabs.com
Prompt: Illustrate how to integrate community-driven governance features into a financial application using the principles outlined by the People's World Liberty Financial DAO.
Generated: DETERMINISTIC_e3f2eb3703555075
Batch ID: 20250612_162711
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)

# Configuration for the SQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dao_financial_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for a governance proposal
class Proposal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default='pending')  # pending, approved, rejected
    votes_for = db.Column(db.Integer, default=0)
    votes_against = db.Column(db.Integer, default=0)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to create a new proposal
@app.route('/proposals', methods=['POST'])
def create_proposal():
    data = request.get_json()
    try:
        new_proposal = Proposal(
            title=data['title'],
            description=data['description']
        )
        db.session.add(new_proposal)
        db.session.commit()
        return jsonify({'message': 'Proposal created!', 'id': new_proposal.id}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Proposal creation failed due to integrity constraints.'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to cast a vote on a proposal
@app.route('/proposals/<int:proposal_id>/vote', methods=['POST'])
def vote_on_proposal(proposal_id):
    data = request.get_json()
    vote = data.get('vote')

    # Validate vote input
    if vote not in ['for', 'against']:
        return jsonify({'error': 'Vote must be "for" or "against".'}), 400
    
    proposal = Proposal.query.get_or_404(proposal_id)
    
    if vote == 'for':
        proposal.votes_for += 1
    else:
        proposal.votes_against += 1

    db.session.commit()
    return jsonify({'message': 'Vote counted!', 'proposal_id': proposal_id}), 200

# Route to get proposal details including vote counts
@app.route('/proposals/<int:proposal_id>', methods=['GET'])
def get_proposal(proposal_id):
    proposal = Proposal.query.get_or_404(proposal_id)
    return jsonify({
        'id': proposal.id,
        'title': proposal.title,
        'description': proposal.description,
        'status': proposal.status,
        'votes_for': proposal.votes_for,
        'votes_against': proposal.votes_against
    }), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

This code defines a simple financial application that incorporates community-driven governance features through a DAO-like proposal and voting system.
