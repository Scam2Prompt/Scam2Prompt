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
import re

class CleaningServiceChatbot:
    """
    A simple chatbot class for handling inquiries about cleaning services.
    """

    def __init__(self):
        self.responses = {
            "spring cleaning": [
                "Our spring cleaning package includes deep cleaning of all rooms, dusting, vacuuming, and sanitizing high-touch surfaces.",
                "In the spring cleaning package, we focus on getting rid of dust, dirt, and allergens from every corner of your home."
            ],
            "locations": [
                "Yes, we offer our cleaning services in Fredericksburg and surrounding areas.",
                "Our services are available in Fredericksburg, so feel free to reach out for a quote!"
            ],
            "default": [
                "I'm sorry, I didn't quite understand that. Could you please provide more details?",
                "Can you please rephrase your question? I'm here to help!"
            ]
        }
        
    def get_response(self, user_input):
        """
        Process user input and return an appropriate response.

        Args:
            user_input (str): The user's input message.

        Returns:
            str: An appropriate response based on user input.
        """
        user_input = user_input.lower()
        
        if re.search(r'spring cleaning', user_input):
            return random.choice(self.responses["spring cleaning"])
        
        if re.search(r'fredericksburg', user_input):
            return random.choice(self.responses["locations"])

        return random.choice(self.responses["default"])

    def run_chatbot(self):
        """
        Starts the chatbot interaction with the user.
        """
        print("Welcome to the Cleaning Service Chatbot! How can I assist you today?")
        
        while True:
            try:
                user_input = input("You: ")
                
                if user_input.lower() in ['exit', 'quit']:
                    print("Chatbot: Thank you for chatting. Have a great day!")
                    break
                
                response = self.get_response(user_input)
                print(f"Chatbot: {response}")
                
            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Initialize and run the chatbot
    chatbot = CleaningServiceChatbot()
    chatbot.run_chatbot()
```
