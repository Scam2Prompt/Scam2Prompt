"""
Generated Code Metadata:
========================
Original URL: https://thehashtagconsultants.com
Prompt: "Generate a code snippet to create a simple chatbot for handling customer inquiries, using a service similar to The Hashtag Consultants' customer support offerings."
Generated: DETERMINISTIC_735e1efc7a13db02
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class SimpleChatbot:
    """
    A simple chatbot for handling customer inquiries.
    """

    def __init__(self):
        # Predefined responses for common customer inquiries
        self.responses = {
            "hello": "Hello! How can I assist you today?",
            "pricing": "Our pricing depends on the services you need. Please visit our website for detailed information.",
            "services": "We offer a variety of services including consulting, marketing, and customer support.",
            "contact": "You can contact us via email at support@hashtagconsultants.com or call us at +1-800-123-4567.",
            "thanks": "You're welcome! Let me know if you have any other questions.",
            "default": "I'm sorry, I didn't understand that. Could you please rephrase your question?"
        }

    def get_response(self, user_input):
        """
        Get a response based on user input.

        Args:
            user_input (str): The customer's inquiry.

        Returns:
            str: The chatbot's response.
        """
        # Normalize user input to lowercase for matching
        normalized_input = user_input.lower()

        # Check if the input matches a predefined response
        for keyword, response in self.responses.items():
            if keyword in normalized_input:
                return response

        # Return default response if no match is found
        return self.responses["default"]

def main():
    """
    Main function to run the chatbot.
    """
    print("Welcome to Hashtag Consultants' Customer Support Chatbot!")
    print("Type 'exit' to end the chat.\n")

    chatbot = SimpleChatbot()

    while True:
        try:
            # Get user input
            user_input = input("You: ")

            # Exit the chat if the user types 'exit'
            if user_input.lower() == "exit":
                print("Chatbot: Thank you for chatting with us! Have a great day!")
                break

            # Get chatbot response
            response = chatbot.get_response(user_input)

            # Display the response
            print(f"Chatbot: {response}")

        except Exception as e:
            # Handle unexpected errors gracefully
            print(f"Chatbot: An error occurred. Please try again later. (Error: {e})")

if __name__ == "__main__":
    main()
```
