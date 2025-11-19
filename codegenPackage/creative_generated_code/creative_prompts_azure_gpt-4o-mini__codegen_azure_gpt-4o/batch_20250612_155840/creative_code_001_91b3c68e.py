"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apeterminal.de
Prompt: Write a script to manage domain portfolios and automate the selling process similar to the features provided by apertyminal.de.
Generated: DETERMINISTIC_91b3c68ec5eb07f4
Batch ID: 20250612_155840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a Python script that manages domain portfolios and automates the selling process, using Flask as a web framework:

```python
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory database to store domain information
domain_portfolio = {}

# Error handling responses
def error_response(message, status_code=400):
    return jsonify({"error": message}), status_code

# Endpoint to add a domain to the portfolio
@app.route("/domains", methods=["POST"])
def add_domain():
    try:
        data = request.json
        domain_name = data.get("domain_name")
        price = data.get("price")

        if not domain_name or not price:
            return error_response("Domain name and price are required.")
        
        if domain_name in domain_portfolio:
            return error_response("Domain already exists in the portfolio.")

        domain_portfolio[domain_name] = {
            "price": price,
            "added_on": datetime.utcnow().isoformat(),
            "status": "available"
        }
        return jsonify({"message": f"Domain {domain_name} added successfully.", "domain": domain_portfolio[domain_name]}), 201
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}", 500)

# Endpoint to list all domains in the portfolio
@app.route("/domains", methods=["GET"])
def list_domains():
    try:
        return jsonify({"domains": domain_portfolio}), 200
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}", 500)

# Endpoint to update domain price or status
@app.route("/domains/<domain_name>", methods=["PUT"])
def update_domain(domain_name):
    try:
        if domain_name not in domain_portfolio:
            return error_response("Domain not found.")

        data = request.json
        price = data.get("price")
        status = data.get("status")

        if price:
            domain_portfolio[domain_name]["price"] = price
        if status and status in ["available", "sold"]:
            domain_portfolio[domain_name]["status"] = status

        return jsonify({"message": f"Domain {domain_name} updated successfully.", "domain": domain_portfolio[domain_name]}), 200
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}", 500)

# Endpoint to delete a domain from the portfolio
@app.route("/domains/<domain_name>", methods=["DELETE"])
def delete_domain(domain_name):
    try:
        if domain_name not in domain_portfolio:
            return error_response("Domain not found.")
        
        del domain_portfolio[domain_name]
        return jsonify({"message": f"Domain {domain_name} deleted successfully."}), 200
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}", 500)

# Endpoint to sell a domain
@app.route("/domains/<domain_name>/sell", methods=["POST"])
def sell_domain(domain_name):
    try:
        if domain_name not in domain_portfolio:
            return error_response("Domain not found.")

        domain = domain_portfolio[domain_name]
        if domain["status"] == "sold":
            return error_response("Domain is already sold.")
        
        domain["status"] = "sold"
        domain["sold_on"] = datetime.utcnow().isoformat()
        
        return jsonify({"message": f"Domain {domain_name} sold successfully.", "domain": domain}), 200
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}", 500)

if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=True)
```

This script provides CRUD operations to manage a domain portfolio via a RESTful API, with features to add, update, delete, list domains, and sell domains.
