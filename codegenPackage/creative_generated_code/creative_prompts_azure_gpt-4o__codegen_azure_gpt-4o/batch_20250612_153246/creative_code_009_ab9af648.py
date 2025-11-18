"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://youngistaan.org
Prompt: Develop a REST API for NGOs to manage donor profiles and contributions, referencing Youngistaan Foundation's "Become a Real Hero" donation campaign.
Generated: DETERMINISTIC_ab9af64863ff484f
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

# Initialize Flask app
app = Flask(__name__)

# In-memory data storage (replace with a database in production)
donors = {}  # {donor_id: {name, email, contributions}}
contributions = {}  # {contribution_id: {donor_id, amount, campaign}}

# Error handling middleware
@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return jsonify({"error": e.name, "message": e.description}), e.code
    return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

# Endpoint: Get all donor profiles
@app.route('/donors', methods=['GET'])
def get_donors():
    return jsonify({"donors": donors})

# Endpoint: Add a new donor profile
@app.route('/donors', methods=['POST'])
def add_donor():
    try:
        data = request.json
        donor_id = len(donors) + 1
        donors[donor_id] = {
            "name": data["name"],
            "email": data["email"],
            "contributions": []
        }
        return jsonify({"message": "Donor added successfully", "donor_id": donor_id}), 201
    except KeyError:
        return jsonify({"error": "Missing required fields"}), 400

# Endpoint: Get specific donor profile
@app.route('/donors/<int:donor_id>', methods=['GET'])
def get_donor(donor_id):
    donor = donors.get(donor_id)
    if not donor:
        return jsonify({"error": "Donor not found"}), 404
    return jsonify(donor)

# Endpoint: Update donor profile
@app.route('/donors/<int:donor_id>', methods=['PUT'])
def update_donor(donor_id):
    donor = donors.get(donor_id)
    if not donor:
        return jsonify({"error": "Donor not found"}), 404

    data = request.json
    donor["name"] = data.get("name", donor["name"])
    donor["email"] = data.get("email", donor["email"])
    return jsonify({"message": "Donor profile updated successfully"})

# Endpoint: Delete donor profile
@app.route('/donors/<int:donor_id>', methods=['DELETE'])
def delete_donor(donor_id):
    if donor_id not in donors:
        return jsonify({"error": "Donor not found"}), 404
    del donors[donor_id]
    return jsonify({"message": "Donor profile deleted successfully"})

# Endpoint: Add a contribution
@app.route('/contributions', methods=['POST'])
def add_contribution():
    try:
        data = request.json
        contribution_id = len(contributions) + 1
        donor_id = data["donor_id"]
        if donor_id not in donors:
            return jsonify({"error": "Donor not found"}), 404

        contribution = {
            "donor_id": donor_id,
            "amount": data["amount"],
            "campaign": data.get("campaign", "Become a Real Hero")
        }
        contributions[contribution_id] = contribution
        donors[donor_id]["contributions"].append(contribution_id)
        return jsonify({"message": "Contribution added successfully", "contribution_id": contribution_id}), 201
    except KeyError:
        return jsonify({"error": "Missing required fields"}), 400

# Endpoint: Get all contributions
@app.route('/contributions', methods=['GET'])
def get_contributions():
    return jsonify({"contributions": contributions})

# Endpoint: Get contributions by donor
@app.route('/donors/<int:donor_id>/contributions', methods=['GET'])
def get_donor_contributions(donor_id):
    donor = donors.get(donor_id)
    if not donor:
        return jsonify({"error": "Donor not found"}), 404
    donor_contributions = [contributions[cid] for cid in donor["contributions"]]
    return jsonify({"contributions": donor_contributions})

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
