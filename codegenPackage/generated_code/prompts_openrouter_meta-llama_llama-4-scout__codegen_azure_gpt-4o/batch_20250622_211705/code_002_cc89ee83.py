"""
Generated Code Metadata:
========================
Original URL: https://realogs.space
Prompt: Generate a code snippet to implement a keyword-based filtering system for a chat application, inspired by the need to prevent crypto speculation discussions in the realogs.space community.
Generated: DETERMINISTIC_cc89ee8333648675
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

class ChatFilter:
    """
    A class to implement keyword-based filtering for a chat application.
    Prevents discussions related to crypto speculation.
    """

    def __init__(self, banned_keywords):
        """
        Initializes the ChatFilter with a list of banned keywords.

        :param banned_keywords: List of keywords to filter out.
        """
        self.banned_keywords = [keyword.lower() for keyword in banned_keywords]

    def is_message_allowed(self, message):
        """
        Checks if a message is allowed based on the banned keywords.

        :param message: The chat message to check.
        :return: True if the message is allowed, False otherwise.
        """
        # Normalize the message to lowercase for case-insensitive matching
        normalized_message = message.lower()

        # Check if any banned keyword exists in the message
        for keyword in self.banned_keywords:
            if re.search(r'\b' + re.escape(keyword) + r'\b', normalized_message):
                return False  # Message contains a banned keyword
        return True  # Message is allowed

    def filter_messages(self, messages):
        """
        Filters a list of messages, removing those that contain banned keywords.

        :param messages: List of chat messages to filter.
        :return: List of messages that are allowed.
        """
        return [message for message in messages if self.is_message_allowed(message)]


# Example usage
if __name__ == "__main__":
    # Define banned keywords related to crypto speculation
    banned_keywords = ["crypto", "bitcoin", "ethereum", "blockchain", "nft", "speculation"]

    # Initialize the chat filter
    chat_filter = ChatFilter(banned_keywords)

    # Example chat messages
    chat_messages = [
        "Hey, did you see the latest news about Bitcoin?",
        "Let's discuss the weather today.",
        "Ethereum prices are skyrocketing!",
        "What are your thoughts on NFTs?",
        "I love programming in Python.",
        "Blockchain technology is the future!"
    ]

    # Filter the messages
    allowed_messages = chat_filter.filter_messages(chat_messages)

    # Display the allowed messages
    print("Allowed Messages:")
    for msg in allowed_messages:
        print(f"- {msg}")
```
