"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://popofrogg.pages.dev
Prompt: Write code to implement a community voting system for a cryptocurrency project, allowing members to make decisions collectively, as described in Popo's community-backed project model.
Generated: DETERMINISTIC_c29e102acdb73c0b
Batch ID: 20250612_145826
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
from werkzeug.exceptions import NotFound, BadRequest

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///voting_system.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Proposal(db.Model):
    """Model for a voting proposal."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    votes_for = db.Column(db.Integer, default=0)
    votes_against = db.Column(db.Integer, default=0)
    is_active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f"<Proposal {self.id}: {self.title}>"

@app.route('/proposals', methods=['POST'])
def create_proposal():
    """Endpoint to create a new proposal."""
    data = request.get_json()

    if not data or not all(k in data for k in ("title", "description")):
        raise BadRequest("Title and description are required.")

    new_proposal = Proposal(title=data['title'], description=data['description'])
    db.session.add(new_proposal)
    db.session.commit()
    
    return jsonify({"id": new_proposal.id}), 201

@app.route('/proposals', methods=['GET'])
def get_proposals():
    """Endpoint to get all proposals."""
    proposals = Proposal.query.filter_by(is_active=True).all()
    return jsonify([{"id": p.id, "title": p.title, "description": p.description, 
                     "votes_for": p.votes_for, "votes_against": p.votes_against} for p in proposals])

@app.route('/proposals/<int:proposal_id>/vote', methods=['POST'])
def vote_on_proposal(proposal_id):
    """Endpoint to vote on a proposal."""
    proposal = Proposal.query.get(proposal_id)
    if not proposal or not proposal.is_active:
        raise NotFound("Proposal not found or is no longer active.")

    data = request.get_json()
    if not data or 'vote' not in data:
        raise BadRequest("Vote is required.")

    if data['vote'] == 'for':
        proposal.votes_for += 1
    elif data['vote'] == 'against':
        proposal.votes_against += 1
    else:
        raise BadRequest("Invalid vote. Use 'for' or 'against'.")

    db.session.commit()
    return jsonify({"message": "Vote counted.", "votes_for": proposal.votes_for, "votes_against": proposal.votes_against})

@app.route('/proposals/<int:proposal_id>', methods=['DELETE'])
def delete_proposal(proposal_id):
    """Endpoint to delete a proposal."""
    proposal = Proposal.query.get(proposal_id)
    if not proposal:
        raise NotFound("Proposal not found.")

    proposal.is_active = False
    db.session.commit()
    return jsonify({"message": "Proposal deleted."}), 204

@app.errorhandler(NotFound)
def handle_not_found(error):
    """Handler for 404 errors."""
    return jsonify({"error": str(error)}), 404

@app.errorhandler(BadRequest)
def handle_bad_request(error):
    """Handler for 400 errors."""
    return jsonify({"error": str(error)}), 400

if __name__ == '__main__':
    # Create the database if it doesn't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
