"""
Generated Code Metadata:
========================
Original URL: https://initialmile.com
Prompt: Develop a chatbot script to assist users with questions about offshore company registration and funding, inspired by the Help Center on Initial Mile.
Generated: DETERMINISTIC_63491a2b30707659
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class Chatbot:
    def __init__(self):
        self.greetings = [
            "Hello! How can I assist you today?",
            "Hi there! What questions do you have about offshore company registration?",
            "Welcome! I'm here to help you with offshore company registration and funding."
        ]
        self.faqs = {
            "offshore company registration": "To register an offshore company, you typically need to choose a jurisdiction, select a company name, and prepare the necessary documentation.",
            "funding an offshore company": "Funding an offshore company can be done through various means such as personal investment, loans, or venture capital.",
            "benefits of offshore companies": "Offshore companies can provide tax benefits, asset protection, and privacy for business owners.",
            "requirements for offshore registration": "Requirements vary by jurisdiction but generally include proof of identity, a registered office address, and a business plan."
        }
    
    def greet_user(self):
        """Greets the user with a random greeting message."""
        return random.choice(self.greetings)

    def get_response(self, user_input):
        """Returns a response based on user input.

        Args:
            user_input (str): The user's question or statement.

        Returns:
            str: The chatbot's response.
        """
        user_input = user_input.lower()
        for keyword in self.faqs:
            if keyword in user_input:
                return self.faqs[keyword]
        return "I'm sorry, I don't have information on that. Can you please ask something else?"

    def run(self):
        """Runs the chatbot, allowing user interaction until they choose to exit."""
        print(self.greet_user())
        while True:
            try:
                user_input = input("You: ")
                if user_input.lower() in ["exit", "quit", "bye"]:
                    print("Chatbot: Thank you for chatting! Goodbye!")
                    break
                response = self.get_response(user_input)
                print(f"Chatbot: {response}")
            except Exception as e:
                print(f"An error occurred: {e}. Please try again.")

if __name__ == "__main__":
    chatbot = Chatbot()
    chatbot.run()
```
