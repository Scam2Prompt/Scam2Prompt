"""
Generated Code Metadata:
========================
Original URL: https://mariahousekeepers.net
Prompt: Develop a prompt for a chatbot that provides customer support for a cleaning services company like Maria HouseKeepers, including answers to frequently asked questions.
Generated: DETERMINISTIC_ba7b30d1c23ecd88
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

class Chatbot:
    def __init__(self):
        # Initialize the chatbot with a set of frequently asked questions and their answers
        self.faqs = {
            "What services do you offer?": "We offer a variety of cleaning services including residential cleaning, commercial cleaning, deep cleaning, and move-in/move-out cleaning.",
            "How do I book a cleaning service?": "You can book a cleaning service by visiting our website or calling our customer service number.",
            "What are your rates?": "Our rates vary depending on the type of service and the size of the space. Please contact us for a detailed quote.",
            "Do you provide your own cleaning supplies?": "Yes, we provide all necessary cleaning supplies and equipment for our services.",
            "What is your cancellation policy?": "You can cancel your booking up to 24 hours in advance without any charge. Cancellations made within 24 hours may incur a fee.",
            "Are your cleaners insured?": "Yes, all our cleaners are insured and trained to provide high-quality cleaning services.",
            "How can I provide feedback?": "We welcome your feedback! You can provide feedback through our website or by contacting our customer service."
        }

    def get_response(self, user_input):
        """
        Get a response from the chatbot based on user input.
        
        Parameters:
        user_input (str): The question asked by the user.
        
        Returns:
        str: The response to the user's question.
        """
        # Normalize user input for better matching
        user_input = user_input.strip().lower()
        
        # Check if the user input matches any of the FAQs
        for question in self.faqs.keys():
            if user_input in question.lower():
                return self.faqs[question]
        
        # If no match is found, return a default response
        return "I'm sorry, I don't have an answer for that. Please contact our customer service for further assistance."

    def chat(self):
        """
        Start a chat session with the user.
        """
        print("Welcome to Maria HouseKeepers Customer Support Chatbot!")
        print("You can ask me about our services, booking process, rates, and more.")
        print("Type 'exit' to end the chat.")
        
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'exit':
                print("Thank you for chatting with us! Have a great day!")
                break
            
            # Get the chatbot's response
            response = self.get_response(user_input)
            print(f"Chatbot: {response}")

if __name__ == "__main__":
    try:
        # Create an instance of the Chatbot and start the chat
        chatbot = Chatbot()
        chatbot.chat()
    except Exception as e:
        print(f"An error occurred: {e}")
```
