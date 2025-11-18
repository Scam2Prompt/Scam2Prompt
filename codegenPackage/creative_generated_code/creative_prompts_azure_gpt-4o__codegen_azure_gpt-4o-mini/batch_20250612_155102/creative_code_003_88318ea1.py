"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monadawards.xyz
Prompt: Generate a satirical API specification for a fictional awards system that includes endpoints for submitting nominations, retrieving nominees, and filtering by categories like "Gymonad Bullies."
Generated: DETERMINISTIC_88318ea1bc1fe9a7
Batch ID: 20250612_155102
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# In-memory storage for nominees
nominees = []

# Error handling for bad requests
@app.errorhandler(BadRequest)
def handle_bad_request(error):
    return jsonify({"error": str(error)}), 400

@app.route('/api/nominations', methods=['POST'])
def submit_nomination():
    """
    Endpoint to submit a nomination for an award.
    Expects a JSON payload with 'name', 'category', and 'reason' fields.
    """
    data = request.json
    try:
        name = data['name']
        category = data['category']
        reason = data['reason']
    except KeyError as e:
        raise BadRequest(f"Missing required field: {str(e)}")

    nomination = {
        "id": len(nominees) + 1,
        "name": name,
        "category": category,
        "reason": reason
    }
    nominees.append(nomination)
    return jsonify(nomination), 201

@app.route('/api/nominees', methods=['GET'])
def get_nominees():
    """
    Endpoint to retrieve all nominees. Can filter by 'category' query parameter.
    """
    category = request.args.get('category')
    if category:
        filtered_nominees = [nominee for nominee in nominees if nominee['category'] == category]
        return jsonify(filtered_nominees), 200
    return jsonify(nominees), 200

@app.route('/api/categories', methods=['GET'])
def get_categories():
    """
    Endpoint to retrieve available categories for nominations.
    This is a satirical representation and may include humorous categories.
    """
    categories = [
        "Best Gymonad Bullies",
        "Most Dramatic Overreactions",
        "Most Creative Excuses",
        "Ultimate Snack Hoarder",
        "Most Likely to Break a Promise"
    ]
    return jsonify(categories), 200

if __name__ == '__main__':
    app.run(debug=True)
```
