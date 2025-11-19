"""
Generated Code Metadata:
========================
Original URL: https://realogs.space
Prompt: Design a simple chatbot that can detect and respond to off-topic messages, such as cryptocurrency speculation, in a community chat forum like realogs.space.
Generated: DETERMINISTIC_3b380a029130016d
Batch ID: 20250622_211705
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re

class ChatBot:
    """
    A simple chatbot that detects and responds to off-topic messages in a community chat forum.
    """

    def __init__(self):
        # Define keywords and patterns for off-topic detection
        self.off_topic_keywords = [
            "crypto", "cryptocurrency", "bitcoin", "ethereum", "blockchain", "dogecoin", "speculation"
        ]
        self.off_topic_patterns = [
            r"\bcrypto\b", r"\bbitcoin\b", r"\bethereum\b", r"\bblockchain\b", r"\bdogecoin\b", r"\bspeculation\b"
        ]
        self.default_response = "Let's keep the discussion relevant to the community topic. 😊"

    def detect_off_topic(self, message):
        """
        Detects if a message is off-topic based on predefined keywords and patterns.

        Args:
            message (str): The message to analyze.

        Returns:
            bool: True if the message is off-topic, False otherwise.
        """
        # Check for keywords
        for keyword in self.off_topic_keywords:
            if keyword.lower() in message.lower():
                return True

        # Check for patterns using regular expressions
        for pattern in self.off_topic_patterns:
            if re.search(pattern, message, re.IGNORECASE):
                return True

        return False

    def respond_to_message(self, message):
        """
        Responds to a message based on whether it is off-topic or not.

        Args:
            message (str): The message to respond to.

        Returns:
            str: The chatbot's response.
        """
        if self.detect_off_topic(message):
            return self.default_response
        else:
            return "Thank you for contributing to the discussion! 😊"

# Example usage
if __name__ == "__main__":
    try:
        # Instantiate the chatbot
        chatbot = ChatBot()

        # Simulate incoming messages
        messages = [
            "What do you think about the latest crypto trends?",
            "I love this community! It's so helpful.",
            "Is anyone here investing in bitcoin?",
            "This forum is great for learning new skills."
        ]

        # Process each message and print the chatbot's response
        for message in messages:
            print(f"User: {message}")
            print(f"ChatBot: {chatbot.respond_to_message(message)}")
            print("-" * 50)

    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"An error occurred: {e}")
```
