"""
Generated Code Metadata:
========================
Original URL: https://www.emerginggifts.com
Prompt: Develop a chatbot prototype for nonprofit organizations in emerging economies to assist with digital-first fundraising, inspired by Emerging Gifts' approach.
Generated: DETERMINISTIC_c0697813a6a591e1
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# chatbot.py

import logging
from typing import Dict

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Chatbot:
    def __init__(self, name: str, intents: Dict[str, Dict[str, str]]):
        """
        Initialize the chatbot with a name and intents.

        Args:
        - name (str): The name of the chatbot.
        - intents (Dict[str, Dict[str, str]]): A dictionary of intents and responses.
        """
        self.name = name
        self.intents = intents

    def process_message(self, message: str) -> str:
        """
        Process a user's message and return a response.

        Args:
        - message (str): The user's message.

        Returns:
        - str: The chatbot's response.
        """
        # Tokenize the message
        tokens = message.split()

        # Determine the intent
        intent = self.determine_intent(tokens)

        # Get the response
        response = self.get_response(intent)

        return response

    def determine_intent(self, tokens: list) -> str:
        """
        Determine the intent behind the user's message.

        Args:
        - tokens (list): The tokenized message.

        Returns:
        - str: The determined intent.
        """
        # Simple intent determination for demonstration purposes
        if "donate" in tokens:
            return "donate"
        elif "learn" in tokens:
            return "learn"
        else:
            return "unknown"

    def get_response(self, intent: str) -> str:
        """
        Get a response based on the determined intent.

        Args:
        - intent (str): The determined intent.

        Returns:
        - str: The chatbot's response.
        """
        try:
            return self.intents[intent]["response"]
        except KeyError:
            logger.error(f"Unknown intent: {intent}")
            return "Sorry, I didn't understand that."

def main():
    # Define intents and responses
    intents = {
        "donate": {"response": "To make a donation, please visit our website at [website URL]."},
        "learn": {"response": "To learn more about our organization, please visit our website at [website URL]."},
    }

    # Create a chatbot instance
    chatbot = Chatbot("Nonprofit Chatbot", intents)

    # Test the chatbot
    while True:
        user_message = input("User: ")
        if user_message.lower() == "quit":
            break
        response = chatbot.process_message(user_message)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
```

```python
# fundraising_chatbot.py

import logging
from typing import Dict
from chatbot import Chatbot

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class FundraisingChatbot(Chatbot):
    def __init__(self, name: str, intents: Dict[str, Dict[str, str]]):
        """
        Initialize the fundraising chatbot with a name and intents.

        Args:
        - name (str): The name of the chatbot.
        - intents (Dict[str, Dict[str, str]]): A dictionary of intents and responses.
        """
        super().__init__(name, intents)

    def process_message(self, message: str) -> str:
        """
        Process a user's message and return a response.

        Args:
        - message (str): The user's message.

        Returns:
        - str: The chatbot's response.
        """
        # Tokenize the message
        tokens = message.split()

        # Determine the intent
        intent = self.determine_intent(tokens)

        # Get the response
        response = self.get_response(intent)

        return response

    def determine_intent(self, tokens: list) -> str:
        """
        Determine the intent behind the user's message.

        Args:
        - tokens (list): The tokenized message.

        Returns:
        - str: The determined intent.
        """
        # Simple intent determination for demonstration purposes
        if "donate" in tokens:
            return "donate"
        elif "campaigns" in tokens:
            return "campaigns"
        else:
            return "unknown"

    def get_response(self, intent: str) -> str:
        """
        Get a response based on the determined intent.

        Args:
        - intent (str): The determined intent.

        Returns:
        - str: The chatbot's response.
        """
        try:
            return self.intents[intent]["response"]
        except KeyError:
            logger.error(f"Unknown intent: {intent}")
            return "Sorry, I didn't understand that."

def main():
    # Define intents and responses
    intents = {
        "donate": {"response": "To make a donation, please visit our website at [website URL]."},
        "campaigns": {"response": "We currently have the following campaigns: [campaign 1], [campaign 2]."},
    }

    # Create a fundraising chatbot instance
    fundraising_chatbot = FundraisingChatbot("Fundraising Chatbot", intents)

    # Test the fundraising chatbot
    while True:
        user_message = input("User: ")
        if user_message.lower() == "quit":
            break
        response = fundraising_chatbot.process_message(user_message)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
```
