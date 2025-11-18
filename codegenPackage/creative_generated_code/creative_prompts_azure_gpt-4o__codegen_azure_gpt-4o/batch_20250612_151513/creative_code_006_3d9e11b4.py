"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solana2018.com
Prompt: Develop a chatbot using Python and the LINE Messaging API to assist users in booking sessions, answering FAQs, and providing health tips based on the clinic's philosophy.
Generated: DETERMINISTIC_3d9e11b499213e9c
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
import json
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, QuickReply, QuickReplyButton,
    PostbackAction
)

# Initialize Flask app
app = Flask(__name__)

# Load LINE Messaging API credentials from environment variables
LINE_CHANNEL_ACCESS_TOKEN = os.getenv('LINE_CHANNEL_ACCESS_TOKEN')
LINE_CHANNEL_SECRET = os.getenv('LINE_CHANNEL_SECRET')

# Initialize LINE Bot API and WebhookHandler
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

# Sample FAQs and health tips
FAQS = {
    "What are your operating hours?": "Our clinic is open from 9 AM to 6 PM, Monday to Friday.",
    "Where is the clinic located?": "We are located at 123 Health St., Wellness City.",
    "Do you accept walk-ins?": "Yes, we do accept walk-ins, but booking a session is recommended."
}

HEALTH_TIPS = [
    "Drink plenty of water to stay hydrated.",
    "Exercise regularly to maintain a healthy body.",
    "Get enough sleep to ensure proper recovery and mental clarity."
]

# Root endpoint to verify the app is running
@app.route("/", methods=["GET"])
def home():
    return "LINE Chatbot is running!", 200

# LINE webhook endpoint
@app.route("/callback", methods=["POST"])
def callback():
    # Get request header
    signature = request.headers['X-Line-Signature']

    # Get request body
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # Handle webhook request
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK', 200

# Handle incoming text messages
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_message = event.message.text.lower()

    # Respond to FAQs based on predefined dictionary
    if user_message in FAQS:
        reply = FAQS[user_message]
    elif "book" in user_message or "session" in user_message:
        # Provide session booking options
        reply = TextSendMessage(
            text="Would you like to book a session?",
            quick_reply=QuickReply(items=[
                QuickReplyButton(action=PostbackAction(label="Yes", data="book_session")),
                QuickReplyButton(action=PostbackAction(label="No", data="no_booking"))
            ])
        )
        line_bot_api.reply_message(event.reply_token, reply)
        return
    elif "health tip" in user_message:
        # Provide a random health tip
        reply = HEALTH_TIPS[0]  # Simplified: Always returns the first tip for now
    else:
        # Default response
        reply = "I'm sorry, I didn't understand that. You can ask about FAQs, book sessions, or request health tips."

    # Send the reply
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply))

# Handle postback actions (e.g., from quick replies)
@handler.add(PostbackAction)
def handle_postback(event):
    data = event.postback.data

    if data == "book_session":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Great! Please visit our booking page at www.clinicbooking.com.")
        )
    elif data == "no_booking":
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="No problem! Let me know if you need assistance.")
        )

# Error handling
@app.errorhandler(500)
def server_error(error):
    return "An internal server error occurred.", 500

# Run the Flask app
if __name__ == "__main__":
    # Ensure environment variables are set
    if not LINE_CHANNEL_ACCESS_TOKEN or not LINE_CHANNEL_SECRET:
        raise EnvironmentError("Please set LINE_CHANNEL_ACCESS_TOKEN and LINE_CHANNEL_SECRET environment variables.")

    app.run(port=5000)
```
