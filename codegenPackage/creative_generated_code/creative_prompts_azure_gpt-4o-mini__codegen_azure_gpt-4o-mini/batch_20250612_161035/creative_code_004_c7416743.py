"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globalmiracle.online
Prompt: Illustrate how to implement a decentralized voting system for community-driven governance within the Global Miracle Coin ecosystem.
Generated: DETERMINISTIC_c741674302d86c33
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import json
from datetime import datetime
from flask import Flask, jsonify, request

app = Flask(__name__)

class Vote:
    def __init__(self, voter_id, proposal, timestamp=None):
        self.voter_id = voter_id
        self.proposal = proposal
        self.timestamp = timestamp or datetime.utcnow().isoformat()
        self.signature = self.sign_vote()

    def sign_vote(self):
        """Generate a unique signature for the vote based on its contents."""
        vote_data = json.dumps(self.__dict__, sort_keys=True).encode()
        return hashlib.sha256(vote_data).hexdigest()

class VotingSystem:
    def __init__(self):
        self.votes = []
        self.proposals = []

    def add_proposal(self, proposal):
        """Add a new proposal to the voting system."""
        self.proposals.append(proposal)

    def cast_vote(self, voter_id, proposal):
        """Cast a vote for a specific proposal."""
        if proposal not in self.proposals:
            return {"error": "Proposal does not exist."}, 404
        
        if any(vote.voter_id == voter_id for vote in self.votes):
            return {"error": "Voter has already cast a vote."}, 400
        
        new_vote = Vote(voter_id, proposal)
        self.votes.append(new_vote)
        return {"message": "Vote cast successfully."}, 201

    def tally_votes(self):
        """Tally the votes for each proposal."""
        tally = {}
        for vote in self.votes:
            tally[vote.proposal] = tally.get(vote.proposal, 0) + 1
        return tally

voting_system = VotingSystem()

@app.route('/proposals', methods=['POST'])
def add_proposal():
    """Endpoint to add a new proposal."""
    data = request.get_json()
    proposal = data.get('proposal', None)
    
    if not proposal:
        return {"error": "Proposal text is required."}, 400

    voting_system.add_proposal(proposal)
    return {"message": "Proposal added successfully."}, 201

@app.route('/vote', methods=['POST'])
def vote():
    """Endpoint to cast a vote."""
    data = request.get_json()
    voter_id = data.get('voter_id', None)
    proposal = data.get('proposal', None)
    
    if not voter_id or not proposal:
        return {"error": "Voter ID and proposal are required."}, 400

    result, status = voting_system.cast_vote(voter_id, proposal)
    return result, status

@app.route('/tally', methods=['GET'])
def tally():
    """Endpoint to tally votes."""
    return jsonify(voting_system.tally_votes()), 200

if __name__ == '__main__':
    app.run(debug=True)
```

This code implements a simple decentralized voting system with Flask, allowing users to add proposals, cast votes, and tally them. The code includes error handling for various scenarios and is structured for clarity and maintainability, following best practices.
