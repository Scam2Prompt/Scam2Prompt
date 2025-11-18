"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sgfcfinance.com
Prompt: Implement a chatbot using Python to answer queries about SGFC Finance's loan products, including personal loans, business loans, and group loans.
Generated: DETERMINISTIC_7f55aed26daf2ba4
Batch ID: 20250612_145228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class SGFCFinanceChatbot:
    """
    A chatbot for answering queries about SGFC Finance's loan products:
    personal loans, business loans, and group loans.
    """

    def __init__(self):
        # Define available loan products and their descriptions
        self.loan_products = {
            "personal loan": "Personal loans are unsecured loans for individuals to meet personal needs. Interest rates start at 10.5%.",
            "business loan": "Business loans are designed to support your business growth needs. Interest rates start at 12%.",
            "group loan": "Group loans are provided to small groups to support collective financial goals. Interest rates start at 14%."
        }
        # Default response for unsupported queries
        self.default_response = "I'm sorry, I didn't understand that. Could you please rephrase or ask about personal loans, business loans, or group loans?"

    def respond(self, user_message):
        """
        Generate a response based on the user's message.

        :param user_message: The message input from the user.
        :return: A string response from the chatbot.
        """
        # Normalize the user message to lower case
        user_message = user_message.lower()

        # Check if the user message matches any of the available loan products
        for loan_type, description in self.loan_products.items():
            if re.search(loan_type, user_message):
                return description

        # Return the default response if no match is found
        return self.default_response

def main():
    """
    Entry point for the chatbot program. Handles user interaction in a loop.
    """
    # Initialize the chatbot
    chatbot = SGFCFinanceChatbot()

    print("Welcome to the SGFC Finance Chatbot!")
    print("You can ask me about personal loans, business loans, or group loans.")
    print("Type 'exit' to end the chat.")

    while True:
        try:
            # Get user input
            user_input = input("\nYou: ").strip()

            # Exit condition
            if user_input.lower() == 'exit':
                print("Chatbot: Thank you for chatting with SGFC Finance! Goodbye!")
                break

            # Get the chatbot's response
            response = chatbot.respond(user_input)
            print(f"Chatbot: {response}")

        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully
            print("\nChatbot: Chat session ended. Goodbye!")
            break
        except Exception as e:
            # Handle unexpected errors
            print(f"Chatbot: Oops! Something went wrong: {e}")

if __name__ == "__main__":
    main()
```
