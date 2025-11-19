"""
Generated Code Metadata:
========================
Original URL: https://jurunensebrazz.blogspot.com
Prompt: "Generate a code snippet for an e-commerce website that allows users to purchase home improvement products via WhatsApp, similar to the features on Jurunense Home Center."
Generated: DETERMINISTIC_88f10e1ae373c658
Batch ID: 20250612_155250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from twilio.rest import Client
import os

# Initialize Flask app
app = Flask(__name__)

# Twilio configuration (replace with your Twilio credentials)
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")  # Twilio Account SID
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")    # Twilio Auth Token
TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")  # Twilio WhatsApp number

# Initialize Twilio client
twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Sample product catalog (in a real-world app, this would come from a database)
PRODUCT_CATALOG = {
    "101": {"name": "Hammer", "price": 15.99},
    "102": {"name": "Screwdriver Set", "price": 25.49},
    "103": {"name": "Paint Roller", "price": 12.99},
}

# Route to handle WhatsApp messages
@app.route("/whatsapp", methods=["POST"])
def handle_whatsapp_message():
    try:
        # Parse incoming message
        incoming_message = request.form.get("Body").strip()
        sender_number = request.form.get("From")

        # Check if the message is a product inquiry
        if incoming_message.lower() == "catalog":
            # Generate product catalog response
            catalog_message = "Welcome to our Home Improvement Store!\nHere are our products:\n"
            for product_id, details in PRODUCT_CATALOG.items():
                catalog_message += f"{product_id}: {details['name']} - ${details['price']:.2f}\n"
            send_whatsapp_message(sender_number, catalog_message)
            return jsonify({"status": "success", "message": "Catalog sent."})

        # Check if the message is a purchase request
        elif incoming_message.startswith("buy"):
            product_id = incoming_message.split(" ")[1]
            if product_id in PRODUCT_CATALOG:
                product = PRODUCT_CATALOG[product_id]
                purchase_message = (
                    f"Thank you for your purchase!\nYou have bought: {product['name']} "
                    f"for ${product['price']:.2f}.\nWe will contact you shortly for delivery details."
                )
                send_whatsapp_message(sender_number, purchase_message)
                return jsonify({"status": "success", "message": "Purchase confirmed."})
            else:
                error_message = "Invalid product ID. Please check the catalog and try again."
                send_whatsapp_message(sender_number, error_message)
                return jsonify({"status": "error", "message": "Invalid product ID."})

        # Handle unknown messages
        else:
            unknown_message = "Sorry, I didn't understand that. Type 'catalog' to see our products or 'buy <product_id>' to purchase."
            send_whatsapp_message(sender_number, unknown_message)
            return jsonify({"status": "error", "message": "Unknown command."})

    except Exception as e:
        # Log the error and send a generic error message
        print(f"Error: {e}")
        error_message = "An error occurred while processing your request. Please try again later."
        send_whatsapp_message(sender_number, error_message)
        return jsonify({"status": "error", "message": "Internal server error."})

# Helper function to send WhatsApp messages
def send_whatsapp_message(to, message):
    try:
        twilio_client.messages.create(
            from_=f"whatsapp:{TWILIO_WHATSAPP_NUMBER}",
            to=to,
            body=message
        )
    except Exception as e:
        print(f"Error sending WhatsApp message: {e}")

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
```

### Notes:
- Replace `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, and `TWILIO_WHATSAPP_NUMBER` with your actual Twilio credentials.
- Ensure you have the Twilio Python SDK installed (`pip install twilio`) and Flask (`pip install flask`).
- This code assumes the Twilio webhook is properly configured to send incoming WhatsApp messages to the `/whatsapp` endpoint.
