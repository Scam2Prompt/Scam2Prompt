"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kaafmall.com
Prompt: Write code to simulate a chat conversation with timestamps and emojis, replicating the design and functionality of the WhatsApp clone on kaafmall.com.
Generated: DETERMINISTIC_d89a16ff32e9aad8
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
from datetime import datetime
from typing import List, Dict, Optional

class Message:
    """A class to represent a single chat message."""
    
    def __init__(self, sender: str, content: str, timestamp: Optional[float] = None):
        self.sender = sender
        self.content = content
        self.timestamp = timestamp if timestamp is not None else time.time()

    def formatted_timestamp(self) -> str:
        """Returns the message timestamp in a human-readable format."""
        return datetime.fromtimestamp(self.timestamp).strftime('%Y-%m-%d %H:%M:%S')

    def __str__(self) -> str:
        return f"{self.formatted_timestamp()} - {self.sender}: {self.content}"


class Chat:
    """A class to represent a chat conversation."""
    
    def __init__(self):
        self.messages: List[Message] = []

    def add_message(self, sender: str, content: str) -> None:
        """Adds a new message to the chat."""
        if not sender or not content:
            raise ValueError("Sender and content must not be empty.")
        
        message = Message(sender, content)
        self.messages.append(message)

    def display_chat(self) -> None:
        """Displays the chat conversation with messages."""
        if not self.messages:
            print("No messages in the chat.")
            return
        
        for message in self.messages:
            print(message)

    def add_emoji_to_message(self, index: int, emoji: str) -> None:
        """Adds an emoji to a specific message."""
        if index < 0 or index >= len(self.messages):
            raise IndexError("Message index out of range.")
        
        self.messages[index].content += f" {emoji}"


def main():
    """Main function to run the chat simulation."""
    chat = Chat()
    
    try:
        chat.add_message("User1", "Hello! 😊")
        chat.add_message("User2", "Hi there! How are you? 🤔")
        chat.add_message("User1", "I'm good, thanks! What about you? 😄")
        
        # Adding an emoji to the second message
        chat.add_emoji_to_message(1, "👍")

        # Display the chat
        chat.display_chat()

    except (ValueError, IndexError) as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
