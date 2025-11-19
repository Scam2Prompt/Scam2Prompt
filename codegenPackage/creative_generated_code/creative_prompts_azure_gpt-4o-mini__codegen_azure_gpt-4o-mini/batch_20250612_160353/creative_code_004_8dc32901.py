"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mansorytoken.xyz
Prompt: Develop a governance model for the Mansory Token community, allowing token holders to vote on future perks and research priorities.
Generated: DETERMINISTIC_8dc329015efce7f3
Batch ID: 20250612_160353
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
from flask_migrate import Migrate
from datetime import datetime
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///governance.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Model for Token Holder
class TokenHolder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(42), unique=True, nullable=False)  # Token holder's wallet address
    vote_count = db.Column(db.Integer, default=0)  # Count of votes cast by the holder

    def __repr__(self):
        return f'<TokenHolder {self.address}>'

# Model for Proposal
class Proposal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)  # Description of the proposal
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp of proposal creation
    votes = db.relationship('Vote', backref='proposal', lazy=True)  # Relationship to votes

    def __repr__(self):
        return f'<Proposal {self.id}: {self.description}>'

# Model for Vote
class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token_holder_id = db.Column(db.Integer, db.ForeignKey('token_holder.id'), nullable=False)  # Reference to token holder
    proposal_id = db.Column(db.Integer, db.ForeignKey('proposal.id'), nullable=False)  # Reference to proposal
    created_at = db.Column(db.DateTime, default=datetime.utcnow)  # Timestamp of vote

    def __repr__(self):
        return f'<Vote {self.id} by {self.token_holder_id} for Proposal {self.proposal_id}>'

# Route to create a new proposal
@app.route('/proposals', methods=['POST'])
def create_proposal():
    try:
        data = request.json
        new_proposal = Proposal(description=data['description'])
        db.session.add(new_proposal)
        db.session.commit()
        return jsonify({'message': 'Proposal created successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to vote on a proposal
@app.route('/vote', methods=['POST'])
def vote():
    try:
        data = request.json
        token_holder_address = data['address']
        proposal_id = data['proposal_id']

        # Check if the token holder exists or create a new one
        token_holder = TokenHolder.query.filter_by(address=token_holder_address).first()
        if not token_holder:
            token_holder = TokenHolder(address=token_holder_address)
            db.session.add(token_holder)

        # Create a new vote
        new_vote = Vote(token_holder=token_holder, proposal_id=proposal_id)
        db.session.add(new_vote)
        token_holder.vote_count += 1  # Increase vote count for the token holder
        db.session.commit()
        return jsonify({'message': 'Vote cast successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to list all proposals
@app.route('/proposals', methods=['GET'])
def list_proposals():
    try:
        proposals = Proposal.query.all()
        return jsonify([{'id': p.id, 'description': p.description, 'created_at': p.created_at} for p in proposals]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=os.environ.get('DEBUG', True), host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
```

Make sure to set the environment variable `DATABASE_URL` to your database connection string before running the application.
