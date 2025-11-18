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
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FollowEvent, UnfollowEvent
)
import logging

# Initialize Flask app
app = Flask(__name__)

# LINE Bot API credentials
LINE_CHANNEL_ACCESS_TOKEN = os.getenv('LINE_CHANNEL_ACCESS_TOKEN')
LINE_CHANNEL_SECRET = os.getenv('LINE_CHANNEL_SECRET')

# Initialize LineBotApi and WebhookHandler
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

# Set up logging
logging.basicConfig(level=logging.INFO)

@app.route("/callback", methods=['POST'])
def callback():
    # Get request body as text
    body = request.get_data(as_text=True)
    signature = request.headers['X-Line-Signature']

    # Verify the signature
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        logging.error("Invalid signature. Please check your channel access token and channel secret.")
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # Handle incoming text messages from users
    user_message = event.message.text.lower()

    # Respond based on user input
    if "book" in user_message:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="To book a session, please visit our booking page: [your_booking_link]"))
    elif "faq" in user_message:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Here are some FAQs: [link_to_faqs]"))
    elif "health tips" in user_message:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="Tip of the day: Stay hydrated and maintain a balanced diet!"))
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="I'm here to help! You can ask me to book a session, get FAQs, or receive health tips."))

@handler.add(FollowEvent)
def handle_follow(event):
    # Welcome message when the user follows the bot
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="Thank you for following us! How can I assist you today?"))


@handler.add(UnfollowEvent)
def handle_unfollow(event):
    # Log unfollow events
    logging.info(f"User {event.source.user_id} has unfollowed the bot.")

if __name__ == "__main__":
    # Run the app on the specified port
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
```

### Notes:
- Ensure to set the environment variables `LINE_CHANNEL_ACCESS_TOKEN` and `LINE_CHANNEL_SECRET` with appropriate values.
- Replace `[your_booking_link]` and `[link_to_faqs]` with actual URLs.
- This code uses Flask as the web framework and the LINE Messaging API's SDK for Python.
