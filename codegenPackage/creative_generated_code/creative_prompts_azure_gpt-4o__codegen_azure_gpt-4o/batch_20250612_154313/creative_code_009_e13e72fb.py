"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://syncconnects.com
Prompt: Create a REST API to manage member benefits and pricing tiers for a subscription-based community platform like Sync Connects.
Generated: DETERMINISTIC_e13e72fbbf88b641
Batch ID: 20250612_154313
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory data storage for simplicity
subscription_tiers = {
    "basic": {"price": 10, "benefits": ["Access to community forums"]},
    "premium": {"price": 25, "benefits": ["Access to forums", "Monthly webinars"]},
    "elite": {"price": 50, "benefits": ["All benefits", "One-on-one coaching"]}
}

# Error handler for general exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return jsonify({"error": str(e)}), e.code
    return jsonify({"error": "Internal Server Error"}), 500

# Endpoint: Get all subscription tiers
@app.route('/api/subscription-tiers', methods=['GET'])
def get_subscription_tiers():
    """
    Returns all subscription tiers and their details.
    """
    return jsonify(subscription_tiers), 200

# Endpoint: Get specific subscription tier details
@app.route('/api/subscription-tiers/<tier_name>', methods=['GET'])
def get_subscription_tier(tier_name):
    """
    Returns details of a specific subscription tier.
    """
    tier = subscription_tiers.get(tier_name.lower())
    if not tier:
        return jsonify({"error": f"Subscription tier '{tier_name}' not found."}), 404
    return jsonify(tier), 200

# Endpoint: Add a new subscription tier
@app.route('/api/subscription-tiers', methods=['POST'])
def add_subscription_tier():
    """
    Adds a new subscription tier. Requires 'name', 'price', and 'benefits' in the request body.
    """
    data = request.get_json()
    
    # Validate request data
    if not data or 'name' not in data or 'price' not in data or 'benefits' not in data:
        return jsonify({"error": "Missing required fields: 'name', 'price', or 'benefits'"}), 400

    tier_name = data['name'].lower()
    if tier_name in subscription_tiers:
        return jsonify({"error": f"Subscription tier '{tier_name}' already exists."}), 400
    
    subscription_tiers[tier_name] = {
        "price": data['price'],
        "benefits": data['benefits']
    }
    return jsonify({"message": f"Subscription tier '{tier_name}' added successfully."}), 201

# Endpoint: Update an existing subscription tier
@app.route('/api/subscription-tiers/<tier_name>', methods=['PUT'])
def update_subscription_tier(tier_name):
    """
    Updates details of an existing subscription tier. Requires 'price' and/or 'benefits' in the request body.
    """
    tier = subscription_tiers.get(tier_name.lower())
    if not tier:
        return jsonify({"error": f"Subscription tier '{tier_name}' not found."}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "Request body is empty."}), 400

    if 'price' in data:
        tier['price'] = data['price']
    if 'benefits' in data:
        tier['benefits'] = data['benefits']
    
    return jsonify({"message": f"Subscription tier '{tier_name}' updated successfully."}), 200

# Endpoint: Delete a subscription tier
@app.route('/api/subscription-tiers/<tier_name>', methods=['DELETE'])
def delete_subscription_tier(tier_name):
    """
    Deletes a specific subscription tier.
    """
    tier = subscription_tiers.pop(tier_name.lower(), None)
    if not tier:
        return jsonify({"error": f"Subscription tier '{tier_name}' not found."}), 404

    return jsonify({"message": f"Subscription tier '{tier_name}' deleted successfully."}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
