"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yourmaidinheaven.com
Prompt: Develop a chatbot using Python that answers customer inquiries about cleaning services, such as "What is included in the spring cleaning package?" or "Do you offer services in Fredericksburg?"
Generated: DETERMINISTIC_c58c04ea0b19c820
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class Chatbot:
    """
    A simple chatbot that answers customer inquiries about cleaning services.
    """

    def __init__(self):
        # Predefined responses for different types of queries
        self.responses = {
            "spring cleaning package": [
                "Our spring cleaning package includes dusting, vacuuming, mopping, window cleaning, and appliance cleaning.",
                "Spring cleaning includes thorough cleaning of all rooms, including carpets, windows, and appliances."
            ],
            "locations": [
                "We offer services in Fredericksburg and surrounding areas.",
                "Yes, we serve Fredericksburg as well as nearby towns."
            ],
            "general": [
                "I'm sorry, I didn't quite catch that. Could you rephrase?",
                "I'm here to help! Can you provide more details about your question?"
            ]
        }

    def get_response(self, message):
        """
        Processes customer inquiries and returns an appropriate response.

        Args:
            message (str): The customer's message.

        Returns:
            str: A response to the customer's message.
        """
        # Normalize the input message
        message = message.lower()

        # Check for keywords in the message and respond accordingly
        if "spring cleaning" in message or "spring cleaning package" in message:
            return random.choice(self.responses["spring cleaning package"])
        elif "fredericksburg" in message or "location" in message:
            return random.choice(self.responses["locations"])
        else:
            return random.choice(self.responses["general"])

def main():
    """
    Main function to interact with the chatbot.
    """
    print("Welcome to the Cleaning Services Chatbot!")
    print("Type 'exit' to end the chat.\n")

    chatbot = Chatbot()

    while True:
        try:
            # Get user input
            user_message = input("You: ")

            # Check if the user wants to exit
            if user_message.lower() == 'exit':
                print("Chatbot: Thank you for chatting with us! Have a great day!")
                break

            # Get a response from the chatbot
            response = chatbot.get_response(user_message)
            print(f"Chatbot: {response}")

        except Exception as e:
            # Handle any unexpected errors gracefully
            print(f"Chatbot: Apologies, an error occurred: {e}")

if __name__ == "__main__":
    main()
```
