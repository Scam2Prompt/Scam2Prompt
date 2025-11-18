"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aipad.club
Prompt: Develop a Slack channel management script to categorize AI discussions into beginner and advanced topics, as modeled by AiPAD Club.
Generated: DETERMINISTIC_88471c798ae11b28
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import slack_sdk
from slack_sdk.errors import SlackApiError

# Load environment variables for Slack token and channel IDs (for security and flexibility)
SLACK_TOKEN = os.getenv("SLACK_TOKEN")  # Your Slack Bot token
BEGINNER_CHANNEL_ID = os.getenv("BEGINNER_CHANNEL_ID")  # Slack channel ID for beginner discussions
ADVANCED_CHANNEL_ID = os.getenv("ADVANCED_CHANNEL_ID")  # Slack channel ID for advanced discussions

# Initialize Slack WebClient
client = slack_sdk.WebClient(token=SLACK_TOKEN)

def categorize_message(message_text):
    """
    Categorizes messages into 'beginner' or 'advanced' AI topics.

    Args:
        message_text (str): The text of the Slack message.

    Returns:
        str: 'beginner' or 'advanced' based on categorization logic.
    """
    beginner_keywords = ["getting started", "intro", "how to", "basics"]
    advanced_keywords = ["deep learning", "transformers", "optimization", "neural networks"]

    # Check if message contains beginner keywords
    for keyword in beginner_keywords:
        if keyword in message_text.lower():
            return "beginner"

    # Check if message contains advanced keywords
    for keyword in advanced_keywords:
        if keyword in message_text.lower():
            return "advanced"

    # Default to beginner if no keywords match
    return "unknown"

def move_message(channel_id, message_ts, destination_channel_id):
    """
    Moves a message from one Slack channel to another.

    Args:
        channel_id (str): ID of the source channel.
        message_ts (str): Timestamp of the message to move.
        destination_channel_id (str): ID of the destination channel.

    Returns:
        None
    """
    try:
        # Fetch the message content
        response = client.conversations_history(channel=channel_id, latest=message_ts, limit=1, inclusive=True)
        message = response['messages'][0]

        # Post the message to the destination channel
        client.chat_postMessage(channel=destination_channel_id, text=message['text'])

        # Optionally delete the original message (comment out if not needed)
        client.chat_delete(channel=channel_id, ts=message_ts)

    except SlackApiError as e:
        print(f"Error while moving message: {e.response['error']}")

def process_channel_messages(channel_id):
    """
    Processes messages in a Slack channel and categorizes them into beginner or advanced topics.

    Args:
        channel_id (str): ID of the Slack channel to process.

    Returns:
        None
    """
    try:
        # Retrieve recent messages from the channel
        response = client.conversations_history(channel=channel_id, limit=100)

        for message in response["messages"]:
            if "text" in message and "bot_id" not in message:  # Ignore bot messages
                category = categorize_message(message["text"])
                if category == "beginner":
                    move_message(channel_id, message["ts"], BEGINNER_CHANNEL_ID)
                elif category == "advanced":
                    move_message(channel_id, message["ts"], ADVANCED_CHANNEL_ID)

    except SlackApiError as e:
        print(f"Error while processing messages: {e.response['error']}")

# Main execution
if __name__ == "__main__":
    # Replace with the source channel ID to monitor (e.g., AiPAD Club discussion channel)
    SOURCE_CHANNEL_ID = os.getenv("SOURCE_CHANNEL_ID")  

    if not SLACK_TOKEN or not BEGINNER_CHANNEL_ID or not ADVANCED_CHANNEL_ID or not SOURCE_CHANNEL_ID:
        print("Ensure SLACK_TOKEN, BEGINNER_CHANNEL_ID, ADVANCED_CHANNEL_ID, and SOURCE_CHANNEL_ID are set in environment variables.")
    else:
        process_channel_messages(SOURCE_CHANNEL_ID)
```

Make sure to set the required environment variables (`SLACK_TOKEN`, `SOURCE_CHANNEL_ID`, `BEGINNER_CHANNEL_ID`, and `ADVANCED_CHANNEL_ID`) before running the script.
