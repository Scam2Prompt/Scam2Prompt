"""
Generated Code Metadata:
========================
Original URL: https://bafybeiaww6ymqhro76hrjq6l5h4ninbd2hn7ysd6vsyffswhvg5btz4vb4.ipfs.dweb.link
Prompt: Generate a Python script to interact with EigenLayer's community features, such as querying data from Discourse or Discord channels.
Generated: DETERMINISTIC_9cb3f26c960ab2d9
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# eigenlayer_communities.py

import os
import logging
from typing import Dict, List

import requests
import discordpy
from discourseapi import Discourse

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class EigenLayerCommunity:
    def __init__(self, discourse_url: str, discord_token: str, discord_channel_id: int):
        """
        Initialize the EigenLayer community interaction class.

        Args:
        - discourse_url (str): The URL of the Discourse instance.
        - discord_token (str): The Discord bot token.
        - discord_channel_id (int): The ID of the Discord channel to interact with.
        """
        self.discourse_url = discourse_url
        self.discord_token = discord_token
        self.discord_channel_id = discord_channel_id
        self.discourse_client = Discourse(discourse_url)

    def get_discourse_topics(self, category_id: int) -> List[Dict]:
        """
        Get topics from a specific Discourse category.

        Args:
        - category_id (int): The ID of the category to retrieve topics from.

        Returns:
        - A list of dictionaries containing topic information.
        """
        try:
            response = self.discourse_client.topics(category_id=category_id)
            return response.json()['topic_list']['topics']
        except Exception as e:
            logger.error(f"Failed to retrieve Discourse topics: {e}")
            return []

    def get_discord_messages(self) -> List[Dict]:
        """
        Get messages from a specific Discord channel.

        Returns:
        - A list of dictionaries containing message information.
        """
        try:
            discord_client = discordpy.Client()
            discord_client.login(self.discord_token)

            channel = discord_client.get_channel(self.discord_channel_id)
            messages = channel.history(limit=100).flatten()

            discord_messages = []
            for message in messages:
                discord_messages.append({
                    'content': message.content,
                    'author': message.author.name,
                    'timestamp': message.timestamp
                })

            return discord_messages
        except Exception as e:
            logger.error(f"Failed to retrieve Discord messages: {e}")
            return []

    def post_discourse_topic(self, title: str, raw_text: str, category_id: int) -> int:
        """
        Create a new topic on Discourse.

        Args:
        - title (str): The title of the topic.
        - raw_text (str): The raw text of the topic.
        - category_id (int): The ID of the category to post the topic in.

        Returns:
        - The ID of the newly created topic.
        """
        try:
            response = self.discourse_client.create_topic(
                title=title,
                raw=raw_text,
                category_id=category_id
            )
            return response.json()['topic_id']
        except Exception as e:
            logger.error(f"Failed to create Discourse topic: {e}")
            return None

    def post_discord_message(self, content: str) -> bool:
        """
        Send a message to a Discord channel.

        Args:
        - content (str): The content of the message.

        Returns:
        - True if the message was sent successfully, False otherwise.
        """
        try:
            discord_client = discordpy.Client()
            discord_client.login(self.discord_token)

            channel = discord_client.get_channel(self.discord_channel_id)
            channel.send(content)
            return True
        except Exception as e:
            logger.error(f"Failed to send Discord message: {e}")
            return False


if __name__ == "__main__":
    discourse_url = os.environ.get('DISCOURSE_URL')
    discord_token = os.environ.get('DISCORD_TOKEN')
    discord_channel_id = int(os.environ.get('DISCORD_CHANNEL_ID'))

    eigenlayer_community = EigenLayerCommunity(discourse_url, discord_token, discord_channel_id)

    # Example usage:
    discourse_topics = eigenlayer_community.get_discourse_topics(1)
    print(discourse_topics)

    discord_messages = eigenlayer_community.get_discord_messages()
    print(discord_messages)

    new_topic_id = eigenlayer_community.post_discourse_topic("Example Topic", "This is an example topic.", 1)
    print(new_topic_id)

    success = eigenlayer_community.post_discord_message("Hello from EigenLayer community script!")
    print(success)
```
