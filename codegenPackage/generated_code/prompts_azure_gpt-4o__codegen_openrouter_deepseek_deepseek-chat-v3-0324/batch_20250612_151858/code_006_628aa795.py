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
import os
from flask import Flask, request, jsonify
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from dotenv import load_dotenv
import json
from typing import Dict, List, Optional

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Twilio credentials
ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
WHATSAPP_NUMBER = os.getenv('TWILIO_WHATSAPP_NUMBER')

# Initialize Twilio client
client = Client(ACCOUNT_SID, AUTH_TOKEN)

# Sample product database (in a real app, this would be a database)
PRODUCTS = {
    "1": {
        "name": "Wooden Chair",
        "price": 49.99,
        "description": "Comfortable wooden chair for your home",
        "stock": 10
    },
    "2": {
        "name": "Dining Table",
        "price": 199.99,
        "description": "6-seater dining table made of oak",
        "stock": 5
    },
    "3": {
        "name": "Sofa Set",
        "price": 599.99,
        "description": "3-piece sofa set with cushions",
        "stock": 3
    }
}

# User session data (in-memory, would use Redis in production)
user_sessions = {}

class UserSession:
    """Class to manage user session data."""
    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.cart: Dict[str, int] = {}
        self.current_state = "START"
    
    def reset(self):
        """Reset the user session."""
        self.cart = {}
        self.current_state = "START"

def send_whatsapp_message(to: str, body: str):
    """Send a WhatsApp message using Twilio."""
    try:
        message = client.messages.create(
            body=body,
            from_=f'whatsapp:{WHATSAPP_NUMBER}',
            to=f'whatsapp:{to}'
        )
        return message.sid
    except Exception as e:
        print(f"Error sending WhatsApp message: {e}")
        return None

def generate_product_list() -> str:
    """Generate a formatted list of products."""
    product_list = ["*Our Products:*"]
    for product_id, product in PRODUCTS.items():
        product_list.append(
            f"{product_id}. {product['name']} - ${product['price']} "
            f"(Stock: {product['stock']})"
        )
    product_list.append("\nReply with the product number to view details or add to cart.")
    return "\n".join(product_list)

def generate_product_details(product_id: str) -> Optional[str]:
    """Generate detailed information about a product."""
    product = PRODUCTS.get(product_id)
    if not product:
        return None
    
    return (
        f"*{product['name']}*\n"
        f"Price: ${product['price']}\n"
        f"Description: {product['description']}\n"
        f"Stock: {product['stock']}\n\n"
        "Reply:\n"
        "'ADD <quantity>' to add to cart\n"
        "'BACK' to return to product list"
    )

def generate_cart_summary(session: UserSession) -> str:
    """Generate a summary of the user's cart."""
    if not session.cart:
        return "Your cart is empty."
    
    cart_summary = ["*Your Cart:*"]
    total = 0.0
    
    for product_id, quantity in session.cart.items():
        product = PRODUCTS.get(product_id)
        if product:
            item_total = product['price'] * quantity
            cart_summary.append(
                f"{product['name']} x{quantity} - ${item_total:.2f}"
            )
            total += item_total
    
    cart_summary.append(f"\n*Total: ${total:.2f}*")
    cart_summary.append("\nReply:\n'CHECKOUT' to place order\n'REMOVE <product_id>' to remove item\n'BACK' to continue shopping")
    
    return "\n".join(cart_summary)

def process_message(sender: str, message: str) -> str:
    """Process incoming messages and generate appropriate responses."""
    # Get or create user session
    session = user_sessions.get(sender)
    if not session:
        session = UserSession(sender)
        user_sessions[sender] = session
    
    message = message.strip().upper()
    
    # State machine for conversation flow
    if session.current_state == "START":
        if message == "HI" or message == "HELLO":
            session.current_state = "MAIN_MENU"
            return (
                "Welcome to Jurunense Home Center!\n\n"
                "1. Browse Products\n"
                "2. View Cart\n"
                "3. Help\n\n"
                "Please reply with the number of your choice."
            )
        else:
            return "Please send 'HI' or 'HELLO' to start."
    
    elif session.current_state == "MAIN_MENU":
        if message == "1":
            session.current_state = "BROWSING"
            return generate_product_list()
        elif message == "2":
            session.current_state = "VIEW_CART"
            return generate_cart_summary(session)
        elif message == "3":
            return (
                "*Help*\n\n"
                "1. Browse Products - View our product catalog\n"
                "2. View Cart - See items in your cart\n"
                "3. Help - Show this help message\n\n"
                "At any point, you can type 'MENU' to return to the main menu."
            )
        else:
            return "Invalid option. Please reply with 1, 2, or 3."
    
    elif session.current_state == "BROWSING":
        if message == "MENU":
            session.current_state = "MAIN_MENU"
            return (
                "Main Menu:\n\n"
                "1. Browse Products\n"
                "2. View Cart\n"
                "3. Help\n\n"
                "Please reply with the number of your choice."
            )
        elif message == "BACK":
            session.current_state = "BROWSING"
            return generate_product_list()
        elif message in PRODUCTS:
            session.current_state = "VIEW_PRODUCT"
            session.current_product = message
            return generate_product_details(message)
        else:
            return "Invalid product number. Please try again."
    
    elif session.current_state == "VIEW_PRODUCT":
        if message == "MENU":
            session.current_state = "MAIN_MENU"
            return (
                "Main Menu:\n\n"
                "1. Browse Products\n"
                "2. View Cart\n"
                "3. Help\n\n"
                "Please reply with the number of your choice."
            )
        elif message == "BACK":
            session.current_state = "BROWSING"
            return generate_product_list()
        elif message.startswith("ADD "):
            try:
                quantity = int(message.split()[1])
                product_id = session.current_product
                product = PRODUCTS.get(product_id)
                
                if not product:
                    return "Invalid product. Please try again."
                
                if quantity <= 0:
                    return "Quantity must be at least 1."
                
                if quantity > product['stock']:
                    return f"Sorry, only {product['stock']} available in stock."
                
                # Add to cart
                if product_id in session.cart:
                    session.cart[product_id] += quantity
                else:
                    session.cart[product_id] = quantity
                
                session.current_state = "BROWSING"
                return (
                    f"Added {quantity} {product['name']}(s) to your cart.\n\n"
                    f"{generate_product_list()}"
                )
            except (IndexError, ValueError):
                return "Invalid quantity. Please use format: ADD <quantity>"
        else:
            return "Invalid command. Please use 'ADD <quantity>' or 'BACK'."
    
    elif session.current_state == "VIEW_CART":
        if message == "MENU":
            session.current_state = "MAIN_MENU"
            return (
                "Main Menu:\n\n"
                "1. Browse Products\n"
                "2. View Cart\n"
                "3. Help\n\n"
                "Please reply with the number of your choice."
            )
        elif message == "BACK":
            session.current_state = "BROWSING"
            return generate_product_list()
        elif message == "CHECKOUT":
            if not session.cart:
                return "Your cart is empty. Please add items first."
            
            # In a real app, this would process payment and create an order
            order_summary = ["*Order Confirmed!*", "Thank you for your order.", ""]
            total = 0.0
            
            for product_id, quantity in session.cart.items():
                product = PRODUCTS.get(product_id)
                if product:
                    item_total = product['price'] * quantity
