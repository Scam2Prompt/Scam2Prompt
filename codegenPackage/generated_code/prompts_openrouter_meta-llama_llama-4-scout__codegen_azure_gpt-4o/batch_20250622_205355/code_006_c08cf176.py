"""
Generated Code Metadata:
========================
Original URL: https://dudemine.com
Prompt: Create a conversation bot that responds to common queries about a website like Dudemine.
Generated: DETERMINISTIC_c08cf17674e47bf0
Batch ID: 20250622_205355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class ConversationBot:
    """
    A simple conversation bot that responds to common queries about a website.
    """

    def __init__(self, website_name):
        """
        Initializes the bot with the website name.
        :param website_name: Name of the website the bot is representing.
        """
        self.website_name = website_name
        self.responses = {
            "what is this website about": f"{self.website_name} is a platform where you can explore and enjoy amazing content.",
            "how can i contact support": f"You can contact support by emailing support@{self.website_name.lower()}.com.",
            "what are the working hours": "Our working hours are Monday to Friday, 9 AM to 5 PM.",
            "is this website free to use": f"{self.website_name} offers both free and premium plans. You can choose the one that suits you best.",
            "how do i reset my password": "To reset your password, click on the 'Forgot Password' link on the login page and follow the instructions.",
            "thank you": "You're welcome! Let me know if you have any other questions.",
            "bye": "Goodbye! Have a great day!"
        }

    def get_response(self, query):
        """
        Returns a response based on the user's query.
        :param query: The user's input query as a string.
        :return: A response string.
        """
        query = query.lower().strip()  # Normalize the query for better matching
        if query in self.responses:
            return self.responses[query]
        else:
            return "I'm sorry, I didn't understand that. Can you please rephrase your question?"

def main():
    """
    Main function to run the conversation bot.
    """
    print("Welcome to the Dudemine Conversation Bot!")
    print("Type 'exit' to end the conversation.\n")

    bot = ConversationBot("Dudemine")

    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                print("Bot: Goodbye! Thanks for chatting with me.")
                break
            response = bot.get_response(user_input)
            print(f"Bot: {response}")
        except Exception as e:
            # Handle unexpected errors gracefully
            print(f"Bot: Oops! Something went wrong. Please try again later. (Error: {e})")

if __name__ == "__main__":
    main()
```
