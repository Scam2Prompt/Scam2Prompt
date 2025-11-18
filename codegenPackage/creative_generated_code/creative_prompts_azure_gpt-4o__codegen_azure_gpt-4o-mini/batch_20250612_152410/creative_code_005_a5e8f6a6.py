"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kaafmall.com
Prompt: Write a Python script to manage chat data storage and retrieval for a WhatsApp-style application, ensuring it supports features like timestamps and multimedia placeholders as seen on kaafmall.com.
Generated: DETERMINISTIC_a5e8f6a69e2c8902
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
from datetime import datetime
from typing import List, Dict, Union


class ChatStorageManager:
    """
    Manages the storage and retrieval of chat messages.
    
    Attributes:
        storage_file (str): Path to the JSON file where chats are stored.
    """

    def __init__(self, storage_file: str):
        """Initializes ChatStorageManager with the specified storage file."""
        self.storage_file = storage_file
        self._ensure_storage_file_exists()

    def _ensure_storage_file_exists(self):
        """Ensures that the storage file exists, creating it if necessary."""
        if not os.path.isfile(self.storage_file):
            with open(self.storage_file, 'w') as file:
                json.dump([], file)

    def save_message(self, sender: str, recipient: str, content: str, media_type: str = None):
        """
        Saves a chat message to the storage file.

        Args:
            sender (str): The sender's identifier.
            recipient (str): The recipient's identifier.
            content (str): The content of the message.
            media_type (str, optional): Type of media if applicable (e.g., 'image', 'video').
        """
        message = {
            'sender': sender,
            'recipient': recipient,
            'content': content,
            'media_type': media_type,
            'timestamp': datetime.now().isoformat()
        }

        try:
            with open(self.storage_file, 'r+') as file:
                # Load existing messages
                messages = json.load(file)
                messages.append(message)
                file.seek(0)
                json.dump(messages, file, indent=4)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error saving message: {e}")

    def retrieve_messages(self, user1: str, user2: str) -> List[Dict[str, Union[str, None]]]:
        """
        Retrieves chat messages between two users.

        Args:
            user1 (str): First user's identifier.
            user2 (str): Second user's identifier.

        Returns:
            List[Dict[str, Union[str, None]]]: List of chat messages exchanged between the two users.
        """
        try:
            with open(self.storage_file, 'r') as file:
                messages = json.load(file)
                return [
                    message for message in messages
                    if (message['sender'] == user1 and message['recipient'] == user2) or
                       (message['sender'] == user2 and message['recipient'] == user1)
                ]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error retrieving messages: {e}")
            return []

    def delete_chat(self, user1: str, user2: str):
        """
        Deletes chat messages between two users.

        Args:
            user1 (str): First user's identifier.
            user2 (str): Second user's identifier.
        """
        try:
            with open(self.storage_file, 'r+') as file:
                messages = json.load(file)
                # Filter out messages not matching user1 and user2
                messages = [
                    message for message in messages
                    if not ((message['sender'] == user1 and message['recipient'] == user2) or
                             (message['sender'] == user2 and message['recipient'] == user1))
                ]
                file.seek(0)
                file.truncate()  # Clear the file before writing
                json.dump(messages, file, indent=4)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error deleting chat: {e}")


# Example usage
if __name__ == "__main__":
    chat_manager = ChatStorageManager('chat_data.json')

    chat_manager.save_message('user1', 'user2', 'Hello!', None)
    chat_manager.save_message('user2', 'user1', 'Hi there!', None)
    chat_manager.save_message('user1', 'user2', 'Check this out!', 'image')

    messages = chat_manager.retrieve_messages('user1', 'user2')
    print("Retrieved messages:", messages)

    chat_manager.delete_chat('user1', 'user2')
    messages_after_deletion = chat_manager.retrieve_messages('user1', 'user2')
    print("Messages after deletion:", messages_after_deletion)
```
