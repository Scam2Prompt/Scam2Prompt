"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://myatom.online
Prompt: Create an API endpoint to retrieve subscription details and content availability from an IPTV service like ATOM, including support for 4K HDR streams.
Generated: DETERMINISTIC_dcb534292d3518b3
Batch ID: 20250612_151026
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

# Set up logging for production-grade monitoring
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

# Mock database for subscriptions and content
subscriptions = {
    "user123": {
        "subscription_type": "Premium",
        "features": ["HD", "4K", "HDR"],
        "expiry_date": "2024-01-01",
    },
    "user456": {
        "subscription_type": "Basic",
        "features": ["HD"],
        "expiry_date": "2023-12-01",
    },
}

content_availability = {
    "sports_channel": {"available_in": ["HD", "4K", "HDR"]},
    "movie_channel": {"available_in": ["HD"]},
    "documentary_channel": {"available_in": ["HD", "4K"]},
}


@app.route('/api/subscription', methods=['GET'])
def get_subscription_details():
    """
    API endpoint to retrieve subscription details for a user.
    Example request: GET /api/subscription?user_id=user123
    """
    user_id = request.args.get('user_id')

    if not user_id:
        # Return error if user_id is missing in the request
        logging.warning("Missing user_id in request")
        return jsonify({"error": "user_id parameter is required"}), 400

    subscription = subscriptions.get(user_id)
    if not subscription:
        # Return error if subscription details for the user are not found
        logging.warning(f"No subscription found for user_id: {user_id}")
        return jsonify({"error": "Subscription not found"}), 404

    logging.info(f"Subscription details retrieved for user_id: {user_id}")
    return jsonify({"user_id": user_id, "subscription": subscription}), 200


@app.route('/api/content', methods=['GET'])
def get_content_availability():
    """
    API endpoint to retrieve content availability based on subscription features.
    Example request: GET /api/content?user_id=user123&content=sports_channel
    """
    user_id = request.args.get('user_id')
    content = request.args.get('content')

    if not user_id or not content:
        # Return error if user_id or content is missing in the request
        logging.warning("Missing user_id or content in request")
        return jsonify({"error": "user_id and content parameters are required"}), 400

    subscription = subscriptions.get(user_id)
    if not subscription:
        # Return error if subscription details for the user are not found
        logging.warning(f"No subscription found for user_id: {user_id}")
        return jsonify({"error": "Subscription not found"}), 404

    content_details = content_availability.get(content)
    if not content_details:
        # Return error if content details are not found
        logging.warning(f"No availability details found for content: {content}")
        return jsonify({"error": "Content not found"}), 404

    # Check if user's subscription features allow access to the content
    available_features = set(content_details["available_in"])
    user_features = set(subscription["features"])
    is_content_accessible = not available_features.isdisjoint(user_features)

    logging.info(f"Content availability checked for user_id: {user_id}, content: {content}")
    return jsonify({
        "user_id": user_id,
        "content": content,
        "accessible": is_content_accessible,
        "subscription_features": subscription["features"],
        "content_available_in": content_details["available_in"]
    }), 200


# Error handler for unexpected server errors
@app.errorhandler(500)
def internal_server_error(e):
    logging.error(f"Internal server error: {e}")
    return jsonify({"error": "An unexpected error occurred"}), 500


# Run the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
```
