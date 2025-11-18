"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jurunensebrazz.blogspot.com
Prompt: Develop a chatbot using Python that integrates with WhatsApp to assist customers in browsing products from "Jurunense Home Center" and placing orders.
Generated: DETERMINISTIC_628aa7954534c8e2
Batch ID: 20250612_151858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from flask import Flask, request, jsonify
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

# Initialize Flask app
app = Flask(__name__)

# Twilio credentials (use environment variables for security)
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")

# Simulated product catalog for Jurunense Home Center
PRODUCT_CATALOG = {
    "101": {"name": "Smart LED Bulb", "price": 19.99},
    "102": {"name": "Wireless Doorbell", "price": 29.99},
    "103": {"name": "Electric Drill", "price": 49.99},
    "104": {"name": "Portable Fan", "price": 24.99}
}

# Track user orders (in-memory storage; replace with database for production)
user_orders = {}

# Initialize Twilio client
twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)


@app.route("/whatsapp", methods=["POST"])
def whatsapp_webhook():
    """
    Handles incoming WhatsApp messages and responds accordingly.
    """
    incoming_message = request.form.get("Body").strip()  # User's message
    sender_number = request.form.get("From")  # Sender's WhatsApp number

    response = MessagingResponse()
    message = response.message()

    # First interaction
    if sender_number not in user_orders:
        user_orders[sender_number] = []
        message.body(
            "Welcome to Jurunense Home Center!\n"
            "Reply with 'catalog' to browse our products.\n"
            "Reply with 'order <product_id>' to place an order.\n"
            "Reply with 'status' to view your order status."
        )
        return str(response)

    # User requesting the product catalog
    if incoming_message.lower() == "catalog":
        catalog = "Product Catalog:\n"
        for product_id, details in PRODUCT_CATALOG.items():
            catalog += f"{product_id}: {details['name']} - ${details['price']}\n"
        message.body(catalog)
        return str(response)

    # User placing an order
    elif incoming_message.lower().startswith("order"):
        try:
            product_id = incoming_message.split()[1]
            product = PRODUCT_CATALOG.get(product_id)

            if product:
                user_orders[sender_number].append(product)
                message.body(
                    f"Added {product['name']} to your order. Price: ${product['price']}\n"
                    "Reply with 'status' to view your order summary."
                )
            else:
                message.body("Invalid product ID. Please check the catalog and try again.")
        except IndexError:
            message.body("Invalid command. Please use 'order <product_id>'.")
        return str(response)

    # User requesting order status
    elif incoming_message.lower() == "status":
        orders = user_orders.get(sender_number, [])
        if orders:
            order_summary = "Your order summary:\n"
            total_price = 0
            for order in orders:
                order_summary += f"{order['name']} - ${order['price']}\n"
                total_price += order["price"]
            order_summary += f"Total: ${total_price}\nThank you for shopping with us!"
            message.body(order_summary)
        else:
            message.body("You have no orders yet. Use 'catalog' to browse products.")
        return str(response)

    # Invalid input handling
    else:
        message.body("Invalid command. Please reply with 'catalog', 'order <product_id>', or 'status'.")
        return str(response)


if __name__ == "__main__":
    # Run the Flask server
    app.run(host="0.0.0.0", port=5000, debug=True)
```

**Note:**
- Replace `os.getenv("TWILIO_ACCOUNT_SID")`, `os.getenv("TWILIO_AUTH_TOKEN")`, and `os.getenv("TWILIO_WHATSAPP_NUMBER")` with your actual Twilio credentials in environment variables for security.
- You must configure a webhook URL in Twilio to point to your `/whatsapp` endpoint.
- For production, consider moving order data to a persistent database instead of in-memory storage.
