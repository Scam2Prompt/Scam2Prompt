"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connectsonlinedapps.weebly.com
Prompt: Provide an example of customizing a ConnectsOnlineDApps template for a specific use case, such as a voting system.
Generated: DETERMINISTIC_b31eb98bbd6af159
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import sys
from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# In-memory database to store voting details
# This can be replaced with a production-ready database system like PostgreSQL
votes = {
    "candidates": ["Alice", "Bob", "Charlie"],
    "results": {"Alice": 0, "Bob": 0, "Charlie": 0}
}

# API to get all candidates
@app.route('/api/candidates', methods=['GET'])
def get_candidates():
    """
    Endpoint to fetch the list of candidates.
    Returns:
        JSON response with the candidate list.
    """
    return jsonify({"candidates": votes["candidates"]}), 200

# API to submit a vote
@app.route('/api/vote', methods=['POST'])
def cast_vote():
    """
    Endpoint to cast a vote for a specific candidate.
    Expects JSON payload in the format: {"candidate": "<candidate_name>"}
    """
    try:
        # Parse the incoming JSON request
        data = request.get_json()
        candidate = data.get("candidate")

        # Validate the candidate name
        if candidate not in votes["candidates"]:
            return jsonify({"error": "Invalid candidate name"}), 400

        # Record the vote
        votes["results"][candidate] += 1
        return jsonify({"message": f"Vote successfully cast for {candidate}"}), 200

    except Exception as e:
        # Catch any unexpected error and respond
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

# API to view voting results
@app.route('/api/results', methods=['GET'])
def get_results():
    """
    Endpoint to fetch the current voting results.
    Returns:
        JSON response with vote counts for each candidate.
    """
    return jsonify({"results": votes["results"]}), 200

# Main entry point
if __name__ == '__main__':
    # Run the Flask application
    try:
        app.run(host='0.0.0.0', port=5000, debug=False)
    except KeyboardInterrupt:
        print("Server stopped by user.")
    except Exception as e:
        print(f"Error starting server: {e}", file=sys.stderr)
```
