"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lethmixedslowpitch.com
Prompt: Develop a web application feature that allows teams to report their own scores using a shortcode, as described in Slo-Pitch Central's platform functionality.
Generated: DETERMINISTIC_86a9c90daf7335ad
Batch ID: 20250612_154949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a production-ready implementation using Python with Flask as the web framework. This code allows teams to report their scores via a shortcode.

```python
from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# In-memory storage for teams' scores
scores = {}

# Regular expression to validate shortcodes (example format: TEAM123-4)
SHORTCODE_PATTERN = r"^[A-Za-z]+\d+-\d+$"

@app.route('/report_score', methods=['POST'])
def report_score():
    """
    Endpoint to report a team's score using a shortcode.
    Example shortcode format: TEAM123-4
    """
    try:
        # Parse input data
        data = request.json
        if not data or 'shortcode' not in data:
            return jsonify({"error": "Missing 'shortcode' in request"}), 400

        shortcode = data['shortcode']

        # Validate shortcode format
        if not re.match(SHORTCODE_PATTERN, shortcode):
            return jsonify({"error": "Invalid shortcode format. Expected format: TEAM123-4"}), 400

        # Parse shortcode into team identifier and score
        team_identifier, score = shortcode.rsplit('-', 1)

        # Update or add score for the team
        scores[team_identifier] = int(score)

        return jsonify({"message": "Score reported successfully", "team": team_identifier, "score": int(score)}), 200

    except ValueError:
        # Handle cases where score is not convertible to integer
        return jsonify({"error": "Invalid score in shortcode"}), 400
    except Exception as e:
        # Catch-all error handling
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


@app.route('/get_scores', methods=['GET'])
def get_scores():
    """
    Endpoint to retrieve all reported scores.
    """
    try:
        return jsonify({"scores": scores}), 200
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

### Example Usage:
1. **POST /report_score**:
   - Request Body: `{"shortcode": "TEAM123-4"}`
   - Response: `{"message": "Score reported successfully", "team": "TEAM123", "score": 4}`

2. **GET /get_scores**:
   - Response: `{"scores": {"TEAM123": 4}}`

This web application provides error handling, input validation, and supports a simple in-memory storage for demonstration purposes. For production systems, you would replace in-memory storage with a database solution like PostgreSQL, MySQL, or MongoDB.
