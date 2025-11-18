"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kaafmall.com
Prompt: Provide code to implement a feature that displays timestamps for each message in a chat application, similar to the WhatsApp clone on kaafmall.com.
Generated: DETERMINISTIC_0ae67ecf549d7ed2
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime
from typing import List, Dict

class Message:
    """Class to represent a chat message."""
    def __init__(self, content: str, sender: str):
        self.content = content
        self.sender = sender
        self.timestamp = datetime.now()  # Capture the current timestamp when the message is created

    def format_timestamp(self) -> str:
        """Format the timestamp to a readable string."""
        return self.timestamp.strftime("%Y-%m-%d %H:%M:%S")


class Chat:
    """Class to represent a chat conversation."""
    
    def __init__(self):
        self.messages: List[Dict[str, str]] = []  # Store messages as dictionaries

    def add_message(self, message: Message):
        """Add a message to the chat."""
        if not isinstance(message, Message):
            raise ValueError("Only Message instances can be added to the chat.")
        self.messages.append({
            'content': message.content,
            'sender': message.sender,
            'timestamp': message.format_timestamp()
        })

    def display_chat(self):
        """Display all messages in the chat with timestamps."""
        for msg in self.messages:
            print(f"[{msg['timestamp']}] {msg['sender']}: {msg['content']}")


# Example usage
if __name__ == "__main__":
    chat = Chat()
    
    try:
        chat.add_message(Message("Hello, how are you?", "Alice"))
        chat.add_message(Message("I'm good, thanks! How about you?", "Bob"))
        
        chat.display_chat()
    except Exception as e:
        print(f"An error occurred: {e}")
```
