"""
Generated Code Metadata:
========================
Original URL: https://solana2018.com
Prompt: Write Python code to integrate an online booking system for a holistic health service using a LINE Messaging API, allowing users to schedule 30-minute sessions via LINE.
Generated: DETERMINISTIC_3aeac7b0140eacdf
Batch ID: 20250612_151513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import logging
from flask import Flask, request, jsonify
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, FlexMessage
from datetime import datetime, timedelta
import sqlite3
import json

app = Flask(__name__)

# LINE Messaging API credentials
LINE_CHANNEL_ACCESS_TOKEN = os.environ['LINE_CHANNEL_ACCESS_TOKEN']
LINE_CHANNEL_SECRET = os.environ['LINE_CHANNEL_SECRET']

# Initialize LINE bot API
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

# Database connection settings
DB_NAME = 'holistic_health.db'

# Create database and table if not exists
def create_table():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS bookings
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  user_id text, 
                  date text, 
                  time text)''')
    conn.commit()
    conn.close()

create_table()

# Define Flex message template for booking confirmation
BOOKING_CONFIRMATION_TEMPLATE = {
    "type": "flex",
    "altText": "Booking Confirmation",
    "contents": {
        "type": "bubble",
        "header": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": "Booking Confirmation",
                    "weight": "bold",
                    "size": "xl"
                }
            ]
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": "{date} {time}",
                    "size": "md"
                },
                {
                    "type": "text",
                    "text": "30-minute session",
                    "size": "md"
                }
            ]
        }
    }
}

# Define Flex message template for booking failure
BOOKING_FAILURE_TEMPLATE = {
    "type": "flex",
    "altText": "Booking Failure",
    "contents": {
        "type": "bubble",
        "header": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": "Booking Failure",
                    "weight": "bold",
                    "size": "xl"
                }
            ]
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": "Failed to book session. Please try again.",
                    "size": "md"
                }
            ]
        }
    }
}

@app.route("/webhook", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        return jsonify({"status": "error", "message": "Invalid signature"}), 400

    return jsonify({"status": "ok"}), 200

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_id = event.source.user_id
    message_text = event.message.text

    if message_text == "book":
        # Send booking form
        flex_message = FlexMessage(
            alt_text="Booking Form",
            contents={
                "type": "bubble",
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "Booking Form",
                            "weight": "bold",
                            "size": "xl"
                        }
                    ]
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "Please select a date (YYYY-MM-DD):",
                            "size": "md"
                        }
                    ]
                }
            }
        )
        line_bot_api.reply_message(
            event.reply_token,
            flex_message
        )
    elif message_text.startswith("date: "):
        date = message_text.split(": ")[1]
        # Send time selection
        flex_message = FlexMessage(
            alt_text="Select Time",
            contents={
                "type": "bubble",
                "header": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "Select Time",
                            "weight": "bold",
                            "size": "xl"
                        }
                    ]
                },
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                        {
                            "type": "text",
                            "text": "Please select a time (HH:MM):",
                            "size": "md"
                        }
                    ]
                }
            }
        )
        line_bot_api.reply_message(
            event.reply_token,
            flex_message
        )
    elif message_text.startswith("time: "):
        time = message_text.split(": ")[1]
        date = get_date_from_user(user_id)
        if date:
            # Book session
            if book_session(user_id, date, time):
                # Send booking confirmation
                booking_confirmation_message = FlexMessage(
                    alt_text="Booking Confirmation",
                    contents=BOOKING_CONFIRMATION_TEMPLATE
                )
                booking_confirmation_message.contents["body"]["contents"][0]["text"] = f"{date} {time}"
                line_bot_api.reply_message(
                    event.reply_token,
                    booking_confirmation_message
                )
            else:
                # Send booking failure message
                line_bot_api.reply_message(
                    event.reply_token,
                    FlexMessage(
                        alt_text="Booking Failure",
                        contents=BOOKING_FAILURE_TEMPLATE
                    )
                )
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextMessage("Please select a date first.")
            )

def get_date_from_user(user_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT date FROM bookings WHERE user_id=? ORDER BY id DESC LIMIT 1", (user_id,))
    row = c.fetchone()
    conn.close()
    if row:
        return row[0]
    return None

def book_session(user_id, date, time):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    try:
        c.execute("INSERT INTO bookings (user_id, date, time) VALUES (?, ?, ?)", (user_id, date, time))
        conn.commit()
        conn.close()
        return True
    except sqlite3.Error as e:
        conn.close()
        logging.error(f"Error booking session: {e}")
        return False

if __name__ == "__main__":
    app.run(debug=True)
```
