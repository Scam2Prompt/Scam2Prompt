"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://letz.dev
Prompt: Generate a code snippet for a web application that displays available domain names for sale, including features like making offers and checking bid statuses, inspired by letz.dev's listing.
Generated: DETERMINISTIC_84998bbed8c2ad24
Batch ID: 20250612_155155
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock data for domain listings
domains = [
    {"id": 1, "name": "letz.dev", "price": 500, "status": "available"},
    {"id": 2, "name": "codehub.dev", "price": 800, "status": "available"},
    {"id": 3, "name": "buildit.dev", "price": 400, "status": "sold"},
]

# Mock data for offers
offers = [
    {"domain_id": 1, "offer_id": 101, "offer_amount": 450, "status": "pending"},
    {"domain_id": 2, "offer_id": 102, "offer_amount": 750, "status": "rejected"},
]

@app.route('/domains', methods=['GET'])
def get_domains():
    """
    Endpoint to fetch all available domain listings.
    Returns a JSON object containing all domain listings.
    """
    available_domains = [domain for domain in domains if domain['status'] == "available"]
    return jsonify({"domains": available_domains}), 200

@app.route('/domains/<int:domain_id>/make_offer', methods=['POST'])
def make_offer(domain_id):
    """
    Endpoint to make an offer on a specific domain.
    Requires 'offer_amount' in the POST request body.
    """
    domain = next((domain for domain in domains if domain['id'] == domain_id), None)
    if not domain or domain['status'] != "available":
        return jsonify({"error": "Domain not found or not available"}), 404

    try:
        offer_amount = request.json['offer_amount']
        if offer_amount <= 0:
            return jsonify({"error": "Offer amount must be greater than zero"}), 400

        new_offer = {
            "domain_id": domain_id,
            "offer_id": len(offers) + 1,
            "offer_amount": offer_amount,
            "status": "pending"
        }
        offers.append(new_offer)

        return jsonify({"message": "Offer submitted successfully", "offer": new_offer}), 201
    except KeyError:
        return jsonify({"error": "Offer amount is required"}), 400

@app.route('/offers/<int:offer_id>/status', methods=['GET'])
def check_offer_status(offer_id):
    """
    Endpoint to check the status of a specific offer by its ID.
    """
    offer = next((offer for offer in offers if offer['offer_id'] == offer_id), None)
    if not offer:
        return jsonify({"error": "Offer not found"}), 404

    return jsonify({"offer_status": offer['status']}), 200

@app.errorhandler(404)
def not_found_error(error):
    """
    Handle 404 errors for undefined routes.
    """
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    """
    Handle unexpected server errors.
    """
    return jsonify({"error": "An internal error occurred"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
