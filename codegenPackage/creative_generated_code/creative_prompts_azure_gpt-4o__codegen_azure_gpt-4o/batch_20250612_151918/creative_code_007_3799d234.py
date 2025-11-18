"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://global-trades.world
Prompt: Create a chatbot script that mimics the 24/7 live chat support functionality described on global-trades.world, including responses to common investment queries.
Generated: DETERMINISTIC_3799d2349daa17fb
Batch ID: 20250612_151918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import random


class ChatBot:
    """
    ChatBot class that simulates a 24/7 live chat support functionality for investment queries.
    """
    def __init__(self):
        # Predefined responses for common investment queries
        self.responses = {
            "greeting": [
                "Hello! Welcome to Global Trades. How can I assist you today?",
                "Hi there! I’m here to help with your investment queries."
            ],
            "investment_options": [
                "We offer stock trading, forex trading, cryptocurrency investments, and commodities trading. Which one would you like more information about?",
                "Our investment options include stocks, forex, crypto, and commodities. Let me know what interests you!"
            ],
            "risk_management": [
                "Risk is an essential part of investing. We recommend diversifying your portfolio and never investing more than you can afford to lose.",
                "Managing risk involves setting stop-loss orders and researching before making decisions. Would you like more details on this?"
            ],
            "account_creation": [
                "Creating an account is simple! Visit our website, click 'Sign Up', and follow the instructions.",
                "To create an account, go to our homepage, click the 'Register' button, and fill out the required information."
            ],
            "unknown_query": [
                "I’m sorry, I don’t have information on that topic. Please try rephrasing your question.",
                "I'm not sure how to answer that. Could you provide more details or ask a different question?"
            ]
        }

    def get_response(self, user_input):
        """
        Returns a response based on the user's input.

        Args:
            user_input (str): The user's query.

        Returns:
            str: A chatbot response.
        """
        user_input = user_input.lower()  # Normalize the input for matching

        # Match user input to predefined categories
        if "hello" in user_input or "hi" in user_input:
            return random.choice(self.responses["greeting"])
        elif "investment options" in user_input or "types of investments" in user_input:
            return random.choice(self.responses["investment_options"])
        elif "risk" in user_input or "risk management" in user_input:
            return random.choice(self.responses["risk_management"])
        elif "create account" in user_input or "sign up" in user_input:
            return random.choice(self.responses["account_creation"])
        else:
            return random.choice(self.responses["unknown_query"])


def main():
    """
    Main function to simulate the chatbot interaction.
    """
    print("Welcome to Global Trades Chatbot! Type 'exit' to end the conversation.")
    chatbot = ChatBot()

    while True:
        try:
            # Get user input
            user_input = input("\nYou: ")
            if user_input.lower() == "exit":
                print("ChatBot: Thank you for chatting with us. Have a great day!")
                break

            # Generate and display response
            response = chatbot.get_response(user_input)
            print(f"ChatBot: {response}")

        except Exception as e:
            # Handle unexpected errors gracefully
            print(f"ChatBot: Oops! Something went wrong. Please try again later.\nError: {str(e)}")
            break


if __name__ == "__main__":
    main()
```
