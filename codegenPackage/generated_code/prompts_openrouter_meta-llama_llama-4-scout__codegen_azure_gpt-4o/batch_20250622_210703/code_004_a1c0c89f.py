"""
Generated Code Metadata:
========================
Original URL: https://kadma-wine.co.il
Prompt: "Design a RESTful API for a wine club platform, allowing users to purchase wines, manage subscriptions, and access exclusive content, similar to Kadma Wine's services."
Generated: DETERMINISTIC_a1c0c89f1194d3da
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Mock database
wines = [
    {"id": 1, "name": "Cabernet Sauvignon", "price": 50.0, "stock": 10},
    {"id": 2, "name": "Pinot Noir", "price": 45.0, "stock": 15},
]
subscriptions = [
    {"id": 1, "user_id": 1, "type": "Premium", "status": "Active"},
    {"id": 2, "user_id": 2, "type": "Basic", "status": "Active"},
]
exclusive_content = [
    {"id": 1, "title": "Wine Pairing Tips", "content": "Learn how to pair wines with food."},
    {"id": 2, "title": "Exclusive Wine Regions", "content": "Explore hidden wine regions."},
]

# Error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({"error": e.name, "message": e.description}).get_data()
    response.content_type = "application/json"
    return response

# Error handler for generic exceptions
@app.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

# Route: Get all wines
@app.route('/api/wines', methods=['GET'])
def get_wines():
    return jsonify(wines), 200

# Route: Purchase a wine
@app.route('/api/wines/<int:wine_id>/purchase', methods=['POST'])
def purchase_wine(wine_id):
    wine = next((w for w in wines if w["id"] == wine_id), None)
    if not wine:
        return jsonify({"error": "Wine not found"}), 404
    if wine["stock"] <= 0:
        return jsonify({"error": "Out of stock"}), 400
    wine["stock"] -= 1
    return jsonify({"message": f"{wine['name']} purchased successfully!"}), 200

# Route: Get all subscriptions
@app.route('/api/subscriptions', methods=['GET'])
def get_subscriptions():
    return jsonify(subscriptions), 200

# Route: Manage subscription (update status)
@app.route('/api/subscriptions/<int:subscription_id>', methods=['PUT'])
def update_subscription(subscription_id):
    subscription = next((s for s in subscriptions if s["id"] == subscription_id), None)
    if not subscription:
        return jsonify({"error": "Subscription not found"}), 404
    data = request.json
    if "status" not in data:
        return jsonify({"error": "Missing 'status' field"}), 400
    subscription["status"] = data["status"]
    return jsonify({"message": "Subscription updated successfully!"}), 200

# Route: Get exclusive content
@app.route('/api/exclusive-content', methods=['GET'])
def get_exclusive_content():
    return jsonify(exclusive_content), 200

# Route: Get specific exclusive content
@app.route('/api/exclusive-content/<int:content_id>', methods=['GET'])
def get_specific_content(content_id):
    content = next((c for c in exclusive_content if c["id"] == content_id), None)
    if not content:
        return jsonify({"error": "Content not found"}), 404
    return jsonify(content), 200

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
