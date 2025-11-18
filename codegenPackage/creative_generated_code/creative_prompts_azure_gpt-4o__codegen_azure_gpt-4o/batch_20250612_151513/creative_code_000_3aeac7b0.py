"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solana2018.com
Prompt: Write Python code to integrate an online booking system for a holistic health service using a LINE Messaging API, allowing users to schedule 30-minute sessions via LINE.
Generated: DETERMINISTIC_3aeac7b0140eacdf
Batch ID: 20250612_151513
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
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import LineBotApiError, InvalidSignatureError
from linebot.models import TextMessage, MessageEvent, TextSendMessage
import datetime

# Flask App Initialization
app = Flask(__name__)

# LINE Channel Access Token and Secret (replace with your actual tokens)
LINE_CHANNEL_ACCESS_TOKEN = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", "your_line_channel_access_token")
LINE_CHANNEL_SECRET = os.getenv("LINE_CHANNEL_SECRET", "your_line_channel_secret")

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

# Booking storage (simple in-memory storage; use a database for production)
bookings = {}

# Helper function to display available slots
def get_available_slots():
    current_time = datetime.datetime.now()
    available_slots = []
    for i in range(8):  # 8 slots from current hour
        slot_time = current_time + datetime.timedelta(minutes=i * 30)
        slot_str = slot_time.strftime('%Y-%m-%d %H:%M')
        if slot_str not in bookings:
            available_slots.append(slot_str)
    return available_slots

# Endpoint to handle webhook requests from LINE
@app.route("/callback", methods=["POST"])
def callback():
    # Get X-Line-Signature header value
    signature = request.headers.get("X-Line-Signature", "")

    # Get request body as text
    body = request.get_data(as_text=True)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        return "Invalid signature", 400

    return "OK", 200

# Event handler for receiving text messages
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_id = event.source.user_id
    user_message = event.message.text.strip().lower()

    # Check if the user is requesting available slots
    if user_message == "available slots":
        available_slots = get_available_slots()
        if available_slots:
            reply = "Available slots for 30-minute sessions:\n" + "\n".join(available_slots)
        else:
            reply = "Sorry, no available slots at the moment."
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply))
    elif user_message.startswith("book "):
        # Parse booking request
        requested_slot = user_message.replace("book ", "").strip()
        if requested_slot in bookings:
            reply = f"Sorry, the slot {requested_slot} is already booked."
        elif requested_slot in get_available_slots():
            bookings[requested_slot] = user_id
            reply = f"Your session has been successfully booked for {requested_slot}. Thank you!"
        else:
            reply = f"Invalid slot or slot unavailable: {requested_slot}. Please check 'available slots' command."
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply))
    else:
        # Default response for unrecognized commands
        reply = "Welcome to the Holistic Health Booking System!\n" \
                "Commands:\n" \
                "- 'available slots': View available session slots.\n" \
                "- 'book YYYY-MM-DD HH:MM': Book a session.\n"
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply))

# Error handling for sending messages via LINE API
@app.errorhandler(LineBotApiError)
def handle_line_api_error(error):
    return jsonify({"error": str(error)}), 500

# Run the Flask app
if __name__ == "__main__":
    app.run(port=int(os.getenv("PORT", 5000)), debug=False)
```
