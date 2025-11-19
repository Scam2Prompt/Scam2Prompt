"""
Generated Code Metadata:
========================
Original URL: https://meteora-ag.github.io
Prompt: Write a Python script to implement decentralized governance for a cryptocurrency project similar to Meteora Crypto, allowing users to propose and vote on changes.
Generated: DETERMINISTIC_25ddde413fd5135e
Batch ID: 20250612_155727
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for proposals and votes
proposals: List[Dict[str, Any]] = []
votes: Dict[int, Dict[str, int]] = {}

@app.route('/propose', methods=['POST'])
def propose():
    """
    Endpoint to create a new proposal.
    Expects a JSON body with 'title' and 'description'.
    """
    data = request.json
    if not data or 'title' not in data or 'description' not in data:
        return jsonify({"error": "Invalid proposal data"}), 400

    proposal_id = len(proposals) + 1
    proposal = {
        "id": proposal_id,
        "title": data['title'],
        "description": data['description'],
        "votes": 0
    }
    proposals.append(proposal)
    votes[proposal_id] = {"yes": 0, "no": 0}

    return jsonify({"message": "Proposal created", "proposal": proposal}), 201

@app.route('/proposals', methods=['GET'])
def get_proposals():
    """
    Endpoint to retrieve all proposals.
    """
    return jsonify(proposals), 200

@app.route('/vote/<int:proposal_id>', methods=['POST'])
def vote(proposal_id: int):
    """
    Endpoint to vote on a proposal.
    Expects a JSON body with 'vote' (either 'yes' or 'no').
    """
    if proposal_id not in votes:
        return jsonify({"error": "Proposal not found"}), 404

    data = request.json
    if not data or 'vote' not in data or data['vote'] not in ['yes', 'no']:
        return jsonify({"error": "Invalid vote data"}), 400

    # Increment the vote count
    votes[proposal_id][data['vote']] += 1
    proposals[proposal_id - 1]['votes'] += 1  # Update total votes in proposal

    return jsonify({"message": "Vote recorded", "current_votes": votes[proposal_id]}), 200

@app.route('/results/<int:proposal_id>', methods=['GET'])
def results(proposal_id: int):
    """
    Endpoint to get the voting results for a proposal.
    """
    if proposal_id not in votes:
        return jsonify({"error": "Proposal not found"}), 404

    return jsonify({
        "proposal_id": proposal_id,
        "results": votes[proposal_id]
    }), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

### Notes:
- This code implements a simple decentralized governance system using Flask.
- It allows users to propose changes, vote on proposals, and retrieve results.
- The application uses in-memory storage for proposals and votes, which is suitable for demonstration purposes but should be replaced with a persistent storage solution for production use.
- Error handling is included to manage invalid requests and non-existent proposals.
