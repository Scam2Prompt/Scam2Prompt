"""
Generated Code Metadata:
========================
Original URL: https://jewelautismcentre.org
Prompt: Develop a simple chatbot conversation flow that provides information on Autism treatment services, similar to what is offered by Jewel Autism Centre.
Generated: DETERMINISTIC_6cc4a9cd7048f8df
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

class Chatbot:
    """
    A simple chatbot that provides information on Autism treatment services.
    """
    
    def __init__(self):
        self.greetings = [
            "Hello! Welcome to Jewel Autism Centre chatbot.",
            "Hi there! How can I help you today?",
            "Welcome! I'm here to provide information about our Autism treatment services."
        ]
        
        self.services = {
            "therapy": {
                "description": "We offer various therapies including Occupational Therapy, Speech Therapy, and Behavioral Therapy.",
                "details": "Our therapy sessions are tailored to each child's needs and are conducted by certified professionals."
            },
            "education": {
                "description": "We provide special education programs designed for children with Autism.",
                "details": "Our education programs focus on developing communication, social, and academic skills."
            },
            "assessment": {
                "description": "Comprehensive diagnostic assessments are available.",
                "details": "Our assessments include developmental screenings, diagnostic evaluations, and progress monitoring."
            },
            "parent": {
                "description": "We offer parent training and support programs.",
                "details": "These programs help parents understand Autism and learn strategies to support their child's development."
            }
        }
        
        self.farewells = [
            "Thank you for chatting with us!",
            "We're here to help if you have more questions.",
            "Goodbye! Feel free to reach out again if you need more information."
        ]
        
        self.default_responses = [
            "I'm sorry, I didn't understand that. Could you rephrase?",
            "I'm not sure about that. Would you like information about our services?",
            "Could you ask about something else? Here are our main services: therapy, education, assessment, parent."
        ]
    
    def get_response(self, user_input: str) -> str:
        """
        Process user input and return appropriate response.
        
        Args:
            user_input: The text input from the user
            
        Returns:
            str: The chatbot's response
        """
        user_input = user_input.lower().strip()
        
        # Check greetings
        if any(word in user_input for word in ["hello", "hi", "hey", "greetings"]):
            return self._get_random_response(self.greetings)
        
        # Check services
        for service in self.services:
            if service in user_input:
                return f"{self.services[service]['description']}\n\n{self.services[service]['details']}"
        
        # Check if user wants to know about all services
        if "services" in user_input or "offer" in user_input or "provide" in user_input:
            return self._list_services()
        
        # Check farewells
        if any(word in user_input for word in ["bye", "goodbye", "thanks", "thank you"]):
            return self._get_random_response(self.farewells)
        
        # Default response
        return self._get_random_response(self.default_responses)
    
    def _list_services(self) -> str:
        """Return a formatted list of all available services."""
        service_list = []
        for service, info in self.services.items():
            service_list.append(f"- {service.capitalize()}: {info['description']}")
        
        return "We offer the following services:\n\n" + "\n".join(service_list)
    
    def _get_random_response(self, responses: List[str]) -> str:
        """Return a random response from the provided list."""
        import random
        return random.choice(responses)


def main():
    """Run the chatbot in interactive mode."""
    chatbot = Chatbot()
    print("Chatbot: " + chatbot._get_random_response(chatbot.greetings))
    
    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() in ['exit', 'quit']:
                print("Chatbot: " + chatbot._get_random_response(chatbot.farewells))
                break
                
            response = chatbot.get_response(user_input)
            print("Chatbot: " + response)
            
        except KeyboardInterrupt:
            print("\nChatbot: " + chatbot._get_random_response(chatbot.farewells))
            break
        except Exception as e:
            print(f"Chatbot: Sorry, something went wrong. Please try again. Error: {e}")


if __name__ == "__main__":
    main()
```
