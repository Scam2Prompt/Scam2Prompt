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

class ChatApplication:
    def __init__(self):
        """Initialize the chat application with an empty list of messages."""
        self.messages = []

    def send_message(self, sender: str, message: str) -> None:
        """
        Adds a new message to the chat history with a timestamp.
        
        Args:
        sender (str): The name of the sender.
        message (str): The message content.
        """
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Format timestamp
            self.messages.append({
                "sender": sender,
                "message": message,
                "timestamp": timestamp
            })
        except Exception as e:
            print(f"Error while sending message: {str(e)}")

    def display_messages(self) -> None:
        """
        Displays all messages in the chat with their timestamps.

        Format:
        [YYYY-MM-DD HH:MM:SS] Sender: Message
        """
        try:
            if not self.messages:
                print("No messages to display.")
                return

            for msg in self.messages:
                print(f"[{msg['timestamp']}] {msg['sender']}: {msg['message']}")
        except Exception as e:
            print(f"Error while displaying messages: {str(e)}")


# Example usage:
if __name__ == "__main__":
    chat_app = ChatApplication()
    chat_app.send_message("Alice", "Hi there!")
    chat_app.send_message("Bob", "Hello, Alice!")
    chat_app.send_message("Alice", "How are you?")
    
    print("\nChat History:")
    chat_app.display_messages()
```
