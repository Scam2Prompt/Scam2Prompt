"""
Generated Code Metadata:
========================
Original URL: https://solana2018.com
Prompt: Develop a chatbot using Python and the LINE Messaging API to assist users in booking sessions, answering FAQs, and providing health tips based on the clinic's philosophy.
Generated: DETERMINISTIC_3d9e11b499213e9c
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
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    QuickReply, QuickReplyButton, PostbackAction
)

# Initialize Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# LINE API configuration
line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))
handler = WebhookHandler(os.getenv('LINE_CHANNEL_SECRET'))

# Clinic information and FAQs
CLINIC_INFO = {
    "name": "Health Harmony Clinic",
    "hours": "Mon-Fri: 9AM-6PM, Sat: 10AM-4PM",
    "location": "123 Wellness St, Health City",
    "phone": "+1 (555) 123-4567"
}

FAQS = {
    "services": "We offer holistic health services including acupuncture, massage therapy, and nutritional counseling.",
    "insurance": "We accept most major insurance providers. Please contact us for specific coverage details.",
    "pricing": "Prices vary by service. Initial consultations start at $80.",
    "philosophy": "We believe in treating the whole person - mind, body, and spirit - for optimal wellness."
}

HEALTH_TIPS = [
    "Drink at least 8 glasses of water daily for optimal hydration.",
    "Practice deep breathing for 5 minutes daily to reduce stress.",
    "Get 7-9 hours of sleep each night for proper rest and recovery.",
    "Incorporate 30 minutes of moderate exercise into your daily routine."
]

# Webhook endpoint for LINE
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# Handle text messages
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_message = event.message.text.lower()
    
    if 'hi' in user_message or 'hello' in user_message:
        send_welcome_message(event.reply_token)
    elif 'book' in user_message or 'appointment' in user_message:
        prompt_booking(event.reply_token)
    elif 'faq' in user_message or 'question' in user_message:
        prompt_faqs(event.reply_token)
    elif 'tip' in user_message or 'advice' in user_message:
        send_health_tip(event.reply_token)
    elif 'info' in user_message or 'about' in user_message:
        send_clinic_info(event.reply_token)
    else:
        send_default_response(event.reply_token)

def send_welcome_message(reply_token):
    welcome_text = (
        f"Welcome to {CLINIC_INFO['name']}! How can I assist you today?\n\n"
        "You can ask about:\n"
        "- Booking an appointment\n"
        "- Our services (FAQ)\n"
        "- Health tips\n"
        "- Clinic information"
    )
    line_bot_api.reply_message(
        reply_token,
        TextSendMessage(text=welcome_text)
    )

def prompt_booking(reply_token):
    quick_reply = QuickReply(items=[
        QuickReplyButton(
            action=PostbackAction(label="Initial Consultation", data="book_initial")
        ),
        QuickReplyButton(
            action=PostbackAction(label="Follow-up Session", data="book_followup")
        ),
        QuickReplyButton(
            action=PostbackAction(label="Therapy Session", data="book_therapy")
        )
    ])
    
    line_bot_api.reply_message(
        reply_token,
        TextSendMessage(
            text="What type of session would you like to book?",
            quick_reply=quick_reply
        )
    )

def prompt_faqs(reply_token):
    quick_reply = QuickReply(items=[
        QuickReplyButton(
            action=PostbackAction(label="Services", data="faq_services")
        ),
        QuickReplyButton(
            action=PostbackAction(label="Insurance", data="faq_insurance")
        ),
        QuickReplyButton(
            action=PostbackAction(label="Pricing", data="faq_pricing")
        ),
        QuickReplyButton(
            action=PostbackAction(label="Philosophy", data="faq_philosophy")
        )
    ])
    
    line_bot_api.reply_message(
        reply_token,
        TextSendMessage(
            text="What would you like to know about?",
            quick_reply=quick_reply
        )
    )

def send_health_tip(reply_token):
    import random
    tip = random.choice(HEALTH_TIPS)
    line_bot_api.reply_message(
        reply_token,
        TextSendMessage(text=f"Health Tip: {tip}")
    )

def send_clinic_info(reply_token):
    info_text = (
        f"{CLINIC_INFO['name']}\n"
        f"Hours: {CLINIC_INFO['hours']}\n"
        f"Location: {CLINIC_INFO['location']}\n"
        f"Phone: {CLINIC_INFO['phone']}"
    )
    line_bot_api.reply_message(
        reply_token,
        TextSendMessage(text=info_text)
    )

def send_default_response(reply_token):
    line_bot_api.reply_message(
        reply_token,
        TextSendMessage(
            text="I'm not sure I understand. You can ask about:\n"
                 "- Booking an appointment\n"
                 "- Our services (FAQ)\n"
                 "- Health tips\n"
                 "- Clinic information"
        )
    )

# Handle postback events (quick reply selections)
@handler.add(PostbackEvent)
def handle_postback(event):
    data = event.postback.data
    
    if data.startswith('book_'):
        handle_booking_selection(event.reply_token, data)
    elif data.startswith('faq_'):
        handle_faq_selection(event.reply_token, data)

def handle_booking_selection(reply_token, booking_type):
    booking_type = booking_type.replace('book_', '')
    response_text = f"Great! You've selected {booking_type.replace('_', ' ')}. " \
                   "Please provide your preferred date and time, and we'll confirm your appointment."
    
    line_bot_api.reply_message(
        reply_token,
        TextSendMessage(text=response_text)
    )

def handle_faq_selection(reply_token, faq_type):
    faq_key = faq_type.replace('faq_', '')
    response_text = FAQS.get(faq_key, "I couldn't find that information. Please try another question.")
    
    line_bot_api.reply_message(
        reply_token,
        TextSendMessage(text=response_text)
    )

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
```
