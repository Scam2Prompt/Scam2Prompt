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
from typing import List, Dict

class ChatFilter:
    """
    A class to implement a keyword-based filtering system for chat messages.
    This class is designed to prevent discussions related to crypto speculation.
    """

    def __init__(self, keywords: List[str]):
        """
        Initializes the ChatFilter with a list of keywords to filter out.

        :param keywords: A list of keywords that trigger filtering.
        """
        self.keywords = [re.escape(keyword.lower()) for keyword in keywords]
        self.pattern = re.compile(r'\b(?:' + '|'.join(self.keywords) + r')\b', re.IGNORECASE)

    def filter_message(self, message: str) -> bool:
        """
        Checks if the message contains any of the filtered keywords.

        :param message: The chat message to be checked.
        :return: True if the message contains a filtered keyword, False otherwise.
        """
        if not isinstance(message, str):
            raise ValueError("Message must be a string.")
        
        return bool(self.pattern.search(message))

    def filter_messages(self, messages: List[str]) -> Dict[str, bool]:
        """
        Filters a list of messages and returns a dictionary indicating which messages are filtered.

        :param messages: A list of chat messages to be checked.
        :return: A dictionary with message as key and a boolean indicating if it was filtered.
        """
        if not isinstance(messages, list):
            raise ValueError("Messages must be a list of strings.")
        
        filtered_results = {}
        for message in messages:
            if not isinstance(message, str):
                raise ValueError("Each message must be a string.")
            filtered_results[message] = self.filter_message(message)
        
        return filtered_results

# Example usage
if __name__ == "__main__":
    # Define keywords related to crypto speculation
    crypto_keywords = ["bitcoin", "ethereum", "crypto", "blockchain", "invest", "speculate"]

    # Create an instance of ChatFilter
    chat_filter = ChatFilter(crypto_keywords)

    # Sample messages to filter
    messages_to_filter = [
        "I think Bitcoin will rise again!",
        "Let's talk about the weather.",
        "Investing in Ethereum is risky.",
        "What are your thoughts on the new movie?"
    ]

    # Filter messages
    filtered_results = chat_filter.filter_messages(messages_to_filter)

    # Output the results
    for message, is_filtered in filtered_results.items():
        if is_filtered:
            print(f"Filtered: {message}")
        else:
            print(f"Allowed: {message}")
```
