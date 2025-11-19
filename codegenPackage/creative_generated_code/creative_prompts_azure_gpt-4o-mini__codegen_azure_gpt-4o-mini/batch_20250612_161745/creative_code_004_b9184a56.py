"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lethmixedslowpitch.com
Prompt: How can teams report their scores easily on Slo-Pitch Central without complex accounts?
Generated: DETERMINISTIC_b9184a56e6008843
Batch ID: 20250612_161745
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

# Load the scores from a JSON file
def load_scores(filename='scores.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    return {}

# Save the scores to a JSON file
def save_scores(scores, filename='scores.json'):
    with open(filename, 'w') as file:
        json.dump(scores, file, indent=4)

@app.route('/report_score', methods=['POST'])
def report_score():
    """
    Endpoint to report team scores.

    Request JSON format:
    {
        "team_name": "Team A",
        "score": 10
    }

    Returns a success message and the updated scores.
    """
    data = request.get_json()
    
    # Validate input data
    if 'team_name' not in data or 'score' not in data:
        return jsonify({"error": "Invalid input, 'team_name' and 'score' are required"}), 400

    team_name = data['team_name']
    try:
        score = int(data['score'])
    except ValueError:
        return jsonify({"error": "Score must be an integer"}), 400

    # Load existing scores
    scores = load_scores()

    # Update the score for the team
    if team_name in scores:
        scores[team_name] += score
    else:
        scores[team_name] = score

    # Save the updated scores
    save_scores(scores)

    return jsonify({"message": "Score reported successfully", "scores": scores}), 200

@app.route('/get_scores', methods=['GET'])
def get_scores():
    """
    Endpoint to retrieve currently reported scores.

    Returns the scores in JSON format.
    """
    scores = load_scores()
    return jsonify(scores), 200

if __name__ == '__main__':
    app.run(debug=True)
```

### Note:
- To run this code, ensure you have Flask installed (`pip install Flask`).
- The scores will be stored in a file named `scores.json` in the same directory.
- The API provides two endpoints: `/report_score` for posting scores, and `/get_scores` for retrieving scores.
