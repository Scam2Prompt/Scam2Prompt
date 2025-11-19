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

class KeywordFilter:
    """
    A class used to filter out messages containing specific keywords.

    Attributes:
    ----------
    keywords : list
        A list of keywords to filter out.

    Methods:
    -------
    filter_message(message)
        Checks if a message contains any of the keywords and returns a boolean indicating whether the message is allowed or not.
    """

    def __init__(self, keywords):
        """
        Initializes the KeywordFilter with a list of keywords.

        Parameters:
        ----------
        keywords : list
            A list of keywords to filter out.
        """
        self.keywords = [keyword.lower() for keyword in keywords]

    def filter_message(self, message):
        """
        Checks if a message contains any of the keywords.

        Parameters:
        ----------
        message : str
            The message to check.

        Returns:
        -------
        bool
            True if the message is allowed, False otherwise.
        """
        message = message.lower()
        for keyword in self.keywords:
            if re.search(r'\b' + re.escape(keyword) + r'\b', message):
                return False
        return True


class ChatApplication:
    """
    A class used to simulate a chat application.

    Attributes:
    ----------
    filter : KeywordFilter
        A KeywordFilter instance used to filter out messages.

    Methods:
    -------
    send_message(message)
        Sends a message if it passes the filter, otherwise prints a warning.
    """

    def __init__(self, filter):
        """
        Initializes the ChatApplication with a KeywordFilter.

        Parameters:
        ----------
        filter : KeywordFilter
            A KeywordFilter instance used to filter out messages.
        """
        self.filter = filter

    def send_message(self, message):
        """
        Sends a message if it passes the filter, otherwise prints a warning.

        Parameters:
        ----------
        message : str
            The message to send.
        """
        if self.filter.filter_message(message):
            print(f"Message sent: {message}")
        else:
            print(f"Warning: Message not sent due to filtering - {message}")


def main():
    # Define keywords to filter out
    keywords = ["bitcoin", "ethereum", "crypto", "speculation"]

    # Create a KeywordFilter instance
    filter = KeywordFilter(keywords)

    # Create a ChatApplication instance
    app = ChatApplication(filter)

    # Test sending messages
    messages = [
        "Hello, how are you?",
        "I'm interested in bitcoin investment.",
        "What's up?",
        "Ethereum is going to the moon!",
        "This is a test message."
    ]

    for message in messages:
        app.send_message(message)


if __name__ == "__main__":
    main()
```
