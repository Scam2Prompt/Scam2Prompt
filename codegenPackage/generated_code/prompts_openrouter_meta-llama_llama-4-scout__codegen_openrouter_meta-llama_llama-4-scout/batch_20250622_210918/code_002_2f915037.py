"""
Generated Code Metadata:
========================
Original URL: https://octaviaone.pages.dev
Prompt: Generate a code example for a community moderation AI tool that provides 24/7 oversight and security, similar to Octavia's features.
Generated: DETERMINISTIC_2f91503718d8e332
Batch ID: 20250622_210918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# community_moderation_ai.py

import logging
import re
from typing import Dict, List

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CommunityModerationAI:
    def __init__(self, 
                 banned_keywords: List[str], 
                 banned_phrases: List[str], 
                 max_message_length: int = 200):
        """
        Initialize the Community Moderation AI tool.

        Args:
        - banned_keywords (List[str]): A list of banned keywords.
        - banned_phrases (List[str]): A list of banned phrases.
        - max_message_length (int): The maximum allowed message length. Defaults to 200.
        """
        self.banned_keywords = banned_keywords
        self.banned_phrases = banned_phrases
        self.max_message_length = max_message_length

    def moderate_message(self, message: str) -> Dict[str, bool]:
        """
        Moderate a message and determine if it's allowed or not.

        Args:
        - message (str): The message to moderate.

        Returns:
        - Dict[str, bool]: A dictionary containing the moderation result.
        """
        result = {"allowed": True, "reason": None}

        # Check message length
        if len(message) > self.max_message_length:
            result["allowed"] = False
            result["reason"] = "Message exceeds maximum length"
            return result

        # Check for banned keywords and phrases
        for keyword in self.banned_keywords:
            if re.search(r"\b" + re.escape(keyword) + r"\b", message, re.IGNORECASE):
                result["allowed"] = False
                result["reason"] = f"Banned keyword '{keyword}' detected"
                return result

        for phrase in self.banned_phrases:
            if re.search(re.escape(phrase), message, re.IGNORECASE):
                result["allowed"] = False
                result["reason"] = f"Banned phrase '{phrase}' detected"
                return result

        return result

    def monitor_chat(self, messages: List[str]) -> List[Dict[str, bool]]:
        """
        Monitor a list of messages and moderate them.

        Args:
        - messages (List[str]): A list of messages to moderate.

        Returns:
        - List[Dict[str, bool]]: A list of moderation results.
        """
        results = []
        for message in messages:
            try:
                result = self.moderate_message(message)
                results.append(result)
            except Exception as e:
                logger.error(f"Error moderating message: {str(e)}")
                results.append({"allowed": False, "reason": "Internal error"})
        return results

def main():
    # Example usage
    banned_keywords = ["spam", "abuse"]
    banned_phrases = ["hello world", "foo bar"]

    ai = CommunityModerationAI(banned_keywords, banned_phrases)

    messages = [
        "Hello, how are you?",
        "This message contains the spam keyword",
        "This is a very long message that exceeds the maximum length " * 10,
        " Foo bar baz"
    ]

    results = ai.monitor_chat(messages)

    for i, result in enumerate(results):
        logger.info(f"Message {i+1}: allowed={result['allowed']}, reason={result['reason']}")

if __name__ == "__main__":
    main()
```
