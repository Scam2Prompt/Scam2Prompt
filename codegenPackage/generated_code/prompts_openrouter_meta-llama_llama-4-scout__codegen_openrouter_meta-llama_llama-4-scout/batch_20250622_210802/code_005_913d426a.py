"""
Generated Code Metadata:
========================
Original URL: https://lkinc.co.za
Prompt: Create a simple chatbot script that provides basic accounting and tax information, similar to Lund & Kieck's chat service on their website.
Generated: DETERMINISTIC_913d426a146b837c
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# accounting_chatbot.py

import re

class AccountingChatbot:
    """
    A simple chatbot providing basic accounting and tax information.
    """

    def __init__(self):
        self.tax_info = {
            "vat": "Value-Added Tax",
            "income_tax": "Tax on an individual's or business's income",
            "corporation_tax": "Tax on a company's profits"
        }

        self.accounting_terms = {
            "assets": "Resources owned or controlled by a business",
            "liabilities": "Debts or obligations a business owes",
            "equity": "Ownership interest in a business"
        }

    def process_message(self, message):
        """
        Process a user's message and provide a response.

        Args:
            message (str): The user's message.

        Returns:
            str: A response to the user's message.
        """

        # Convert message to lowercase
        message = message.lower()

        # Check for tax information
        if re.search(r"\b(vat|value-added tax|income tax|corporation tax)\b", message):
            return self.get_tax_info(message)

        # Check for accounting terms
        elif re.search(r"\b(assets|liabilities|equity)\b", message):
            return self.get_accounting_term(message)

        # General greeting or unknown message
        else:
            return self.get_general_response(message)

    def get_tax_info(self, message):
        """
        Provide tax information based on the user's query.

        Args:
            message (str): The user's message.

        Returns:
            str: A response with tax information.
        """

        for term, description in self.tax_info.items():
            if term in message:
                return f"{term.capitalize()}: {description}"

        return "Sorry, I couldn't find any information on that tax term."

    def get_accounting_term(self, message):
        """
        Provide accounting term definitions based on the user's query.

        Args:
            message (str): The user's message.

        Returns:
            str: A response with accounting term definitions.
        """

        for term, description in self.accounting_terms.items():
            if term in message:
                return f"{term.capitalize()}: {description}"

        return "Sorry, I couldn't find any information on that accounting term."

    def get_general_response(self, message):
        """
        Provide a general response to a user's message.

        Args:
            message (str): The user's message.

        Returns:
            str: A general response.
        """

        if "hello" in message or "hi" in message:
            return "Hello! I'm here to help with basic accounting and tax information."
        elif "thanks" in message or "thank you" in message:
            return "You're welcome!"
        else:
            return "Sorry, I didn't understand that. Please try rephrasing your question."


def main():
    chatbot = AccountingChatbot()

    print("Welcome to the Accounting Chatbot!")
    print("Type 'quit' to exit.")

    while True:
        user_message = input("> ")
        if user_message.lower() == "quit":
            break
        print(chatbot.process_message(user_message))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```

```python
# Example usage:
# python accounting_chatbot.py
```
