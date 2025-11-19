"""
Generated Code Metadata:
========================
Original URL: https://inqubeta-ai.web.app
Prompt: Design an API for InQubeta's governance system, enabling $QUBE token holders to propose, discuss, and vote on platform developments, and describe how to integrate it with the existing platform.
Generated: DETERMINISTIC_7e1c26260f746823
Batch ID: 20250622_204914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from datetime import datetime
import uuid

app = Flask(__name__)

# In-memory database for demonstration purposes
proposals = {}
votes = {}

# Error messages
ERROR_INVALID_INPUT = "Invalid input provided."
ERROR_PROPOSAL_NOT_FOUND = "Proposal not found."
ERROR_VOTE_ALREADY_CAST = "Vote already cast for this proposal."

# Helper function to validate input
def validate_input(data, required_fields):
    for field in required_fields:
        if field not in data:
            return False
    return True

# API endpoint to create a new proposal
@app.route('/proposals', methods=['POST'])
def create_proposal():
    """
    Create a new proposal.
    Request Body:
    {
        "title": "Proposal Title",
        "description": "Detailed description of the proposal",
        "creator": "Wallet address of the creator"
    }
    """
    data = request.json
    if not validate_input(data, ["title", "description", "creator"]):
        return jsonify({"error": ERROR_INVALID_INPUT}), 400

    proposal_id = str(uuid.uuid4())
    proposals[proposal_id] = {
        "id": proposal_id,
        "title": data["title"],
        "description": data["description"],
        "creator": data["creator"],
        "created_at": datetime.utcnow().isoformat(),
        "votes": {"yes": 0, "no": 0},
        "comments": []
    }
    return jsonify({"message": "Proposal created successfully.", "proposal_id": proposal_id}), 201

# API endpoint to list all proposals
@app.route('/proposals', methods=['GET'])
def list_proposals():
    """
    List all proposals.
    Response:
    [
        {
            "id": "Proposal ID",
            "title": "Proposal Title",
            "description": "Proposal Description",
            "creator": "Creator Wallet Address",
            "created_at": "Timestamp",
            "votes": {"yes": 0, "no": 0},
            "comments": []
        }
    ]
    """
    return jsonify(list(proposals.values())), 200

# API endpoint to vote on a proposal
@app.route('/proposals/<proposal_id>/vote', methods=['POST'])
def vote_on_proposal(proposal_id):
    """
    Vote on a proposal.
    Request Body:
    {
        "voter": "Wallet address of the voter",
        "vote": "yes" or "no"
    }
    """
    data = request.json
    if not validate_input(data, ["voter", "vote"]):
        return jsonify({"error": ERROR_INVALID_INPUT}), 400

    if proposal_id not in proposals:
        return jsonify({"error": ERROR_PROPOSAL_NOT_FOUND}), 404

    voter = data["voter"]
    vote = data["vote"]

    if vote not in ["yes", "no"]:
        return jsonify({"error": ERROR_INVALID_INPUT}), 400

    # Check if the voter has already voted
    if proposal_id in votes and voter in votes[proposal_id]:
        return jsonify({"error": ERROR_VOTE_ALREADY_CAST}), 400

    # Record the vote
    if proposal_id not in votes:
        votes[proposal_id] = {}
    votes[proposal_id][voter] = vote
    proposals[proposal_id]["votes"][vote] += 1

    return jsonify({"message": "Vote cast successfully."}), 200

# API endpoint to add a comment to a proposal
@app.route('/proposals/<proposal_id>/comment', methods=['POST'])
def comment_on_proposal(proposal_id):
    """
    Add a comment to a proposal.
    Request Body:
    {
        "commenter": "Wallet address of the commenter",
        "comment": "Text of the comment"
    }
    """
    data = request.json
    if not validate_input(data, ["commenter", "comment"]):
        return jsonify({"error": ERROR_INVALID_INPUT}), 400

    if proposal_id not in proposals:
        return jsonify({"error": ERROR_PROPOSAL_NOT_FOUND}), 404

    proposals[proposal_id]["comments"].append({
        "commenter": data["commenter"],
        "comment": data["comment"],
        "timestamp": datetime.utcnow().isoformat()
    })

    return jsonify({"message": "Comment added successfully."}), 200

# API endpoint to get details of a specific proposal
@app.route('/proposals/<proposal_id>', methods=['GET'])
def get_proposal(proposal_id):
    """
    Get details of a specific proposal.
    Response:
    {
        "id": "Proposal ID",
        "title": "Proposal Title",
        "description": "Proposal Description",
        "creator": "Creator Wallet Address",
        "created_at": "Timestamp",
        "votes": {"yes": 0, "no": 0},
        "comments": [
            {
                "commenter": "Wallet address of the commenter",
                "comment": "Text of the comment",
                "timestamp": "Timestamp"
            }
        ]
    }
    """
    if proposal_id not in proposals:
        return jsonify({"error": ERROR_PROPOSAL_NOT_FOUND}), 404

    return jsonify(proposals[proposal_id]), 200

# Error handling for invalid routes
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found."}), 404

# Integration with the existing platform
# To integrate this API with the existing platform:
# 1. Deploy this Flask application on a server or cloud service.
# 2. Ensure the platform's frontend interacts with this API using HTTP requests.
# 3. Use authentication mechanisms (e.g., JWT) to secure endpoints.
# 4. Connect the API to a persistent database for production use.

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
