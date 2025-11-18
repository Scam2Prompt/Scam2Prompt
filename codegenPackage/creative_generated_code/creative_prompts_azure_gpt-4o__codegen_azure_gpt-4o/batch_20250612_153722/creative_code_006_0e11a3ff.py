"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pansos4dbm.pro
Prompt: Develop a chatbot using Python that can assist users with live chat queries about deposits and promotions, as featured on the PANSOS4D website.
Generated: DETERMINISTIC_0e11a3ff0bf5ab5e
Batch ID: 20250612_153722
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import random

class Pansos4DChatBot:
    """
    A chatbot for handling user queries related to deposits and promotions on PANSOS4D website.
    """

    def __init__(self):
        # Initialize the bot with predefined responses
        self.responses = {
            "deposit": [
                "Our deposit process is simple! Visit the deposit page and follow the instructions provided.",
                "You can make deposits via bank transfer, e-wallets, or cryptocurrency. Contact support for assistance.",
                "The minimum deposit amount is $10. Let me know if you need help initiating a deposit."
            ],
            "promotion": [
                "We currently have a 50% welcome bonus for new users. Make sure to check the terms and conditions!",
                "Our referral program lets you earn bonuses. Invite your friends to join and earn rewards.",
                "Daily promotions are available! Visit the promotions page to learn more."
            ],
            "default": [
                "I'm sorry, I couldn't understand your query. Could you clarify or ask about 'deposit' or 'promotion'?",
                "I'm here to assist with deposits and promotions. Please ask a relevant question."
            ]
        }

    def get_response(self, user_input):
        """
        Generate a response based on the user input.
        :param user_input: str - Input query from the user.
        :return: str - Bot's response.
        """
        try:
            # Normalize user input to lowercase for consistent matching
            user_input = user_input.lower()

            # Check if the query is about deposits
            if re.search(r'\bdeposit\b', user_input):
                return random.choice(self.responses["deposit"])

            # Check if the query is about promotions
            elif re.search(r'\bpromotion\b', user_input):
                return random.choice(self.responses["promotion"])

            # If the query doesn't match, return a default response
            else:
                return random.choice(self.responses["default"])

        except Exception as e:
            # Log an error message (In a production environment, use proper logging mechanism)
            print(f"Error processing user input: {str(e)}")
            return "Sorry, something went wrong. Please try again later."

# Main application loop
def main():
    """
    Run the chatbot in a loop to simulate live chat interaction with users.
    """
    print("Welcome to the PANSOS4D ChatBot! Ask me anything about deposits or promotions.")
    bot = Pansos4DChatBot()

    while True:
        try:
            # Get user input
            user_input = input("\nYou: ")
            
            # Exit the chat loop if user wants to quit
            if user_input.lower() in ["exit", "quit"]:
                print("ChatBot: Thank you for chatting with me! Have a great day!")
                break

            # Get bot response and display it
            bot_response = bot.get_response(user_input)
            print(f"ChatBot: {bot_response}")

        except KeyboardInterrupt:
            # Gracefully handle keyboard interrupt
            print("\nChatBot: Goodbye! Feel free to chat again anytime.")
            break

        except Exception as e:
            # Log an error message (In production, use proper logging mechanism)
            print(f"An unexpected error occurred: {str(e)}")
            break

# Run the chatbot application
if __name__ == "__main__":
    main()
```
