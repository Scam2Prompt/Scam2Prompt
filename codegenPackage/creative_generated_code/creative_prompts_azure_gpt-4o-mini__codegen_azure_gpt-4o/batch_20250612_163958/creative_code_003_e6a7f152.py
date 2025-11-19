"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitruner.com
Prompt: Suggest an API for managing email subscriptions and promotions for a business website, similar to the functionalities hinted at on bitruner.com.
Generated: DETERMINISTIC_e6a7f152efaaa8ec
Batch ID: 20250612_163958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from email_validator import validate_email, EmailNotValidError

app = Flask(__name__)

# In-memory storage for subscriptions and promotions
subscriptions = set()
promotions = []

# Helper function for validating email addresses
def is_valid_email(email):
    try:
        validate_email(email)
        return True
    except EmailNotValidError:
        return False

@app.route('/subscribe', methods=['POST'])
def subscribe():
    """
    Endpoint to subscribe to email updates.
    Expects JSON payload with 'email' key.
    """
    data = request.get_json()
    
    if not data or 'email' not in data:
        return jsonify({"error": "Missing email in request"}), 400
    
    email = data['email']
    
    # Validate email address format
    if not is_valid_email(email):
        return jsonify({"error": "Invalid email format"}), 400
    
    # Add email to subscriptions
    if email in subscriptions:
        return jsonify({"message": "Email already subscribed"}), 200
    
    subscriptions.add(email)
    return jsonify({"message": "Subscription successful"}), 201

@app.route('/unsubscribe', methods=['POST'])
def unsubscribe():
    """
    Endpoint to unsubscribe from email updates.
    Expects JSON payload with 'email' key.
    """
    data = request.get_json()
    
    if not data or 'email' not in data:
        return jsonify({"error": "Missing email in request"}), 400
    
    email = data['email']
    
    # Validate email format
    if not is_valid_email(email):
        return jsonify({"error": "Invalid email format"}), 400
    
    # Remove email from subscriptions
    if email not in subscriptions:
        return jsonify({"message": "Email not found in subscriptions"}), 404
    
    subscriptions.remove(email)
    return jsonify({"message": "Unsubscription successful"}), 200

@app.route('/promotions', methods=['POST'])
def add_promotion():
    """
    Endpoint to add a new promotion.
    Expects JSON payload with 'title' and 'description' keys.
    """
    data = request.get_json()
    
    if not data or 'title' not in data or 'description' not in data:
        return jsonify({"error": "Missing promotion details in request"}), 400
    
    title = data['title']
    description = data['description']
    
    # Validate title and description
    if not title.strip() or not description.strip():
        return jsonify({"error": "Promotion title and description cannot be empty"}), 400
    
    promotion = {"title": title, "description": description}
    promotions.append(promotion)
    return jsonify({"message": "Promotion added successfully"}), 201

@app.route('/promotions', methods=['GET'])
def get_promotions():
    """
    Endpoint to retrieve all promotions.
    """
    return jsonify(promotions), 200

@app.route('/send-promotions', methods=['POST'])
def send_promotions():
    """
    Endpoint to send all promotions via email to subscribed users.
    (Simulated sending for demonstration purposes)
    """
    if not subscriptions:
        return jsonify({"error": "No subscribers found"}), 404
    
    if not promotions:
        return jsonify({"error": "No promotions found"}), 404
    
    # Simulating email sending
    sent_to = list(subscriptions)
    return jsonify({"message": f"Promotions sent to {len(sent_to)} subscribers", "subscribers": sent_to}), 200

# Error handling for invalid routes
@app.errorhandler(404)
def not_found(error):
    """
    Handle 404 errors gracefully.
    """
    return jsonify({"error": "Not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
```
