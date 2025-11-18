"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ranchioffline.com
Prompt: Develop a chatbot using Python that can assist users with inquiries about RanchiOffline's services, including banking assistance, insurance, and government documentation support.
Generated: DETERMINISTIC_992a9baf23bd03d2
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

# Import necessary libraries for the chatbot
class RanchiOfflineChatbot:
    """
    RanchiOfflineChatbot is a chatbot designed to assist users with inquiries
    about RanchiOffline services, such as banking assistance, insurance, 
    and government documentation support.
    """

    def __init__(self):
        """
        Initialize the chatbot with predefined services and responses.
        """
        self.services = {
            "banking": "We offer assistance with opening accounts, resolving queries, and guiding you through online banking services.",
            "insurance": "We provide help with choosing insurance policies, filing claims, and understanding premiums.",
            "documentation": "We assist with applying for government documents such as PAN cards, Aadhar cards, and passports."
        }

        # Default response
        self.default_response = (
            "I'm sorry, I couldn't understand your query. "
            "Please ask about banking, insurance, or government documentation support."
        )

    def get_response(self, user_input):
        """
        Process the user input and return an appropriate response.

        Parameters:
            user_input (str): The user's query.

        Returns:
            str: The chatbot's response.
        """
        # Normalize the user input (convert to lowercase and strip extra spaces)
        user_input = user_input.lower().strip()

        # Match user input to predefined services
        if re.search(r'\bbanking\b', user_input):
            return self.services["banking"]
        elif re.search(r'\binsurance\b', user_input):
            return self.services["insurance"]
        elif re.search(r'\bdocumentation\b', user_input) or re.search(r'\bgovernment\b', user_input):
            return self.services["documentation"]
        else:
            return self.default_response


def run_chatbot():
    """
    Run the RanchiOffline chatbot, allowing users to interact with it.
    """
    print("Welcome to RanchiOffline Chatbot!")
    print("You can ask about our services related to banking, insurance, or government documentation support.")
    print("Type 'exit' to end the chat.\n")

    chatbot = RanchiOfflineChatbot()

    while True:
        try:
            # Get user input
            user_input = input("You: ")

            # Exit the chat if the user types 'exit'
            if user_input.lower() == 'exit':
                print("Chatbot: Thank you for using RanchiOffline Chatbot! Goodbye!")
                break

            # Get the chatbot's response and display it
            response = chatbot.get_response(user_input)
            print(f"Chatbot: {response}")

        except Exception as e:
            # Handle unexpected errors gracefully
            print(f"Chatbot: Sorry, an unexpected error occurred. ({e})")


# Entry point for the script
if __name__ == "__main__":
    run_chatbot()
```
