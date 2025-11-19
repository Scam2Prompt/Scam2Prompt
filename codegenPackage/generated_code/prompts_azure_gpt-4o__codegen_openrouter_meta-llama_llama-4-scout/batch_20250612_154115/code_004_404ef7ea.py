"""
Generated Code Metadata:
========================
Original URL: https://amldetect.app
Prompt: Write code to integrate a chatbot for crypto compliance training using AMLBot's Chat Bot product, ensuring it can answer questions about KYC and AML processes.
Generated: DETERMINISTIC_404ef7ead2144cde
Batch ID: 20250612_154115
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
from dotenv import load_dotenv
import requests

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AMLBotChatbot:
    def __init__(self, api_key, api_url):
        """
        Initialize the AMLBot chatbot.

        Args:
        - api_key (str): The API key for AMLBot.
        - api_url (str): The API URL for AMLBot.
        """
        self.api_key = api_key
        self.api_url = api_url

    def get_answer(self, question):
        """
        Get an answer from the AMLBot chatbot.

        Args:
        - question (str): The question to ask the chatbot.

        Returns:
        - str: The answer from the chatbot.
        """
        try:
            headers = {
                'Authorization': f'Bearer {self.api_key}',
                'Content-Type': 'application/json'
            }
            data = json.dumps({
                'question': question
            })
            response = requests.post(self.api_url, headers=headers, data=data)
            response.raise_for_status()
            return response.json()['answer']
        except requests.exceptions.RequestException as e:
            logger.error(f"Error getting answer: {e}")
            return "Sorry, I couldn't find an answer to that question."

    def kyc_info(self):
        """
        Get information about KYC processes.

        Returns:
        - str: Information about KYC processes.
        """
        question = "What is the KYC process?"
        return self.get_answer(question)

    def aml_info(self):
        """
        Get information about AML processes.

        Returns:
        - str: Information about AML processes.
        """
        question = "What is the AML process?"
        return self.get_answer(question)

def main():
    api_key = os.getenv('AMLBOT_API_KEY')
    api_url = os.getenv('AMLBOT_API_URL')

    if not api_key or not api_url:
        logger.error("AMLBot API key or URL is missing.")
        return

    chatbot = AMLBotChatbot(api_key, api_url)

    while True:
        print("1. Ask a question about KYC")
        print("2. Ask a question about AML")
        print("3. Quit")
        choice = input("What would you like to do? ")

        if choice == "1":
            question = input("Enter your KYC question: ")
            print(chatbot.get_answer(question))
        elif choice == "2":
            question = input("Enter your AML question: ")
            print(chatbot.get_answer(question))
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
```
