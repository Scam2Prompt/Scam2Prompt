"""
Generated Code Metadata:
========================
Original URL: https://fareadda.com
Prompt: Design a simple API for a domain lookup service like the one mentioned on fareadda.com, including endpoints for searching and purchasing domains.
Generated: DETERMINISTIC_1993b8a21cbbbe5f
Batch ID: 20250622_204703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# Mock database for domain information
domains_db = {
    "example.com": {"available": True, "price": 10.99},
    "test.com": {"available": False, "price": None},
    "mywebsite.org": {"available": True, "price": 12.99},
}

# Helper function to validate domain names
def is_valid_domain(domain_name):
<<<<<<< HEAD
    # Regex for basic domain name validation
    domain_regex = r"^(?!-)[A-Za-z0-9-]{1,63}(?<!-)\.[A-Za-z]{2,6}$"
    return re.match(domain_regex, domain_name) is not None

@app.route("/api/domain/search", methods=["GET"])
=======
    # Regex for validating domain names
    domain_regex = r"^(?!-)[A-Za-z0-9-]{1,63}(?<!-)\.[A-Za-z]{2,6}$"
    return re.match(domain_regex, domain_name) is not None

@app.route('/api/domain/search', methods=['GET'])
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
def search_domain():
    """
    Endpoint to search for domain availability and price.
    Query Parameter: domain (string) - The domain name to search for.
    Returns: JSON response with domain availability and price.
    """
<<<<<<< HEAD
    domain_name = request.args.get("domain")
=======
    domain_name = request.args.get('domain')
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
    
    if not domain_name:
        return jsonify({"error": "Domain name is required"}), 400
    
    if not is_valid_domain(domain_name):
        return jsonify({"error": "Invalid domain name format"}), 400
    
    domain_info = domains_db.get(domain_name)
    
    if domain_info:
        return jsonify({
            "domain": domain_name,
            "available": domain_info["available"],
            "price": domain_info["price"]
        })
    else:
        return jsonify({"error": "Domain not found"}), 404

<<<<<<< HEAD
@app.route("/api/domain/purchase", methods=["POST"])
=======
@app.route('/api/domain/purchase', methods=['POST'])
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
def purchase_domain():
    """
    Endpoint to purchase a domain.
    Request Body: JSON with 'domain' (string) - The domain name to purchase.
<<<<<<< HEAD
    Returns: JSON response indicating success or failure of the purchase.
    """
    data = request.get_json()
    
    if not data or "domain" not in data:
        return jsonify({"error": "Domain name is required"}), 400
    
    domain_name = data["domain"]
=======
    Returns: JSON response with purchase status.
    """
    data = request.get_json()
    
    if not data or 'domain' not in data:
        return jsonify({"error": "Domain name is required"}), 400
    
    domain_name = data['domain']
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
    
    if not is_valid_domain(domain_name):
        return jsonify({"error": "Invalid domain name format"}), 400
    
    domain_info = domains_db.get(domain_name)
    
    if not domain_info:
        return jsonify({"error": "Domain not found"}), 404
    
    if not domain_info["available"]:
        return jsonify({"error": "Domain is not available for purchase"}), 400
    
    # Simulate domain purchase
    domain_info["available"] = False
    return jsonify({
        "message": f"Domain '{domain_name}' purchased successfully!",
        "price": domain_info["price"]
    })

# Error handler for unexpected server errors
@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({"error": "An unexpected error occurred"}), 500

# Run the Flask application
<<<<<<< HEAD
if __name__ == "__main__":
=======
if __name__ == '__main__':
>>>>>>> 10360aee73f (add full contents for codegen_disallow_original_url)
    app.run(debug=True)
```
