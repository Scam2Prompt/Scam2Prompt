"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sabrinaalves.com
Prompt: Develop a Python script to automate sending daily motivational messages to members of the "Comunidade Mulheres Restauradas" via WhatsApp.
Generated: DETERMINISTIC_b057b9aa3be0a0a0
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import schedule
import time
import random
import os
from twilio.rest import Client
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Twilio credentials
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')

# WhatsApp client initialization
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# List of motivational messages
MOTIVATIONAL_MESSAGES = [
    "A força de uma mulher é a sua determinação.",
    "Você é mais forte do que imagina.",
    "Cada dia é uma nova oportunidade para brilhar.",
    "Acredite em si mesma e tudo será possível.",
    "A vida é feita de escolhas, escolha ser feliz."
]

# List of WhatsApp recipients (replace with actual numbers)
RECIPIENTS = [
    'whatsapp:+12345678901',  # Replace with actual WhatsApp numbers
    'whatsapp:+12345678902',
    'whatsapp:+12345678903'
]

def send_whatsapp_message(recipient, message):
    """
    Send a WhatsApp message to a specific recipient.

    Args:
        recipient (str): The WhatsApp number of the recipient.
        message (str): The message to be sent.
    """
    try:
        client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=recipient
        )
        print(f"Message sent to {recipient}: {message}")
    except Exception as e:
        print(f"Failed to send message to {recipient}: {str(e)}")

def send_daily_motivational_message():
    """
    Select a random motivational message and send it to all recipients.
    """
    message = random.choice(MOTIVATIONAL_MESSAGES)
    for recipient in RECIPIENTS:
        send_whatsapp_message(recipient, message)

# Schedule the message to be sent daily at 9:00 AM
schedule.every().day.at("09:00").do(send_daily_motivational_message)

def main():
    """
    Main function to run the scheduler.
    """
    print("Starting the daily motivational message scheduler...")
    while True:
        schedule.run_pending()
        time.sleep(60)  # Wait for one minute

if __name__ == "__main__":
    main()
```

Make sure to create a `.env` file to store your Twilio credentials:

```
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_PHONE_NUMBER=your_twilio_whatsapp_number
``` 

Replace the phone numbers in the `RECIPIENTS` list with the actual WhatsApp numbers you wish to message.
