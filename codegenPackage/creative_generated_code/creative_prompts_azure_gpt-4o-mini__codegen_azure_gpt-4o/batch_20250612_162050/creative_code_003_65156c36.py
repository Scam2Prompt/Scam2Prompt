"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://taramediaworks.com
Prompt: Provide an example of a personalized bulk messaging API that could be used to enhance customer engagement for a digital marketing agency.
Generated: DETERMINISTIC_65156c36132a216e
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import logging

# Initialize Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Sample database of customers (for demonstration purposes)
CUSTOMERS = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com"}
]

# Function to send message (mock implementation)
def send_message(email, message):
    """
    Mock function to send a message to a customer.
    Replace this with actual email-sending logic in production.
    """
    logging.info(f"Sending message to {email}: {message}")
    return True  # Assume the message was sent successfully

@app.route('/bulk-message', methods=['POST'])
def bulk_message():
    """
    API endpoint to send personalized bulk messages to customers.
    Expects a JSON payload containing 'message_template' and optionally 'customer_ids'.
    """
    try:
        # Parse incoming JSON request
        data = request.get_json()
        
        if not data or 'message_template' not in data:
            return jsonify({"error": "Invalid request. 'message_template' is required."}), 400

        message_template = data['message_template']
        customer_ids = data.get('customer_ids')  # Optional: list of customer IDs to target

        # Filter customers if specific IDs are provided
        target_customers = CUSTOMERS if not customer_ids else [
            customer for customer in CUSTOMERS if customer['id'] in customer_ids
        ]

        if not target_customers:
            return jsonify({"error": "No matching customers found."}), 404

        # Send personalized messages
        results = []
        for customer in target_customers:
            personalized_message = message_template.replace("{name}", customer["name"])
            success = send_message(customer["email"], personalized_message)
            results.append({
                "customer_id": customer["id"],
                "email": customer["email"],
                "status": "success" if success else "failed"
            })

        # Return response with results
        return jsonify({"results": results}), 200

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return jsonify({"error": "An internal error occurred."}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
