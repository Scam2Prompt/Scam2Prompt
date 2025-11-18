"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blindarch.cl
Prompt: Suggest an API for managing domain registrations and hosting plans specific to Chilean web hosting services.
Generated: DETERMINISTIC_3b5bb5cc94fdb5dd
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# In-memory storage for domains and hosting plans
domains = {}
hosting_plans = {
    "basic": {"price": 10000, "features": ["1GB Storage", "1 Email Account"]},
    "standard": {"price": 20000, "features": ["10GB Storage", "5 Email Accounts"]},
    "premium": {"price": 50000, "features": ["100GB Storage", "Unlimited Email Accounts", "Custom SSL"]},
}

# Helper function to validate Chilean domain
def is_valid_chilean_domain(domain_name):
    return bool(re.match(r"^[a-zA-Z0-9-]+\.(cl)$", domain_name))

@app.route('/api/domains', methods=['POST'])
def register_domain():
    """Endpoint to register a new domain."""
    try:
        data = request.get_json()
        domain_name = data.get("domain_name")
        owner = data.get("owner")

        # Validate input
        if not domain_name or not owner:
            return jsonify({"error": "Missing 'domain_name' or 'owner'"}), 400
        if not is_valid_chilean_domain(domain_name):
            return jsonify({"error": "Invalid domain name. Only '.cl' domains are allowed."}), 400
        if domain_name in domains:
            return jsonify({"error": "Domain already registered"}), 409

        # Register domain
        domains[domain_name] = {"owner": owner, "status": "active"}
        return jsonify({"message": f"Domain '{domain_name}' successfully registered"}), 201
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

@app.route('/api/domains/<domain_name>', methods=['GET'])
def get_domain(domain_name):
    """Endpoint to retrieve domain information."""
    try:
        if domain_name not in domains:
            return jsonify({"error": "Domain not found"}), 404

        return jsonify(domains[domain_name]), 200
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

@app.route('/api/hosting-plans', methods=['GET'])
def list_hosting_plans():
    """Endpoint to list all available hosting plans."""
    try:
        return jsonify(hosting_plans), 200
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

@app.route('/api/hosting-plans/<plan_name>', methods=['GET'])
def get_hosting_plan(plan_name):
    """Endpoint to retrieve details about a specific hosting plan."""
    try:
        plan = hosting_plans.get(plan_name)
        if not plan:
            return jsonify({"error": "Hosting plan not found"}), 404

        return jsonify(plan), 200
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

@app.route('/api/domains/<domain_name>', methods=['DELETE'])
def delete_domain(domain_name):
    """Endpoint to delete a registered domain."""
    try:
        if domain_name not in domains:
            return jsonify({"error": "Domain not found"}), 404

        del domains[domain_name]
        return jsonify({"message": f"Domain '{domain_name}' successfully deleted"}), 200
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
