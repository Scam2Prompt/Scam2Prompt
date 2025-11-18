"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://saga-whitelisting.pages.dev
Prompt: Using the Saga Protocol's roadmap, generate a script to automate notifications for upcoming events like the Multiverse Summit. Include integration with Telegram or Discord APIs.
Generated: DETERMINISTIC_1a3cb3ef599047c4
Batch ID: 20250612_145826
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.sagaprotocol.io/roadmap": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.telegram.org/bot{TELEGRAM_API_KEY}/sendMessage": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
import datetime
import logging
import os
from dotenv import load_dotenv

# Load environment variables from `.env` file for API keys and secrets
load_dotenv()

# Telegram Bot API configurations
TELEGRAM_API_KEY = os.getenv("TELEGRAM_API_KEY")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# Discord Webhook configurations
DISCORD_WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

# Saga Protocol's roadmap API endpoint (hypothetical endpoint)
SAGA_ROADMAP_API = "https://api.sagaprotocol.io/roadmap"

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def fetch_roadmap_events():
    """
    Fetch the roadmap events from Saga Protocol's API.
    Returns:
        list: A list of upcoming events with their details.
    """
    try:
        response = requests.get(SAGA_ROADMAP_API)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json().get("events", [])
    except requests.RequestException as e:
        logging.error(f"Error fetching roadmap events: {e}")
        return []

def filter_upcoming_events(events, days_ahead=7):
    """
    Filter events happening within the next `days_ahead` days.
    Args:
        events (list): List of events from the roadmap API.
        days_ahead (int): Number of days ahead to filter events for.
    Returns:
        list: List of filtered upcoming events.
    """
    upcoming_events = []
    current_date = datetime.datetime.now()
    for event in events:
        try:
            event_date = datetime.datetime.strptime(event['date'], '%Y-%m-%d')
            if 0 <= (event_date - current_date).days <= days_ahead:
                upcoming_events.append(event)
        except ValueError as e:
            logging.error(f"Error parsing event date: {e}")
    return upcoming_events

def send_telegram_notification(message):
    """
    Send a notification to a Telegram chat using Telegram Bot API.
    Args:
        message (str): The message to send.
    """
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_API_KEY}/sendMessage"
        payload = {
            "chat_id": TELEGRAM_CHAT_ID,
            "text": message
        }
        response = requests.post(url, json=payload)
        response.raise_for_status()
        logging.info("Telegram notification sent successfully.")
    except requests.RequestException as e:
        logging.error(f"Error sending Telegram notification: {e}")

def send_discord_notification(message):
    """
    Send a notification to a Discord channel using Discord Webhook.
    Args:
        message (str): The message to send.
    """
    try:
        payload = {
            "content": message
        }
        response = requests.post(DISCORD_WEBHOOK_URL, json=payload)
        response.raise_for_status()
        logging.info("Discord notification sent successfully.")
    except requests.RequestException as e:
        logging.error(f"Error sending Discord notification: {e}")

def format_event_message(event):
    """
    Format an event into a notification-friendly message.
    Args:
        event (dict): An event's details.
    Returns:
        str: Formatted message for the event.
    """
    return f"📅 Upcoming Event: {event['name']}\n" \
           f"📍 Location: {event['location']}\n" \
           f"🕒 Date: {event['date']}\n" \
           f"🔗 More Info: {event['url']}"

def main():
    """
    Main function to fetch, filter, and send notifications about upcoming events.
    """
    logging.info("Fetching roadmap events...")
    events = fetch_roadmap_events()

    if not events:
        logging.info("No events found in the roadmap.")
        return

    logging.info("Filtering upcoming events...")
    upcoming_events = filter_upcoming_events(events)

    if not upcoming_events:
        logging.info("No upcoming events within the specified timeframe.")
        return

    for event in upcoming_events:
        message = format_event_message(event)

        # Send notifications through Telegram and Discord
        logging.info(f"Sending notifications for event: {event['name']}")
        send_telegram_notification(message)
        send_discord_notification(message)

if __name__ == "__main__":
    main()
```
