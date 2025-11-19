"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://telegram-gods.net
Prompt: Create a function that filters and collects active users from various Telegram chats using the audience parser feature of Telegram Expert.
Generated: DETERMINISTIC_6b2d84da57090974
Batch ID: 20250612_164000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import telethon
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch

# Configuration for Telegram API client
API_ID = 'your_api_id'  # Replace with your Telegram API ID
API_HASH = 'your_api_hash'  # Replace with your Telegram API Hash
PHONE_NUMBER = '+1234567890'  # Replace with your Telegram phone number

def fetch_active_users(chats, keyword=''):
    """
    Fetches active users from specified Telegram chats.

    Args:
        chats (list): List of chat usernames or IDs to parse.
        keyword (str): Optional keyword to filter users. Default is empty string.

    Returns:
        dict: A dictionary where keys are chat names and values are lists of active user IDs.
    """
    # Dictionary to store results
    active_users = {}

    # Initialize Telegram client
    with TelegramClient(PHONE_NUMBER, API_ID, API_HASH) as client:
        for chat in chats:
            try:
                # Fetch the chat entity
                chat_entity = client.get_entity(chat)

                # Prepare for collecting participants
                participants = []
                offset = 0
                limit = 100

                # Fetch participants in chunks
                while True:
                    result = client(GetParticipantsRequest(
                        channel=chat_entity,
                        filter=ChannelParticipantsSearch(keyword),
                        offset=offset,
                        limit=limit,
                        hash=0
                    ))

                    participants.extend(result.participants)

                    if len(result.participants) < limit:
                        # Break the loop if no more participants are available
                        break

                    offset += limit

                # Filter active users (users who have recent activity)
                active_users[chat] = [
                    user.id for user in participants if hasattr(user, 'status') and user.status
                ]

            except telethon.errors.rpcerrorlist.ChannelInvalidError:
                print(f"Error: The chat {chat} is invalid or inaccessible.")
            except telethon.errors.rpcerrorlist.ChannelPrivateError:
                print(f"Error: The chat {chat} is private and cannot be accessed.")
            except Exception as e:
                print(f"An unexpected error occurred while processing {chat}: {e}")

    return active_users

# Example usage
if __name__ == "__main__":
    chat_list = ['ChatUsername1', 'ChatUsername2', 'ChatUsername3']  # Replace with chat usernames or IDs
    active_users = fetch_active_users(chat_list)
    for chat_name, users in active_users.items():
        print(f"Active users in {chat_name}: {users}")
```

Replace placeholders such as `your_api_id`, `your_api_hash`, and `+1234567890` with your actual Telegram API credentials and phone number. Ensure the `Telethon` library is installed (`pip install telethon`) before running the script.
