"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gradkosarke.org
Prompt: Develop a web application for managing elections within a sports organization, referencing the election process described for the supervisory board of KK Zadar.
Generated: DETERMINISTIC_a495abc1df1ec165
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: app.py
# Description: Flask-based web application for managing elections in a sports organization.

from flask import Flask, request, jsonify
from datetime import datetime
import uuid

app = Flask(__name__)

# In-memory database (replace with a proper database in production)
elections = []
candidates = []
votes = []

# Utility function to generate unique IDs
def generate_id():
    return str(uuid.uuid4())

# Error handling middleware
@app.errorhandler(404)
def not_found_error(e):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({"error": "Internal server error"}), 500

@app.errorhandler(400)
def bad_request_error(e):
    return jsonify({"error": str(e)}), 400

# Route: Create a new election
@app.route('/elections', methods=['POST'])
def create_election():
    """
    Endpoint to create a new election.
    Request payload:
    {
        "name": "Supervisory Board Election",
        "start_date": "2023-10-01",
        "end_date": "2023-10-05"
    }
    """
    data = request.json
    try:
        name = data['name']
        start_date = datetime.strptime(data['start_date'], "%Y-%m-%d")
        end_date = datetime.strptime(data['end_date'], "%Y-%m-%d")
        
        if end_date <= start_date:
            raise ValueError("End date must be after start date.")
        
        election_id = generate_id()
        elections.append({
            "id": election_id,
            "name": name,
            "start_date": start_date,
            "end_date": end_date,
            "candidates": []
        })
        return jsonify({"message": "Election created successfully", "id": election_id}), 201
    
    except KeyError:
        return jsonify({"error": "Missing required fields"}), 400
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

# Route: Add a candidate to an election
@app.route('/elections/<election_id>/candidates', methods=['POST'])
def add_candidate(election_id):
    """
    Endpoint to add a candidate to an election.
    Request payload:
    {
        "name": "John Doe"
    }
    """
    data = request.json
    try:
        candidate_name = data['name']
        election = next((e for e in elections if e['id'] == election_id), None)
        
        if not election:
            raise ValueError("Election not found.")
        
        candidate_id = generate_id()
        candidate = {"id": candidate_id, "name": candidate_name}
        election['candidates'].append(candidate)
        return jsonify({"message": "Candidate added successfully", "id": candidate_id}), 201
    
    except KeyError:
        return jsonify({"error": "Missing required fields"}), 400
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

# Route: Cast a vote
@app.route('/elections/<election_id>/votes', methods=['POST'])
def cast_vote(election_id):
    """
    Endpoint to cast a vote for a candidate in an election.
    Request payload:
    {
        "candidate_id": "candidate-uuid"
    }
    """
    data = request.json
    try:
        candidate_id = data['candidate_id']
        election = next((e for e in elections if e['id'] == election_id), None)
        
        if not election:
            raise ValueError("Election not found.")
        
        candidate = next((c for c in election['candidates'] if c['id'] == candidate_id), None)
        
        if not candidate:
            raise ValueError("Candidate not found.")
        
        vote_id = generate_id()
        votes.append({"id": vote_id, "election_id": election_id, "candidate_id": candidate_id})
        return jsonify({"message": "Vote cast successfully", "id": vote_id}), 201
    
    except KeyError:
        return jsonify({"error": "Missing required fields"}), 400
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

# Route: Get election results
@app.route('/elections/<election_id>/results', methods=['GET'])
def get_results(election_id):
    """
    Endpoint to get election results.
    Response payload:
    {
        "election_id": "election-uuid",
        "results": [
            {"candidate_id": "candidate-uuid", "votes": 10},
            {"candidate_id": "candidate-uuid2", "votes": 5}
        ]
    }
    """
    try:
        election = next((e for e in elections if e['id'] == election_id), None)
        
        if not election:
            raise ValueError("Election not found.")
        
        results = {}
        for vote in votes:
            if vote['election_id'] == election_id:
                results[vote['candidate_id']] = results.get(vote['candidate_id'], 0) + 1
        
        formatted_results = [{"candidate_id": cid, "votes": count} for cid, count in results.items()]
        return jsonify({"election_id": election_id, "results": formatted_results}), 200
    
    except ValueError as e:
        return jsonify({"error": str(e)}), 404

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
