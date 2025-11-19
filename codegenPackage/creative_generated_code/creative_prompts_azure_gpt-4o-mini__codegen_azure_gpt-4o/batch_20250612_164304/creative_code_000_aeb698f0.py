"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rtfasfsa.pages.dev
Prompt: Generate code to create a web application that allows users to claim digital collectibles similar to the RTFKT Claim Drops feature.
Generated: DETERMINISTIC_aeb698f0c4f14573
Batch ID: 20250612_164304
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: app.py
# Description: Web application for claiming digital collectibles similar to RTFKT Claim Drops.
# Language: Python (Flask framework)

from flask import Flask, request, jsonify, render_template
import uuid

app = Flask(__name__)

# In-memory database for demo purposes
# In production, use an actual database like PostgreSQL, MySQL, or MongoDB
collectibles_db = [
    {"id": 1, "name": "Exclusive NFT #1", "claimed": False},
    {"id": 2, "name": "Exclusive NFT #2", "claimed": False},
    {"id": 3, "name": "Exclusive NFT #3", "claimed": False},
]

claim_history = []

@app.route('/')
def home():
    """Render the homepage with available collectibles."""
    return render_template('index.html', collectibles=collectibles_db)

@app.route('/claim/<int:collectible_id>', methods=['POST'])
def claim_collectible(collectible_id):
    """
    Endpoint to claim a digital collectible.
    Args:
        collectible_id: ID of the collectible to claim.
    Returns:
        JSON response with status and message.
    """
    try:
        # Find the collectible by ID
        collectible = next((item for item in collectibles_db if item["id"] == collectible_id), None)
        if not collectible:
            return jsonify({"status": "error", "message": "Collectible not found"}), 404
        if collectible["claimed"]:
            return jsonify({"status": "error", "message": "Collectible already claimed"}), 400

        # Update collectible status
        collectible["claimed"] = True

        # Record the claim in history
        claim_entry = {
            "id": str(uuid.uuid4()),
            "collectible_id": collectible_id,
            "name": collectible["name"],
            "claimed_by": request.remote_addr,
        }
        claim_history.append(claim_entry)

        return jsonify({"status": "success", "message": "Collectible claimed successfully", "details": claim_entry}), 200
    except Exception as e:
        # Generic error handling
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/claim-history', methods=['GET'])
def get_claim_history():
    """Endpoint to retrieve claim history."""
    return jsonify({"status": "success", "data": claim_history}), 200

if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=True)

```

```html
<!-- File: templates/index.html -->
<!-- Description: Homepage HTML template for displaying available collectibles -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Claim Digital Collectibles</title>
</head>
<body>
    <h1>Available Digital Collectibles</h1>
    <ul>
        {% for collectible in collectibles %}
        <li>
            <strong>{{ collectible.name }}</strong>
            {% if collectible.claimed %}
                <span style="color: red;">(Already Claimed)</span>
            {% else %}
                <form action="/claim/{{ collectible.id }}" method="post" style="display: inline;">
                    <button type="submit">Claim</button>
                </form>
            {% endif %}
        </li>
        {% endfor %}
    </ul>
</body>
</html>
```
