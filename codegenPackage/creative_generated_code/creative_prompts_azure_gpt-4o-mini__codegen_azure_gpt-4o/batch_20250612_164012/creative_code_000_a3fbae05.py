"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zk.fest.co
Prompt: How can I create a simple API to facilitate the sale of domain names like Fest.co?
Generated: DETERMINISTIC_a3fbae05013a6a83
Batch ID: 20250612_164012
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Filename: domain_sale_api.py

from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database to store domain listings
# In production, replace with a persistent database (e.g., PostgreSQL, MongoDB)
domain_listings = [
    {"id": 1, "domain": "fest.co", "price": 5000, "status": "available"},
    {"id": 2, "domain": "example.com", "price": 3000, "status": "available"},
]

# Error messages
NOT_FOUND_ERROR = {"error": "Domain not found"}
INVALID_REQUEST_ERROR = {"error": "Invalid request data"}

@app.route("/domains", methods=["GET"])
def get_domains():
    """
    Get all domain listings.
    Returns:
        JSON response with all available domain listings.
    """
    return jsonify(domain_listings), 200


@app.route("/domains/<int:domain_id>", methods=["GET"])
def get_domain(domain_id):
    """
    Get details of a specific domain listing by its ID.
    Args:
        domain_id (int): ID of the domain listing.
    Returns:
        JSON response with domain details or error message if not found.
    """
    domain = next((d for d in domain_listings if d["id"] == domain_id), None)
    if domain:
        return jsonify(domain), 200
    return jsonify(NOT_FOUND_ERROR), 404


@app.route("/domains", methods=["POST"])
def create_domain():
    """
    Create a new domain listing.
    Expects JSON in the request body with 'domain', 'price', and 'status'.
    Returns:
        JSON response with the created domain listing or error message.
    """
    try:
        data = request.get_json()
        # Validate input data
        if not data or "domain" not in data or "price" not in data or "status" not in data:
            return jsonify(INVALID_REQUEST_ERROR), 400

        # Create new domain listing
        new_domain = {
            "id": len(domain_listings) + 1,
            "domain": data["domain"],
            "price": data["price"],
            "status": data["status"],
        }
        domain_listings.append(new_domain)
        return jsonify(new_domain), 201
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


@app.route("/domains/<int:domain_id>", methods=["PUT"])
def update_domain(domain_id):
    """
    Update an existing domain listing.
    Expects JSON in the request body with 'domain', 'price', or 'status'.
    Args:
        domain_id (int): ID of the domain listing to update.
    Returns:
        JSON response with updated domain details or error message.
    """
    domain = next((d for d in domain_listings if d["id"] == domain_id), None)
    if not domain:
        return jsonify(NOT_FOUND_ERROR), 404

    try:
        data = request.get_json()
        # Update the domain listing fields if provided
        if "domain" in data:
            domain["domain"] = data["domain"]
        if "price" in data:
            domain["price"] = data["price"]
        if "status" in data:
            domain["status"] = data["status"]
        return jsonify(domain), 200
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


@app.route("/domains/<int:domain_id>", methods=["DELETE"])
def delete_domain(domain_id):
    """
    Delete a domain listing by its ID.
    Args:
        domain_id (int): ID of the domain listing to delete.
    Returns:
        JSON response with success message or error message if not found.
    """
    global domain_listings
    domain = next((d for d in domain_listings if d["id"] == domain_id), None)
    if not domain:
        return jsonify(NOT_FOUND_ERROR), 404

    domain_listings = [d for d in domain_listings if d["id"] != domain_id]
    return jsonify({"message": f"Domain with ID {domain_id} deleted successfully"}), 200


# Run the Flask app
if __name__ == "__main__":
    # Use built-in Flask development server for simplicity; replace with WSGI server in production (e.g., Gunicorn)
    app.run(debug=True, host="0.0.0.0", port=5000)
```
