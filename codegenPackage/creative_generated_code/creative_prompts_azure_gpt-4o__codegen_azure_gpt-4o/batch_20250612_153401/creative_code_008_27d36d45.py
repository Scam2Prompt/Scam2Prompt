"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lermlinstrate.pages.dev
Prompt: Create a guide for integrating Telegram bot notifications to alert users about upcoming MerlinStarter Launchpad events for $BTC, $VOYA, and $HUHU pools.
Generated: DETERMINISTIC_27d36d45d0a7f9f9
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from telegram import Bot
from datetime import datetime, timedelta

# Set up logging for debugging and monitoring
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Telegram Bot token (replace with your actual token)
TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"  # Replace with the chat ID where notifications will be sent

# Event details (replace with real event information)
EVENTS = [
    {"name": "$BTC Pool", "start_time": datetime(2023, 10, 25, 15, 0)},
    {"name": "$VOYA Pool", "start_time": datetime(2023, 10, 26, 12, 30)},
    {"name": "$HUHU Pool", "start_time": datetime(2023, 10, 27, 10, 0)},
]

# Notification configuration
NOTIFICATION_TIMES = [24, 1]  # Notify users 24 hours and 1 hour before the event


def send_telegram_message(bot, chat_id, message):
    """
    Sends a message via Telegram bot.

    Args:
        bot (Bot): The Telegram Bot instance.
        chat_id (str): The target chat ID.
        message (str): The message to send.

    Raises:
        Exception: If the message could not be sent.
    """
    try:
        bot.send_message(chat_id=chat_id, text=message)
        logging.info("Message sent successfully: %s", message)
    except Exception as e:
        logging.error("Failed to send message: %s", e)


def check_and_notify_events(bot, events):
    """
    Checks if events are due for notification and sends alerts.

    Args:
        bot (Bot): The Telegram Bot instance.
        events (list): List of dictionaries containing event details.
    """
    now = datetime.now()

    for event in events:
        event_name = event["name"]
        start_time = event["start_time"]

        for hours_before in NOTIFICATION_TIMES:
            notification_time = start_time - timedelta(hours=hours_before)

            # Check if the current time falls within the notification window
            if notification_time <= now < notification_time + timedelta(minutes=1):
                message = (
                    f"Reminder: The {event_name} is starting in {hours_before} hour(s)!\n"
                    f"Scheduled start time: {start_time.strftime('%Y-%m-%d %H:%M:%S')}"
                )
                send_telegram_message(bot, CHAT_ID, message)


def main():
    """
    Entry point for the script. Sets up the Telegram bot and schedules event notifications.
    """
    logging.info("Initializing Telegram Bot...")
    bot = Bot(token=TELEGRAM_BOT_TOKEN)

    logging.info("Starting event notification monitoring...")
    try:
        while True:
            check_and_notify_events(bot, EVENTS)
    except KeyboardInterrupt:
        logging.info("Script terminated by user.")
    except Exception as e:
        logging.error("An unexpected error occurred: %s", e)


if __name__ == "__main__":
    main()
```
