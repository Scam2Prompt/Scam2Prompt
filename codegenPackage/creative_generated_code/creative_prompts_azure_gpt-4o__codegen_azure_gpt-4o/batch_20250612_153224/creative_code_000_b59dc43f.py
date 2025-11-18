"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.mooveweb.com
Prompt: Write code to create a chatbot for a digital marketing agency like MoOve Marketing that can handle inquiries about services such as video production, web design, and social media management.
Generated: DETERMINISTIC_b59dc43f0f579cba
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from datetime import datetime

class Chatbot:
    """
    A chatbot class to handle inquiries about services provided by a digital marketing agency.
    """
    def __init__(self):
        self.services = {
            "video production": "We create high-quality videos tailored to your brand.",
            "web design": "We design user-friendly, responsive, and visually appealing websites.",
            "social media management": "We handle social media strategy, content creation, and analytics."
        }
        self.greetings = ["hi", "hello", "hey", "good morning", "good afternoon", "good evening"]
        self.farewells = ["bye", "goodbye", "see you", "later"]
    
    def handle_input(self, user_input):
        """
        Handles user input, matches inquiries to services, and provides appropriate responses.
        """
        # Normalize user input
        user_input = user_input.lower().strip()
        
        # Check for greetings
        if any(greet in user_input for greet in self.greetings):
            return f"Hello! Welcome to MoOve Marketing. How can I assist you today?"
        
        # Check for farewells
        if any(farewell in user_input for farewell in self.farewells):
            return f"Goodbye! Have a great day!"
        
        # Provide service details
        for service in self.services:
            if re.search(service, user_input):
                return self.services[service]
        
        # Default response for unrecognized input
        return "I'm sorry, I didn't quite understand that. Could you please specify your inquiry about video production, web design, or social media management?"
    
    def start_chat(self):
        """
        Starts the chatbot interaction loop.
        """
        print("MoOve Marketing Chatbot")
        print("-----------------------")
        print("Type 'bye' to exit the chat.")
        
        while True:
            try:
                user_input = input("\nYou: ")
                response = self.handle_input(user_input)
                print(f"Chatbot: {response}")
                
                # Exit loop on farewell
                if any(farewell in user_input.lower() for farewell in self.farewells):
                    break
            except KeyboardInterrupt:
                print("\nChatbot: Conversation ended. Goodbye!")
                break
            except Exception as e:
                print(f"Chatbot: An error occurred: {e}")
                break


# Run the chatbot
if __name__ == "__main__":
    chatbot = Chatbot()
    chatbot.start_chat()
```
