"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jurunensebrazz.blogspot.com
Prompt: "Generate a code snippet for an e-commerce website that allows users to purchase home improvement products via WhatsApp, similar to the features on Jurunense Home Center."
Generated: DETERMINISTIC_88f10e1ae373c658
Batch ID: 20250612_155250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from twilio.rest import Client
import os

# Flask app setup
app = Flask(__name__)

# Load environment variables (Best practice: Store keys in environment variables)
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")

# Sample product catalog (in a production setup, this would be replaced with a database)
PRODUCT_CATALOG = {
    "1": {"name": "Hammer", "price": 15.99},
    "2": {"name": "Screwdriver", "price": 7.99},
    "3": {"name": "Drill", "price": 49.99},
}

# Initialize Twilio client
twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

@app.route("/purchase", methods=["POST"])
def purchase_product():
    """
    Endpoint to handle product purchase requests via WhatsApp.
    Expects JSON payload with 'product_id' and 'user_phone' fields.
    """
    try:
        # Parse the incoming data
        data = request.json
        product_id = data.get("product_id")
        user_phone = data.get("user_phone")

        # Validate input
        if not product_id or not user_phone:
            return jsonify({"error": "Missing product_id or user_phone"}), 400

        if product_id not in PRODUCT_CATALOG:
            return jsonify({"error": "Invalid product_id"}), 404

        # Get product details
        product = PRODUCT_CATALOG[product_id]
        product_name = product["name"]
        product_price = product["price"]

        # Generate the WhatsApp message
        message_body = (
            f"Thank you for your purchase!\n\n"
            f"Product: {product_name}\n"
            f"Price: ${product_price:.2f}\n\n"
            "We will contact you shortly for delivery details."
        )

        # Send the message via WhatsApp using Twilio
        twilio_client.messages.create(
            from_=f"whatsapp:{TWILIO_WHATSAPP_NUMBER}",
            to=f"whatsapp:{user_phone}",
            body=message_body,
        )

        # Return success response
        return jsonify({"message": "Purchase successful! WhatsApp message sent."}), 200

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    # Run the Flask app on port 5000
    app.run(debug=True)
```

### Notes:
- **Environment Variables**: Ensure `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, and `TWILIO_WHATSAPP_NUMBER` are set in your environment for secure configuration.
- **Dependencies**: Install required Python modules using `pip install flask twilio`.
- **Database Integration**: For production, replace the `PRODUCT_CATALOG` with a proper database system like PostgreSQL or MongoDB.
