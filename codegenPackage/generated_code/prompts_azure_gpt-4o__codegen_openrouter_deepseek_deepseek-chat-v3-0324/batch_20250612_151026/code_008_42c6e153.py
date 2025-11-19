"""
Generated Code Metadata:
========================
Original URL: https://virtual5.com.mx
Prompt: Generate code to create a chatbot that provides information about Virtual5's services, including experiential learning, habit creation, and organizational change management.
Generated: DETERMINISTIC_42c6e153193ae0e4
Batch ID: 20250612_151026
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

class Virtual5Chatbot:
    """
    A chatbot that provides information about Virtual5's services.
    Handles inquiries about experiential learning, habit creation, and organizational change management.
    """
    
    def __init__(self):
        self.services_data = self._load_services_data()
        self.greetings = [
            "Hello! How can I help you with Virtual5's services today?",
            "Hi there! What would you like to know about Virtual5?",
            "Welcome! I can tell you about Virtual5's services."
        ]
        self.farewells = [
            "Goodbye! Feel free to return if you have more questions.",
            "Thanks for chatting! Come back anytime.",
            "Have a great day! Let us know if you need more information."
        ]
    
    def _load_services_data(self) -> Dict[str, Dict]:
        """Load service information from a structured dictionary."""
        return {
            "experiential learning": {
                "description": "Virtual5's experiential learning programs immerse participants in real-world scenarios to develop practical skills.",
                "benefits": [
                    "Hands-on skill development",
                    "Immediate application of knowledge",
                    "Enhanced retention through experience"
                ],
                "examples": [
                    "Simulation-based training",
                    "Role-playing exercises",
                    "Case study analysis"
                ]
            },
            "habit creation": {
                "description": "Our habit creation framework helps individuals and teams build sustainable, positive behaviors.",
                "benefits": [
                    "Science-backed methodology",
                    "Personalized habit plans",
                    "Accountability systems"
                ],
                "examples": [
                    "21-day challenge programs",
                    "Behavioral nudges",
                    "Progress tracking tools"
                ]
            },
            "organizational change management": {
                "description": "Virtual5 provides comprehensive change management solutions to guide organizations through transitions.",
                "benefits": [
                    "Minimized disruption",
                    "Employee engagement strategies",
                    "Sustainable change implementation"
                ],
                "examples": [
                    "Change readiness assessments",
                    "Leadership alignment workshops",
                    "Communication planning"
                ]
            }
        }
    
    def get_service_info(self, service_name: str) -> Optional[Dict]:
        """Retrieve information about a specific service."""
        service_name = service_name.lower().strip()
        return self.services_data.get(service_name)
    
    def list_services(self) -> List[str]:
        """Return a list of available services."""
        return list(self.services_data.keys())
    
    def generate_response(self, user_input: str) -> str:
        """Process user input and generate an appropriate response."""
        user_input = user_input.lower().strip()
        
        # Handle greetings
        if any(greet in user_input for greet in ["hi", "hello", "hey"]):
            return self._get_random_response(self.greetings)
        
        # Handle farewells
        if any(bye in user_input for bye in ["bye", "goodbye", "exit"]):
            return self._get_random_response(self.farewells)
        
        # Handle service inquiries
        for service in self.services_data:
            if service in user_input:
                info = self.get_service_info(service)
                return self._format_service_response(service, info)
        
        # Handle list services request
        if "services" in user_input or "offer" in user_input:
            services = self.list_services()
            return f"Virtual5 offers these services: {', '.join(services)}. Which one would you like to know more about?"
        
        # Default response for unrecognized input
        return "I'm not sure I understand. Could you ask about our services like experiential learning, habit creation, or organizational change management?"
    
    def _format_service_response(self, service_name: str, service_info: Dict) -> str:
        """Format service information into a readable response."""
        response = [
            f"Here's information about our {service_name} service:",
            f"\nDescription: {service_info['description']}",
            "\nKey Benefits:",
            *[f"- {benefit}" for benefit in service_info['benefits']],
            "\nExamples:",
            *[f"- {example}" for example in service_info['examples']]
        ]
        return "\n".join(response)
    
    def _get_random_response(self, responses: List[str]) -> str:
        """Select a random response from a list of possible responses."""
        import random
        return random.choice(responses)

def run_chatbot():
    """Run the chatbot in an interactive loop."""
    chatbot = Virtual5Chatbot()
    print("Virtual5 Chatbot: Hi! I can tell you about our services. Type 'exit' to end the conversation.")
    
    while True:
        try:
            user_input = input("\nYou: ")
            if user_input.lower() in ['exit', 'quit', 'bye']:
                print(f"Virtual5 Chatbot: {chatbot._get_random_response(chatbot.farewells)}")
                break
            
            response = chatbot.generate_response(user_input)
            print(f"Virtual5 Chatbot: {response}")
        
        except KeyboardInterrupt:
            print("\nVirtual5 Chatbot: Goodbye!")
            break
        except Exception as e:
            print(f"Virtual5 Chatbot: Sorry, I encountered an error. Please try again. Error: {str(e)}")

if __name__ == "__main__":
    run_chatbot()
```
