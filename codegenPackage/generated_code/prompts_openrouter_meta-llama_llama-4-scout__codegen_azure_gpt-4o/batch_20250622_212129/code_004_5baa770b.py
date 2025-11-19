"""
Generated Code Metadata:
========================
Original URL: https://symibyotic.fi
Prompt: Design a RESTful API for managing domain name sales, including endpoints for buying, leasing, and transferring domains, inspired by the features on symibyotic.fi.
Generated: DETERMINISTIC_5baa770b5edf323e
Batch ID: 20250622_212129
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory database for demonstration purposes
domains = {
    "example.com": {"status": "available", "price": 1000, "owner": None},
    "test.com": {"status": "leased", "price": 500, "owner": "user1"},
}

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({"error": e.name, "message": e.description}).get_data()
    response.content_type = "application/json"
    return response

# Error handler for general exceptions
@app.errorhandler(Exception)
def handle_general_exception(e):
    return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

# Endpoint to list all domains
@app.route("/domains", methods=["GET"])
def list_domains():
    """
    List all domains with their details.
    """
    return jsonify(domains)

# Endpoint to buy a domain
@app.route("/domains/buy/<domain_name>", methods=["POST"])
def buy_domain(domain_name):
    """
    Buy a domain if it is available.
    """
    domain = domains.get(domain_name)
    if not domain:
        return jsonify({"error": "Domain not found"}), 404

    if domain["status"] != "available":
        return jsonify({"error": "Domain is not available for purchase"}), 400

    buyer = request.json.get("buyer")
    if not buyer:
        return jsonify({"error": "Buyer information is required"}), 400

    domain["status"] = "sold"
    domain["owner"] = buyer
    return jsonify({"message": f"Domain '{domain_name}' purchased successfully", "domain": domain})

# Endpoint to lease a domain
@app.route("/domains/lease/<domain_name>", methods=["POST"])
def lease_domain(domain_name):
    """
    Lease a domain if it is available for leasing.
    """
    domain = domains.get(domain_name)
    if not domain:
        return jsonify({"error": "Domain not found"}), 404

    if domain["status"] != "available":
        return jsonify({"error": "Domain is not available for leasing"}), 400

    lessee = request.json.get("lessee")
    if not lessee:
        return jsonify({"error": "Lessee information is required"}), 400

    domain["status"] = "leased"
    domain["owner"] = lessee
    return jsonify({"message": f"Domain '{domain_name}' leased successfully", "domain": domain})

# Endpoint to transfer a domain
@app.route("/domains/transfer/<domain_name>", methods=["POST"])
def transfer_domain(domain_name):
    """
    Transfer ownership of a domain.
    """
    domain = domains.get(domain_name)
    if not domain:
        return jsonify({"error": "Domain not found"}), 404

    current_owner = domain.get("owner")
    if not current_owner:
        return jsonify({"error": "Domain does not have an owner"}), 400

    new_owner = request.json.get("new_owner")
    if not new_owner:
        return jsonify({"error": "New owner information is required"}), 400

    domain["owner"] = new_owner
    return jsonify({"message": f"Domain '{domain_name}' transferred successfully", "domain": domain})

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
```
