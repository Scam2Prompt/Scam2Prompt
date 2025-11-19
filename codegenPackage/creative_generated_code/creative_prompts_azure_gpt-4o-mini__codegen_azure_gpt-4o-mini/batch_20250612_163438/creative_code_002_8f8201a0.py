"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nodegenix.com
Prompt: Write a Python script that connects to Slack and automates task notifications using Nodegenix's API solutions.
Generated: DETERMINISTIC_8f8201a0e0993724
Batch ID: 20250612_163438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import requests
import json
import logging
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# Configure logging
logging.basicConfig(level=logging.INFO)

# Load environment variables
SLACK_TOKEN = os.getenv("SLACK_TOKEN")
NODEGENIX_API_URL = os.getenv("NODEGENIX_API_URL")
NODEGENIX_API_KEY = os.getenv("NODEGENIX_API_KEY")
SLACK_CHANNEL = os.getenv("SLACK_CHANNEL")

# Initialize Slack client
slack_client = WebClient(token=SLACK_TOKEN)

def fetch_task_notifications():
    """
    Fetch task notifications from Nodegenix's API.
    
    Returns:
        List of task notifications.
    """
    try:
        headers = {
            'Authorization': f'Bearer {NODEGENIX_API_KEY}',
            'Content-Type': 'application/json'
        }
        response = requests.get(NODEGENIX_API_URL, headers=headers)

        # Raise an error for bad response
        response.raise_for_status()

        # Parse the JSON response
        notifications = response.json()
        return notifications.get('tasks', [])
    
    except requests.exceptions.HTTPError as http_err:
        logging.error(f"HTTP error occurred: {http_err}")
    except Exception as err:
        logging.error(f"An error occurred: {err}")
    
    return []

def send_slack_notification(task):
    """
    Send a notification to Slack for the provided task.
    
    Args:
        task (dict): A dictionary containing task details.
    """
    message = f"New Task Notification:\n*Task ID:* {task['id']}\n*Title:* {task['title']}\n*Status:* {task['status']}"
    
    try:
        response = slack_client.chat_postMessage(channel=SLACK_CHANNEL, text=message)
        logging.info(f"Notification sent to Slack: {response['message']['text']}")
    except SlackApiError as e:
        logging.error(f"Slack API error: {e.response['error']}")

def main():
    """
    Main function to fetch notifications and send them to Slack.
    """
    logging.info("Fetching task notifications...")
    tasks = fetch_task_notifications()

    # Send notifications for each task retrieved
    for task in tasks:
        send_slack_notification(task)

if __name__ == "__main__":
    main()
```

Make sure you have the necessary environment variables set (`SLACK_TOKEN`, `NODEGENIX_API_URL`, `NODEGENIX_API_KEY`, `SLACK_CHANNEL`) for the script to run successfully. You can install the required library using:

```
pip install slack_sdk requests
```
