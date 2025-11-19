"""
Generated Code Metadata:
========================
Original URL: https://scottytheai-def.web.app
Prompt: Develop a chatbot using Python and OpenAI's GPT API that mimics ScottyChat, providing cryptocurrency market insights and answering blockchain-related queries.
Generated: DETERMINISTIC_be6ef62dc80967b6
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
import json
import logging
from typing import Dict

import openai
from openai import OpenAIError

# Set up logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# OpenAI GPT API Configuration
class GPTConfig:
    def __init__(self, api_key: str, model: str = "gpt-4"):
        """
        Initialize OpenAI GPT API configuration.

        Args:
        - api_key (str): OpenAI API key
        - model (str): GPT model to use (default: gpt-4)
        """
        self.api_key = api_key
        self.model = model

    def get_client(self) -> openai.Client:
        """
        Get an OpenAI client instance.

        Returns:
        - openai.Client: OpenAI client instance
        """
        return openai.Client(api_key=self.api_key)


# ScottyChat class
class ScottyChat:
    def __init__(self, gpt_config: GPTConfig):
        """
        Initialize ScottyChat.

        Args:
        - gpt_config (GPTConfig): OpenAI GPT API configuration
        """
        self.gpt_config = gpt_config
        self.client = self.gpt_config.get_client()

    def get_crypto_market_insights(self, query: str) -> str:
        """
        Get cryptocurrency market insights.

        Args:
        - query (str): User query

        Returns:
        - str: Response from OpenAI GPT API
        """
        try:
            response = self.client.chat.completions.create(
                model=self.gpt_config.model,
                messages=[
                    {"role": "user", "content": f"Cryptocurrency market insights: {query}"}
                ]
            )
            return response.choices[0].message.content
        except OpenAIError as e:
            logger.error(f"OpenAI error: {e}")
            return "Failed to retrieve cryptocurrency market insights."

    def answer_blockchain_query(self, query: str) -> str:
        """
        Answer blockchain-related queries.

        Args:
        - query (str): User query

        Returns:
        - str: Response from OpenAI GPT API
        """
        try:
            response = self.client.chat.completions.create(
                model=self.gpt_config.model,
                messages=[
                    {"role": "user", "content": f"Blockchain query: {query}"}
                ]
            )
            return response.choices[0].message.content
        except OpenAIError as e:
            logger.error(f"OpenAI error: {e}")
            return "Failed to answer blockchain query."


# Main function
def main():
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        logger.error("OPENAI_API_KEY environment variable not set.")
        return

    gpt_config = GPTConfig(api_key)
    scotty_chat = ScottyChat(gpt_config)

    while True:
        user_input = input("User: ")
        if user_input.lower() == "quit":
            break

        if user_input.startswith("crypto"):
            response = scotty_chat.get_crypto_market_insights(user_input)
        elif user_input.startswith("blockchain"):
            response = scotty_chat.answer_blockchain_query(user_input)
        else:
            response = "Invalid query. Please start with 'crypto' or 'blockchain'."

        print("ScottyChat:", response)


if __name__ == "__main__":
    main()
```
