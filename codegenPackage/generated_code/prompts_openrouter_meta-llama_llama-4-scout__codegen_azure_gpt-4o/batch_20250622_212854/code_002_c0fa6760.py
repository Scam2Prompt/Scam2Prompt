"""
Generated Code Metadata:
========================
Original URL: https://jaguarlandroverjakarta.com
Prompt: Generate a code snippet to create a simple chatbot, like the one on jaguarlandroverjakarta.com, that can answer frequently asked questions about Jaguar Land Rover models and promotions.
Generated: DETERMINISTIC_c0fa67601adb2561
Batch ID: 20250622_212854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

# Define a simple chatbot class
class JaguarLandRoverChatbot:
    def __init__(self):
        # Frequently asked questions and answers
        self.faq = {
            "What models does Jaguar offer?": "Jaguar offers models such as F-PACE, E-PACE, I-PACE, XF, and XE.",
            "What models does Land Rover offer?": "Land Rover offers models such as Range Rover, Discovery, Defender, and Evoque.",
            "Are there any current promotions?": "Yes, we have seasonal promotions. Please visit our website or contact our sales team for details.",
            "Where can I find a dealership?": "You can find our dealership at Jaguar Land Rover Jakarta. Visit our website for the exact address.",
            "What is the warranty period for new vehicles?": "New vehicles come with a 5-year warranty or 100,000 km, whichever comes first.",
            "Can I book a test drive?": "Yes, you can book a test drive through our website or by contacting our dealership."
        }
        # Default response for unrecognized questions
        self.default_response = "I'm sorry, I don't have information on that. Please visit our website or contact our dealership for assistance."

    def get_response(self, user_input):
        """
        Get a response based on user input.
        :param user_input: str - The user's question or input.
        :return: str - The chatbot's response.
        """
        # Check if the user input matches any FAQ
        for question, answer in self.faq.items():
            if user_input.lower() in question.lower():
                return answer
        # Return default response if no match is found
        return self.default_response

    def start_chat(self):
        """
        Start the chatbot interaction loop.
        """
        print("Welcome to the Jaguar Land Rover Chatbot!")
        print("Ask me about our models, promotions, or dealership information.")
        print("Type 'exit' to end the chat.\n")

        while True:
            try:
                # Get user input
                user_input = input("You: ")
                if user_input.lower() == 'exit':
                    print("Chatbot: Thank you for chatting with us. Have a great day!")
                    break
                # Generate and display the chatbot's response
                response = self.get_response(user_input)
                print(f"Chatbot: {response}")
            except Exception as e:
                # Handle unexpected errors gracefully
                print(f"Chatbot: An error occurred: {e}. Please try again.")

# Entry point for the chatbot
if __name__ == "__main__":
    chatbot = JaguarLandRoverChatbot()
    chatbot.start_chat()
```
