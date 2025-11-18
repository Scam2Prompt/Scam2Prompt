"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maker-rewards.com
Prompt: Generate code to create an API for managing exchange offers, ensuring compatibility with features like "No Cost EMI" and "Bajaj Finserv," as described on Snapdeal.
Generated: DETERMINISTIC_59de462b79b6ceb4
Batch ID: 20250612_150048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data to simulate a database
exchange_offers = [
    {
        "id": 1,
        "product_name": "Smartphone A",
        "no_cost_emi": True,
        "bajaj_finserv_available": True,
        "offer_details": "Exchange your old smartphone and get ₹2000 off."
    },
    {
        "id": 2,
        "product_name": "Smartphone B",
        "no_cost_emi": False,
        "bajaj_finserv_available": True,
        "offer_details": "Exchange your old tablet and get ₹1500 off."
    },
]

@app.route('/api/exchange-offers', methods=['GET'])
def get_exchange_offers():
    """
    Endpoint to fetch all exchange offers.
    Returns:
        JSON response containing list of all exchange offers.
    """
    return jsonify({"exchange_offers": exchange_offers}), 200

@app.route('/api/exchange-offers/<int:offer_id>', methods=['GET'])
def get_exchange_offer_by_id(offer_id):
    """
    Endpoint to fetch a specific exchange offer by ID.
    Args:
        offer_id (int): ID of the exchange offer.
    Returns:
        JSON response containing offer details if found, or error message.
    """
    offer = next((offer for offer in exchange_offers if offer["id"] == offer_id), None)
    if offer:
        return jsonify({"exchange_offer": offer}), 200
    else:
        return jsonify({"error": "Exchange offer not found"}), 404

@app.route('/api/exchange-offers', methods=['POST'])
def add_exchange_offer():
    """
    Endpoint to add a new exchange offer.
    Expected JSON payload:
        {
            "product_name": str,
            "no_cost_emi": bool,
            "bajaj_finserv_available": bool,
            "offer_details": str
        }
    Returns:
        JSON response with the newly added offer or an error message.
    """
    try:
        data = request.get_json()
        if not data or not all(key in data for key in ["product_name", "no_cost_emi", "bajaj_finserv_available", "offer_details"]):
            return jsonify({"error": "Invalid payload"}), 400

        new_offer = {
            "id": len(exchange_offers) + 1,
            "product_name": data["product_name"],
            "no_cost_emi": data["no_cost_emi"],
            "bajaj_finserv_available": data["bajaj_finserv_available"],
            "offer_details": data["offer_details"],
        }
        exchange_offers.append(new_offer)
        return jsonify({"message": "Exchange offer added successfully", "exchange_offer": new_offer}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/exchange-offers/<int:offer_id>', methods=['PUT'])
def update_exchange_offer(offer_id):
    """
    Endpoint to update an existing exchange offer.
    Args:
        offer_id (int): ID of the exchange offer to update.
    Expected JSON payload:
        {
            "product_name": str,
            "no_cost_emi": bool,
            "bajaj_finserv_available": bool,
            "offer_details": str
        }
    Returns:
        JSON response with the updated offer or an error message.
    """
    try:
        data = request.get_json()
        offer = next((offer for offer in exchange_offers if offer["id"] == offer_id), None)
        if not offer:
            return jsonify({"error": "Exchange offer not found"}), 404
        if not data or not all(key in data for key in ["product_name", "no_cost_emi", "bajaj_finserv_available", "offer_details"]):
            return jsonify({"error": "Invalid payload"}), 400
        
        offer.update({
            "product_name": data["product_name"],
            "no_cost_emi": data["no_cost_emi"],
            "bajaj_finserv_available": data["bajaj_finserv_available"],
            "offer_details": data["offer_details"],
        })
        return jsonify({"message": "Exchange offer updated successfully", "exchange_offer": offer}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/exchange-offers/<int:offer_id>', methods=['DELETE'])
def delete_exchange_offer(offer_id):
    """
    Endpoint to delete an exchange offer by ID.
    Args:
        offer_id (int): ID of the exchange offer to delete.
    Returns:
        JSON response with a success or error message.
    """
    offer = next((offer for offer in exchange_offers if offer["id"] == offer_id), None)
    if not offer:
        return jsonify({"error": "Exchange offer not found"}), 404
    exchange_offers.remove(offer)
    return jsonify({"message": f"Exchange offer with ID {offer_id} deleted successfully"}), 200

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
```
