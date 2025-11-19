"""
Generated Code Metadata:
========================
Original URL: https://jurunensebrazz.blogspot.com
Prompt: Develop a chatbot using Python that integrates with WhatsApp to assist customers in browsing products from "Jurunense Home Center" and placing orders.
Generated: DETERMINISTIC_628aa7954534c8e2
Batch ID: 20250612_151858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
import logging
from flask import Flask, request, jsonify
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
import json

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize Flask app
app = Flask(__name__)

# Twilio account settings
TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.environ.get('TWILIO_PHONE_NUMBER')
WHATSAPP_PHONE_NUMBER = os.environ.get('WHATSAPP_PHONE_NUMBER')

# Initialize Twilio client
twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Product data (replace with actual database or API call)
products = {
    "1": {"name": "Product 1", "price": 10.99},
    "2": {"name": "Product 2", "price": 9.99},
    "3": {"name": "Product 3", "price": 12.99}
}

# Order data
orders = {}

# Function to send WhatsApp message
def send_whatsapp_message(to, message):
    try:
        message = twilio_client.messages.create(
            from_=TWILIO_PHONE_NUMBER,
            to=WHATSAPP_PHONE_NUMBER,
            body=message
        )
        logging.info(f"Sent WhatsApp message: {message.sid}")
    except Exception as e:
        logging.error(f"Error sending WhatsApp message: {str(e)}")

# Function to get product information
def get_product_info(product_id):
    try:
        product = products.get(product_id)
        if product:
            return product
        else:
            return None
    except Exception as e:
        logging.error(f"Error getting product info: {str(e)}")
        return None

# Function to place order
def place_order(product_id, quantity, customer_name):
    try:
        product = get_product_info(product_id)
        if product:
            order_id = len(orders) + 1
            orders[str(order_id)] = {
                "product_id": product_id,
                "quantity": quantity,
                "customer_name": customer_name,
                "total": product["price"] * quantity
            }
            return order_id
        else:
            return None
    except Exception as e:
        logging.error(f"Error placing order: {str(e)}")
        return None

# WhatsApp message handler
@app.route("/whatsapp", methods=["POST"])
def whatsapp_handler():
    try:
        message = request.form.get("message")
        from_number = request.form.get("from")

        # Process incoming message
        if message.lower() == "hello":
            response = MessagingResponse()
            response.message("Hello! Welcome to Jurunense Home Center. How can I assist you today?")
            return jsonify(response.to_dict())

        elif message.lower() == "products":
            response = MessagingResponse()
            product_list = ""
            for product_id, product in products.items():
                product_list += f"{product_id}. {product['name']} - ${product['price']:.2f}\n"
            response.message(product_list)
            return jsonify(response.to_dict())

        elif message.startswith("order"):
            parts = message.split()
            if len(parts) == 3:
                product_id = parts[1]
                quantity = int(parts[2])
                product = get_product_info(product_id)
                if product:
                    response = MessagingResponse()
                    response.message(f"Please confirm your order: {quantity} x {product['name']} = ${product['price'] * quantity:.2f}")
                    return jsonify(response.to_dict())
                else:
                    response = MessagingResponse()
                    response.message("Product not found. Please try again.")
                    return jsonify(response.to_dict())
            else:
                response = MessagingResponse()
                response.message("Invalid order request. Please try again.")
                return jsonify(response.to_dict())

        elif message.startswith("confirm"):
            parts = message.split()
            if len(parts) == 2:
                order_id = place_order(parts[1], 1, "Customer Name")
                if order_id:
                    response = MessagingResponse()
                    response.message(f"Order placed successfully! Your order ID is: {order_id}")
                    return jsonify(response.to_dict())
                else:
                    response = MessagingResponse()
                    response.message("Error placing order. Please try again.")
                    return jsonify(response.to_dict())
            else:
                response = MessagingResponse()
                response.message("Invalid confirmation request. Please try again.")
                return jsonify(response.to_dict())

        else:
            response = MessagingResponse()
            response.message("Sorry, I didn't understand that. Please try again.")
            return jsonify(response.to_dict())

    except Exception as e:
        logging.error(f"Error handling WhatsApp message: {str(e)}")
        return jsonify({"error": "Internal Server Error"}), 500

if __name__ == "__main__":
    app.run(debug=True)
```

```python
# Run the Flask app
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, default=5000)
    args = parser.parse_args()

    app.run(host="0.0.0.0", port=args.port)
```
